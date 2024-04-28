import subprocess
import time
import keyboard

def send_key_event(key):
    # # Command to send key event via adb
    # command = f"adb shell input keyevent {key_event}"

    print("")
    for i in range(4):    
        print(key[i])
        command = f"adb shell input text '" +str(key[i])+"'"
        subprocess.run(command, shell=True)
        

    # command = f"adb shell input keyevent 66"
    # subprocess.run(command, shell=True)
    time.sleep(0.3)
    for j in range(4):
        command = f"adb shell input keyevent 20"
        subprocess.run(command, shell=True)
    
    command = f"adb shell input keyevent 66"    
    subprocess.run(command, shell=True)
    
pause =False
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for m in range(10):
                send_key_event([i,j,k,m])
                
