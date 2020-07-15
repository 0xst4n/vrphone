import os, subprocess
import PySimpleGUI as sg

INSTALL_TYPE = "CHOCO"

sg.theme('DarkBlue3')	# Add a touch of color
def launch(ip):
    adb_binary = "adb"
    scrcpy_binary = "scrcpy"
    if INSTALL_TYPE == "LOCAL":
        # TODO: navigate to scrcpy install dir
        adb_binary = "./adb.exe"
        scrcpy_binary = "./scrcpy.exe"
        pass
    else:
        DETACHED_PROCESS = 0x08000000
        subprocess.Popen([f"{adb_binary}", "connect", f"{ip}:5555"], creationflags=DETACHED_PROCESS)
        subprocess.Popen([f"{scrcpy_binary}", "-s", f"{ip}:5555", "--window-borderless", "-w", "-b2M", "-m800"], creationflags=DETACHED_PROCESS)

layout = [  [sg.Text('Phone IP'), sg.InputText()],
            [sg.Button('Launch')] ]

window = sg.Window('VRPhone', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    ip = values[0]
    window.close()
    launch(ip)
    break

window.close()



