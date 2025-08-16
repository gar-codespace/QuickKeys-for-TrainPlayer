@echo off

set "qktDir=%homepath%\AppData\Roaming\TrainPlayer\Subroutines\QuickKeys\"
xcopy %cd% %qktDir% /H /S /C /Y

set "sourceFile=%homepath%\AppData\Roaming\TrainPlayer\Subroutines\QuickKeys\qkSupport\PressX.txt"
xcopy %sourceFile% %qktDir% /C /Y

set "sourceFile=%homepath%\AppData\Roaming\TrainPlayer\Subroutines\QuickKeys\qkSupport\PressY.txt"
xcopy %sourceFile% %qktDir% /C /Y

set "sourceFile=%homepath%\AppData\Roaming\TrainPlayer\Subroutines\QuickKeys\qkSupport\PressZ.txt"
xcopy %sourceFile% %qktDir% /C /Y

set "dksDir=%cd%\dkSupport\"
set "dktDir=%homepath%\AppData\Roaming\TrainPlayer\Cartypes\Defaults\"
xcopy %dksDir% %dktDir% /H /S /C /Y

md "%homepath%\AppData\Roaming\TrainPlayer\Reports"
md "%homepath%\AppData\Roaming\TrainPlayer\Reports\Scanners"

wmic path win32_processor get CurrentClockSpeed, DeviceID, MaxClockSpeed, Name, NumberOfCores /format:LIST |more > %homepath%\AppData\Roaming\TrainPlayer\Reports\ProcessorInfo.txt