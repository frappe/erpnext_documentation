<!-- add-breadcrumbs -->

# Assignment Rule

> Introduced in Version 12

**An Assignment Rule lets you set up automatic assignment of documents to Users.**

Assignment Rule will be useful in a scenario like—you have a support team and incoming support tickets. To assign the support tickets automatically amongst the employees who work on support, an Assignment Rule can be used.

To access Assignment Rule, go to:
> Home > Settings > Assignment Rule

## 1. How to create an Assignment Rule
To set up an automatic assignment:

1. Go to the Assignment Rule list, click on New.
1. Select the Document Type you want to assign automatically (for example **Issue**).
1. Write the "Description" that will be added to the To Do.
1. Select the condition for the assignment.
    You can write simple Python expressions for automatic assignment in the `Assign Rule` and `Unassign Rule`. You will have access to all the properties of the document and can use operators like >, <, ==, etc and also multiple conditions like `and` and `or`

    Examples:

    - `status == "Open"`
    - `issue_type == "Technical" and priority=="High" and status == "Open"`

1. Select the assignment rule (**Round Robin** or **Load Balancing**).
    * **Round Robin**: Assign each document to a User in sequence.
    * **Load Balancing**: Assign new documents to the User who has the least number of assignments.

    ![Assignment Rule](/docs/assets/img/setup/automation/assignment-rule-select.png)
1. Select the list of Users to whom this Assignment Rule will apply.
    <img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/setup/automation/auto-assign-2.png">

1. Save.

You can use properties of the document in the Description field that will be part of the assignment. Higher 'Priority' Assignment Rules will be applied first.

Example:

High Priority Issue *File Upload not working* has been assigned to you.

### 1.1 Multiple Assignment Rules

You can also set up multiple auto assignments for each Document Type, the one with the highest Priority will be applied first:

Here is an example of an Assignment Rule.

Set Document Type, Descriptions and Conditions.
<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/setup/automation/auto-assign-1.png">

### 2. Related Topics
1. [Workflows](/docs/user/manual/en/setting-up/workflows)
1. [Workflow Actions](/docs/user/manual/en/setting-up/workflow-actions)
