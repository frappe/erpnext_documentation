<!-- add-breadcrumbs -->
# Google Contacts Integration

ERPNext provides an integration with Google Contacts in order for all users to synchronize their Google Contacts with ERPNext.

The following should be noted when synchronizing contacts in ERPNext from Google Contacts:
- All the contacts present in Google Contacts will be synchronized to ERPNext.
- If any of the Google Contacts has multiple Email IDs associated with it, new ERPNext contacts will be created each Email ID.

## How to set up Google Contacts Integration

In order to allow a synchronization with Google Contacts, you need to authorize ERPNext to get Contacts data from Google. Google Contacts Integration is set up with the following steps:

1. Create a new project on Google Cloud Platform and generate new OAuth 2.0 credentials.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_project_creation.gif">
- Enable Google People API Access in API Library.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/api.gif">
- Add `https://{yoursite}` to Authorized JavaScript origins.
- Add `https://{yoursite}?cmd=frappe.integrations.doctype.google_contacts.google_contacts.google_callback` as an authorized redirect URI.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_oauth.gif">
- Add your Client ID and Client Secret in the Google Settings in **Home > Integrations > Google Services > Google Settings**
- In the Google Contacts list, click on New. Enter the Google Account Email you want to sync and then save it. Now click on **Authorize Contacts Access** to authorize ERPNext to get Contacts data from Google.
- Once Authorized, you can manually sync Google Contacts or let ERPNext sync Google Contacts daily.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_sync.gif">
