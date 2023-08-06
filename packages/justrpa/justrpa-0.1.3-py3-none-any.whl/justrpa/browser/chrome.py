import os
import subprocess
import platform
import psutil

# todo: doublecheck: multiple platform handle 

def RunAsAdmin(path_to_file,*args):
    cmd = r'Powershell -Command "Start-Process "'+path_to_file+'"' + ' -ArgumentList @('+str(args)[1:-1]+')'+ ' -Verb RunAs"'
    print(cmd)
    os.system(cmd)

def RunByPowershell(path_to_file,*args):
    cmd = r'Powershell -Command "Start-Process "'+path_to_file+'"'+ ' -ArgumentList @('+str(args)[1:-1]+')"' 
    print(cmd)
    os.system(cmd)

def kill_process_as_admin(process_name:str):
    RunAsAdmin('taskkill','/F','/T','/IM', process_name)

def kill_process(process_name:str):
    cmd_map = {
        "Windows": f"taskkill /F /T /IM {process_name}",
        "Linux": f"killall -9 {process_name}",
        "Darwin": f"pkill -f  {process_name}"
    }
    system = platform.system()
    cmd = cmd_map[system]
    print(f"system:{system}, cmd:{cmd}")
    subprocess.call(cmd, shell=True)

def kill_all_chrome():
    proc_map = {
        "Windows": ["CHROME.EXE", "CHROMEDRIVER.EXE"],
        "Linux": ["chrome", "chromedriver"],
        "Darwin": ["Chrome", "chromedriver"]
    }
    system = platform.system()
    for proc in proc_map[system]:
        kill_process(proc)
        if check_process_exists(proc):
            print(f"warning: process {proc} still exists. kill failed.")
            if system == "Windows":
                print("Retry with windows runas admin")
                kill_process_as_admin(proc)
                if check_process_exists(proc):
                    print(f"warning: process {proc} still exists. kill failed.")
                else:
                    print(f"kill {proc} success")
        else:
            print(f"kill {proc} success")

def does_chrome_exists():
    proc_map = {
        "Windows": ["CHROME.EXE"],
        "Linux": ["chrome"],
        "Darwin": ["Chrome"]
    }
    system = platform.system()
    any_exists = False
    for proc in proc_map[system]:
        any_exists = any_exists or check_process_exists(proc)
    return any_exists

def clean_up_chrome():
    kill_all_chrome()
    return does_chrome_exists()==False

def check_process_exists(exename:str):
    for proc in psutil.process_iter(['pid', 'name']):
        # This will check if there exists any process running with executable name
        if proc.info['name'].lower() == exename.lower():
            return True
    return False

def start_chrome_windows(clean=False):
    if clean:
        cleaned = clean_up_chrome()
        if cleaned==False:
            print(f"!!warning: cleanup failed ...")
            print(f"!!warning: can't start new chrome due to cleanup failed ...")
            return False
    if does_chrome_exists():
        print(f"Chrome already exists. Skip launch new chrome.")
        return True
    # cmd =  "start Chrome --remote-debugging-port=9222 --kiosk-printing --start-maximized --disable-dev-shm-usage --disable-web-security --allow-running-insecure-content"
    # print(f"run cmd:{cmd}")
    # subprocess.call(cmd, shell=True)
    RunByPowershell('Chrome', '--remote-debugging-port=9222', '--kiosk-printing', '--start-maximized', '--disable-dev-shm-usage', '--disable-web-security', '--allow-running-insecure-content')
    return does_chrome_exists()==True

