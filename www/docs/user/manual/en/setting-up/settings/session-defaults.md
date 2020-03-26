<!-- add-breadcrumbs -->
# Session Defaults

**Session Defaults are configurable default values set during user sessions.**

Consider a scenario where you have 8 companies set up in your account and you have to set the 'Company' field every time while creating a new Sales Order. This is a very time-consuming process when you have to deal with multiple Sales Orders daily.

## 1. How to Create Session Defaults

### 1.1 Set up the Session Default Settings

1. Go to Session Default Settings. There you can see a table for Session Defaults.
2. Click on 'Add Row'.
3. Select the DocType for which you want to set Session Defaults.
4. Save.

    <img class="screenshot" alt="Session Defaults Settings" src="{{docs_base_url}}/assets/img/setup/settings/session-defaults-settings.png">

### 1.2 Set up the Session Default Values

1. Click on the 'Settings' menu in the toolbar. You will find an option 'Session Defaults' there. Click on it.

    <img class="screenshot" alt="Session Defaults Menu" src="{{docs_base_url}}/assets/img/setup/settings/session-defaults-menu.png">

2. A 'Session Defaults' prompt will appear. Set the default values for the respective fields and Save.

    <img class="screenshot" alt="Session Defaults Prompt" src="{{docs_base_url}}/assets/img/setup/settings/session-defaults-prompt.png">

After saving, the default values will be set everywhere.

You can open a new Sales Order and check. The company field is set to the default Company.

<img class="screenshot" alt="Session Defaults Set" src="{{docs_base_url}}/assets/img/setup/settings/session-defaults-set-1.png">

Open a new Task. The 'Project' field is set to the default Project.

<img class="screenshot" alt="Session Default Set" src="{{docs_base_url}}/assets/img/setup/settings/session-defaults-set-2.png">

Open a report, for example, General Ledger. Company filter is set to the default Company.

<img class="screenshot" alt="Session Default " src="{{docs_base_url}}/assets/img/setup/settings/session-defaults-set-3.png">

## 2. Features

### 2.1 Defaults cleared on logout

The default values are set for that particular user for the ongoing session. Once logged out, these default values are cleared.

### 2.2 'Settings' button visibility

The Settings button is only visible to the System Manager or to a person having permission to access 'Session Default Settings'. This button navigates you to Session Default Settings where you can add or remove the document types for which you want to set Session Defaults.

<img class="screenshot" alt="Session Defaults Prompt" src="{{docs_base_url}}/assets/img/setup/settings/settings-button.png">

### 3. Related Topics
1. [Global Defaults](/docs/user/manual/en/setting-up/settings/global-defaults)
1. [System Settings](/docs/user/manual/en/setting-up/settings/system-settings)
