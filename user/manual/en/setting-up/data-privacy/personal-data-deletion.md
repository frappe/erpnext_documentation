<!--add breadcrumbs-->

# Personal Data Deletion

Personal data deletion tool enables a user to anonymize all the personally identifiable data a user has generated while using ERPNext. This includes personally identifiable data from communication, lead, contact, and so on, however, this excludes data that is required by law to be maintained by a business.

### 1. How to request deletion of user data

1. To begin deleting data, you need to visit [host-name]/request-to-delete-data (e.g. example.erpnext.com/request-to-delete-data) in the url field.

    <img class="screenshot" alt="Request Data Webform" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/request-to-delete-data-webform.png">

2. After submitting your request, you will receive a success response.

    <img class="screenshot" alt="Deletion Request Success" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/deletion-request-success.png">

3. This will sent a mail with a verification link of the data to the email address associated with the user.

    <img class="screenshot" alt="Verification Email" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/verification-email.png">

4. Once the user clicks on the verification link. A confirmation message will be displayed.
    <img class="screenshot" alt="Confirmed Verification" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/confirmed-verification.png">

### 2. How deleting user's personal data works

The request to delete data is recorded in the doctype "Personal Data Deletion Request".

<img class="screenshot" alt="Personal Data Download Request Doctype" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/personal-data-deletion-request-doctype.png">

This doctype maintains three states of status to complete the process of removal of user data.
#### 1. Pending Verification
This status indicates that the user has requested the deletion via the web-form. However, verification of this request is still pending.

<img class="screenshot" alt="Pending Verification" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/pending-verification.png">

#### 2. Pending Approval
This indicates that the user has verified the request via email link. This enables the option of "delete-data" for System Managers.

<img class="screenshot" alt="Pending Approval" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/pending-approval.png">

#### 3. Deleted
This indicates that the System Manager has clicked on the "Delete Data" button. The user personally identifiable data has been anonymized.

<img class="screenshot" alt="Deleted User" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/deleted-user.png">