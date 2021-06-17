<!-- add-breadcrumbs -->

# Assignment Rule

> Introduced in Version 12

**An Assignment Rule lets you set up automatic assignment of documents to Users.**

Assignment Rule will be useful in a scenario wherein you have a support team and incoming support tickets. To assign the support tickets automatically amongst the employees who work on support, an Assignment Rule can be used.

To access Assignment Rule, go to:
> Home > Settings > Assignment Rule

## 1. How to create an Assignment Rule
To set up an automatic assignment:

1. Go to the Assignment Rule list, click on New.
1. Select the Document Type you want to assign automatically (for example **Issue**).
1. Write the "Description" that will be added to the To Do.
1. Select the condition for the assignment.
    You can write simple Python expressions for automatic assignment in the `Assign Rule`, `Close Rule` and `Unassign Rule`. You will have access to all the properties of the document and can use operators like >, <, ==, etc and also multiple conditions like `and` and `or`.

    Examples:

    - `status == "Open"`
    - `issue_type == "Technical" and priority=="High" and status == "Open"`

1. Select the assignment rule.
    ![Assignment Rule](/docs/v12/assets/img/automation/assignment-rule-select.png)

    * **Round Robin**: Assign each document to a User in sequence.
    * **Load Balancing**: Assign new documents to the User who has the least number of assignments.

        Select the list of Users to whom this Assignment Rule will apply:
        <img class="screenshot" alt="Assign" src="{{docs_base_url}}/v12/assets/img/automation/auto-assign-2.png">

    * **Based on Field**: Introduced in v13, this rule can be used to assign a document to the User that is set in the configured field.

        Select the User link field which will determine to whom this Assignment Rule will apply:
        <img class="screenshot" alt="Field Assign" src="{{docs_base_url}}/v12/assets/img/automation/field-auto-assign.png">


1. Save.

You can use properties of the document in the Description field that will be part of the assignment. Higher 'Priority' Assignment Rules will be applied first.

Example:

High Priority Issue *File Upload not working* has been assigned to you.

### 1.1 Multiple Assignment Rules

You can also set up multiple auto assignments for each Document Type, the one with the highest Priority will be applied first:

Here is an example of an Assignment Rule.

Set Document Type, Descriptions and Conditions.
<img class="screenshot" alt="Assign" src="{{docs_base_url}}/v12/assets/img/automation/auto-assign-1.png">

### 1.2 Setting Due Date for assignment

You can auto set due dates for assignments based on the date field in the reference document.

Example:

If you want to set a due date on Issue assignment based on the "Resolution By" date of the Issue, you can do so by selecting "Resolution By" field in `Due Date Based On` option in Assignment Rule.

![Due Date Based On](/docs/v12/assets/img/automation/assignment-rule-due-date-based-on.png)

**Note:**

- "Due Date Based On" option will not be available if "Document Type" is not yet selected or if the selected Document Type does not have any "Date" or "Datetime" field.
- Due Date in the assignment/ToDo will be updated whenever the "Due Date Based On" field value is updated in the reference document.

### 2. Related Topics

1. [Workflows](/docs/user/manual/en/setting-up/workflows)
1. [Workflow Actions](/docs/user/manual/en/setting-up/workflow-actions)
