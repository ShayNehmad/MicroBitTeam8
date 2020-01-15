hostMACAddress = '48-F1-7F-00-15-1C'
"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

# hostMACAddress = '00:1f:e1:dd:08:3d' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    print("listening")
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        print("data")
        if data:
            print("yes")
            import vlc
            p = vlc.MediaPlayer("smooth.mp3")
            p.play()
except:
    print("Closing socket")
    client.close()
    s.close()