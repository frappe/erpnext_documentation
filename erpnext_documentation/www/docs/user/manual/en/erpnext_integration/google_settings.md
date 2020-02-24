<!-- add-breadcrumbs -->
# Google Settings

To enable Google Integrations, ERPNext needs access to the API through which the data will be synced which is acheived using OAuth 2.0 Authentication Protocol.

## How to set up Google Settings

### For Google Calendar, Google Contacts, Google Drive

In order to allow a synchronization with Google Calendar, Google Contacts or Google Drive you need to authorize ERPNext to get data from Google. Following is an example for setting up Google Contacts Integration

1. Create a new project on Google Cloud Platform and generate new OAuth 2.0 credentials.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_project_creation.gif">
- Enable API Access in API Library for the Integration you wish to integrate.
  - Google Calendar: **Calendar API**
  - Google Contacts: **People API**
  - Google Drive: **Drive API**

 <img class="screenshot" src="/docs/assets/img/erpnext_integrations/api.gif">
- Add `https://{yoursite}` to Authorized JavaScript origins.
- Add `https://{yoursite}?cmd=frappe.integrations.doctype.{integration_name}.{integration_name}.google_callback` as an authorized redirect URI.
  - You need to replace `integration_name` with one of the following:
     - Google Calendar: **google\_calendar**
     - Google Contacts: **google\_contacts**
     - Google Drive: **google\_drive**
  - eg: for Google Contacts URL will be `https://{yoursite}?cmd=frappe.integrations.doctype.google_contacts.google_contacts.google_callback`

 <img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_oauth.gif">
- Add your Client ID and Client Secret in the Google Settings in **Home > Integrations > Google Services > Google Settings**

### For Google Maps

In order to allow a synchronization with Google Maps you need to generate an API key as Google Maps doesn't need access to data from Google.

1. Create a new project on Google Cloud Platform and generate new API Key.
- Enable API Access in API Library for the Directions API and then add the API Key in the Google Settings in **Home > Integrations > Google Services > Google Settings**.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/api_key.gif">