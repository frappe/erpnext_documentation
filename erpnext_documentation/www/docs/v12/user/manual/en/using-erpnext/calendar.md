<!-- add-breadcrumbs -->
# Calendar

**The Calendar is a Tool which helps you to create, share and keep track of events in your ERPNext account.**

You can have a Day, Week or Month view in a calendar.

![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-1.png)

To access calendar, go to:

> Home > Tools > Calendar

## 1. Creating Events in Calendar

1. Go to Calendar and click on New.
2. Enter the Subject and the Start Date of the event.
3. Save.

![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-2.gif)

Alternatively, you can also create an event from the 'Day View' of the Calendar. This view is broken into various slots throughout the day. You can select the slot for the start of the event, enter the subject of the event and drag it own till the event end time.

![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-3.gif)

### 1.1. Event Based on a Lead

In the Lead form, you will find a field called Next Contact By and Next Contact Date. Once you specify the date and the User in these fields, an event will automatically be created for the User on the given date and time.

![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-4.png)

### 1.2. Event Based on Job Cards

For every Job Card that gets created for a User in the ERPNext account, a corresponding event will be created in the Calendar. 

![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-job-card.png)

### 1.3. Birthday Event

Birthday Event is created based on Date of Birth specified in the Employee master.

### 1.4. Recurring Events

There are various events in an organization that occur regularly at periodic intervals. In ERPNext, you can create such events by enabling the 'Repeat this Event' property for that particular event. 

When you do this, you will ve asked to enter the periodicity of this event in the 'Repeat On'. This could be daily, monthly, weekly or Yearly. 

You can also enter the last day of the repeated occurrence in the 'Repeat Till' field. In case of infinite repetitions, you may choose to leave this field blank.

![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-5.gif)

### 1.5. Event Reminders

There are two ways you can receive email reminder for an event.

1. Enable Reminder in Event

 In the Event master, checking "Send an email reminder in the morning" will trigger a notification email to all the participants for this event.

 ![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-6.png)

2. Create Email Digest

 To get email reminders for event, you should set Email Digest for Calendar Events.

 Email Digest can be set from:

 > Setup > Email > Email Digest

 ![Calendar](/docs/v12/assets/img/using-erpnext/using-calender-7.png)

{next}
