@echo off
virtualenv venv
set venv=%CD%\venv\Scripts
cd sibooru
%venv%\pip install tg.devtools
%venv%\pip install -e .
echo -----
echo Done!
pause