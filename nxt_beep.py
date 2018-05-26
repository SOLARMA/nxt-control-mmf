# Program to make NXT brick beep using NXT Python with Bluetooth socket
#
# Simon D. Levy  CSCI 250   Washington and Lee University    April 2011

# Change this ID to match the one on your brick.  You can find the ID by doing Settings / NXT Version.  
# You will have to put a colon between each pair of digits.
ID = '00:16:53:05:15:50'

# This is all we need to import for the beep, but you'll need more for motors, sensors, etc.
from nxt.bluesock import BlueSock

# Create socket to NXT brick
sock = 	BlueSock(ID)


# Connect to brick
brick = sock.connect()

# Play tone A above middle C for 1000 msec
brick.play_tone_and_wait(440, 1000)

# Close socket
sock.close()

# EOF
