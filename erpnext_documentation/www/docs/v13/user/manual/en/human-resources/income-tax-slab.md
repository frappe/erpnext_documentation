<!-- add-breadcrumbs -->
# Income Tax Slab

**Income Tax Slab is a document to define income tax rates based on different taxable income slab.** 

In many countries, income tax is levied on individual taxpayers based on a slab system where different tax rates have been prescribed for different slabs and such tax rates keep increasing with an increase in the income slab. In ERPNext, you can define multiple Income Tax Slabs and link them to individual employee's salary structure via Salary Structure Assignment.

To access Income Tax Slab, go to:
> Home > Human Resources > Payroll > Income Tax Slab

## 1. How to create an Income Tax Slab

To create a new Income Tax Slab:

1. Enter a Name for the IT Slab, Company and the date from which it will be Effective From.
1. Enable the checkbox 'Allow Tax Exemption' if applicable.
1. Save and Submit.

## 2. Features

### 2.1 Tax Slabs

In the Tax Slab table, you can define the rate for different income slabs. To define slab, From Amount and To Amount should be entered. For the first slab, From Amount is optional and for the last slab, To Amount is optional. Both the amount is inclusive while evaluating tax based on taxable income.


<img class="screenshot" alt="Income Tax Slab" src="/docs/assets/img/human-resources/income-tax-slab.png">

The tax slab can be applicable based on specific conditions. Conditions can be written using all field names of Employee, Salary Structure, Salary Structure Assignment, and Salary Slip documents.

Examples:

```
// Apply tax if employee born between 31-12-1937 and 01-01-1958 (Employees aged 60 to 80)
date_of_birth > date(1937, 12, 31) and date_of_birth < date(1958, 01, 01)

// Apply tax by employee gender
gender == "Male"

// Apply tax by Salary Component
base > 10000

// Annual Taxable income is greater than 5 lakhs
annual_taxable_earning > 500000
```

### 2.2 Other Taxes and Charges on Income Tax

If other taxes are applicable on calculated income tax, you can enter those using this table. You can also define the min and max taxable amount for which this tax will be applicable.
For example, Health and Education Cess is applied additionally on income tax to everyone in India.

<img class="screenshot" alt="Other Charged on Income Tax" src="/docs/assets/img/human-resources/other-taxes-on-income-tax.png">


### 2.3 Other Properties

- **Allow Tax Exemptions:** Tax exemptions can be allowed for a specific Income Tax Slab. If enabled, while calculating taxes based on this tax slab, Employee Tax Exemption Declaration and Proof Submission are considered for calculating taxable income.
- **Standard Tax Exemption Amount:** If exemption is allowed, the Standard Tax Exemption Amount defined by the government can be added here. This exemption generally does not need any kind of document proof and applicable to all employees linked to this income tax slab.

## 3. Related Topics

1. [Salary Component](/docs/user/manual/en/human-resources/salary-component)
1. [Salary Structure](/docs/user/manual/en/human-resources/salary-structure)
1. [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment)
1. [Payroll Entry](/docs/user/manual/en/human-resources/payroll-entry)
1. [Employee Tax Exemption Declaration](/docs/user/manual/en/human-resources/employee-tax-exemption-declaration) 
1. [Employee Tax Exemption Proof Submission](/docs/user/manual/en/human-resources/employee-tax-exemption-proof-submission)
