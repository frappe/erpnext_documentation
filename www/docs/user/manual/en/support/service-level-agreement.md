<!-- add-breadcrumbs -->
# Service Level Agreement

**A service level agreement (SLA) is a contract between a service provider (either internal or external) and the end user on the level of service expected from the service provider.**

SLAs are output-based, their purpose is specifically to define the timeline in which the Customer will receive the service. SLAs do not define how the service itself is provided or delivered.

To access the Service Level Agreement list, go to:
> Home > Support > Service Level Agreement > Service Level Agreement

## 1.Prerequisites
* [Service Level](/docs/user/manual/en/support/service-level)

* Enable **Track Service Level Agreement** in Support Settings

    <img class="screenshot" alt="Service Level Agreement" src="{{docs_base_url}}/assets/img/support/sla-setting.png">

## 2. How to Create a Service Level Agreement
1. Go to the Service Level Agreement list, click on New.
1. Select the Service Level. This will fetch the Employee Group the SLA applies to, the default priority, and the Holiday list the SLA is excluded from.
1. 'Enable' determines if a Service Level Agreement is enabled or disabled.
1. Ticking 'Default Service Level Agreement' will apply this SLA to a customer if they don't have a particular SLA assigned to them.
1. Entity Type: Service Level Agreements can be assigned to a Customer/Customer Group/Territory enabling you to apply Service Level Agreement based on these factors.
1. Entity: Select the specific Customer/Customer Group/Territory.
1. Start / End Date: Defines the validity of the agreement.
1. Priorities and Support days are fetched as set in the Service Level. These values can be changed if needed.
1. Save.

    ![SLA](/docs/assets/img/support/sla.png)

## 3. Features
### 3.1 Applies to New Issues

Once an SLA is saved, it'll be applied to Issues raised by Customers/Territories as per the option you chose in Entity Type:
    ![SLA in Issue](/docs/assets/img/support/sla-issue.png)

### 3.2 Resetting an SLA
An SLA can also be reset until the time does not fail. For example, if the SLA is 3 days, you can reset the SLA only within 3 days of the Issue being created. After that, the Service Level will display failed. 
    ![SLA Issue](/docs/assets/img/support/reset-sla.gif)

### 3.3 Time respond / resolve in Issues
The time to respond to an Issue and the time to resolve will be shown:
    ![SLA in Issue](/docs/assets/img/support/sla-in-issue.png)

These times are based on the timelines set in the 'Priority' field in the Service Level's Priorities table.