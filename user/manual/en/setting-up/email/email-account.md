<!-- add-breadcrumbs -->
# Email Account

**You can sync your email account with ERPNext to send and receive emails from ERPNext.**

You can manage multiple incoming and outgoing Email Accounts in ERPNext. There has to be at least one default outgoing account and one default incoming account. If you are on the ERPNext cloud, the default outgoing email is set by us.

To access Email Accounts, go to:
> Home > Settings > Email Account

## 1. Prerequisites
Before creating an Email Account, you need an [Email Domain](/docs/user/manual/en/setting-up/email/email-domain). However, you can skip creating an Email Domain if you're using one of the services listed [here](/docs/user/manual/en/setting-up/email/email-inbox#2-create-an-email-domain).

## 2. How to create an Email Account
1. Go to the Email Account list, click on New.
1. Enter the email address with the domain. [Domains](/docs/user/manual/en/setting-up/email/email-domain) need to be created in order to create an email account.
    You don't need to create a domain if you're syncing an email from certain providers as listed [here](/docs/user/manual/en/setting-up/email/email-inbox#2-create-an-email-domain).
1. Enter the email account password.
1. Save.
If the credentials are correct, the email account will be synced.

> Note: For some services like Gmail, you may need to turn on the settings to allow less secure apps.

### 2.1 Additional options when creating an Email Account
1. **Use Different Email Login ID**: To use an alternative email login and password to access this account. For example, if you have notifications@example.com and you want users to access this email with an alternate email ID, they should tick this checkbox. The recipients will see notifications@example.com as the sender.
1. **Awaiting password**: If you're creating this account on behalf of someone and the password is unknown, tick this checkbox. When the other user logs in, they'll be prompted to enter the password.
1. **Use ASCII encoding for password**: Ticking this will use ASCII encoding for the password.

## 3. Configuration of the Email Account
### 3.1 Default Email Accounts

ERPNext will create templates for a bunch of email accounts by default. Not all of them are enabled. To enable them, you must set valid email account details.

There are two types of email accounts, outgoing and incoming. Outgoing email accounts use an SMTP service to send emails and emails are retrieved from your inbox using an IMAP or POP. Most email providers such as Gmail, Outlook, or Yahoo provide these services.

<img class="screenshot" alt="Defining Criteria" src="{{docs_base_url}}/assets/img/setup/email/email-account-list.png">

### 3.2 Incoming Email Accounts

To set up an incoming Email Account, check on **Enable Incoming** and set your POP3 settings, if you are using a popular email service, these will be preset for you.

<img class="screenshot" alt="Incoming EMail" src="{{docs_base_url}}/assets/img/setup/email/email-account-incoming.png">

The following options are available for incoming emails:

* **Use IMAP**
* **Use SSL**
* **Attachment Limit**
* **Default Incoming**: If ticked, all replies to your company (eg: replies@yourcomany.com) will come to this account.
* **Email Sync Option**: Whether to sync all or only unseen emails.
* **Initial Sync Count**: Number of emails to sync the first time.

#### Appending Emails To Documents
This feature creates DocTypes when an email is sent to a particular email account. For example, you can append support@example.com to the Issue DocType. On doing this, whenever an email is sent to support@example.com, the system will create an Issue for it. Similarly if you link jobs@example.com, when emails are sent to jobs@example.com, a Job Applicant DocType is created.


Enable Automatic Linking in Documents will link emails to documents, to know more [click here](/docs/user/manual/en/setting-up/email/linking-emails-to-document).

### 3.3 Notification for unreplied messages

If you would like ERPNext to notify you if an email is unreplied for a certain amount of time, then you can set **Notify if Unreplied**. Here you can set the number of minutes to wait before notifications are sent and whom the notifications must go to.

<img class="screenshot" alt="Incoming EMail" src="{{docs_base_url}}/assets/img/setup/email/email-account-unreplied.png">

#### Setting Import Conditions for Email Import

Email Accounts allows you to set conditions according to the data of the incoming emails. The email will be imported to ERPNext only if all conditions are true. For example, if you want to import an email if the subject is "Some important email", you put doc.subject == "Some important email" in the conditions textbox. You can also set more complex conditions by combining them, as shown on the following screenshot.

<img class="screenshot" alt="Incoming EMail Conditions" src="{{docs_base_url}}/assets/img/setup/email/email-account-incoming-conditions.png">

### 3.4 Outgoing Email Accounts

All emails sent from the system, either by the user to a contact or via notifications or via transaction emails, will be sent from an Outgoing Email Account.

To set up an outgoing Email Account, check on **Enable Outgoing** and set your SMTP server settings, if you are using a popular email service, these will be preset for you.

<img class="screenshot" alt="Outgoing EMail" src="{{docs_base_url}}/assets/img/setup/email/email-account-sending.png">

The following options are available for outgoing emails:

* **Use TLS**
* **Port**
* **Disable SMTP server authentication**
* **Add Signature**: The default signature appended to the end of each email.
* **Default Outgoing**: Notifications and bulk emails will be sent from this outgoing server.
* **Always use Account's Email Address as Sender**: The email address of this account will be mentioned as the sender for outgoing emails.
* **Send unsubscribe message in email**: Send a link to unsubscribe from emails sent from this account.
* **Track Email Status**: Track if your email has been opened by the recipient. Note that, if you're sending to multiple recipients, even if one recipient reads the email, it'll be considered "Opened".
* **Enable Auto Reply**: If enabled, enter an auto reply message.

## 4. How ERPNext handles replies

In ERPNext when you send an email to a contact like a customer, the sender will be the user who sent the email. In the **Reply-To** property, the Email Address will be of the default incoming account (like `replies@yourcompany.com`). ERPNext will automatically extract these emails from the incoming account and tag it to the relevant communication.

> **Note for self implementers:** For outgoing emails, you should set up your own SMTP server or sign up with an SMTP relay service like mandrill.com or sendgrid.com that allows a larger number of transactional emails to be sent. Regular email services like Gmail will restrict you to a limited number of emails per day.

If you encounter errors when configuring and email account, refer [this page](/docs/user/manual/en/setting-up/articles/email-error).

## 5. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/ChsFbIuG06g?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

### 6. Related Topics
1. [Email Inbox](/docs/user/manual/en/setting-up/email/email-inbox)
1. [Email Digest](/docs/user/manual/en/setting-up/email/email-digest)
1. [Auto Email Reports](/docs/user/manual/en/setting-up/email/auto-email-reports)
1. [Sending Email](/docs/user/manual/en/setting-up/email/sending-email)
1. [Email Domain](/docs/user/manual/en/setting-up/email/email-domain)
