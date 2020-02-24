<!-- add-breadcrumbs -->
# Salary Component

**Salaries are paid by organizations to their employees in exchange for the services rendered by them. The different components that make up the Salary Structure are called as Salary Components.** 

The salary paid to the employees comprises of a number of different components, such as basic salary, allowances, arrears, etc. ERPNext allows you to define these Salary Components and also specify its various attributes.

To access Salary Component, go to:
> Home > Human Resources > Payroll > Salary Component

## 1. How to create a Salary Component

To create a new Salary Component:

1. Go to: Salary Component > New.
2. Enter its Name and Abbr.
3. Enter Description of the Salary Component (optional).
1. Enter the Company name and the Default Account of the Salary Component.
3. Save.

<img class="screenshot" alt="Salary Component" src="{{docs_base_url}}/assets/img/human-resources/salary-component1.png">

## 2. Features

Apart from the above mentioned mandatory fields, some of the additional features of the Salary Component are given below:

### 1. Condition and Formula

In this section, the Condition and Formula required for the calculation of the Salary Component can be specified. In order to specify the formula, enable the 'Amount based on formula' checkbox. 

<img class="screenshot" alt="Holiday List" src="{{docs_base_url}}/assets/img/human-resources/salary-component2.png">

> Note: In case the Salary Component is based on a pre-defined amount, ERPNext allows you to directly enter the amount in the Amount field (disable the 'Amount based on formula' checkbox).

### 2. Additional Checkboxes

Some of the additional attributes of the Salary Component that can be enabled using checkboxes are as follows:

* Is Payable: This checkbox can be enabled if the Salary Component type is payable.
* Depends on Payment Days: If this checkbox is enabled then the Salary Component will be calculated based on the number of working days.
* Is Tax Applicable: Selecting this checkbox allows you to apply tax on this Salary Component.
* Deduct Full Tax on Selected Payroll Date: 
* Round to the Nearest Integer: Selecting this checkbox allows you to round the amount of this Salary Component to the nearest integer.
* Statistical Component: If selected, the value specified or calculated in this component will not contribute to the earnings or deductions. However, it's value can be referenced by other components that can be added or deducted.
* Do Not Include in Total: Selecting this checkbox ensures that the Salary Component is not included in the Total Salary.
* Disabled: This checkbox can be selected to disable this Salary Component. A disabled Salary Component cannot be used in the Salary Structure.


## 3. Related Topics

1. [Salary Structure](/docs/user/manual/en/human-resources/salary-structure)
1. [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment)
1. [Payroll Entry](/docs/user/manual/en/human-resources/payroll-entry)
1. [Payroll Period](/docs/user/manual/en/human-resources/payroll-period)