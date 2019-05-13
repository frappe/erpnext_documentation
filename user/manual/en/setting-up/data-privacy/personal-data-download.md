<!--add breadcrumbs-->

# Personal Data Download

Personal data download tool enables user to automatically download all the personal data a user has generated while using erpnext.

### 1. How to request user data download

1. To begin downloading data, the user needs to visit [host-name]/request-data (e.g. erpnext.com/request-data) in the url field.

    <img class="screenshot" alt="Request Data" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/request-data-webform.png">

2. After submitting your request, you will receive a success response.
    <img class="screenshot" alt="Request Data" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/download-request-succes.png">

3. This will sent a mail with a download link of the data to the email address associated with the user.
    <img class="screenshot" alt="Download Data Email" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/download-data-email.png">

### 2. Personal Data Download Request DocType

The request is also recorded in the doctype "Personal Data Download Request", the file-link that is sent to the user via email is also attached to the doc.

<img class="screenshot" alt="Personal Data Download Request Doctype" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/personal-data-download-request-doctype.png">