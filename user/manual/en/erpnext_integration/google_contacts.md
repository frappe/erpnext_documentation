<!-- add-breadcrumbs -->
# Google Contacts Integration

ERPNext provides an integration with Google Contacts in order for all users to synchronize their Google Contacts with ERPNext.

The following should be noted when synchronizing contacts in ERPNext from Google Contacts:

- All the contacts present in Google Contacts will be synchronized to ERPNext.
- If any of the Google Contacts has multiple Email IDs associated with it, new ERPNext contacts will be created for each Email ID.

## How to set up Google Contacts Integration

In order to allow a synchronization with Google Contacts, you need to authorize ERPNext to get Contacts data from Google. Google Contacts Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/docs/user/manual/en/erpnext_integration/google_settings).
- In the Google Contacts list, click on New. Enter the Google Account Email you want to sync and then save it. Now click on **Authorize Contacts Access** to authorize ERPNext to get Contacts data from Google.

## How to use Google Contacts Integration

### Syncing Contacts from Google Contacts
- Once Google Calendar Integration is succesful, you can manually sync Google Contacts or let ERPNext sync Google Contacts daily.
  <img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_sync.gif">