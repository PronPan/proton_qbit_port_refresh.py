import os
import re
import time
import traceback
import psutil

"""
This is my take on the problem. 
The Script checks if you have an instance of qBitTorrent currently running and stops it if there is one. 
Then the port is read from the ProtonVPN logs and the qBit settings are changed.
In the end qBitTorrent is restarted.
"""

# Set up file paths
config_file = os.getenv('APPDATA') + "\\qBittorrent\\qBittorrent.ini"
log_file = os.getenv('LOCALAPPDATA') + "\\ProtonVPN\\Logs\\app-logs.txt"

def killQBit():
	qBit_running = True
	while qBit_running:
		qBit_running = False
		for proc in psutil.process_iter():
			try:
				if proc.name() == "qbittorrent.exe":
					proc.terminate()
					qBit_running = True
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass
		if qBit_running:
			print("Instances found, Terminating now! Next check in three seconds.")
			time.sleep(3)
		else:
			print("No instances found, starting qBitTorrent")

def searchPort() -> str:
	port_number = ""
	with open(log_file, "r") as f:
		log_content = f.readlines()
		for line in reversed(log_content):
			match = re.search(r"Port pair (\d{1,5})", line)
			if match:
				port_number = match.group(1)
				break
	return port_number


# Replace the port number in the qBittorrent config file
def qBitSettings(port_number):
	if port_number:
		with open(config_file, "r") as f:
			config_content = f.read()

		with open(config_file, "w") as f:
			for line in config_content.splitlines():
				if line.startswith("Session\\Port="):
					f.write("Session\\Port=" + port_number)
					print("Port set")
				else:
					f.write(line)
				f.write("\n")


def startQBit():
	qbittorrent_exe = "C:\\Program Files\\qBittorrent\\qbittorrent.exe"
	if os.path.exists(qbittorrent_exe):
		os.startfile(qbittorrent_exe)
		print("Start qBitTorrent")
	else:
		print("Error: qBittorrent executable not found.")

def main() -> int:
	# kill qBitTorrent
	killQBit()

	# search for the port
	try:
		port = searchPort()
	except FileNotFoundError:
		print("ERROR: ProtonVPN log file not found")
		return -1
	if port == "":
		print("ERROR: Port not found in ProtonVPN log file")
		return -2
	print("Port: " + port)

	# set port in qBit settings
	try:
		qBitSettings(port)
	except FileNotFoundError:
		print("ERROR: qBitTorrent settings file not found")
		return -3

	# start qBitTorrent
	try:
		startQBit()
	except Exception as e:
		print("ERROR: Failed to start qBitTorrent")
		return -4
	
	return 0

# keep console window open, if there was an error
try:
	return_code = main()
except Exception as e:
	traceback.print_exc() 
	return_code = -5

if return_code < 0:
	print("\npress <ENTER> to close the window")
	input()