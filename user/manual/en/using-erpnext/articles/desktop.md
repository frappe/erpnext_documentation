<!-- add-breadcrumbs -->
# Desktop 2.0

> Introduced in v12

## Home Page

![New Desktop](/assets/erpnext_com/images/desktop/desktop.png)

We have replaced the icons from previous desk and added module cards. These cards, based on their scope and relevance are categorized in 4 major categories:

- **Modules**: These are all the domain egnostic modules availble in ERPNext that are common to business of all types. Modules like Human Resources, CRM, Buying, Selling, etc. are put under this category
- **Domains**: This is where you can find all domain specific modules like Education and Manufacturing. You can learn more about all industry specific modules [here](docs/user/manual/en#3-industry-specific-modules).
- **Places**: Places is where you can find features that are not industry specific and are not requried in day to day operations of your company. Features like website and dashbaords and marketplace can be found here.
- **Administration**: Here you can find modules related to your ERPNext setup and adminstration.

These cards allow better navigation with shortcut items in the dropdown menu. You can customize this dropdown to add or remove links to various doctype for that module.

![Desktop Dropdown](/assets/erpnext_com/images/desktop/desktop-dropdown.png)

You can reorder as well show or hide these module cards.

![Drag and Drop](/assets/erpnext_com/images/desktop/drag-and-drop.gif)

## Module Page

Clicking on any module card will take you to the module page. Here the user can navigate through all the doctypes, reports and settings associated to a particular module.

For example here is how the accounting module page looks like.

![Accounts Module](/assets/erpnext_com/images/desktop/accounts-module-page.png)

### Navigating the page.

Some links of these modules may be marked grey, clicking on these links won't open any new page. They are marked so because there is a dependant document that needs to be created first. For example you will need to build a sales invoice before accessing the sales register. Hovering on any of these links will show a pop-up guiding the user to the dependent document.

![Muted Link in Module Page](/assets/erpnext_com/images/desktop/module-link-hover.png)

You shall also notice a color indicator before some of the links. These indicators are used to inform the user if there are any open or urgent documents that need to be looked at.

![Color Indicators](/assets/erpnext_com/images/desktop/color-indicator.png)

The *red* indicator in the above example indicated that there are open or overdue tasks in the list. Accordingly a *blue* indicator would mean that there are no open tasks. An *orange* indicator means that the report has not been accessed or no document is created in the corresponding doctype.