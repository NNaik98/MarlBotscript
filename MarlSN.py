import os
import subprocess
import psutil
import time


print("\x1b[31mScript created by \x1b[0m")


print("""                                                          
                                                                     
NNNNNNNN        NNNNNNNN                    iiii  kkkkkkkk           
N:::::::N       N::::::N                   i::::i k::::::k           
N::::::::N      N::::::N                    iiii  k::::::k           
N:::::::::N     N::::::N                          k::::::k           
N::::::::::N    N::::::N  aaaaaaaaaaaaa   iiiiiii  k:::::k    kkkkkkk
N:::::::::::N   N::::::N  a::::::::::::a  i:::::i  k:::::k   k:::::k 
N:::::::N::::N  N::::::N  aaaaaaaaa:::::a  i::::i  k:::::k  k:::::k  
N::::::N N::::N N::::::N           a::::a  i::::i  k:::::k k:::::k   
N::::::N  N::::N:::::::N    aaaaaaa:::::a  i::::i  k::::::k:::::k    
N::::::N   N:::::::::::N  aa::::::::::::a  i::::i  k:::::::::::k     
N::::::N    N::::::::::N a::::aaaa::::::a  i::::i  k:::::::::::k     
N::::::N     N:::::::::Na::::a    a:::::a  i::::i  k::::::k:::::k    
N::::::N      N::::::::Na::::a    a:::::a i::::::ik::::::k k:::::k   
N::::::N       N:::::::Na:::::aaaa::::::a i::::::ik::::::k  k:::::k  
N::::::N        N::::::N a::::::::::aa:::ai::::::ik::::::k   k:::::k 
NNNNNNNN         NNNNNNN  aaaaaaaaaa  aaaaiiiiiiiikkkkkkkk    kkkkkkk
                                                                                                                                         
""")
# Function to install a package using pip
def install_package(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])

# Check if psutil is installed
try:
    import psutil
except ImportError:
    print("psutil is not installed. Installing...")
    install_package("psutil")
    import psutil

# Check if PyInstaller is installed
try:
    import PyInstaller
except ImportError:
    print("PyInstaller is not installed. Installing...")
    install_package("pyinstaller")
    import PyInstaller

def find_rocket_league_pids():
    rocket_league_pids = []
    for proc in psutil.process_iter(['pid', 'name']):
        if "rocketleague.exe" in proc.info['name'].lower():
            rocket_league_pids.append(proc.info['pid'])
    return rocket_league_pids

def find_rocket_league_pid():
    rocket_league_pids = find_rocket_league_pids()
    if not rocket_league_pids:
        print("\x1b[31mPlease ensure Rocket League is running.\x1b[0m")
        while True:
            choice = input("\n\x1b[31m1. Try again to find the process\n2. Exit\x1b[0m\n\x1b[32mEnter your choice:\x1b[0m ")
            if choice == '1':
                return find_rocket_league_pid()
            elif choice == '2':
                exit()
            else:
                print("\x1b[31mInvalid choice. Please enter 1 to try again or 2 to exit.\x1b[0m")
    elif len(rocket_league_pids) == 1:
        return rocket_league_pids[0]
    else:
        print("\x1b[31mMultiple Rocket League processes found with the following PIDs:\x1b[0m")
        for i, pid in enumerate(rocket_league_pids):
            print(f"{i+1}. PID: {pid}")
        
        while True:
            choice = input("\x1b[32mChoose the PID of the Rocket League process (enter number):\x1b[0m ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(rocket_league_pids):
                    return rocket_league_pids[choice-1]
                else:
                    print("\x1b[31mInvalid choice. Please enter a number between 1 and", len(rocket_league_pids), "\x1b[0m")
            except ValueError:
                print("\x1b[31mInvalid input. Please enter a number.\x1b[0m")

def find_marlbot_exe():
    found = False
    exe_paths = []

    # Ask user for drive selection
    print("\x1b[34mSearching for Marlbot executable files...\x1b[0m")
    print("\x1b[34mDo you know which drive the Marlbot executable file is located?\x1b[0m")
    drives = [chr(i) + ':' for i in range(65, 91) if os.path.exists(chr(i) + ':')]
    for i, drive in enumerate(drives):
        print(f"\x1b[32m{i+1}. {drive}\x1b[0m")
    print(f"\x1b[32m{len(drives)+1}. Not sure\x1b[0m")

    while True:
        drive_choice = input("\x1b[32mEnter the drive number where Marlbot executable is located:\x1b[0m ")
        try:
            drive_choice = int(drive_choice)
            if 1 <= drive_choice <= len(drives):
                drive_to_search = drives[drive_choice - 1]
                break
            elif drive_choice == len(drives) + 1:
                drive_to_search = None
                break
            else:
                print("\x1b[31mInvalid choice. Please enter a number between 1 and", len(drives), "or", len(drives) + 1, "\x1b[0m")
        except ValueError:
            print("\x1b[31mInvalid input. Please enter a number.\x1b[0m")

    if drive_to_search:
        print(f"\x1b[34mScanning {drive_to_search} drive...\x1b[0m")
        start_time = time.time()
        for root, dirs, files in os.walk(drive_to_search + '\\'):  # Include the root directory of the drive
            for name in files:
                if name.startswith("marlbot") and name.endswith(".exe"):
                    exe_paths.append(os.path.join(root, name))
                    found = True
                    print(f"\x1b[32mFound: {os.path.join(root, name)}\x1b[0m")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\x1b[34mScanning completed in {elapsed_time:.2f} seconds.\x1b[0m")

        # Ask if user wants to search other drives
        while True:
            search_other_drives = input("\x1b[34mDo you want to search other drives? (1 for Yes, 2 for No):\x1b[0m ")
            if search_other_drives == '1':
                find_marlbot_exe()
                return
            elif search_other_drives == '2':
                break
            else:
                print("\x1b[31mInvalid choice. Please enter 1 for Yes or 2 for No.\x1b[0m")
    else:
        for drive in drives:
            print(f"\x1b[34mScanning {drive} drive...\x1b[0m")
            start_time = time.time()
            for root, dirs, files in os.walk(drive + '\\'):  # Include the root directory of the drive
                for name in files:
                    if name.startswith("marlbot") and name.endswith(".exe"):
                        exe_paths.append(os.path.join(root, name))
                        found = True
                        print(f"\x1b[32mFound: {os.path.join(root, name)}\x1b[0m")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"\x1b[34mScanning completed in {elapsed_time:.2f} seconds for {drive} drive.\x1b[0m")

    if not found:
        print("\x1b[31mExecutable files starting with 'marlbot' not found.\x1b[0m")
        return None  # Return None if not found
    elif len(exe_paths) == 1:
        print("\x1b[32mFound:", exe_paths[0], "\x1b[0m")
        return exe_paths[0]  # Return the path
    else:
        print("\x1b[31mMultiple executable files found:\x1b[0m")
        for i, exe_path in enumerate(exe_paths):
            print(f"\x1b[32m{i+1}. {exe_path}\x1b[0m")
        
        while True:
            choice = input("\x1b[32mChoose the version (enter number):\x1b[0m ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(exe_paths):
                    print("\x1b[32mSelected:", exe_paths[choice-1], "\x1b[0m")
                    return exe_paths[choice-1]  # Return the selected path
                else:
                    print("\x1b[31mInvalid choice. Please enter a number between 1 and", len(exe_paths), "\x1b[0m")
            except ValueError:
                print("\x1b[31mInvalid input. Please enter a number.\x1b[0m")

def select_bot():
    print("\x1b[34mSelect the bot to use:\x1b[0m")
    print("\x1b[32m1. Nexto\x1b[0m")
    print("\x1b[32m2. Necto\x1b[0m")
    print("\x1b[32m3. Seer (old version)\x1b[0m")
    print("\x1b[32m4. Element\x1b[0m")
    while True:
        bot_choice = input("\x1b[32mYour choice (1/2/3/4):\x1b[0m ")
        if bot_choice in ['1', '2', '3', '4']:
            return bot_choice
        else:
            print("\x1b[31mInvalid choice. Please enter 1, 2, 3, or 4.\x1b[0m")

def select_arguments():
    print("\x1b[34mSelect additional arguments to add:\x1b[0m")
    print("\x1b[32m1. Kickoff (Uses Element bot kickoff)\x1b[0m")
    print("\x1b[32m2. Minimap (Shows the minimap)\x1b[0m")
    print("\x1b[32m3. Monitor (Enable monitoring)\x1b[0m")
    print("\x1b[32m4. Clock (Enables to run over 120fps)\x1b[0m")
    print("\x1b[32m5. Debug keys (Displays the labels of the pressed keys)\x1b[0m")
    print("\x1b[32m6. Debug (for dev purpose only)\x1b[0m")
    print("\x1b[32m7. Skip\x1b[0m")
    while True:
        arg_choice = input("\x1b[32mYour choice (1/2/3/4/5/6/7):\x1b[0m ")
        if arg_choice in ['1', '2', '3', '4', '5', '6', '7']:
            return arg_choice
        else:
            print("\x1b[31mInvalid choice. Please enter a number between 1 and 7.\x1b[0m")

def add_additional_arguments():
    arguments = []
    while True:
        arg_choice = select_arguments()
        if arg_choice == '7':
            break
        else:
            arguments.append(arg_choice)
            while True:
                add_more = input("\x1b[32mDo you want to add another argument? (1 for Yes, 2 for No):\x1b[0m ")
                if add_more == '1':
                    break
                elif add_more == '2':
                    return arguments
                else:
                    print("\x1b[31mInvalid choice. Please enter 1 for Yes or 2 for No.\x1b[0m")
    return arguments

# Check for Rocket League process
rocket_league_pid = find_rocket_league_pid()
if rocket_league_pid:
    print("\x1b[32mRocket League process found with PID:", rocket_league_pid, "\x1b[0m")
else:
    print("\x1b[31mPlease ensure Rocket League is running.\x1b[0m")
    while True:
        choice = input("\n\x1b[31m1. Try again to find the process\n2. Exit\x1b[0m\n\x1b[32mEnter your choice: \x1b[0m")
        if choice == '1':
            rocket_league_pid = find_rocket_league_pid()
            if rocket_league_pid:
                print("\x1b[32mRocket League process found with PID:", rocket_league_pid, "\x1b[0m")
                break
        elif choice == '2':
            exit()
        else:
            print("\x1b[31mInvalid choice. Please enter 1 to try again or 2 to exit.\x1b[0m")

# Search for Marlbot executables
marlbot_exe_path = find_marlbot_exe()

# Check if exe_path is None
if marlbot_exe_path is None:
    print("\x1b[31mNo executable file found. Exiting.\x1b[0m")
    exit()

# Select bot
selected_bot = select_bot()
bot_names = {
    '1': 'nexto',
    '2': 'necto',
    '3': 'seer',
    '4': 'element'
}
selected_bot_name = bot_names[selected_bot]
print("\x1b[32mSelected bot:", selected_bot_name, "\x1b[0m")

# Add additional arguments
additional_arguments = add_additional_arguments()

# Get the directory of the executable file
exe_dir = os.path.dirname(marlbot_exe_path)

# Change the current working directory to the directory containing the executable
os.chdir(exe_dir)

# Print the current working directory
print("\x1b[34mCurrent directory:", os.getcwd(), "\x1b[0m")

# Initialize command as a list
command = [marlbot_exe_path, '-p', str(rocket_league_pid), '-b', selected_bot_name]

# Mapping of argument numbers to their corresponding names
arg_names = {
    '1': '--kickoff',
    '2': '--minimap',
    '3': '--monitoring',
    '4': '--clock',
    '5': '--debug-keys',
    '6': '--debug',
    '7': '--skip'
}

# Modify the section where you build the command
command = f'{marlbot_exe_path} -p {rocket_league_pid} -b {selected_bot_name}'
if additional_arguments:
    for arg in additional_arguments:
        command += f' {arg_names[arg]}'

# Print the command
print("\x1b[34mCommand:", command, "\x1b[0m")

# Execute the command
subprocess.run(command, shell=True)
