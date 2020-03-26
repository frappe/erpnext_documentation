<!-- add-breadcrumbs -->
# Google Contacts Integration

ERPNext provides an integration with Google Contacts in order for all users to synchronize their Google Contacts with ERPNext.

## How to set up Google Contacts Integration

In order to allow a synchronization with Google Contacts, you need to authorize ERPNext to get Contacts data from Google. Google Contacts Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/docs/user/manual/en/erpnext_integration/google_settings).
- In the Google Contacts list, click on New. Enter the Google Account Email you want to sync and then save it. Now click on **Authorize Contacts Access** to authorize ERPNext to get Contacts data from Google.

## How to use Google Contacts Integration

### Creating a Contacts in ERPNext
- Once Google Contacts Integration is succesful, all the contacts created in ERPNext will be synced if `Push to Google Contacts` is checked.

Creating a Contact in ERPNext:
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_create_contact.gif">

It will be shown in Google Contacts:
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_create_contact_!.gif">

### Syncing Contacts from Google Contacts
- Once Google Contacts Integration is succesful, all the contacts in Google Contacts will be synced if `Pull from Google Contacts` is checked.
  <img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_contact_sync.gif">
