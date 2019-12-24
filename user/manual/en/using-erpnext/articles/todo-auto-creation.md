<!-- add-breadcrumbs -->
# To-Do Auto Creation

Every Document in ERPNext has an option called 'Assign To' in the side-bar. Using this option, any Dcoument can be assigned to the user. The User would be assigned a ToDo simultaneously. 

![ToDo Auto Creation](/docs/assets/img/using-erpnext/using-todo-auto-assign-1.gif)

Under such conditions, the three ToDo stasuses are defined as per the updates on the assignment. 

Let's consider a scenario where a ToDo is assigned via an Issue. Let's say that there are 2 levels of Support in an organization L1 and L2 and every new support ticket is considered as an L1 support issue and assigned to relevant team members. In this case, the ToDo stasuses would vary as follows:

1. **Open**: When an issue is created and assigned to an L1 support team member.
2. **Closed**: L1 support team member identifies the issue and resolves it.
3. **Cancelled**: L1 support team member identifies the issue as a L2 support level issue and assignes it to the relevant team member.

## Reopening of Closed Assignments

In the same scenario as above, let's say that the support ticket was marked close by an L1 support team member. However, the ISsue gets reopened if the ticket is reopened again, or there was an activity in this issue

Simultaneously the ToDo associated with the Support Ticket will also be reopened.

![ToDo](/docs/assets/img/using-erpnext/using-to-do-6.png)
