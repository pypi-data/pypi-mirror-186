#include <Constants.au3>
;
; AutoIt Version: 3.0
; Language:       English

_Example()
Exit
; Finished!

Func _Example()

	WinActivate("Terminal")
	WinWaitActive("Terminal")
	Send("cert candidates{ENTER}")
	Sleep(5000)

	WinActivate("Terminal")
	WinWaitActive("Terminal")
	Send("cert approve{ENTER}")
	Sleep(5000)

EndFunc   ;==>_Example