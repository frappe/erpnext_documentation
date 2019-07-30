<!-- add-breadcrumbs -->
# Email Domain

**An email domain is the name of the network/service you're using for your email account.**

You can skip to [Email Account](/docs/user/manual/en/setting-up/email/email-account) creation if you are using one of the services listed [here](/docs/user/manual/en/setting-up/email/email-inbox#2-create-an-email-domain).

You can configure your Email Domain in ERPNext for easy setup of all Email Accounts. To find Email Domain settings go to:

> Home > Settings > Email Domain

**What is my Email Domain?:** You might have purchased an Email service from your internet service provider or your IT services provider. For example, if you access your business mailbox with URL like http://mail.yourcompany.com, then yourcompany.com is your email domain.

If you want to send and receive emails on your ERPNext account, you need to correctly setup an email domain. You may be using free mail services like Gmail or Yahoo. In this case, you don't need to create a domain, instead select a service provider from the list. However, you might have to allow access to ERPNext for your Gmail account.

ERPNext creates a template email domain using example.com for your reference. You should add your new domain if you want to use it in your ERPNext account.

<img class="screenshot" alt="Email Domain" src="{{docs_base_url}}/assets/img/setup/email/email-domain.png">

## 1. How to create an Email Domain
1. Go to the Email Domain list, click on New.
1. Enter the Example Email Address. This is where you enter your business email address. For example, if your email ID is yourname@yourcompanyname.com you should enter this.
1. Email Server. This is the URL of your mail server or the email service that you have purchased. For example, it may be mail.yourcompany.com or imap.yourcompany.com. 
1. Use IMAP. IMAP and POP are two services used by most mail servers for incoming emails. If your Email server allows IMAP service for the incoming emails keep this checked. Otherwise, leave this unchecked.

1. Use SSL. If your mail server uses SSL (Secure Socket Layer) communication keep this checked. 

    **Do I have SSL?:** You may have purchased SSL certificate from your IT service provider for SSL and they may have set up SSL for your mail server. If you're using 'https' while accessing mail server over browser then you might have SSL setup.

1. Attachment Limit (MB). You can limit the size of file attachments in emails sent from ERPNext.

1. SMTP Server is the outgoing email service address of your email server.

1. Tick Use TLS if your SMTP service supports TLS for security.

1. Default port. SMTP service is usually set on port 25. If your email server is set up on a separate port number you can set that up here.

### 1.1 After saving the domain

Once you click on save, these settings are validated by ERPNext and the Email Domain gets saved. Sometimes this could take a few seconds and you might have to wait. This email domain is then available in a dropdown called Domain in the Email Accounts screen.

![Email domain in email account](/docs/assets/img/setup/email/email-domain1.png)

#### Entered everything but still unable to setup Email Domain?

If you've entered and verified the above settings and are still unable to setup Email Domain, you can contact [ERPNext support](/in-app-support) for help.

### 2. Related Topics
1. [Email Account](/docs/user/manual/en/setting-up/email/email-account)
1. [Email Inbox](/docs/user/manual/en/setting-up/email/email-inbox)
