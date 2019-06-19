<!-- add-breadcrumbs -->

# Assignment Rule

You can setup automatic assignment of documents to users by creating **Assignment Rule**.

> Introduced in Version 12

To setup an automatic assignment:

1. Select the Document Type you want to assign automatically (for example **Issue**).
1. Write the "Description" that will be added to the To Do
1. Select the condition for assignment (see section below).
1. Select the assignment rule (**Round Robin** or **Load Balancing**).
1. Select the list of users who need to be assigned issues.

### Description

You can uses properties of the document in description that will be part of the assignment.

Example:

    High Priority Issue -> "{{ name }}" has been assigned to you.

### Assign / Unassign Conditions

You can write simple Python expressions for automatic assignment in the `Assign Rule` and `Unassign Rule`. You will have access to all the properties of the document and can use operators like >, <, == etc and also multiple conditions like `and` and `or`

Examples:

- `status == "Open"`
- `issue_type == "Technical" and priority=="High" and status == "Open"`

### Assignment Rules

There are 2 rules:

1. Round Robin: Assign each document to a user in sequence.
2. Load Balancing: Assign to the user who has the least number of assignments.

### Multiple Assignment Rules

You can aslo setup multiple auto assignments for each Document Type, the one with the highest Priority will be applied first

### Example

<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/setup/automation/auto-assign-1.png">

Image 1: Set Document Type, Descriptions and Conditions

<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/setup/automation/auto-assign-2.png">

Image 2: Set Rule and Users
