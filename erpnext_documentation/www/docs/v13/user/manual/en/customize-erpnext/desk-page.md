<!-- add-breadcrumbs -->
# Desk Page

When you log in, you're presented with the Desk. It features a persistent sidebar sorted into categories. Each sidebar item links to a page called Desk Page.

A Desk Page represents a module (for example CRM in ERPNext). A Desk Page includes the following:

- A dashboard section for that particular module.
- A shortcut section for frequently used masters, transactions or pages.
- A masters section where all the reports and masters are grouped and listed.

<img alt="Standard Desk Page" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/standard-desk-page.png">

## Standard Desk Page

Every module in ERPNext has its own Standard Desk Page which is generated with appropriate shortcuts and links.

<img alt="Desk Page List" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/desk-page-list.png">

Any customization to be made to the Standard Desk Page can be done with Customize Desk Page option in the top right corner of the Desk Page.

> Note: These customizations will be user-specific and will only be visible to that user.

<img alt="Customize Desk Page" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/customize-desk-page.png">

## Custom Desk Page

You can also create your own Desk Pages by simply creating a new Desk Page document.

<img alt="New Desk Page" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/new-desk-page.png">

1. Go to the Desk Page list and click on New.

1. **Name**: The text you enter here will be shown in the sidebar.

1. **Module**: Select the module which the Desk Page will represent.

1. ***Is Standard***: If checked, this Desk Page will be shown in the sidebar. Otherwise it will be treated as a customized version of a Standard Desk Page.

1. ***Extends Another Page***: If checked, this Desk Page will be treated as a customized version of another Desk Page.

1. ***Is Default***: If checked, this Desk Page will be the default Desk Page displayed to all users for a particular module.

1. ***Dashboard***: Add a Dashboard to display it on the top of the Desk Page.

1. ***Shortcuts***: Add Shortcuts to a specific page, reports or list which will be displayed below the dashboard.

1. ***Link Cards***: You can add cards that will display a list that links to a specific page, report, or list. You must add these in a specific JSON format as displayed in the image below.

<img alt="Desk Page Card" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/desk-page-card.png">

{next}
