# Python Email Automator
Easy way to automate emails!

# How to use
1. Download this repo as a zip file
2. Follow the steps below

# Getting your token.json
For getting your token.json follow these steps
1. Go to the Google Developers Console at https://console.developers.google.com/
2. Create a new project by clicking on the dropdown next to "Google APIs" and selecting "New Project". Follow the prompts to name your project and select your organization, if applicable.
3. Once your project is created, select it from the dropdown at the top of the screen.
4. Enable the necessary APIs for your project. For example, if you want to use the Gmail API, you should enable the Gmail API for your project. You can do this by clicking on the "Enable APIs and Services" button on the Dashboard page of your project and searching for the API you want to use.
5. Create credentials for your project by clicking on "Credentials" in the left-hand menu and selecting "Create Credentials". Choose "OAuth client ID" and follow the prompts to configure your OAuth consent screen and create your client ID.
6. Download your credentials file (credentials.json) by clicking on the "Download" button next to the client ID you just created.
7. Place your credentials.json file in the same directory as your Python script.
8. Run your Python script to generate your token.json file. You will be prompted to authorize the script to access your Google account. Follow the prompts to authorize   the script and generate your token.json file.

# Getting your credentials.json
1. Go to the Google Cloud Console at https://console.cloud.google.com/.
2. Create a new project by clicking on the project dropdown in the top left corner and clicking "New Project".
3. Give your project a name and click "Create".
4. From the dashboard, navigate to "APIs & Services" in the left-hand menu and click "Dashboard".
5. Click "Enable APIs and Services" at the top of the page.
6. Search for "Gmail API" and click on it.
7. Click "Enable".
8. Click "Create Credentials".
9. Select "Desktop App" or "Other non-UI (e.g. cron job, daemon)" for the "Which API are you using?" and "What data will you be accessing?" questions, respectively.
10. Select "Application data" for "Where will you be calling the API from?".
11. Select "No, I'm not using them" for "Are you planning to use this API with App Engine or Compute Engine?".
12. Enter a name for your OAuth client ID and click "Create".
13. Click "Download" to download your credentials.
14. Rename the downloaded file to credentials.json and place it in the same directory as your Python script.
