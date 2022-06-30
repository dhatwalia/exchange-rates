@echo off

@REM Run the python update and predict commands
python update.py
python predict.py

@REM Read the count from file
set /p count=<counter.txt

@REM Prepare the commit message
set message=Update #%count%

@REM Update the count in file
set /a count=%count% + 1
>counter.txt echo %count%

@REM Stage, commit and push the changes
git add .
git commit -m "%message%"
git push
