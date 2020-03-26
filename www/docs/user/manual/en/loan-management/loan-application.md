<!-- add-breadcrumbs -->
# Loan Application
> Introduced in Version 13

**A Loan Application contains details about the applicant and loan security details for review.**

During a loan process, the first step a customer or employee has to do is submit a Loan Application for review. In case of a secured loan, a Loan Application can also contain proposed loan securities.

<img class="screenshot" alt="Make Loan Application" src="{{docs_base_url}}/assets/img/loan-management/loan-application-flow.png">

To access the Loan Application list, go to:
> Home > Loan Management > Loan > Loan Application


<img class="screenshot" alt="Loan Application" src="{{docs_base_url}}/assets/img/loan-management/loan-application.png">

## 1. Prerequisites
Before creating and using a Loan Security, it is advised that you create the following first:

* [Loan Security Type](/docs/user/manual/en/loan-management/loan-security-type)
* [Loan Security](/docs/user/manual/en/loan-management/loan-security)
* [Loan Type](/docs/user/manual/en/loan-management/loan-type)

## 2. How to Create a Loan Application
1. Go to Loan Application List, click on New.
2. Select the Applicant Type.
3. Select the Applicant.
4. Select the Loan Type. All the loan details like rate of interest, loan accounts will be automatically fetched from the Loan Type.
5. Enter the Loan Amount.
6. If the loan is a term loan, enter the Repayment Method. If the Repayment Method is selected as "Repay Over Number Of Periods" then you will have to enter the number of months in which the repayment will be made in "Repayment Period in Months". If the repayment method is selected as "Repay Over Number Of Periods" then you will have to enter the "Monthly Repayment Amount".
7. You can also mention the proposed securities that will be pledged against a loan. For that, first tick the "Is Secure Loan" checkbox. Then in the proposed pledges table, you can enter the securities and their quantities.
8. Click "Save" to save the draft of the Loan Application.
9. Click "Submit" to submit the loan application.

## 3. Features

### 3.1 Creating the Loan Security Pledge
A [Loan Security Pledge](/docs/user/manual/en/loan-management/loan-security-pledge) based on the proposed securities can be created from the Loan Application itself via **Create** button on the top right. This Loan Security Pledge can then be pledged against a loan as an initial Loan Security Pledge.

<img class="screenshot" alt="Loan Application" src="{{docs_base_url}}/assets/img/loan-management/create-loan-security-pledge.png">

### 3.2 Submitting the Loan Application
Once a Loan Application is submitted and approved, you can create a Loan from the Loan Application using the **Create** button and all the required details from the Loan Application will be automatically mapped in the loan.

<img class="screenshot" alt="Loan Application" src="{{docs_base_url}}/assets/img/loan-management/create-loan.png">

{next}


