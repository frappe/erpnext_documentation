<!-- add-breadcrumbs -->

# Employee Referral

> Introduced In Version 13

Internal Recruitment is one of the best processes for recruitment, and it also saves effort and capital.
The Employee Referral is a process where existing employees refer a suitable candidate from their network for a vacant designation/position.

In ERPNext, you can manage Employee Referrals.

To access Employee Referral, go to:

> Human Resources > Recruitment > Employee Referral


## 1. Prerequisites
1. [Employee](/docs/v13/user/manual/en/human-resources/employee)
1. [Additional Salary](/docs/v13/user/manual/en/human-resources/additional-salary)
1. [Job Applicant](/docs/v13/user/manual/en/human-resources/job-applicant)

## 2. How to create Employee Referral
1. Go to Employee Referral > Add Employee Referral.
1. Fill in basic details of the person you want to refer like First Name, Last Name, Email, etc.
1. Select Employee under Referrer.
1. Save and Submit.


<img class="screenshot" alt="Leave Allocations"
    src="{{docs_base_url}}/assets/img/human-resources/employee-referral.png">

## 3. Features

### 3.1 Creating Job Applicant and auto-syncing status from Job Applicant
When you submit an employee referral document the initial status will be "Pending". After submitting the document, the "Create Job Applicant" button will appear at the top right corner.

Clicking this button will create a new **Job Applicant** with the status "Open". The status of the **Employee Referral** document will change to "In Process"

<img class="screenshot" alt="Leave Allocations"
    src="{{docs_base_url}}/assets/img/human-resources/create-job-applicant.png">

When someone changes the status of the **Job Applicant** to "Hold" or "Replied", the status of the **Employee Referral** will remain "In Process". If the status of the **Job Applicant** changes to "Accepted" or "Rejected", the status of the **Employee Referral** document will also change to "Accepted" or "Rejected" respectively.

### 3.2 Managing referral bonus
Many companies provide bonuses to their employees for such referrals. ERPNext allows you to track the payment of the bonus to the employee for their referral.

For the Referral bonus, you need to check the "Is applicable for referral bonus" checkbox before submitting the document. After submitting the document, the "Create Additional Salary" button will appear at the top right corner, if the status is "Accepted".

<img class="screenshot" alt="Leave Allocations"
    src="{{docs_base_url}}/assets/img/human-resources/referral-bonus.png">

On Click, It will redirect you to the Additional salary form where you need to select Salary component and Payroll date and after that, you need to save and submit the document.

<img class="screenshot" alt="Leave Allocations"
    src="{{docs_base_url}}/assets/img/human-resources/create-referral-bonus.png">
