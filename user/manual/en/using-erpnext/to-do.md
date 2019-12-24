<!-- add-breadcrumbs -->
# To Do

ToDo is a list of activities that is to be done by a particular individual. 

**In ERPNext, a ToDo is a simple tool where you can define the activities to be done. The ToDo List will enlist all the activities assigned to you and by you.**

![ToDo](/docs/assets/img/using-erpnext/using-to-do-1.png)

A ToDo also gets auto-created when any other Document is assigned to you. Checkout [ToDo-Auto Creation](/docs/user/manual/en/using-erpnext/articles/todo-auto-creation)

To access ToDo, go to

> Home > Tools > ToDo

## 1. How to create a ToDo

1. Go to the ToDo list, and click new.
2. You will be redirected to a Quick Entry for ToDo, wherein you will be required to enter the description of the ToDo.
3. Save.

    ![ToDo](/docs/assets/img/using-erpnext/using-to-do-2.gif)

> Note: While creating a ToDo using the Quick Entry, the ToDo by default gets assigned to the creator. To prevent the same, and assign it to other users, ensure that you edit the ToDo in Full Page.

### ToDo Notification

Once a ToDo is created, the assigned user will get a notification for the ToDo.

![ToDo](/docs/assets/img/using-erpnext/using-todo-notification.png)

### 1.1. Additional Options while creating a ToDo

1. **Status**: You can define the status of the ToDo. While creation, the status of the ToDo would be 'Open' by default. The user can change it to 'Closed' when the assignment is completed.
2. **Priority**: You can define the Priority of this task as Low, Medium or High.
3. **Color**: You can choose to assign a color to each of your ToDos. E.g., a ToDo created as a weekly reminder for sending reports can be assigned the color Purple, where as all the personal ToDos can be assigned the Color Yellow.
4. **Due Date**: You can add the Due Date to all the ToDos.
5. **Allocated To**: In cases where you are assigning a ToDo to another ERPNext User, you can do so here.

    ![ToDo](/docs/assets/img/using-erpnext/using-to-do-3.png)

### 1.2. References

Every Document in ERPNext has an option called 'Assign To' in the side-bar. Using this option, any Dcoument can be assigned to the user. The User would be assigned a ToDo simultaneously. 

1. **Reference Type**: When a ToDo is created from another document, say a Task or an Issue, the Reference Document Type gets linked to the ToDo here. You can also choose to add a Reference Document Type manually.
2. **Reference Name**: On assignment via another DocType, the name of the Reference DocType also gets linked over here.
3. **Assignment By**: When you get assigned aa ToDo via another Document Type, the name of the person making the assignment also gets tagged.

    ![ToDo](/docs/assets/img/using-erpnext/using-to-do-4.png)

## 2. ToDo Statuses
ToDo has 3 statuses, each describing the current state of a task.

* **Open**: A ToDo by default is marked Open when it is created.
* **Closed**: When an activity is completed, the ToDo can be marked as 'Closed' or 'Resolved' or 'Completed'. Further, for conditions like Issue Resolved or task Completed; the ToDo gets closed automatically. It can also be Reopened if required.
* **Cancelled**: When a user gets removed from the assignment of a ToDo/Task/Issue, the ToDo linked to that Document automatically gets 'Cancelled'.

    ![ToDo](/docs/assets/img/using-erpnext/using-to-do-5.png)


{next}
