<!-- add-breadcrumbs -->
# Web Forms

Stakeholders who are not part of your organization may need to interact with
your ERPNext instance. You can authorize customers, suppliers, job applicants,
students, and guardians to access certain information or even create certain
transactions. For example, you can let anyone create an account on your website
(created with ERPNext) and apply for a job. You can let your customers see the
details of the complaints they have registered. These can be done using Web Forms.

> There are two types of in-built interfaces available in ERPNext. The
> *Desk View* and the *Web View*. Desk is for users who regularly interact
> with ERPNext instance, like employees of your organization.

> Web View is for users who need to interact with an ERPNext instance occasionally.
> Web forms are similar to the forms you generally fill in various websites on the
> internet. Webforms are part of the *Web View* interface in ERPNext.

To create a new **Web Form** go to:

> Home > Website > Web Site > Web Form

![New Web Form](/docs/assets/img/website/new-web-form-1.png)
*New Web Form*

Select the **DocType** based on which you want to build your Web Form. The
**Route** will be set based on the **Title** of your Web Form. You can also add
an Introduction text to show a friendly message above your form.

Add fields to your Web Form. These are the fields from the DocType you have
selected. You can change the Label for these fields. Try to keep number of
fields to be minimum as long forms are cumbersome to fill.

![Web Form Fields](/docs/assets/img/website/new-web-form-2.png)
*Web Form Fields*

Click on **See on Website** in the sidebar to view your Web form.
![Web Form](/docs/assets/img/website/web-form.png)
*Web Form*

Here is an explanation of each of the checkboxes on the right.

1. **Published**: Web Form will be accessible only if this is enabled.
1. **Login Required**: User can fill the Web Form only if they are logged in.
    When Login Required is checked,
1. **Route to Success Link**: Go to Success Link after the form is submitted.
1. **Allow Edit**: If this is unchecked the form becomes read-only once it is
   saved.
1. **Allow Multiple**: Allow user to create more than one record.
1. **Show as Grid**: Show records in a table format.
1. **Allow Delete**: Allow user to delete the records that he/she has
   created.
1. **Allow Comments**: Allow user to add comments on the created form.
1. **Allow Print**: Allow user to print the document in the selected Print Format.
1. **Allow Incomplete Forms**: Allow user to submit form with partial data.

## 2. Features
### 2.1 Sidebar

You can also show contextual links in a sidebar on your Web Form. Set it up in
**Sidebar Settings**.

![Web Form Sidebar](/docs/assets/img/website/web-form-sidebar.png)
*Web Form Sidebar*

![Web Form with Sidebar](/docs/assets/img/website/web-form-with-sidebar.png)
*Web Form with Sidebar*

### 2.2 Creating Web Forms with Child Table

You can add child tables to your web forms, just like regular forms.

<img class="screenshot" alt="Web form Grid"
src="{{docs_base_url}}/assets/img/website/grid-in-webform.png">

### 2.3 Pagination

To help your users fill out long new forms, you can insert page breaks that will
appear on new sections. This way the user can focus on only filling one section
at a time.

<img class="screenshot" alt="Web form paging"
src="{{docs_base_url}}/assets/img/website/paging-in-webform.png">

### 2.4 Payment Gateway Integration

You can now add a Payment Gateway to the web form, so that you can ask users to
pay against a web form. A good example for this is a conference ticket.

<img class="screenshot" alt="Web form payment"
src="{{docs_base_url}}/assets/img/website/payment-in-webform.png">

### 2.5 Portal User

We have also introduced roles for Website users. Before version 11, if you
assigned any 'Role' to a user he would get access to 'Desk View'. From version
11 you can assign a 'Role' but still disallow access to 'Desk View' by
unchecking 'Desk Access' in Role.

<img class="screenshot" alt="Disallow Desk Access"
src="{{docs_base_url}}/assets/img/website/disallow_desk_access.png">

In Portal Settings, you can set a role against each menu item so that only users
with that role will be allowed to see that item.

<img class="screenshot" alt="portal settings"
src="{{docs_base_url}}/assets/img/website/portal-settings.png">

### 2.6 Custom Script

You can write custom scripts for your Web Form for things like validating your
inputs, auto-filling values, showing a success message, or any arbitrary
action.

Learn how to write custom scripts for your Web Forms
[here](https://frappe.io/docs/user/en/web-forms#custom-script).

### 2.7 Actions

You can add the text in 'Success Message' field and this text will be shown to
user once he successfully submits the web form . And the user is redirected to
the URL given at 'Success URL' when clicked on 'Continue' button. This is only
applicable to webforms accessible without the user login(webforms with 'Login
Required' checkbox unchecked).

<img class="screenshot" alt="Success Message"
src="{{docs_base_url}}/assets/img/website/success_message.png">


### 2.8 Result

When a website user submits the form, the data will be stored in the
document/doctype for which web form is created.

### 2.9 Customizing

For customizing web forms, see the [Frappe Web
Forms Documentation](https://frappe.io/docs/user/en/guides/portal-development/web-forms)


{next}
