# Employee Separation

**Employee Separation is a situation when the service agreement of an Employee with his/her organization comes to an end and the Employee leaves the organization.**

Employee Separation is created for an Employee who has resigned or terminated from the organization.

**Use Case:** Let's assume that following are the activities which need to be performed as soon as an Employee needs to be separated from the organization.

- Collect laptop
- Clear dues
- Delete Employee Email Account
- Collect identity card


In ERPNext, these standard activities can be tracked in the Employee Separation Template. To access Employee Separation, go to: 

> Human Resources > Employee Lifecycle > Employee Separation

## 1.  Prerequisites

Before creating an Employee Separation, it is advisable that you create the following documents:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Department](/docs/user/manual/en/human-resources/department)
* [Designation](/docs/user/manual/en/human-resources/designation)
* [Employee Grade](/docs/user/manual/en/human-resources/employee-grade)

## 2. How to create an Employee Separation

1. Go to: Employee Separation > New.
1. Select the Employee. Once the Employee is selected, the corresponding Employee information such as Department, Designation and Employee Grade will automatically get fetched.
1. Select the [Employee Separation Template](#31-employee-separation-template). Based on the template selected, information such as Department, Designation and Employee grade will be automatically fetched (if already mentioned in the Separation Template).
1. Enter the Resignation Letter Date.
1. Additionally, you can also enter the Exit Interview Summary.
1. Save and Submit.


  <img class="screenshot" alt="Separation Template" src="{{docs_base_url}}/assets/img/human-resources/employee-separation.png">



> Note 1: If an Employee Separation Template isn't created, you can directly fill the separation information in the Employee Separation doctype itself.

> Note 2: The 'Status' of the Employee Separation will change to Completed once all the associated Activities are complete.


## 3. Features

### 3.1 Employee Separation Template

The Employee Separation Template is a blueprint which contains a predefined list of Activities for Employee Separation. An Employee Separation Template can be created for a particular Department, Designation and Employee Grade. 

To create a new Employee Separation Template:

1. Go to: Human Resources > Employee Lifecycle > Employee Separation Template > New.
1. Enter the Department, Designation and Employee Grade (optional).
1. Mention the Activities for separation. For each Activity, you can also mention the User or Role, or one of it, to whom this Activity will be assigned.
  
  <img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/employee-separation-template.png">


### 3.2 Tasks and Assignments

On submission of the Employee Separation, a [Project](/docs/user/videos/learn/project-and-task) will be created. Within the Project, [Tasks](/docs/user/videos/learn/project-and-task) will also be created for each Activity. 

You can view the created Projects and Tasks through View > Project/ Tasks.


Additionally, each Activity can be assigned weights based on its importance.

<img class="screenshot" alt="Tasks and Assignments" src="{{docs_base_url}}/assets/img/human-resources/employee-sep1.png">

Based on the progress on the Tasks, progress can be updated in the Employee Separation process.


### 3.3 Employee Status

You can directly view the separated Employee through the Employee Separation doctype through View > Employee once the form is submitted.

> Note: Once the Employee Separation form is submitted, the status of the Employee changes from 'Active' to 'Left'. 


## 4. Related Topics

1. [Employee Onboarding](/docs/user/manual/en/human-resources/employee-onboarding)
1. [Employee Promotion](/docs/user/manual/en/human-resources/employee_promotion)
1. [Employee Separation](/docs/user/manual/en/human-resources/employee-separation)



