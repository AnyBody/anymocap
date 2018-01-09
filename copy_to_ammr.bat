IF "%1" =="" (
  set AMMRPATH=%USERPROFILE%\Documents\AMMRs\ammr
) ELSE (
  set AMMRPATH=%1
)

rmdir /s /q %AMMRPATH%\Application\MocapExamples\
rmdir /s /q %AMMRPATH%\Tools\AnyMocap\
rmdir /s /q %AMMRPATH%\Tests\AnyMocap\

xcopy /s /y Examples %AMMRPATH%\Application\MocapExamples\
xcopy /s /y Model %AMMRPATH%\Tools\AnyMocap\
xcopy /s /y Tests %AMMRPATH%\Tests\AnyMocap\

pause
