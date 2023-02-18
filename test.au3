; A simple custom messagebox that uses the MessageLoop mode

#include <Constants.au3>
#include <GUIConstantsEx.au3>
#include <Array.au3>

_Main()
Exit

Func _Main()
	$hGUI = GUICreate("MyGUI", 384, 200, 793, 464)
	GUISetOnEvent($GUI_EVENT_CLOSE, "_onExitMain")

	$Edit_1 = GUICtrlCreateEdit("", 7, 10, 171, 121)
	GUICtrlSetFont(-1, 24)
	$Button_1 = GUICtrlCreateButton("Start", 60, 150, 80, 40)
	$Button_2 = GUICtrlCreateButton("Cancel", 210, 150, 80, 40)

	$Group_1 = GUICtrlCreateGroup("", 185, 8, 180, 35)
	$Radio_1 = GUICtrlCreateRadio("LP1", 193, 18, 51, 20)
	$Radio_2 = GUICtrlCreateRadio("LP2", 252, 18, 51, 20)
	$Radio_3 = GUICtrlCreateRadio("LP3", 311, 18, 41, 20)
	GUICtrlCreateGroup("", -99, -99, 1, 1)

	$Group_2 = GUICtrlCreateGroup("", 185, 39, 180, 35)
	$Radio_4 = GUICtrlCreateRadio("LP1", 193, 49, 41, 20)
	$Radio_5 = GUICtrlCreateRadio("LP2", 252, 49, 41, 20)
	$Radio_6 = GUICtrlCreateRadio("LP3", 311, 49, 61, 20)
	GUICtrlCreateGroup("", -99, -99, 1, 1)

	$Group_3 = GUICtrlCreateGroup("", 185, 70, 180, 35)
	$Radio_7 = GUICtrlCreateRadio("LP1", 193, 80, 51, 20)
	$Radio_8 = GUICtrlCreateRadio("LP2", 252, 80, 51, 20)
	$Radio_9 = GUICtrlCreateRadio("LP3", 312, 80, 51, 20)
	GUICtrlCreateGroup("", -99, -99, 1, 1)

	GUISetState() ; display the GUI

	Local $iMsg
	Do
		$iMsg = GUIGetMsg()

		Select
		Case $iMsg = $Button_1
			;ConsoleWrite(GUICtrlRead($Edit_1))
			;~ ConsoleWrite(GUICtrlRead(GUICtrlCreateGroup))
			$text = GUICtrlRead($Edit_1)
			If $text == "" Then
				MsgBox($MB_ICONERROR, "Error", "Please put something, the Text is empty!!!!!!!")
			Else
				Local $totalArr[0]
				$split = StringSplit($text, @CRLF)
				For $i = 1 to $split[0]
					Local $tempArr[1]
					If $split[$i] == "" Then
						ContinueLoop
					Else
						;Consolewrite("$split["&$i&"] = "&$split[$i]&@CRLF)
						_ArrayPush($tempArr, $split[$i])
						_ArrayAdd($totalArr, $tempArr)
					EndIf
				Next

				;~ _ArrayDisplay($totalArr, "all item need to prepare")
				For $i = 0 to UBound($totalArr) - 1
					Consolewrite(""&$i&" = "&$totalArr[$i]&@CRLF)
				Next



				; if checkbox Select
				If GUICtrlRead($Radio_1) == 1 Then
					MsgBox($MB_SYSTEMMODAL, "", "Value might be hexadecimal!")
				Else
				#Au3Stripper_Ignore_Variables	MsgBox($MB_SYSTEMMODAL, "", "Value is a string.")
				EndIf
			EndIf



			_start()

		EndSelect
	Until $iMsg = $GUI_EVENT_CLOSE Or $iMsg = $Button_2
EndFunc   ;==>_Main


Func _start()
	;MsgBox(0, "au", "testes", 10)

	ConsoleWrite("test")
EndFunc

Func _onExitMain()
	GUIDelete()
	Exit
EndFunc   ;==>_onExitMain
