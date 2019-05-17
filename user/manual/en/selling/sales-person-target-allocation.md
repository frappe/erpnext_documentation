<!-- add-breadcrumbs -->
# Sales Person Target Allocation

Along with the management of Sales Persons, ERPNext also allows you to assign target Sales Persons based on Item Group and Territory. Based on target allocated and actual sales booked by Sales Person, you will get the Target Variance Report for the Sales Person.

##1. Sales Person - Item Groupwise Target Allocation

###1.1 Open Sales Person's Master

To allocate target, you need to open specific Sales Person master.

**Selling > Sales Partners and Territory > Sales Person > Edit**

###1.2 Allocate Item Groupwise Target

In the Sales Person master, you will find table a called Sales Person Target.

<img class="screenshot" alt="Sales person target" src="{{docs_base_url}}/assets/img/selling/sales-person-target-item-group.png">

In this table, you should select Item Group, Fiscal Year, Target Qty, Target Amount, and Target Distribution. 

You can give target in amount or quantity, or both. Item Group can also be left blank. In this case, the system will calculate target based on All Item Groups.

**Target Distribution**

You can spread the target across months. For this create a new monthly distribution, you can see the option when you click on the Target Distribution field in the Targets table. For example, a target of selling 1,000 units for first quarter of the Fiscal Year 2019-2020 as shown in the preceding screenshot.

<img class="screenshot" alt="Target Distribution" src="{{docs_base_url}}/assets/img/selling/sales-person-target-distribution.png">

###1.3 Report - Sales Person Target Variance Item Groupwise

To check this report, go to:

**Selling > Other Reports > Sales Person Target Variance Item Group-wise**

This report will provide you variance between target and actual performance of Sales Person. This report is based on Sales Order report.

Here, as per the report, allocated target to Sales Person was roughly 83 in quantity for a month, but he has achieved a target of 80 when the report is being viewed, hence the variance report is shown accordingly.

<img class="screenshot" alt="Target Item Group" src="{{docs_base_url}}/assets/img/selling/sales-person-item-group-report.png">

**Note:** For the report to reflect correct details, you need to link a Sales Person to a Sales Order, it's present in the Sales Team section of Sales Order. The Sales Order has also has to be in the submitted stage.

---

##2. Sales Person - Territorywise Target Allocation

For allocating Territory-wise targets to Sales Person, select the specific Sales Person in the Territory master. This Sales Person is entered just for the reference. Sales Person details are not updated in the variance report of Territorywise Target Allocation.

###2.1 Go to Territory master

**Selling > Settings > Territory > (Edit specific Territory)**

In the selected Territory, you will find a field to select Territory Manager. This field is linked to "Sales Person" master.

<img class="screenshot" alt="Sales Person Territory Manager" src="{{docs_base_url}}/assets/img/selling/sales-person-territory-manager.png">

###2.2 Allocating Target

Target Allocation in the Territory master is similar to Sales Person master. You can follow the same steps given in section _1.2 Allocate Item Groupwise Target_ to specify target in the Territory master also.

###2.3 Report - Territory Target Variance Item Groupwise

This report will provide you variance between target and actual performance of Sales in particular territory. This report is based on Sales Order report. Though Sales Person is defined in the Territory master, its details are not pulled in the report.

**Note** that the Territory of the Customer/Customers must be set accordingly for this report to work. For example, in the following screenshot, the target was approx eight units and five was achieved, hence the variance is three.

<img class="screenshot" alt="Sales Person Territory Report" src="{{docs_base_url}}/assets/img/selling/sales-person-territory-report.png">

---

##3. Target Distribution

To create a new Monthly Distribution, go to:
**Accounting > Monthly Distribution**

Target Distribution document allows you to divide allocated targets across multiple months. If your products and services are seasonal, you can distribute the sales target accordingly. For example, if you are into umbrella business, then target allocated in the monsoon season will be higher than in other months.

<img class="screenshot" alt="Target Distribution" src="{{docs_base_url}}/assets/img/selling/target-distribution.png">

You can link Monthly Distribution while allocating targets in Sales Person and in Territory master.

### 4. Related Topics
1. [Sales Persons in the Sales Transactions](/docs/user/manual/en/selling/articles/sales-persons-in-the-sales-transactions)
1. [Using Sales Person in transactions](/docs/user/manual/en/selling/articles/sales-persons-in-the-sales-transactions)
