<!-- add-breadcrumbs -->
# Customizing Module Visibility

**ERPNext as a system can be used by multiple businesses at every scale, Manufacturing, Education, Retail being some of the businesses benefitted the most from the usability of the system.**

Keeping in mind, the interests of all kinds of business owners, the usability of the system for different business has been mapped into different 'Modules' represented as 'Cards' in the system. Similarly the core modules in the system, such as Human Resource, Accounting, CRM etc. are also represented by different cards on the dashboard.

Every ERPNext account holder has the option of customizing the visibility of the different modules based on their business case.

*In Version 12, you can go to Show / Hide Modules on the top right corner of the home screen for checking visibility of modules.**

<img alt="Module Visibility" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-module-visibility-2.png">

<img alt="Module Visibility" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-module-visibility.gif">

> Note: Modules are automatically hidden for users that have no permissions on the documents within that module. For example, if a User has no permissions on Purchase Order, Purchase Request, Supplier, the “Buying” module will automatically hidden for that User.

If you have permissions to a specific module, but it is still not visible, the following could be the possible reasons for it. 

Let's consider a scenario that a user has the permission for the Website module, but is not able to access it.

As a basic requirement, ensure that the "Website Manager" role is assigned to that user. It is a standard Role that grants permission on the Website module. If permissions have been customized in your account, check Role Permission Manager to know which Role has permission on Website, and then check if the same Role is assigned to the User.

<img alt="Module Visibility" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-module-visibility-4.png">

Further, you should also check if the under the settings, 'Allow Modules', the required module has been enabled for the user

<img alt="Module Visibility" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-module-visibility-1.png">

Reload tab of your ERPNext account and the changes made will be applied and will be visible in the system.

{next}
