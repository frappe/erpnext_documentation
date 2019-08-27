<!-- add-breadcrumbs -->
# Workstation

**A Workstation stores information regarding the place where the workstation operations are carried out.**

Data regarding the operation cost, rent, electricity can be stored here. 

> Note: An Operation can take place at multiple Workstations.

> An Operation takes place at a Workstation. The Operation is the work performed and the Workstation is the place/machine where it is performed. For example, melting is an Operation that can be done at 10 different Workstations.

To access the Workstation list, go to:

> Home > Manufacturing > Bill of Materials > Workstation

## 1. How to create a Workstation
1. Go to the Workstation list, click on New.
1. Enter a name for the Workstation.
1. Under Operating Costs, enter the following as applicable:
 * Electricity Cost
 * Rent Cost
 * Consumable Cost
 * Wages
1. Save.

Optionally, you can enter a description for the Workstation.

![Workstation](/docs/assets/img/manufacturing/workstation.png)

The hours when the Workstation will be Operational can be added. On adding a Holiday list, the days listed as holidays won't be counted as working for the Workstation.
![Workstation Hours](/docs/assets/img/manufacturing/workstation-hours.png)

After saving the Workstation, the following actions can be performed against it:
![Workstation submit](/docs/assets/img/manufacturing/workstation-submit.png)

## 2. Features
### 2.1 Working Hours
Under Working Hours table, you can add start and end times for a Workstation. For example, a Workstation may be active from 9 am to 1 pm, then 2 pm to 5 pm. You can also specify the working hours based on shifts. While scheduling a [Work Order](/docs/user/manual/en/manufacturing/work-order), the system will check for the availability of the Workstation based on the working hours specified.

### 2.2 Holiday List
1. A [Holiday List](/docs/user/manual/en/human-resources/holiday-list) can be added to exclude counting these days for the Workstation.


> Note : You can enable overtime for a Workstation in [Manufacturing Settings](/docs/user/manual/en/manufacturing/manufacturing-settings)

## 3. Video
<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/UVGfzwOOZC4?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
 </iframe>
</div>

## 4. Related Topics
1. [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials)
1. [Operation](/docs/user/manual/en/manufacturing/operation)
1. [Routing](/docs/user/manual/en/manufacturing/routing)
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)
1. [Job Card](/docs/user/manual/en/manufacturing/job-card)

{next}