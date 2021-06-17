<!-- add-breadcrumbs -->

# Upload Backups to Amazon S3

## Prerequisites

- [Email Account](/docs/v13/user/manual/en/setting-up/email/email-account)

    To receive emails for failed and successful backups, please create an **Email Account** first.

## Create S3 bucket and set up access

1. Create a new s3 bucket.

    In the bucket settings, enable "Block all public access" to keep your data private. Feel free to enable encryption, versioning or object lock as per your requirements (please refer to [Amazon's documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)).

2. Open Identity and Access Management (IAM).

    1. Create a new policy for the Service "S3", allowing the Actions "ListBucket" and "PutObject".

    2. Create a new user for programmatic access.

        ![Screenshot of "Add User" in AWS](/docs/v13/assets/img/erpnext_integrations/s3_backup_add_user.png)

    3. Attach the policy you created to the new user.

    4. Copy the user's access key and secret.

To automatically delete old backups or move them to a cheaper storage class, have a look at [lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

## Set up ERPNext

- Open **S3 Backup Settings**.
- Check "Enable Automatic Backup".
- Paste the access key and secret from AWS.
- Set an email address to receive a notification when a backup fails. If you would like an email for successful backups as well, enable "Send Email for Successful Backup".
- Specify the name of the bucket that you created in step 1.
- Choose how often you want to take and upload backups. This can range from monthly to daily. If you only want to take manual backups, set the frequency to "None".

![S3 Backup Settings in ERPNext](/docs/v13/assets/img/erpnext_integrations/s3_backup_settings.png)
