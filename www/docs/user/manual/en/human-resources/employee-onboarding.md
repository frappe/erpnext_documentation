# Employee Onboarding 

**In the process of hiring an Employee, there are set of standard activities which need to be executed. This feature helps you to maintain the masters of these activities, and create a set of tasks at the time of each Employee hiring.**

Employee Onboarding is created for a Job Application, who is approved for the hiring.

**Use Case:** Let's assume that following are the activities which need to be performed as soon as a job applicant is approved to be hired.

- Perform a legal and professional background check
- Create an Employee master
- Create an Email Account
- Create an identity card
- Allocate leaves


In ERPNext, these standard activities can be tracked in the Employee Onboarding Template. To access Employee Onboarding, go to: 

> Human Resources > Employee Lifecycle > Employee Onboarding

## 1.  Prerequisites

Before creating an Employee Onboarding, it is advisable that you create the following documents:

* [Job Applicant](/docs/user/manual/en/human-resources/job-applicant)
* [Employee](/docs/user/manual/en/human-resources/employee)
* [Department](/docs/user/manual/en/human-resources/department)
* [Designation](/docs/user/manual/en/human-resources/designation)
* [Employee Grade](/docs/user/manual/en/human-resources/employee-grade)

## 2. How to create an Employee Onboarding

1. Go to: Employee Onboarding > New.
1. Select the Job Applicant. once the Job Applicant is selected, the corresponding Employee will automatically get fetched.
1. Select the [Employee Onboarding Template](#31-employee-onboarding-template). Based on the template selected, information such as Department, Designation and Employee grade will be automatically fetched (if already mentioned in the Onbaording Template).
1. Enter Date of Joining.
1. Save and Submit.


  <img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/employee-onboarding1.png">



> Note 1: If an Employee Onboarding Template isn't created, you can directly fill the onboarding information in the Employee Onboarding doctype itself.

> Note 2: The 'Status' of the Employee Onbaording will change to Completed once all the associated Activities are complete.


## 3. Features

### 3.1 Employee Onboarding Template

The Employee Onboarding Template is a blueprint which contains a predefined list of Activities for Employee Onboarding. An Employee Onboarding Template can be created for a particular Department, Designation and Employee Grade. 

To create a new Employee Onboarding Template:

1. Go to: Human Resources > Employee Lifecycle > Employee Onboarding Template > New.
1. Enter the Department, Designation and Employee Grade (optional).
1. Mention the Activities for onboarding. For each Activity, you can also mention the User or Role, or one of it, to whom this Activity will be assigned.
  
  <img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-template.png">


### 3.2 Tasks and Assignments

On submission of the Employee Onboarding, a [Project](/docs/user/manual/en/projects/project) will be created. Within the Project, [Tasks](/docs/user/manual/en/projects/task) will also be created for each Activity. 

You can view the created Projects and Tasks as shown below:

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/project-task.png">

Additionally, each Activity can be assigned weights based on its importance.

<img class="screenshot" alt="Tasks and Assignments" src="{{docs_base_url}}/assets/img/human-resources/employee-onboarding3.png">

Based on the progress on the Tasks, progress can be updated in the Employee Onboarding process.


### 3.3 Employee Creation

You can directly create an Employee through the Employee Onboarding doctype (if not already created) once all the mandatory onboarding tasks are complete.

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-employee.png">


## 4. Related Topics

1. [Employee Promotion](/docs/user/manual/en/human-resources/employee_promotion)
1. [Employee Separation](/docs/user/manual/en/human-resources/employee-separation)
1. [Employee Transfer](/docs/user/manual/en/human-resources/employee_transfer)


