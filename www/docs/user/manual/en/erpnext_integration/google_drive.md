<!-- add-breadcrumbs -->
# Google Drive Integration

ERPNext provides an integration with Google Drive in order for all users to backup their data to Google Drive.


## How to set up Google Drive Integration

In order to allow a ERPNext to upload backups to Google Drive, you need to authorize ERPNext to upload files to Google Drive. Google Drive Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/docs/user/manual/en/erpnext_integration/google_settings).
- In the Google Drive list, click on New. Enter the Backup folder name to save backups to Google Drive, the backup frequency and the email of the person to whom email is sent notifying the status of the backup and then save it. Now click on **Authorize Drive Access** to authorize ERPNext to push files to Google Drive.
- Once Authorized, you can save your backup to Google Drive.

## How to use Google Drive Integration

### Uploading backup to Google Drive
- Once Google Drive Integration is succesful, you can upload the system backup as well as all your public and private files to Google Drive.
- To backup data to Google Drive, click on **Take Backup**. Backup process will run in the background and you will be notified regarding the backup status.
  <img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_drive.gif">
