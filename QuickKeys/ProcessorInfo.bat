wmic path win32_processor get CurrentClockSpeed, DeviceID, MaxClockSpeed, Name, NumberOfCores /format:LIST |more > %homepath%\AppData\Roaming\TrainPlayer\Reports\ProcessorInfo.txt
