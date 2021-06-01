# Ainthiram
Multi Linguistic OCR converter from Bulk pdf to Text. integrated with Google API

# API Setup
Create a new project for this tool to access your Google drive
Visit https://console.developers.google.com/ , create project, name it anything you like, ex: gdcmdtools.
Enable the following Google APIs in "APIs & auth/APIs"
Drive API

# Fusion Tables API
Make sure your application has an application name in "APIs & auth/Credentials/OAuthConsent screen"
Find "PRODUCT NAME" field. Make sure it's not blank.
Grant access to Google Drive for gdcmdtools in "APIs & auth/Credentials"
Click "Create new Client ID", APPLICATION TYPE: Installed application, INSTALLED APPLICATION TYPE: Other
Check the section "Client ID for native application", click at the "Download JSON".

# Requirements or How to install
1. Python 3.0 (Download from here : https://www.python.org/downloads/)
2. Image Magick (Download from here : https://imagemagick.org/script/download.php)
3. Ghost Script (https://www.ghostscript.com/download.html)
4. PIP 3 (For package install : First Run "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py" in cmd and Second : "py get-pip.py"
5. Requirements (Attached with Repo) (Just run pip install -r requirements.txt)
