<!-- add-breadcrumbs -->
# Setting Up Income Tax Deduction
Calculating Tax deductions for employees every month is a time-consuming activity for most businesses, especially for large enterprises. If set up properly, ERPNext simplifies most of the tax-related calculations by automatically calculating tax deductions while generating Salary Slips. Here's how you can configure ERPNext to ease your payroll processing -

# Income Tax Exemption
In many countries, especially in India, regulations allow exempting a part (or all) of some type of spendings by individuals from being added to their annual taxable income. Examples of such spendings could be contributions to charitable institutions, the amount spent on the education of children, specific investments, etc. To
avail the exemption from their taxable income, individuals are required to submit proof of such spendings.

ERPNext allows you to configure Income Tax Slabs and the tax is calculated based on the projected annual earnings of the employee. For this, employees are required to declare the exemption amount they plan to claim at the start of the financial year so that the payroll deductions for tax will be calculated based on the projected annual earnings minus the exemption. Employees can declare this through [Employee Tax Exemption Declaration](/docs/v13/user/manual/en/human-resources/employee-tax-exemption-declaration).

If no declaration is submitted by the employee, the monthly deductions will be calculated without any exemption from the employee's annual earnings. However, if the employee submits a declaration in between the payroll period, the tax exemption will be applied from the next payroll onwards. Any additional tax collected in earlier payrolls will be adjusted in the last payroll or when using _Deduct Tax For Unsubmitted Tax Exemption Proof_ in Payroll Entry or Salary Slip.

Also, at the end of the year employees submit the actual proof of the spendings for filing via [Employee Tax Exemption Proof Submission](/docs/v13/user/manual/en/human-resources/employee-tax-exemption-proof-submission). In the last payroll of the Payroll Period, ERPNext checks for proof submissions of employees, and if not found, tax for the exempted income will be added to the standard deduction component.

### Employee Tax Exemption Category
Exemptions from taxable salary are usually restricted to spendings on particular categories decided by government or regulatory agencies. ERPNext allows you to configure various categories which are allowed to be exempted. Examples of this could be, for India, 80G, 80C, B0CC, etc.

You can configure Employee Tax Exemption Category by going to,
> Human resources > Payroll Setup > Employee Tax Exemption Category > New Employee Tax Exemption Category

<img class="screenshot" alt="Employee Tax Exemption Category" src="/docs/v13/assets/img/human-resources/employee-tax-exemption-category.png">

### Employee Tax Exemption Sub Category
Under each category, there could be many heads for which the exemptions are allowed. For example, in India, subcategories under 80C could be Life Insurance Premium

You can configure Employee Tax Exemption Sub Category by going to,
> Human resources > Payroll Setup > Employee Tax Exemption Sub Category > New Employee Tax Sub Exemption Category

<img class="screenshot" alt="Employee Tax Exemption Sub Category" src="/docs/v13/assets/img/human-resources/employee-tax-exemption-subcategory.png">

### HRA Exemption - Regional, India
For the fiscal year 2018-19, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:
 * The actual amount allotted by the employer as the HRA.
 * Actual rent paid less 10% of the basic salary.
 * 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

 As part of the Employee Tax Exemption Declaration, employees shall also fill out the HRA Exemption. ERPNext will calculate the exemption eligible for HRA and exempt it while calculating the taxable earnings.

 > Note: Basic and HRA salary component shall be configured in Company for HRA exemption to work

### Options in Payroll Entry and Salary Slip
ERPNext simplifies payroll processing by automatically processing payroll in bulk via [Payroll Entry](/docs/v13/user/manual/en/human-resources/payroll-entry).

* Deduct Tax For Unclaimed Employee Benefits: Flexible benefits (Salary Components which are _Is Flexible Benefit_) are not included in the taxable income of the employee. However, the amount received for these components will be included in the taxable earnings of the employee if she fails to submit [Employee Benefit Claim](/docs/v13/user/manual/en/human-resources/employee-benefit-claim) while calculating tax in the last payroll of the Payroll Period.

If you wish to collect tax for benefits before the last payroll, check this option and ERPNext will recalculate the tax and add the tax for all untaxed benefits while generating the Salary Slip.

* Deduct Tax For Unsubmitted Tax Exemption Proof: This option allows you to deduct taxes for the earnings which were exempted in previous payrolls as declared in [Employee Tax Exemption Declaration](/docs/v13/user/manual/en/human-resources/employee-tax-exemption-declaration) but the Employee has not submitted sufficient proof via  [Employee Tax Exemption Proof Submission](/docs/v13/user/manual/en/human-resources/employee-tax-exemption-proof-submission). It is to be noted that if this option is checked ERPNext does not consider the Employee Tax Exemption Declaration by employees and will only take into account _Employee Tax Exemption Proof Submission_ instead while calculating exemption from employees' annual earnings.

> Note: If required, you can still process payroll for employees individually, by manually creating a new Salary Slip and both these options are made available in the Salary Slip

# Income Tax Slab
[Income Tax Slab](/docs/v13/user/manual/en/human-resources/income-tax-slab) helps you define Tax slabs applicable for the period, making it easier to manage changing laws. You can add multiple tax slabs for the payroll period depending on the tax regulations. Note that you can use fields in Employee document in the _Condition_ field to apply tax slabs based on attributes of employees.

# Salary Component
To enable automatic tax deduction based on Tax slabs configured in Income Tax Slab, you have to configure a Salary Component of type _Deduction_ with _Variable Based On Taxable Salary_ option enabled. This checkbox enables auto calculation of Income Tax considering the tax slabs and declaration submitted by an employee. The tax will be calculated annually on the remaining taxable salary and equally divide it in 12 months.

>**Important Note:** If you configure condition and formula for this Deduction component, the condition and formula will be considered for calculating the Salary Component and the Tax Slabs configured in Income Tax Slab will be ignored. However, you can still use _Deduct Tax For Unsubmitted Tax Exemption Proof_ option in Payroll Entry / Salary Slip to deduct taxes based on the Tax Slabs configured in Income Tax Slab, exempting [Employee Tax Exemption Proof Submission](/docs/v13/user/manual/en/human-resources/employee-tax-exemption-proof-submission) which will give precedence to the Tax Slab based tax deduction.
This is particularly helpful if you need to deduct a fixed amount as a deduction in each payroll rather than ERPNext automatically calculating the deductions based on the projected annual salary of the employee after exemption as declared by the employee via [Employee Tax Exemption Declaration](/docs/v13/user/manual/en/human-resources/employee-tax-exemption-declaration). At the end of the fiscal year, you can still use _Deduct Tax For Unsubmitted Tax Exemption Proof_ to deduct the remaining tax liability of the employee for the whole period.

{next}
