# ITHOWTOO Startup Script

# Load modules:
import os
import webbrowser

## VPN
# Connect to VPN
openvpn =r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --connect config.ovpn'
os.system(openvpn)

## Chrome
url = 'https://github.com/ithowtoo/' # Open Github
url1 = 'https://www.ithowtoo.com/' # Open ithowtoo.com
url2 = 'https://mail.google.com/' # Open Gmail:
url3 = 'www.google.co.uk' # Open Google:
webbrowser.open_new(url)
webbrowser.open_new(url1)
webbrowser.open_new(url2)
webbrowser.open_new(url3)

## WSL2

# Open New Window
os.startfile("wsl")

## Outlook
# Scrape new emails

# Open Outlook
os.startfile("outlook")

## Open Slack
# Replace USERNAME wit real username
slack =r'"C:\Users\USERNAME\AppData\Local\slack\slack.exe"'
os.startfile(slack)

## Open Teams
os.startfile(r"C:\Users\NB250346\AppData\Local\Microsoft\Teams\current\Teams.exe")
