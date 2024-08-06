import os
import re
import shutil
import time
import psutil

# Set up file paths
config_file = r"C:\Users\****YOUR_USERNAME****\AppData\Roaming\qBittorrent\qBittorrent.ini"
log_file = r"C:\Users\****YOUR_USERNAME****\AppData\Local\ProtonVPN\Logs\app-logs.txt"

# Custom error message
error_message = "An error occured:"

# Define function to simulate the passage of time
def simulate_time_passage(decimal_count):
    for i in range(decimal_count, 0, -1):
        print("." * i)
        time.sleep(1)

# Check if programs are open
print("Checking program status...")
time.sleep(2)  # TIME_SIMULATION
print(".")

programs_running = False
process_names = ["openvpn.exe", "qbittorrent.exe", "ProtonVPN.exe", "ProtonVPNService.exe"]

for proc in psutil.process_iter():
    try:
        if proc.name() in process_names:
            if proc.name() == "openvpn.exe":
                proc.kill()
            elif proc.name() == "qbittorrent.exe":
                proc.terminate()
            elif proc.name() == "ProtonVPN.exe":
                proc.kill()
            elif proc.name() == "ProtonVPNService.exe":
                proc.kill()
            programs_running = True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if programs_running:
    print("Instances found. Terminating now...")
    time.sleep(3)  # Wait for 5 seconds before moving on

    for proc in psutil.process_iter():
        try:
            if proc.name() in process_names:
                if proc.name() == "openvpn.exe":
                    proc.kill()
                elif proc.name() == "qbittorrent.exe":
                    proc.terminate()
                elif proc.name() == "ProtonVPN.exe":
                    proc.kill()
                elif proc.name() == "ProtonVPNService.exe":
                    proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    time.sleep(1)  # TIME_SIMULATION
    print(".")
    
else:
    print("No instances found. Programs ready to start.")
    time.sleep(1)
    print(".")

# Start ProtonVPN
print("Initializing ProtonVPN...")
os.startfile(r"C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe")
time.sleep(5)  # TIME_SIMULATION
print(".")
time.sleep(5)  # TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")

# Wait for log file to be updated
print("Waiting to establish connection...")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
time.sleep(1) # **NECESSARY** TIME_SIMULATION
print(".")
print("Verifying the log file was updated...")
time.sleep(2) # **NECESSARY** TIME_SIMULATION
print(".")

# Search the log file for the most recent port number
print("Searching for the most recent port number...")
time.sleep(3)  # TIME_SIMULATION

port_number = ""
with open(log_file, "r") as f:
    log_content = f.readlines()
    for line in reversed(log_content):
        match = re.search(r"Port pair (\d{1,5})", line)
        if match:
            port_number = match.group(1)
            print(".")
            print(f"Found port number: {port_number}")
            break
            
simulate_time_passage(1)  # TIME_SIMULATION

# Replace the port number in the qBittorrent config file
if port_number:
    with open(config_file, "r") as f:
        config_content = f.read()
    # Use a negative lookahead assertion to exclude WebUI\Port from the search pattern
    pattern = r"(?<!WebUI\\Port=)(Advanced\\trackerPort=|Session\\Port=)\d{1,5}"
    config_content = re.sub(pattern, f"\\g<1>{port_number}", config_content)
    with open(config_file, "w") as f:
        f.write(config_content)
    print("Replacing port number in qBittorrent config file...")
    simulate_time_passage(1) #TIME_SIMULATION
    print("Port updated successfully. Starting qBittorrent...")
    
simulate_time_passage(1)  # TIME_SIMULATION

# Start qBittorrent
qbittorrent_exe = r"C:\Program Files\qBittorrent\qbittorrent.exe"
if os.path.exists(qbittorrent_exe):
    os.startfile(qbittorrent_exe)
else:
    print("Error: qBittorrent executable not found.")

# Check for errors
errors = []
if not port_number:
    errors.append("Error: Port number not found in log file.")
if errors:
    print(error_message)
    for e in errors:
        print(e)
else:
        print("Done!")
                       
time.sleep(3)
print("X_X")
time.sleep(1)
exit
