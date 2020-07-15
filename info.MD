# Having your phone screen in VR

	1. Plug in phone into PC
	2. Enable ADB debugging in developer settings
	3. Download scrcpy-win64-* from https://github.com/Genymobile/scrcpy/releases/
	4. Unzip and run ./scrcpy.exe
	5. In your VR overlay app open the scrcpy window.

# Using WiFi
	1. Enable ADB over WiFi in Android settings
	2. adb connect PHONE_IP:5555 in scrcpy folder (Trust PC on android device if needed)
	3. scrcpy --window-borderless -b2M -m800
