<!-- add-breadcrumbs -->
# Project

**A Project is a planned piece of work that is designed to find information about something, to produce something new, or to improve something.**

In ERPNext, Project Management is Task-driven. You can create a Project and divide it into multiple assignable Tasks.

A Project generally has a broad scope and hence can be divided into tasks. Whilst each task within a Project can be assigned to an individual or a group of individuals, the assignment can also be done on a project level.

These Tasks can be created from a Project itself or a [Task](/docs/user/manual/en/projects/tasks.html) can be created separately as well.

To access Projects, go to:

> Home > Projects > Projects > Project 

<img class="screenshot" alt="Project" src="{{docs_base_url}}//assets/img/project/projects-project-intro.png">

## 1. How to Create a Project

  1. Go to the Project list and click on New.
  2. Add the following details:
      * **Project Name**: Title of the Project.
      * **Status**: The default status of a Project is going to be 'Open' which can later be changed to 'Completed' or 'Cancelled'.
      * **Expected End Date**: Enter the date on which you aim to finish the project.
  3. Save.

### 1.1 Additional Options while creating a Project

  1. **From Template**: If you have an existing [Project Template](/docs/user/manual/en/projects/project-template), you can choose to create your project using this template.
  2. **Expected Start Date**: If you have a time-line fixed for the project, you can define both expected Start Date and Expected End Date in the form.
  3. **Project Type**: You can classify your projects into different [Project Types](/docs/user/manual/en/projects/project-type), e.g., Internal or External. 
  4. **Priority**: You can select how the priority level of the Project based on how crucial it is. You can also add more priority levels.
  5. **Department**: If there is an owner [Department](/docs/user/manual/en/human-resources/department) for the project, you can add that here.
  6. **Is Active**: A Yes/No tab, which lets you change the active status of the project at any later stage.
  7. **Completion Method**: You can track the % completion of your project based on one of the three methods, viz. **Manual, Task Completion, Task Progress and Task Weight**. 
  
  <img class="screenshot" alt="Project 2" src="{{docs_base_url}}/assets/img/project/project-proj.png">

  Some examples of how the Percentage Completion is calculated based on Tasks:

  | Project     | Activity     | % Progress     | Weight     | Status     |
  |:-----------:|:------------:|:--------------:|:----------:|:----------:|
  | SC001       | Build        | 100            | 0.4        | Completed  |
  | SC001       | Operate      | 100            | 0.2        | Completed  |
  | SC001       | Transfer     | 50             | 0.2        | Open       |

  | Method              | Formula                                            | Calculation                        | % Task Completed     |
  |:-------------------:|:--------------------------------------------------:|:----------------------------------:|:--------------------:|
  | **Manual**          | -                                                  |-                                   | Manual               |
  | **Task Completion** | Task completed / Total no. of Tasks                  | 2/3                                | 66.66                |
  | **Task Progress**   | Sum of % Progress of all Tasks / Total No. of Tasks | (100+100+50)/3                     | 83.33                |
  | **Task Weight**     | Sum of (Task weight + % Progress)                   | (0.4 * 100 + 0.2 * 100 + 0.2 * 100)| 70                   |

## 2. Features

### 2.1. Customer Details, Users and Notes

* **Customer**: If a Project is being carried out for a particular Customer, the details can be fed in here.
* **Sales Order**: If a Project is based on a [Sales Order](/docs/user/manual/en/selling/sales-order) from a Customer, you can fetch the details here. This would enable you to update the Customer on the Progress on the project as per the Sales Order issued.
* **Users**: You can add any [website user](/docs/user/manual/en/setting-up/users-and-permissions/adding-users) to give them access to this Project. E.g., you can add your customer as a Website User, to enable him to have access to your project to monitor progress and/or give any inputs/remarks. Similarly, a Supplier or a Contractual Employee/Freelancer who is involved in the Project can be added as a User.

  Further, you can also expand the window and select if you want to send a Welcome Email to any particular user or give them Attachment Viewing rights.

* **Notes**: You can add any additional notes to the project.

  <img class="screenshot" alt="Project - Costing" src="{{docs_base_url}}/assets/img/project/projects-customer-users-notes.png">

### 2.2. Start and End Dates

* **Actual Start Date**: Basis the Actual Start of the project, tracked via Timesheets, the Actual Start Date and Time of the Project will get recorded automatically. 
* **Actual End Date**: Basis the Actual End of the project, tracked via the last update of the Timesheet, the Actual End Date and Time of the Project will get recorded automatically. To know more about Timesheets, [click here](/docs/user/manual/en/projects/timesheets/).

  <img class="screenshot" alt="Project - Costing" src="{{docs_base_url}}/assets/img/project/projects-start-time-end-time.png">

### 2.3. Costing and Billing

* **Estimated Cost**: Enter the Estimated Cost of the Project.
* **Total Sales Amount**: If you have already linked the Project with a Sales Order, the Total Sales Order Amount will be auto-populated here.
* **Total Costing Amount**: The system will automatically fetch the Total Costing Amount from all the Timesheets linked to this project.
* **Total Billable Amount**: The system will automatically fetch the Total Billable Amount from all the Timesheets linked to this project.
* **Total Expense Claim**: Based on the expenses claimed by an [Employee](/docs/user/manual/en/human-resources/employee) for the completion of the Project, the Total Expense Claim will be auto-calculated.
* **Total Billed Amount**: The Total Billed Amount gets auto-populated in the system using the Sales Invoice created against the Sales Order.
* **Total Purchase Cost**: The Total Purchase Cost of a Project is the cost fetched from the Purchase Invoices that get created against a Purchase Order issued for supply of Materials required for a Project.
* **Total Consumed Material Cost**: Using the Stock Entry made as per the requirement of Materials in the Project, the Total Consumed Material Cost gets captured.

**Note:** If the total weight of the Tasks is not 100, then the calculated result will be divided by the total weight.
For example, if the total of task weights is 70, then percenrage completed = (70/0.8)% = 87.5%.

### 2.4. Margin

* **Gross Margin**: Gross Margin would give you the Margin you have between your Total Costing Amount and the Total Billed Amount.

  **Gross Margin = (Total Sales Amount + Total Billable Amount) - Total Costing Amount + Total Billable Amount + Total Expense Claim + Total Purchase Cost + Total Consumed Material Cost)**

* **Gross %**: The percentage of the Total Billed Amount spent in the Total Costing Amount makes for the Gross %.

  **((Total Sales Amount + Total Billable Amount) - Total Costing Amount + Total Billable Amount + Total Expense Claim + Total Purchase Cost + Total Consumed Material Cost) / Total Sales Amount)* 100**

  <img class="screenshot" alt="Project - Costing" src="{{docs_base_url}}/assets/img/project/projects-costing-and-billing.png">

### 2.5. Monitor progress

When you enable the 'Collect Progress' option by checking the box, it will enable you to add monitoring details to the project. A report on the progress of the project shall be sent to all the stakeholders of the project.

* **Holiday List**: You can select the [Holiday List](/docs/user/manual/en/human-resources/holiday-list) for your company. This will allow you to collect the Progress Reports only on the Working Days.
* **Frequency**: You can select the frequency at which you wish to get the reports. It can be set to an hourly, twice daily, daily or on a weekly frequency.

  <img class="screenshot" alt="Project - Costing" src="{{docs_base_url}}/assets/img/project/projects-monitor-progress.png">

## 3. Related Topics
  1. [Task](/docs/user/manual/en/projects/tasks)
  2. [Project Type](/docs/user/manual/en/projects/project-type)
  3. [Project Template](/docs/user/manual/en/projects/project-template)

{next}
