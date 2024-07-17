@echo off

@REM Pull changes that could be made on other machines
git pull

@REM Run the python update and predict commands
@REM Create python virtual environment if it does not exist
if not exist "venv" (
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    deactivate
)

@REM Run the python update and predict scripts
venv\Scripts\activate
python update.py
python predict.py
deactivate

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
