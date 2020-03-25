<!-- add-breadcrumbs -->
# Loan Security Unpledge
> Introduced in Version 13

**Once all the loan amount is paid, a Loan Security Unpledge is created for unpledging the securities.**

<img class="screenshot" alt="Make Loan Security Unpledge" src="{{docs_base_url}}/assets/img/loan-management/loan-security-unpledge-flow.png">

To access the Loan Security Unpledge list, go to:
> Home > Loan Management > Loan Security > Loan Security Unpledge

## 1. Prerequisites
Before creating a Loan Security Unpledge, you must create the following first:

* [Loan Security Type](/docs/user/manual/en/loan-management/loan-security-type)
* [Loan Security](/docs/user/manual/en/loan-management/loan-security)
* [Loan](/docs/user/manual/en/loan-management/loan)


## 2. How to Create a Loan Security Unpledge
1. Go to Loan Security Unpledge List, click on New.
2. Select Loan against which the securities are unpledged.
3. Select Applicant.
4. Select Company
5. In the securities table enter the Loan Security and their quantity to be unpledged. Also enter the [Loan Security Pledge](/docs/user/manual/en/loan-management/loan-security-pledge) for which the securities needs to be unpledged.
6. Click "Save" to save the draft of the Loan Security Unpledge.
7. Click "Submit" to unpledge the loan securities

<img class="screenshot" alt="Loan Application" src="{{docs_base_url}}/assets/img/loan-management/loan-security-unpledge.png">


### 2.1. Other ways to create a Loan Security Unpledge
You can also create a Loan Security Unpledge from a Loan on which loan closure is requested via the **Create** button on the top right

<img class="screenshot" alt="Loan Application" src="{{docs_base_url}}/assets/img/loan-management/create-loan-security-unpledge.png">

## 3. Features

### 3.1 Approval of Loan Security Unpledge Request
On approval of the Loan Security Unpledge it will automatically update the qty and status in the corresponding [Loan Security Pledge](/docs/user/manual/en/loan-management/loan-security-pledge). In case of full unpledge the status in Loan Security Pledge against which the unpledge request is made will set as "Unpledge" otherwise it will be set as "Partially Pledged". In case of full unpledge, the Loan against which unledge request is made will also be automatically closed.

{next}



