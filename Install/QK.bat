@ECHO OFF
cd "%homepath%\AppData\Roaming\TrainPlayer\Subroutines\QuickKeys-Base"

GOTO S1
:S1
SET /p sMax=Enter the maximum speed for this layout:
SET "var="&for /f "delims=0123456789" %%i in ("%sMax%") do set var=%%i
if defined var GOTO Error
ECHO Max speed set to %sMax%
GOTO End
:Error
ECHO Please enter a number
GOTO S1
:End

GOTO S2
:S2
SET /P sMin=Enter the coupling speed for this layout:
SET "var="&for /f "delims=0123456789" %%i in ("%sMin%") do set var=%%i
if defined var GOTO Error
ECHO Coupling speed set to %sMin%
GOTO End
:Error
ECHO Please enter a number
GOTO S2
:End

type 1.txt > ms.txt
echo %sMax% >> ms.txt
type 2.txt >> ms.txt
echo %sMin% >> ms.txt
type 3.txt >> ms.txt
type ms.txt | clip
