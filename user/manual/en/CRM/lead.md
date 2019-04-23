<!-- add-breadcrumbs -->
# Lead

**A lead is a potential customer who might be interested in your products or services.**

To get the customer through the door, you may be doing all or any of the
following:

  * Listing your product on directories.
  * Maintaining an updated and searchable website.
  * Meeting people at trade events.
  * Advertising your products or services.

When you send out the word that you are around and have something valuable to
offer, people will come in to check out your products. These are your Leads.

They are called Leads because they may lead you to a sale. Sales executives
usually work on leads by calling them, building a relationship and sending
information about products or services. It is important to track all
this conversation to enable another person who may have to follow-up on that
contact. The new person is then able to know the history of that particular
Lead.

---
### 1. How to Create a Lead

To create a new Lead:

1. Go to **CRM > Sales Pipeline > Lead > New**.
1. If the person represents an organization, check the 'Lead is an Organization' checkbox. Notice that when you check, the 'Company Name
' field becomes mandatory. Enter the Company Name.
1. If the person is an individual, leave the checkbox unchecked and enter Person Name and Gender.  
1. Enter the 'Email Address'.
1. **Status is the important field** in the Lead. You can set the status manually and also it will be updated automatically based on your actions against the lead.
 * Lead: This is the default status assigned when a Lead is created and it indicates an action is needed against this Lead.
 * Open: Sales executive needs to contact the Lead.
 * Replied: A sales executive has provided the information needed and response from Lead is awaited.
 * Opportunity: If an Opportunity is created against the Lead, the status is set to Opportunity. It indicates that the Lead is qualified and may lead to sales.
 * Quotation: If a quotation is created against a Lead, then the status is set to Quotation.
 * Lost Quotation: If the quotation given to the lead has been marked as lost, then the status is set to 'Lost Quotation'.
 * Interested: The lead is interested in the products or services.
 * Converted: If the quotation given to the Lead has resulted in confirmation of an order and if the Sales Order has been created against the quotation, then the status is set to Converted.
 * Do Not Contact: Lead is not interested and no further communication is needed.
1. It is important to track the source from which you are getting the leads. This will help in allocating the marketing budgets effectively. You can set the same in Source field.
1. Enter email ID for communication.
1. Click on 'Save'.

<img class="screenshot" alt="Lead" src="{{docs_base_url}}/assets/img/crm/lead.png">

You can also record the details of the conversation in the NOTES section.

Further details like Lead Type, Market Segment, Industry can be added in the 'MORE INFORMATION' section.

If you have a healthy number of leads, all this information will help you prioritize
the leads you can pursue.


You can assign the Lead to a user by clicking on 'Assign' button on left bar. You can also attach files/images by clicking on 'Attach File' button.

### 2. Features

#### 2.1 Reminders to Follow Up on the Leads

It is important to reach out to leads from time to time and build the relationship. You can set the 'Next Contact Date' and 'Next Contact By' fields and a calendar event will be added for the user chosen in 'Next Contact By' field and a notification is shown on the that Date.

#### 2.2 Adding Multiple Contacts and Addresses

In Busines-to-business(B2B) scenario, in order to close a sales deal, you will have to contact multiple people working in the prospective company.
You can add the details of all such people in the same lead. Once you save a Lead, you will get the option to add [Contact](/docs/user/manual/en/CRM/contact) details by clicking on 'New Contact' button. Similarly, you can add the [Address](/docs/user/manual/en/CRM/address) details by clicking on 'New Address'.

<img class="screenshot" alt="Lead" src="{{docs_base_url}}/assets/img/crm/multiple_address_contacts_in_lead.png">

#### 2.3 Recording Comments, Emails and Events

* **Comments**: You can write your comment in 'Add a comment' box and click on 'Comment'.
* **Emails**: You can send an email to the lead by clicking on the 'New Email' button and when the lead responds to your email, it will visible.
* **Events**: You can also records the Meetings, Calls etc you have had with the Lead by clicking on 'New Event'

#### 2.4 Creating Opportunity, Customer and Quotation

You can create an Opportunity, Customer or a Quotation from the Make dropdown. Relevant field values will be copied over.


#### 2.5 Auto-assigning the Leads to Sales Executives
>Introduced in Version 12

You can define [Assignment Rules](/docs/user/manual/en/setting-up/automation/assignment-rule) to automatically assign the leads to sales executives.

<img class="screenshot" alt="Lead" src="{{docs_base_url}}/assets/img/crm/lead_assignment_rule.png">

### 3. Automating Lead Creation
Leads come from many different sources. It is important that all leads are recorded.

#### 3.1 Automating Lead Creation for Emails Received

You may have an email address like 'sales@yourcompany.com' which is probably displayed on your website. People may send emails asking information about your products and services. You can enable [Email Account](/docs/user/manual/en/setting-up/email/email-account)  to pull these emails and create a lead for each email.

#### 3.2 Capturing Leads from Your Website via a Webform

You can also map the Lead form to a [Web Form](/docs/user/manual/en/website/web-form) and publish it on your website. When visitors of your website fill the form, it will be automatically added as a Lead.

#### 3.3 Lead Creation for an Incomplete Order in E-Commerce Module

You can publish an e-commerce website and allow users to place an order for your products. If a user selects items but doesn't complete the process you can pursue that user as a lead.

#### 3.4 Importing Leads

If you have a spreadsheet with details of the leads, you can use the [Data Import](/docs/user/manual/en/setting-up/data/data-import) feature to import the leads.

---
### 4. Adding Custom Fields

You may need to add custom fields to capture additional details as per your needs.

You can customize the Lead DocType using [Customize Form](/docs/user/manual/en/customize-erpnext/custom-field) tool.

### 5. Related Topics
1. [Opportunity](/docs/user/manual/en/CRM/opportunity)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Difference between Lead, Contact, and Customer](/docs/user/manual/en/CRM/articles/difference_between_lead_contact_and_customer)

{next}
