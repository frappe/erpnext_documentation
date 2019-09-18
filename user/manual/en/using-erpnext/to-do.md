<!-- add-breadcrumbs -->
# To Do

To Do is a simple tool where all the activities [assigned](/docs/user/manual/en/using-erpnext/assignment) to you and assigned by you are listed. You can also add your own to-do items in the list.

<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/collaboration-tools/assign-3.png">

When a task is completed, you should simply remove the assignment from the assigned document. With this, the task will be removed from your Todo list as well. For ToDos which are not assigned via document, you can set their status as Closed from the Todo master itself.

## ToDo Statuses
ToDo has 3 statuses, each describing a current state of a task.

| Status | Description | Visible in sidebar |
|-----------|------------------------------------------------------------------------------------------------|-----------------------|
| **Open** | When the assignment is first created | Yes |
| **Closed** | For conditions like Issue is resolved or Task is completed (can be reopened) | Yes |
| **Cancelled** | Assignment is removed via the sidebar and the User is not associated to the task/issue anymore | No |

## Assignment Rules
ToDos can be automatically assigned via assignment rules. [Assignment rule](/docs/user/manual/en/setting-up/automation/assignment-rule) also has three conditions. Let's consider an example of the Issue form where there are two priority levels, Level 1 (L1) and Level 2 (L2).

| Condition | Example Scenario | ToDo State |
|--------------------|-----------------------------|------------|
| Assign Condition | A L1 issue is created | Open |
| Close Condition | L1 issue is solved | Closed |
| Unassign Condition | L1 Issue is escalated to L2 | Cancelled |

## Reopening of Closed Assignments
In going through the workflow, if no assignments or cancellations are made, the system will try to see if there are any assignments associated with the documents which are closed. For example, if a support ticket was marked resolved by someone and the assignment is marked closed manually or via assignment rule, but the issue was not solved and the ticket is reopened, the system will reopen the closed assignment.

<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/collaboration-tools/assign-4.png">

{next}
