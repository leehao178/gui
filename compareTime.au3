#include <Date.au3>

; determine how many days a file was created.
MsgBox ( 0, "", "Number of days since creation : " & _DateDiff ( 'd', _ConvertTimeFormat ( FileGetTime ( "c:\boot.ini", 1, 1 ) ), _NowCalc ( ) ) )

; determine the difference in days of creation between two files.
MsgBox ( 0, "", "Number of days between this 2 files : " & _DateDiff ( 'd', _ConvertTimeFormat ( FileGetTime ( @WindowsDir & "\explorer.exe", 1, 1 ) ), _ConvertTimeFormat ( FileGetTime ( "c:\boot.ini", 1, 1 ) ) ) )


Func _ConvertTimeFormat ( $_FileTime ) ; convert 20100716213616 string time format to this time format YYYY/MM/DD HH:MM:SS
    Return StringMid ( $_FileTime, 1 , 4 ) & '/' & StringMid ( $_FileTime, 5 , 2 ) & '/' & StringMid ( $_FileTime, 7 , 2 ) & _
    ' ' & StringMid ( $_FileTime, 9 , 2 ) & ':' & StringMid ( $_FileTime, 11 , 2 ) & ':' & StringMid ( $_FileTime, 13 , 2 )
EndFunc ;==> _ConvertTimeFormat ( )
