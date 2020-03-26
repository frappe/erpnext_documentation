# Email Template

Every email sent is different but certain emails can be standardized, usually known as Email Template or Standard Reply.

To access the Email Template list, go to:
> Home > Settings > Email > Email Template

## 1. How to create an Email Template
1. Go to the Email Template list, click on New.
1. Enter a name for this Email Template.
1. Enter a Subject for this Email Template.
1. Response is the standard content of the email that will be a part of this template. 
1. Save.

<img class="screenshot" alt="Email Template" src="{{docs_base_url}}/assets/img/setup/email/email-template-example.png">

**DocType Associated:** (optional) The DocType associated with this template.

### 1.1 How to use Email Template
You can use this Email Template in the Emails that are sent from ERPNext in the "CC, BCC & Email Template" field of the email section of the document. ERPNext will fetch the subject and response as per the template selected.

### 1.2 How to get fieldnames
The fieldnames you can use in your email template are the fields in the document from which you are sending the email. You can find out the fields of any documents via Setup > Customize Form View and selecting the document type (e.g. Sales Order)

### 1.3 Templating
Templates are compiled using the Jinja. To learn more about Jinja, [visit this page](https://jinja.palletsprojects.com/en/2.10.x/).

## 2. Related Topics
1. [Email Account](/docs/user/manual/en/setting-up/email/email-account)
1. [Email Inbox](/docs/user/manual/en/setting-up/email/email-inbox)
