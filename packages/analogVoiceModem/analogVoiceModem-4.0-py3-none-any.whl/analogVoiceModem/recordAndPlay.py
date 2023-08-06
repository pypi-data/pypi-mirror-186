##------------------------------------------
##--- Version: 1.0
##--- Python Ver: 3.9
##--- Description: This python code will make a call/ pick incoming call and record/ play the audio msg.
##--- Hardware: Raspberry Pi3 and USRobotics USR5637 USB Modem
##------------------------------------------


import serial
import time
import threading
import atexit
import sys
import re
import wave
from datetime import datetime
import os
import fcntl
import subprocess
import argparse

RINGS_BEFORE_AUTO_ANSWER = 2  # Must be greater than 1
MODEM_RESPONSE_READ_TIMEOUT = 120  # Time in Seconds (Default 120 Seconds)
MODEM_NAME = 'U.S. Robotics'  # Modem Manufacturer, For Ex: 'U.S. Robotics' if the 'lsusb' cmd output is similar to "Bus 001 Device 004: ID 0baf:0303 U.S. Robotics"

# Record Voice Mail Variables
REC_VM_MAX_DURATION = 5  # Time in Seconds

# Used in global event listener
disable_modem_event_listener = True

# Global Modem Object
analog_modem = serial.Serial()

audio_file_name = ''


# =================================================================
# Set COM Port settings
# =================================================================
def set_COM_port_settings(com_port):
    analog_modem.port = com_port

    analog_modem.baudrate = 115200
    analog_modem.bytesize = serial.EIGHTBITS  # number of bits per bytes
    analog_modem.parity = serial.PARITY_NONE  # set parity check: no parity
    analog_modem.stopbits = serial.STOPBITS_ONE  # number of stop bits
    analog_modem.timeout = 3  # non-block read
    analog_modem.xonxoff = False  # disable software flow control
    analog_modem.rtscts = False  # disable hardware (RTS/CTS) flow control
    analog_modem.dsrdtr = False  # disable hardware (DSR/DTR) flow control
    analog_modem.writeTimeout = 3  # timeout for write


# =================================================================
# Initialize Modem
# =================================================================
def detect_COM_port():
    # List all the Serial COM Ports on Raspberry Pi
    # proc = subprocess.Popen(['ls /dev/ttyACM*'], shell=True, stdout=subprocess.PIPE)
    # com_ports = proc.communicate()[0]
    # com_ports_list = com_ports.split('\n')
    com_ports_list = ["/dev/ttyACM0"]
    print (com_ports_list)

    # Find the right port associated with the Voice Modem
    for com_port in com_ports_list:
        print (com_port)
        if 'tty' in com_port:
            # Try to open the COM Port and execute AT Command
            try:
                # Set the COM Port Settings
                set_COM_port_settings(com_port)
                analog_modem.open()
            except:
                print ("Unable to open COM Port: " + com_port)
                pass
            else:
                # Try to put Modem in Voice Mode
                if not exec_AT_cmd("AT+FCLASS=8\r", "OK"):
                    print ("Error: Failed to put modem into voice mode.")
                    if analog_modem.isOpen():
                        analog_modem.close()
                else:
                    # Found the COM Port exit the loop
                    print ("Modem COM Port is: " + com_port)
                    analog_modem.flushInput()
                    analog_modem.flushOutput()
                    break


# =================================================================
# Initialize Modem
# =================================================================
def init_modem_settings():
    # Detect and Open the Modem Serial COM Port
    try:
        detect_COM_port()
    except:
        print ("Error: Unable to open the Serial Port.")
        sys.exit()

    # Initialize the Modem
    try:
        # Flush any existing input outout data from the buffers
        analog_modem.flushInput()
        analog_modem.flushOutput()

        # Test Modem connection, using basic AT command.
        if not exec_AT_cmd("AT\r"):
            print ("Error: Unable to access the Modem")

        # reset to factory default.
        if not exec_AT_cmd("ATZ3\r"):
            print ("Error: Unable reset to factory default")

        # Display result codes in verbose form
        if not exec_AT_cmd("ATV1\r"):
            print ("Error: Unable set response in verbose form")

        # Enable Command Echo Mode.
        if not exec_AT_cmd("ATE1\r"):
            print ("Error: Failed to enable Command Echo Mode")

        # Enable formatted caller report.
        if not exec_AT_cmd("AT+VCID=1\r"):
            print ("Error: Failed to enable formatted caller report.")

        # RESET MODE
        if not exec_AT_cmd("AT+FCLASS=0\r"):
            print ("Error: Failed to enable formatted caller report.")

        # Flush any existing input outout data from the buffers
        analog_modem.flushInput()
        analog_modem.flushOutput()


    except:
        print ("Error: unable to Initialize the Modem")
        sys.exit()


# =================================================================
# Reset Modem
# =================================================================
def reset_USB_Device():
    # Close the COM Port if it's open
    try:
        if analog_modem.isOpen():
            analog_modem.close()
    except:
        pass

    # Equivalent of the _IO('U', 20) constant in the linux kernel.
    USBDEVFS_RESET = ord('U') << (4 * 2) | 20
    dev_path = ""

    # Bases on 'lsusb' command, get the usb device path in the following format -
    # /dev/bus/usb/<busnum>/<devnum>
    proc = subprocess.Popen(['lsusb'], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    lines = out.split('\n')
    for line in lines:
        if MODEM_NAME in line:
            parts = line.split()
            bus = parts[1]
            dev = parts[3][:3]
            dev_path = '/dev/bus/usb/%s/%s' % (bus, dev)

    # Reset the USB Device
    fd = os.open(dev_path, os.O_WRONLY)
    try:
        fcntl.ioctl(fd, USBDEVFS_RESET, 0)
        print ("Modem reset successful")
    finally:
        os.close(fd)

    # Re-initialize the Modem
    init_modem_settings()


# =================================================================
# Execute AT Commands at the Modem
# =================================================================
def exec_AT_cmd(modem_AT_cmd, expected_response="OK"):
    global disable_modem_event_listener
    disable_modem_event_listener = True

    try:
        # Send command to the Modem
        time.sleep(0.1)
        analog_modem.write(modem_AT_cmd.encode())
        time.sleep(0.1)
        # Read Modem response
        execution_status = read_AT_cmd_response(expected_response.encode())
        print("execution_status", execution_status)
        disable_modem_event_listener = False
        # Return command execution status
        return execution_status

    except:
        disable_modem_event_listener = False
        print ("Error: Failed to execute the command")
        return False


# =================================================================
# Read AT Command Response from the Modem
# =================================================================
def read_AT_cmd_response(expected_response="OK"):
    # Set the auto timeout interval
    start_time = datetime.now()

    try:
        while 1:
            # Read Modem Data on Serial Rx Pin

            print (analog_modem.readline())
            modem_response = analog_modem.readline()
            print ("modem_response", modem_response)
            modem1 = modem_response.rstrip()
            time.sleep(1)
            # Recieved expected Response
            if modem1 == expected_response:
                return True
            elif "CONNECT" in modem1:
                return True
                # Failed to execute the command successfully
            elif "ERROR" in modem1:
                return False
            # Timeout
            elif (datetime.now() - start_time).seconds > MODEM_RESPONSE_READ_TIMEOUT:

                return False

    except:
        print ("Error in read_modem_response function...")
        return False


# =================================================================
# Recover Serial Port
# =================================================================
def recover_from_error():
    # Stop Global Modem Event listener
    global disable_modem_event_listener
    disable_modem_event_listener = True

    # Reset USB Device
    reset_USB_Device()

    # Start Global Modem Event listener
    disable_modem_event_listener = False


# =================================================================
# Read DTMF Digits
# =================================================================
def dtmf_digits(modem_data):
    digits = ""
    digit_list = re.findall('/(.+?)~', modem_data)
    for d in digit_list:
        digits = digits + d[0]
    return digits


# =================================================================
# =================================================================
# Call
# =================================================================
def call(n):
    print("\n Calling", n)

    # reset
    if not exec_AT_cmd("AT+FCLASS=0\r", "OK"):
        print ("Error: Failed to put modem into voice mode.")
        return

    # Enter Voice Mode
    if not exec_AT_cmd("AT+FCLASS=8\r", "OK"):
        print ("Error: Failed to put modem into voice mode.")
        return

    # Set speaker volume to normal
    if not exec_AT_cmd("AT+VGT=128\r", "OK"):
        print ("Error: Failed to set speaker volume to normal.")
        return

    # Put modem into TAD Mode
    if not exec_AT_cmd("AT+VLS=7\r", "OK"):
        print ("Error: Unable put modem into TAD mode")
        return

    # call
    num = str(n)

    if not exec_AT_cmd("ATDT " + num + "\r", "OK"):
        print ("Error: Unable to call")
        return

    # Compression Method and Sampling Rate Specifications
    # Compression Method: 8-bit linear / Sampling Rate: 8000MHz
    if not exec_AT_cmd("AT+VSM=128,8000\r", "OK"):
        print ("Error: Failed to set compression method and sampling rate specifications.")
        return

    # Disables silence detection (Value: 0)
    if not exec_AT_cmd("AT+VSD=128,0\r", "OK"):
        print ("Error: Failed to disable silence detection.")
        return

    # Put modem into TAD Mode
    if not exec_AT_cmd("AT+VLS=1\r", "OK"):
        print ("Error: Unable put modem into TAD mode.")
        return

    # Enable silence detection.
    # Select normal silence detection sensitivity
    # and a silence detection interval of 5 s.
    if not exec_AT_cmd("AT+VSD=128,50\r", "OK"):
        print ("Error: Failed tp enable silence detection.")
        return

    # Play beep.
    if not exec_AT_cmd("AT+VTS=[933,900,100]\r", "OK"):
        print ("Error: Failed to play 1.2 second beep.")
    # return

    # Select voice receive mode
    if not exec_AT_cmd("AT+VRX\r", "CONNECT"):
        print ("Error: Unable put modem into voice receive mode.")
        return

    global disable_modem_event_listener
    CHUNK = 1024
    ring_data = b''
    modem_data_striped = b''
    status = "false"
    endtime = time.time() + 160.0  # 10 sec
    print("waiting for call to be answered")
    while (time.time() < endtime):

        if not disable_modem_event_listener:
            audio_data = analog_modem.read(CHUNK)

            if (b'\x10b' in audio_data):
                print("\n busy tone detected, call not picked")
                if not exec_AT_cmd("\x10!\r", "OK"):
                    print ("Error: Unable to signal end of voice receive state")
                status = "true"
                break;

            if (b'\x10s' in audio_data):
                print("\n call picked")
                if not exec_AT_cmd("\x10!\r", "OK"):
                    print ("Error: Unable to signal end of voice receive state")
                status = "true"
                break;
    time.sleep(0.5)
    if not exec_AT_cmd("\x10!\r", "OK"):
        print ("Error: Unable to signal end of voice receive state")
    return
    # =================================================================


# Answer
# =================================================================
def answer():
    print("\n Answering")

    # Enter Voice Mode
    if not exec_AT_cmd("AT+FCLASS=8\r", "OK"):
        print ("Error: Failed to put modem into voice mode.")
        return

    # Set speaker volume to normal
    if not exec_AT_cmd("AT+VGT=128\r", "OK"):
        print ("Error: Failed to set speaker volume to normal.")
        return

    # answer call
    if not exec_AT_cmd("AT+VLS=7\r", "OK"):
        print ("Error: Failed to answer call")
        return

    time.sleep(10)


# =================================================================
# Record wav file (Voice Msg/Mail)
# =================================================================
def record_audio():
    print ("Record Audio Msg - Start")
    print("recording**")
    # Enter Voice Mode
    if not exec_AT_cmd("AT+FCLASS=8\r", "OK"):
        print ("Error: Failed to put modem into voice mode.")
        return

    # Set speaker volume to normal
    if not exec_AT_cmd("AT+VGT=128\r", "OK"):
        print ("Error: Failed to set speaker volume to normal.")
        return

    # Compression Method and Sampling Rate Specifications
    # Compression Method: 8-bit linear / Sampling Rate: 8000MHz
    if not exec_AT_cmd("AT+VSM=128,8000\r", "OK"):
        print ("Error: Failed to set compression method and sampling rate specifications.")
        return

    # Disables silence detection (Value: 0)
    if not exec_AT_cmd("AT+VSD=128,0\r", "OK"):
        print ("Error: Failed to disable silence detection.")
        return

    # Put modem into TAD Mode
    if not exec_AT_cmd("AT+VLS=1\r", "OK"):
        print ("Error: Unable put modem into TAD mode.")
        return

    # Enable silence detection.
    # Select normal silence detection sensitivity
    # and a silence detection interval of 5 s.
    if not exec_AT_cmd("AT+VSD=128,50\r", "OK"):
        print ("Error: Failed tp enable silence detection.")
        return

    # Play beep.
    if not exec_AT_cmd("AT+VTS=[933,900,100]\r", "OK"):
        print ("Error: Failed to play 1.2 second beep.")
    # return

    # Select voice receive mode
    if not exec_AT_cmd("AT+VRX\r", "CONNECT"):
        print ("Error: Unable put modem into voice receive mode.")
        return
    time.sleep(2)

    # Record Audio File

    global disable_modem_event_listener
    disable_modem_event_listener = True

    # Set the auto timeout interval
    start_time = datetime.now()
    CHUNK = 1024
    audio_frames = []

    for i in range(0, int(44100 / CHUNK * 10)):
        # Read audio data from the Modem
        audio_data = analog_modem.read(CHUNK)
        audio_data_decoded = audio_data.decode('iso-8859-1')

        # Add Audio Data to Audio Buffer
        audio_frames.append(audio_data)

    # Save the Audio into a .wav file
    print("\n Appending to audio.wav")
    wf = wave.open('audio.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(1)
    wf.setframerate(8000)
    wf.writeframes(b''.join(audio_frames))
    wf.close()

    analog_modem.reset_input_buffer()
    print("written and resetted")

    # Send End of Voice Recieve state by passing "<DLE>!"
    if not exec_AT_cmd("\x10!\r", "OK"):
        print ("Error: Unable to signal end of voice receive state")

    # Hangup the Call
    if not exec_AT_cmd("ATH\r", "OK"):
        print ("Error: Unable to hang-up the call")

    # Reset Modem to default
    if not exec_AT_cmd("ATZ3\r", "OK"):
        print ("Error: Unable to hang-up the call")

    # ResetMode
    if not exec_AT_cmd("AT+FCLASS=0\r", "OK"):
        print ("Error: Unable to hang-up the call")

        # Enable global event listener
    disable_modem_event_listener = False

    print ("Record Audio Msg - END")
    return


# =================================================================
# Play wav file (Voice Msg/Mail)
# =================================================================

def play_audio(action):
    print("Play Audio Msg - Start")

    # Enter Voice Mode
    if not exec_AT_cmd("AT+FCLASS=8\r"):
        print("Error: Failed to put modem into voice mode.")
        return

    # Compression Method and Sampling Rate Specifications
    # Compression Method: 8-bit linear / Sampling Rate: 8000MHz
    if not exec_AT_cmd("AT+VSM=128,8000\r"):
        print("Error: Failed to set compression method and sampling rate specifications.")
        return

    # Put modem into TAD Mode
    if not exec_AT_cmd("AT+VLS=1\r"):
        print("Error: Unable put modem into TAD mode.")
        return

    # Put modem into TAD Mode
    if not exec_AT_cmd("AT+VTX\r", "CONNECT"):
        print("Error: Unable put modem into TAD mode.")
        return

    if (action == "call"):
        print("Sleeping for 5 sec")
        time.sleep(5)
    if (action == "answer"):
        print("Sleeping for 9 sec")
        time.sleep(7)

    # Play Audio File

    global disable_modem_event_listener
    disable_modem_event_listener = True

    print("After sleep")
    print("Playing play.wav")
    wf = wave.open('play.wav', 'rb')
    chunk = 1024

    data = wf.readframes(chunk)
    while data != b'':
        analog_modem.write(data)
        data = wf.readframes(chunk)
        # You may need to change this sleep interval to smooth-out the audio
        time.sleep(.12)
    cmd = "<DLE><ETX>\r"
    analog_modem.write(cmd.encode())
    wf.close()

    print("closed wf")

    # analog_modem.flushInput()
    # analog_modem.reset_input_buffer()

    print('Finished playing')

    cmd = "ATH" + "\r"
    analog_modem.write(cmd.encode())

    print("Play Audio Msg - END")
    return


# =================================================================
# Data Listener
# =================================================================
def read_data():
    global disable_modem_event_listener
    ring_data = b''
    modem_data_striped = b''

    while 1:

        if not disable_modem_event_listener:
            modem_data = analog_modem.readline()

            if (b'RING' in modem_data):

                if b'RING' in modem_data:
                    modem_data_striped = modem_data.rstrip()
                    print("modem_data_striped:  ", modem_data_striped)
                    print("ring_data:  ", ring_data)
                    print("modem_data:  ", modem_data_striped)
                    ring_data = ring_data + modem_data_striped
                    ring_count = ring_data.count(b'RING')
                    print("ring_count:  ", ring_count)
                    if ring_count == 1:
                        pass
                    elif ring_count == RINGS_BEFORE_AUTO_ANSWER:
                        ring_data = b''
                        answer()
                        return

            if not b'RING' in modem_data:
                print ("Error: No Ring")
                close_modem_port()
                return

            if b'\x10b' in modem_data:

                if b'\x10b' in modem_data:
                    print("busytone")
                    cmd = "ATH" + "\r"
                    analog_modem.write(cmd.encode())
                    return
                else:
                    return
            if b'\x10s' in modem_data:

                if b'\x10b' in modem_data:
                    print("silence")
                    cmd = "ATH" + "\r"
                    analog_modem.write(cmd.encode())
                    return
                else:
                    return
                    # print("yes")
            # Terminate the call
            # if not exec_AT_cmd("ATH\r"):
            #   print ("Error: Busy Tone - Failed to terminate the call")
            #  print ("Trying to revoer the serial port")
            # recover_from_error()
            # else:
            #   print ("Busy Tone: Call Terminated")

            if modem_data != b"":
                print (modem_data)

                # Check if <DLE>b is in the stream

                # Check if <DLE>s is in the stream
                if (chr(16) + chr(115)).encode() == modem_data:
                    # Terminate the call
                    if not exec_AT_cmd("ATH\r"):
                        print ("Error: Silence - Failed to terminate the call")
                        print ("Trying to revoer the serial port")
                        recover_from_error()
                    else:
                        print ("Silence: Call Terminated")

                if ("-s".encode() in modem_data) or (("<DLE>-s").encode() in modem_data):
                    print ("silence found during recording")
                    analog_modem.write(("<DLE>-!" + "\r").encode())
                    return


# =================================================================
def read_data_answer():
    global disable_modem_event_listener
    ring_data = b''
    modem_data_striped = b''

    endtime = time.time() + 60.0  # 1minute
    while (time.time() < endtime):
        print("waiting for ring")
        if not disable_modem_event_listener:
            modem_data = analog_modem.readline()

            if (b'RING' in modem_data):

                if b'RING' in modem_data:
                    modem_data_striped = modem_data.rstrip()
                    print("modem_data_striped:  ", modem_data_striped)
                    print("ring_data:  ", ring_data)
                    print("modem_data:  ", modem_data_striped)
                    ring_data = ring_data + modem_data_striped
                    ring_count = ring_data.count(b'RING')
                    print("ring_count:  ", ring_count)
                    if ring_count == 1:
                        pass
                    elif ring_count == RINGS_BEFORE_AUTO_ANSWER:
                        ring_data = b''
                        answer()
                        return

    if not b'RING' in modem_data:
        print ("Error: No Ring")
        close_modem_port()
        return

    # =================================================================


def read_data_call():
    global disable_modem_event_listener
    ring_data = b''
    modem_data_striped = b''

    endtime = time.time() + 60.0  # 1minute
    while (time.time() < endtime):
        print("waiting for ring")
        if not disable_modem_event_listener:
            modem_data = analog_modem.readline()

            if (b'\x10b' in audio_data):
                print("busy tone//")
                if not exec_AT_cmd("\x10!\r", "OK"):
                    print ("Error: Unable to signal end of voice receive state")
                    break;
            if (b'\x10s' in audio_data):
                print("silence tone//")
                if not exec_AT_cmd("\x10!\r", "OK"):
                    print ("Error: Unable to signal end of voice receive state")
                    break;


# =================================================================

# =================================================================
# Close the Serial Port
# =================================================================
def close_modem_port(action):
    # Try to close any active call
    try:
        if action == "call":
            cmd = "ATH" + "\r"
            analog_modem.write(cmd.encode())


        elif action == "answer":
            time.sleep(5)
            cmd = "ATH" + "\r"
            analog_modem.write(cmd.encode())

        print ("Ended the active calls")
    except:
        pass

    # Close the Serial COM Port
    try:
        if analog_modem.isOpen():
            analog_modem.close()
            print ("Serial Port closed...")
    except:
        print ("Error: Unable to close the Serial Port.")
        sys.exit()


# =================================================================


# Main Function
# init_modem_settings()

# Close the Modem Port when the program terminates
# atexit.register(close_modem_port)

# Monitor Modem Serial Port
# read_data()


# =================================================================
# Arg parsing
def main():
    parser = argparse.ArgumentParser(prog='gfg',
                                     description='This a voice modem testing script.')

    parser.add_argument('-o', default=False, help="call/answer", required=True)
    parser.add_argument('-number', nargs='+',
                        help='a mobile number')
    parser.add_argument('-f', help='record/play')

    args = parser.parse_args()
    n = args.number
    action = args.o

    if args.o:
        print("\n Welcome to voice Modem testing ! Checked if i see ne updates\n")
        init_modem_settings()
        if args.o == "call":
            call(n)

        elif args.o == "answer":
            read_data_answer()

    if args.f:
        if args.f == "record":
            time.sleep(3)
            record_audio()
        elif args.f == "play":
            play_audio(action)

    close_modem_port(action)


if __name__ == "__main__":
    main()
