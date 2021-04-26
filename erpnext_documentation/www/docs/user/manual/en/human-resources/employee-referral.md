<!-- add-breadcrumbs -->

# Employee Referral

> Introduced In Version 13

Internal Recruitment is one of the best process for recruitment, and it also saves effort and capital.
The Employee Referral is the process where Employees refer to a person which is the best fit for a vacant designation/position in Company.

In ERPNext, you can manage Employee Referral.

To access Employee Referral, go to:

> Human Resources > Recruitment > Employee Referral


## 1. Prerequisites
1. [Employee](/docs/user/manual/en/human-resources/employee)
1. [Additional Salary](/docs/user/manual/en/human-resources/additional-salary)
1. [Job Applicant](/docs/user/manual/en/human-resources/job-applicant)

## 2. How to create Employee Referral
1. Go to: Employee Referral > Add Employee Referral.
1. Fill Basic Details of person you want to refer like First Name, Last Name, Email etc.
1. Select Employee under Referrer.
1. Save and Submit.


<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/employee-referral.png">

## 3. Features

### 3.1 Creating Job Applicant and auto syncing status from Job applicant
When you submit employee referral document the initial status will be "Pending". After submit, you will see a custom button for creating a Job Applicant. After Submitting the document Create Job Applicant Button will Appear at top right corner.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/create-job-applicant.png">

On click, Job Applicant will be created with status "Open" and the status of Employee Referral document will change to "In Process"

If someone changes the status of the Job Applicant document to "Hold" or "Replied", The status of the Employee Referral document will remain "In Process". If the status of the Job Applicant is "Accepted" or "rejected", The status of the Employee Referral document will also change to "Accepted" or "rejected" respectively.

### 3.2 Is applicable for referral bonus
Many companies provides Bonus to there employees for such referral. ERPNext allow you pay bonus to employee for there referral.

For Referral bonus you need to check **Is applicable for referral bonus** checkbox before submitting the document. After submitting the document Create Additional Salary Button will Appear at top right corner, if status is Accepted.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/referral-bonus.png">

On Click, It will redirect you to Additional salary form where you need to select Salary component and Payroll date and after that you need to save and submit the document.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/create-referral-bonus.png">







