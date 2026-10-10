Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\TCM\acupuncture_app"
WshShell.Run "D:\TCM\acupuncture_app\launch_app.bat", 0, False
Set WshShell = Nothing
