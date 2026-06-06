echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\ANSYSS~1\v261\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\ANSYSS~1\v261\fluent\ntbin\win64\tell.exe" DESKTOP-EEIK6UR 56621 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\ANSYSS~1\v261\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="DESKTOP-EEIK6UR" (%KILL_CMD% 32972) 
if /i "%LOCALHOST%"=="DESKTOP-EEIK6UR" (%KILL_CMD% 29368) 
if /i "%LOCALHOST%"=="DESKTOP-EEIK6UR" (%KILL_CMD% 13508) 
if /i "%LOCALHOST%"=="DESKTOP-EEIK6UR" (%KILL_CMD% 31108) 
if /i "%LOCALHOST%"=="DESKTOP-EEIK6UR" (%KILL_CMD% 34080) 
if /i "%LOCALHOST%"=="DESKTOP-EEIK6UR" (%KILL_CMD% 15108)
del "C:\Users\Mateus\OneDrive\Documentos\UnB\4 sem\Projetos\Cold plate\cleanup-fluent-DESKTOP-EEIK6UR-34080.bat"
