@echo off

pyinstaller main.py --noconsole --hidden-import PySide2.QtXml --icon="logo.ico"
copy "%cd%\pds.pkl" "%cd%\dist\main\pds.pkl"
copy "%cd%\reg.dll" "%cd%\dist\main\reg.dll"
copy "%cd%\logo.*" "%cd%\dist\main\logo.*"
xcopy "%cd%\UIs" "%cd%\dist\main\UIs\"