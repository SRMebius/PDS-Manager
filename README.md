# PDS-Manager
A simple software for storing and managing Account Username and Password
# Executable Program（Windows）
1. Run "Install.bat".
2. Find the folder in ".\dist\main", and copy to where you want.
3. Run "main.exe" in the folder.
# Usage
1. Run "main.py" or "main.exe" if you'v generated.
2. Sign in by using the "registration code"
3. Log in without username(UN) and password(PW) the first time.
4. Insert the UN and PW in the row of "PDS Manager", and remember to use such UN and PW for the next time of logging in. (Recommended)
5. Saving your manipulation before quit.
# Notes
The "serial number" is created according to the CPU serial number, and transferred to ASCII code.
The "registration code" is generated based on base64 by encoding the CPU serial number.
You can just obtain the CPU serial number by yourself, or by decoding the "serial number". 
