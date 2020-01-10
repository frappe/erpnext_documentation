<!-- add-breadcrumbs -->
# Downloading Backups

In the ERPNext, you can manually download database backup. To get the latest database backup, go to:

> Home > Settings > Download Backups

Backup available for the download is updated in every eight hours. Click on the link to download the backup at a given time.

<img class="screenshot" alt="Download Backup" src="{{docs_base_url}}/assets/img/articles/download-backup-1.png">

By default three latest backups will be available for the download. To change this, click on "Set Number of Backups". This will take you to System Settings where you can set Number of Backups available for download at a time. 

<img class="screenshot" alt="Download Backup" src="{{docs_base_url}}/assets/img/articles/download-backup-2.png">

## Downloading Files Backup

Clicking on Download Files Backup will send an email with links to the backup for both private and public files. [Email](/docs/user/manual/en/setting-up/email) must be configured for this to work.

<img class="screenshot" alt="Download Backup" src="{{docs_base_url}}/assets/img/articles/download-backup-files.png">

## Automating Backups to Cloud Storage

You can also automate your backups to be uploaded directly on a cloud storage platform. Currently, ERPNext supports:

1. Amazon S3
1. [Dropbox](/docs/user/manual/en/erpnext_integration/dropbox-backup)
1. [Google Drive](/docs/user/manual/en/erpnext_integration/google_drive)



