@echo off
set venv=%CD%\venv\Scripts
cd sibooru
%venv%\gearbox serve
pause