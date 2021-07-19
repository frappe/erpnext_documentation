<!-- add-breadcrumbs -->
# Salary Component

**Salaries are paid by organizations to their employees in exchange for the services rendered by them. The different components that make up the Salary Structure are called as Salary Components.** 

Salary paid to the employees comprises of several different components, such as basic salary, allowances, arrears, etc. ERPNext allows you to define these Salary Components and also specify its various attributes.

To access Salary Component, go to:
> Home > Human Resources > Payroll > Salary Component

## 1. How to create a Salary Component

To create a new Salary Component:

1. Go to Salary Component list, click on New.
2. Enter its Name and Abbreviation.
3. Enter Description of the Salary Component (optional).
1. Enter the Company name and the Default Account of the Salary Component in the Accounts table.
3. Save.

 <img class="screenshot" alt="Salary Component" src="{{docs_base_url}}/v12/assets/img/human-resources/salary-component1.png">

## 2. Features

Apart from the above mentioned mandatory fields, some of the additional features of the Salary Component are given below:

### 2.1 Condition and Formula

In this section, the Condition and Formula required for the calculation of the Salary Component can be specified. To specify the formula, enable the 'Amount based on formula' checkbox. 

<img class="screenshot" alt="Salary Component" src="{{docs_base_url}}/v12/assets/img/human-resources/salary-component2.png">

In case the Salary Component is based on a pre-defined amount, ERPNext allows you to directly enter the amount in the Amount field (disable the 'Amount based on formula' checkbox).

> **Note:** This above setup is optional. You can define Amount and Formula/Condition for a Salary Component directly in the Salary Structure also. If they are specified in the Salary Component document itself, the information will be directly fetched in the Salary Structure when the Component is selected.

### 2.2 Additional Properties

Some of the additional attributes of the Salary Component that can be enabled using checkboxes are as follows:

* **Is Payable:** Select this if the Salary Component is payable.
* **Depends on Payment Days:** If this checkbox is enabled then the Salary Component will be calculated based on the number of working days.
* **Is Tax Applicable:** This checkbox is applicable for Earning Components. Selecting this checkbox allows tax to be applied on this Salary Component.
* **Deduct Full Tax on Selected Payroll Date:** If checked and the component is used in Additional Salary, the tax amount applicable on the additional amount will be deducted on the specific payroll month. If not checked, the tax will be distributed over the remaining months of the payroll period. For example, if a bonus is given in a particular month using Additional Salary, then you can deduct full tax amount in the same month only.
* **Round to the Nearest Integer:** Selecting this checkbox allows you to round the amount of this Salary Component to the nearest integer.
* **Statistical Component:** If selected, the value specified or calculated in this component will not contribute to the earnings or deductions. However, it's value can be referenced by other components that can be added or deducted. If you set a Salary Component as a Statistical component, then you do not have to set the Default Account for the same. Also, you would not be able to set this component as a Flexible Benefit.
* **Do Not Include in Total:** Selecting this checkbox ensures that the Salary Component is not included in the Total Salary. It is used to define the component which is part of the CTC but not payable (e.g. Usage of Company Cars).
* **Variable Based On Taxable Salary:** The component is calculated automatically on taxable income based on applicable Income Tax Slab (e.g. TDS or Income Tax).
* **Exempted from Income Tax:** If checked, the full amount will be deducted from taxable income before calculating income tax without any [declaration](/docs/user/manual/en/human-resources/employee-tax-exemption-declaration) or [proof submission](/docs/user/manual/en/human-resources/employee-tax-exemption-proof-submission). For example, Professional Tax in India is deducted from taxable income before calculating income tax. 
* **Disabled:** This checkbox can be selected to disable this Salary Component. A disabled Salary Component cannot be used in the Salary Structure.

### 2.3 Flexible Benefits

This section is shown if the Salary Component is an Earning Component. Flexible Benefit plans allow employees to avail the benefits they want or need from a package of programs offered by an employer. They may include health insurance, pension plans, telephone expenses, etc. To set a Salary Component as a Flexible Benefit, check the 'Is Flexible Benefit' checkbox.

<img class="screenshot" alt="Flexible Benefit" src="{{docs_base_url}}/v12/assets/img/human-resources/flexible-ben.png">

Enter the maximum yearly amount for this flexible benefit in the 'Max Benefit Amount (Yearly)' field. Some of the additional attributes of the Flexible Benefits that can be enabled using checkboxes are as follows:   

* **Pay Against Benefit Claim:** Enable this checkbox if you want to pay this benefit via the [Employee Benefit Claim](/docs/user/manual/en/human-resources/employee-benefit-claim).
* **Only Tax Impact (Cannot Claim But Part of Taxable Income):** If set, the flexible benefit will be part of taxable income.
* **Create Separate Payment Entry Against Benefit Claim:** If this checkbox is checked, it will let you create a separate payment entry against the Benefit Claim.

## 3. Related Topics

1. [Salary Structure](/docs/user/manual/en/human-resources/salary-structure)
1. [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment)
1. [Payroll Entry](/docs/user/manual/en/human-resources/payroll-entry)
1. [Payroll Period](/docs/user/manual/en/human-resources/payroll-period)
