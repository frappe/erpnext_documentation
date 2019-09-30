<!-- add-breadcrumbs -->
# Maintenance Schedule

**The Maintenance Schedule shows all upcoming Maintenance Visits.**

All machines require regular maintenance, especially those that contain a lot
of moving parts, so if you are in the business of maintaining those or have
some of them in your own premises, this is a useful tool to plan a calendar of
activities for its maintenance.

To create a new Maintenance Schedule go to:

> Home > Support > Maintenance > Maintenance Schedule

A Maintenance Schedule is usually created from a Sales Order of type 'Maintenance'.
![SO Maintenance Schedule](/docs/assets/img/support/so-maintenance-schedule.png)

## 1. Prerequisites
* [Customer](/docs/user/manual/en/CRM/customer)
* [Item](/docs/user/manual/en/stock/item)

## 2. How to Create a Maintenance Schedule
1. Go to the Maintenance Schedule, click on New.
1. Select the Customer and the Items for which maintenance needs to be done.
1. Set the start and end dates.
1. Select a Periodicity to set how frequently the visits will happen. The options are "Weekly", "Monthly", "Quarterly", "Half Yearly", "Yearly" and "Random". Maintenance Schedule will get generated based on selected Periodicity. Selecting Random will generate random dates
1. The Number of Visits will be set as per the Periodicity selected. Eg: If you selected Weekly and set the whole month between the start and dates, 4 visits are ideal.
1. Select the Sales Person performing the visits.
1. Save.
1. After saving, click on the **Generate Schedule** button to generate a Maintenance Schedule.
1. Submit.

    <img class="screenshot" alt="Maintenance Schedule" src="{{docs_base_url}}/assets/img/support/maintenance-schedule-1.png">

The **Generate Schedule** button will generate a separate row for each maintenance activity. Each Item in a Maintenance Schedule is allocated to a Sales Person. 

When the document is Submitted Calendar events are created for the Sales Person User for each maintenance.

## 3. Related Topics
1. [Serial Number](/docs/user/manual/en/stock/serial-no)
1. [Warranty Claim](/docs/user/manual/en/support/warranty-claim)
1. [Maintenance Visit](/docs/user/manual/en/support/maintenance-visit)
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
