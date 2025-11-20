' Create AI Hub Shortcut in Start Menu (for taskbar pinning)
' This script creates a shortcut that can be pinned to the taskbar

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Define paths
strDesktop = objShell.SpecialFolders("AllUsersDesktop")
strStartMenu = objShell.SpecialFolders("AllUsersStartMenu")
strBatFile = "D:\AI-HUB 2 Claude\run_ai_hub.bat"
strProjectDir = "D:\AI-HUB 2 Claude"

' Create Desktop Shortcut
Set objLink = objShell.CreateShortcut(strDesktop & "\AI Hub.lnk")
objLink.TargetPath = strBatFile
objLink.WorkingDirectory = strProjectDir
objLink.Description = "AI Hub - AI Assistant Application"
objLink.WindowStyle = 1
objLink.Save

WScript.Echo "Desktop shortcut created!"

' Create Start Menu Shortcut
Set objLink2 = objShell.CreateShortcut(strStartMenu & "\AI Hub.lnk")
objLink2.TargetPath = strBatFile
objLink2.WorkingDirectory = strProjectDir
objLink2.Description = "AI Hub - AI Assistant Application"
objLink2.WindowStyle = 1
objLink2.Save

WScript.Echo "Start Menu shortcut created! You can now pin it to the taskbar."
WScript.Echo "To pin to taskbar: Right-click the shortcut and select 'Pin to taskbar'"

