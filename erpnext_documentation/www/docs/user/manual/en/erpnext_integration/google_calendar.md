<!-- add-breadcrumbs -->
# Google Calendar Integration

ERPNext provides an integration with Google Calendar in order for all users to synchronize their Google Calendar Events with ERPNext.


## How to set up Google Calendar Integration

In order to allow a synchronization with Google Calendar, you need to authorize ERPNext to get Calendar Events data from Google. Google Calendar Integration is set up with the following steps:

- Create OAuth 2.0 Credentials via [Google Settings](/docs/user/manual/en/erpnext_integration/google_settings).
- In the Google Calendar list, click on New. Enter Calendar Name and the User for whom you want to sync and then save it.
- Depending what data you want to sync, you can select following
  - Pull from Google Calendar - Syncs all event from Google Calendar to ERPNext.
  - Push to Google Calendar - Syncs all event from ERPNext to Google Calendar.
- Now click on **Authorize Calendar Access** to authorize ERPNext to get Calendar Events data from Google.
- Once Authorized, you can manually sync Google Calendar Event or let ERPNext sync Google Contacts daily.

## How to use Google Calendar Integration

### Creating an Event in ERPNext
- Once Google Calendar Integration is succesful, all the events created in ERPNext will be synced if `Push to Google Calendar` is checked.
- Creating an Event in ERPNext
  <img class="screenshot" src="/docs/assets/img/erpnext_integrations/erpnext-gc.gif">
- Deleting an Event in ERPNext
  <img class="screenshot" src="/docs/assets/img/erpnext_integrations/gc-erpnext.gif">

### Syncing Events from Google Calendar
- Once Google Calendar Integration is succesful, all the events in Google Calendar will be synced if `Pull from Google Calendar` is checked.
- Syncing Events from Google Calendar to ERPNext
  <img class="screenshot" src="/docs/assets/img/erpnext_integrations/gc-sync.gif">
