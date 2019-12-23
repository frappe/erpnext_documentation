# Appointment Booking Settings

## 1. Enable Appointment scheduling

This checkbox will enable appointment scheduling and also enable the `/book_appointment` Route for website users (your customers).

## 2. Agent Details 

In this section, you can add details about agents, such as their working hours and holidays.

### 2.1  Availability of Slots

Here you can set the timing in which your agents are available to attend an appointment. This is set per day of the week. Each row represents a continuous block of time, you can have multiple entries for each day of the week.

For example if your agents work Monday to Friday, 9am to 5pm but with a lunch break at 1.30 for half and hour. You will need to create two entries for each day. One from 9am to 1.30pm and another from 2pm to 5pm.

### 2.2 Agents

This is the list of agents which will be autoassigned to appointments. The number of appointments which can exist in one timeslot also depends upon the number employees in this list.

### 2.3 Holiday list

You can link a (holiday list)[https://erpnext.com/docs/user/manual/en/human-resources/holiday-list] here to apply to the appointment schedule. If the day is a holiday, scheduling an appointment on that day won't be allowed.

## 3. Appointment Details

This section contains details about the appointment themselves.

### 3.1 Appointment Duration in minutes

The duration of appointment in minutes. This is used to calculate appointment timeslots for the web portal. Changing this does not affect the appointments created before the change.

### 3.2 Notify Via Email

Enabling this checkbox will send an email to the participants of the appointments i.e. your employee and the customer on the day of the appointment. Changing this checkbox does not affect the appointments created before the change.

### 3.3 Number of days appointment can be books in advance

This is the number of days the appointment can be booked in advance. If the Holiday List provided above ends before the date calculated using this number, appointment schedulling will be stopped at the end of holiday list end.


## 4. Success settings

### 4.1 Success Redirect URL

This is the URL where the user will be redirect on creation of successful appoitnment creation via Web Portal. Does not apply to desk.
Leave blank for home. This is relative to site URL, for example "about" will redirect to "https://yoursitename.com/about"
