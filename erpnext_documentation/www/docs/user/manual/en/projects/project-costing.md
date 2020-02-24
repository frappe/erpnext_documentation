<!-- add-breadcrumbs -->
# Project Costing

Each project has multiple tasks associated with it. To track actual costing of a Project, primarily in terms of services, a User has to create a Timesheet based on actual time spent on a Task within a Project. Following ways in which you can track actual service cost against Project.

## Activity Type

Activity Type is a master of service offered by your personnel. You can add new Activity type from:

> Home > Project > Activity Type > New

## Activity Cost

Activity Cost is a master where you can track billing and costing rate for each Employee, for each Activity Type.

<img class="screenshot" alt="Activity Cost" src="{{docs_base_url}}/assets/img/project/projects-activity-cost.png">

## Timesheet

Based on Actual Time spent on the Project-Task, an Employee will create a [Timesheet](/docs/user/manual/en/projects/timesheets/).

<img class="screenshot" alt="Timesheet" src="{{docs_base_url}}/assets/img/project/projects-timesheet.png">

On selection of Activity Type in the Time Log, Billing and Costing Rate will be fetched for that Employee from respective Activity Cost master. 

Multiplying these rates with total no. of Hours in the Time Log gives Costing Amount and Billing Amount for the specific Time Log.

## Costing in Project and Task

Based on total Timesheets created for specific Tasks, its costing will be updated in the respective Task master. 

<img class="screenshot" alt="Task" src="{{docs_base_url}}/assets/img/project/projects-task-costing.png">

Same way, Project master will have cost updated based on Timesheets created against each of its associated tasks and the cost of the Project gets updated simultaneously.

<img class="screenshot" alt="Project - Costing" src="{{docs_base_url}}/assets/img/project/projects-costing-and-billing.png">

