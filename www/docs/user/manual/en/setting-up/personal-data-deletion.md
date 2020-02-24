<!--add breadcrumbs-->

# Personal Data Deletion

As a part of GDPR compliance, ERPNext has Personal Data Deletion.

Personal data deletion tool enables a user to anonymize all the personally identifiable data a user has generated while using ERPNext. That is, personally identifiable information will be randomized. This includes personally identifiable data from your user account like: username, full name, birth date, phone numbers, mobile numbers, location, interests, bio, email signature, Email, Contact, Address, Communication, etc. It also includes data from Leads and Opportunities, the details you have saved like phone numbers, mobile numbers, fax, website, and name.

However, this excludes data that is required by law to be maintained by a business.

## 1. How to request the deletion of user data

1. To begin deleting personally identifiable data, you need to visit [host-name]/request-to-delete-data (e.g. example.erpnext.com/request-to-delete-data) in the URL field.

    <img class="screenshot" alt="Request Data Webform" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/request-to-delete-data-webform.png">

2. Enter the email associated with your ERPNext account. After submitting your request, you will receive a success response.

    <img class="screenshot" alt="Deletion Request Success" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/deletion-request-success.png">

3. This will send an email with a verification link to delete data to the email address associated with the user.

    <img class="screenshot" alt="Verification Email" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/verification-email.png">

4. Once the user clicks on the verification link. A confirmation message will be displayed.
    <img class="screenshot" alt="Confirmed Verification" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/confirmed-verification.png">

## 2. How deleting user's personal data works

The request to delete data is recorded in the doctype "Personal Data Deletion Request".

<img class="screenshot" alt="Personal Data Download Request Doctype" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/personal-data-deletion-request-doctype.png">

This doctype maintains three states of status to complete the process of removal of user data.

### 2.1 Pending Verification
This status indicates that the user has requested data deletion via the web-form. However, verification of this request is still pending. Search for Personal Data Deletion Request from the search bar.

<img class="screenshot" alt="Pending Verification" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/pending-verification.png">

### 2.2 Pending Approval
This indicates that the user has verified the request via email. This enables the option of "Delete Data" for System Managers.

<img class="screenshot" alt="Pending Approval" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/pending-approval.png">

### 2.3 Deleted
This indicates that the System Manager has clicked on the "Delete Data" button. This means that the user's personally identifiable data has been anonymized.

<img class="screenshot" alt="Deleted User" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/deleted-user.png">

### 3. Related Topics
1. [Personal Data Download](/docs/user/manual/en/setting-up/personal-data-download)

