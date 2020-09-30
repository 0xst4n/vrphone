import os, subprocess, sys
import PySimpleGUI as sg


ip = ''
borderless = False

if (os.path.isfile('settings.txt')):
    with open('settings.txt') as f:
        ip = f.readline().rstrip()
        borderless = f.readline() == "True"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

sg.theme('Reddit')	# Add a touch of color
def launch(ip,borderless):
    adb_binary = resource_path('scrcpy/adb.exe')
    scrcpy_binary = resource_path('scrcpy/scrcpy.exe')

    DETACHED_PROCESS = 0x08000000
    subprocess.Popen([f"{adb_binary}", "connect", f"{ip}:5555"], creationflags=DETACHED_PROCESS)
    args = [f"{scrcpy_binary}", "-s", f"{ip}:5555", "-w", "-b2M", "-m800"]
    if borderless:
        args.append("--window-borderless")
    cmd = subprocess.Popen(args, creationflags=DETACHED_PROCESS)

layout = [  [sg.Text('Phone IP', font='Arial'), sg.InputText(ip)],
            [sg.Checkbox('Window & border less', default=borderless, font='Arial')],
            [sg.Button('Launch', size=(50,3), font=('Arial', 20))] ]

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



