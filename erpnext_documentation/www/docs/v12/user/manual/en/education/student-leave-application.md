<!-- add-breadcrumbs -->
# Student Leave Application

**Student Leave Application is a formal document to keep a track of leaves for a student.**

To access Student Leave Application list, go to:

> Home > Education > Attendance > Student Leave Application

## 1 How to create a Student Leave Application

1. Go to the Student Leave Application list, and click on New.
2. Select the Student.
3. Set the 'From Date' and 'To Date' fields for specifying the period.
4. Marking Attendance for the Leave Application is governed by the 'Attendance Based On' field. In ERPNext, Student Attendance can be marked in two ways:

    * **Course Schedule**: If attendance is taken for every lecture (in colleges/universities), then the leave application can be created for that particular course schedule slot.

    * **Student Group**: If attendance is taken for the entire day then student group (class/division) is used to mark attendance so that leave is calculated for the entire day

5. Based on the Attendance field, select the Student Group or Course Schedule. Optionally enter the reason.
6. In case the student is not attending the institute to participate or represent the institute in any event, he/she can be marked as "Present" from the Leave Application itself by checking _Mark as Present_.
7. Save. The 'Total Leave Days' will be calculated and set in the document after excluding the holidays which are part of your default [Holiday List](/docs/user/manual/en/human-resources/holiday-list).

    ![Student Leave Application](/docs/v12/assets/img/education/student-leave-application.png)

### 1.2 On Submission of Student Leave Application

Once the Student Leave Application is submitted, a Student Attendance record is automatically created with status as 'Absent'. If _Mark as Present_ is checked, then the status of the Attendance Record is set as 'Present'. The Leave Application is linked to this Student Attendance document for reference.

![Student Attendance](/docs/v12/assets/img/education/leave-attendance-record.png)

If any of the dates within the leave period is a holiday, then, Student Attendance record creation is skipped for that date.

### 1.3 On Cancellation of Student Leave Application

On cancellation of the Student Leave Application, the linked Student Attendance record is also cancelled automatically.

## 2. Tutorial Video for Student Leave Application

<div>
    <div class='embed-container'>
        <iframe src='https://www.youtube.com/embed/NwwH5t-NKBE' frameborder='0' allowfullscreen>
        </iframe>
    </div>
</div>

## 3. Related Topics

1. [Student Attendance](/docs/user/manual/en/education/student-attendance).

{next}
