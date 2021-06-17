<!-- add-breadcrumbs -->
# Education Settings

**The Education Settings will allow you to do a basic setup for your Institute wherein you can define the Academic Year, Academic Term, and other defaults for your ERPNext account.**

These configuration settings will have an impact throughout the module.

To access Academic term, go to:

> Home > Education > Settings > Education Settings

## 1. Steps to configure Education Settings

1. Select the current Academic Year. This will become the default Academic Year throughout your account.
2. Select the current Academic Term. This will become the default Academic Term throughout your account.
3. Select the Attendance Freeze date. Any attendance captured after the Attendance Freeze Date would not be valid.
4. Select how you want the Instructor Records to be created, using Full Name, using Naming series or using Employee Number.
5. **Instructor Record to be created by**: You can select how you want the Instructor Records to be created in your ERPNext system, whether it should be by Full Name, by Naming series, or by Employee Code.

 ![Education Settings](/docs/assets/img/education/education-seetings-1.png)

### 1.1. Configuring Properties

* **Validate Batch for Students in Student Group**: When adding students to a student group via Batch, the system will verify whether the student belongs to that batch or no, and if the same has not happened, an error will be shown while saving the Student Group.
* **Validate Batch for Students in Student Group**: When adding students to a student group via Course, the system will verify whether the student is enrolled to that course or no, and if the same has not happened, an error will be shown while saving the Student Group.
* **Make Academic Term Mandatory**: When enabled, this option will ensure that while creating a Program Enrollment via the [Program Enrollment Tool](/docs/user/manual/en/education/program-enrollment-tool), the user has to enter the Academic Term.
* **Skip User Creation for New Student**: Whenever a new student is created, by default a User is created against it. If this option is enabled, no new User will be created when a new Student is created.

### 1.2. LMS Settings

The Education module is bundled with a Learning Management System (LMS) out of the box. This allows institutes to publish their programs on their website. Programs can contain rich text articles, videos, and even quizzes. The progress of individual students can be tracked through the desk as well as the portal.

Once you Enable LMS for your ERPNext Education module, the following settings would be available for configuration:

1. **LMS Title**: Enter the Title for your LMS. It could be the name of your Institute.
2. **Description**: You can add the description of the course for your LMS.

![Education Settings](/docs/assets/img/education/education-seetings-1.png)

You can further go to [LMS Activity](/docs/user/manual/en/education/setting-up-lms) to add the courses, articles or quizzes for your LMS. To access your LMS portal, you may go to the URL, {yourdomainname}.erpnext.com/lms

{next}
