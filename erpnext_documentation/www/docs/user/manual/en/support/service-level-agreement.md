<!-- add-breadcrumbs -->
# Service Level Agreement

**A service level agreement (SLA) is a contract between a service provider (either internal or external) and the end-user on the level of service expected from the service provider.**

SLAs are output-based, their purpose is specifically to define the timeline in which the Customer will receive the service. SLAs do not define how the service itself is provided or delivered. You might want to create service level agreements for Issue, Lead, Opportunity, etc.

To access the Service Level Agreement list, go to:
> Home > Support > Service Level Agreement > Service Level Agreement

## 1.Prerequisites

Before creating and using a Service Level Agreement, it is advised that you create/update the following first:

* [Holiday List](/docs/user/manual/en/human-resources/holiday-list)

* If you want to apply SLA on Issue document type, enable **Track Service Level Agreement** in Support Settings

    ![Support Setting](/docs/assets/img/support/sla-setting.png)

## 2. How to Create a Service Level Agreement
1. Go to the Service Level Agreement list, click on New.
1. Select the document type for which you want to apply the SLA.
1. Enter a name for the Service Level.
1. Select the Default Priority.
1. Set a Holiday List. Service Level Agreement won't be applied in the days mentioned in the Holiday List.
1. 'Enable' determines if a Service Level Agreement is enabled or disabled.
1. Ticking 'Default Service Level Agreement' will automatically apply this SLA to a customer if they don't have a particular SLA assigned to them.
1. Entity Type: Service Level Agreements can be assigned to a Customer/Customer Group/Territory enabling you to apply Service Level Agreement based on these factors.
1. Entity: Select the specific Customer/Customer Group/Territory.
    ![SLA Basic Details](/docs/assets/img/support/sla-basic-details.png)
1. Start / End Date: Defines the validity of the agreement.
1. In the "SLA Fulfilled On" table, select the document status (you can also choose multiple) for which the agreement will be marked as fulfilled if it satisfies the time to respond and resolve.
    ![SLA Status Details](/docs/assets/img/support/sla-status-details.png)
1. Priorities: You can set multiple Issue Priorities and their Time to Respond and Resolve (in hours and mins).
    ![SLA Priorities](/docs/assets/img/support/priorities.png)
1. Default Priority: Default Priority selected in Priorities table that will be applied in the Service Level Agreement.
1. Working Hours: Contains the Days of the week on which Support is provided. Has a Start Time and End Time of the Working day.
    ![Working Hours](/docs/assets/img/support/working-hours.png)
1. Save.

## 3. Features
### 3.1 Applies to New Document

Once an SLA is saved, it'll be applied to Documents as per the option you chose in Entity Type:
    ![SLA in Issue](/docs/assets/img/support/sla-issue.png)

### 3.2 Resetting an SLA
An SLA can also be reset until the time does not fail. For example, if the SLA is 3 days, you can reset the SLA only within 3 days of the Issue being created. After that, the Service Level will display failed.
    ![SLA Issue](/docs/assets/img/support/reset-sla.gif)

### 3.3 Time to respond / resolve in Documents
The time to respond and the time to resolve will be shown in the document:
    ![SLA in Issue](/docs/assets/img/support/sla-in-issue.png)

These times are based on the timelines set in the 'Priority' field in the Service Level's Priorities table.


### 3.4 Pause SLA on Statuses
From version 13 onwards, ERPNext allows you to pause SLA on issues when you are waiting for an event to happen. You can do this by selecting a status that is configured in this "Pause SLA On" table.

* Set the statuses on which you want to pause SLA in the SLA document. You can also add custom statuses here.
    <img class="screenshot" alt="Service Level" src="{{docs_base_url}}/assets/img/support/pause-sla.png">
* When the status is changed to any of the above, resolution and response fields are unset and the dashboard indicators change to:
    <img class="screenshot" alt="Service Level" src="{{docs_base_url}}/assets/img/support/hold-indicator.png">
* When the status of the issue changes back to a non-hold status (which is not configured in the "Pause SLA On" table), the **Total Hold time** field will be set in your document.
    <img class="screenshot" alt="Service Level" src="{{docs_base_url}}/assets/img/support/total-hold-time.png">
The Response and Resolution time will be recalculated by adding the hold time, thereby restarting your SLA timers.

> Note: Service Level DocType was removed in version 13 and all functions are handled only with the Service Level Agreement DocType