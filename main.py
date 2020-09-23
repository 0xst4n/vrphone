import os, subprocess
import PySimpleGUI as sg

INSTALL_TYPE = "CHOCO"

ip = ''
borderless = False

if (os.path.isfile('settings.txt')):
    with open('settings.txt') as f:
        ip = f.readline().rstrip()
        borderless = f.readline() == "True"



sg.theme('DarkBlue3')	# Add a touch of color
def launch(ip,borderless):
    adb_binary = "adb"
    scrcpy_binary = "scrcpy"
    if INSTALL_TYPE == "LOCAL":
        # TODO: navigate to scrcpy install dir
        adb_binary = "./adb.exe"
        scrcpy_binary = "./scrcpy.exe"
        pass
    else:
        DETACHED_PROCESS = 0x08000000
        subprocess.Popen([f"{adb_binary}", "connect", f"{ip}:5555"])
        args = [f"{scrcpy_binary}", "-s", f"{ip}:5555", "-w", "-b2M", "-m800"]
        if borderless:
            args.append("--window-borderless")
        cmd = subprocess.Popen(args, creationflags=DETACHED_PROCESS)

layout = [  [sg.Text('Phone IP'), sg.InputText(ip)],
            [sg.Checkbox('Window & border less', default=borderless)],
            [sg.Button('Launch')] ]

window = sg.Window('VRPhone', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    ip = values[0]
    borderless = values[1]

    window.close()

    f = open("settings.txt", "w")
    f.write(ip)
    f.write("\n")
    f.write(str(borderless))
    f.close()

    launch(ip, borderless)
    break

window.close()



