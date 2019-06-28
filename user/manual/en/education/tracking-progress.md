# Tracking the Progress

The students can view their progress on the portal itself and do not have access to the desk. For instructors and other users of ERPNext, the following doctypes are used to track the progress of the student:

- Program Enrollment
- Course Enrollment
- Course Activity
- Quiz Activity

---

## Program Enrollment

If 'Allow Self Enroll' is enabled for a particular program, an entry is created automatically on behalf of the student. Each student will have only one program enrollment for each program. You can learn more about program enrollment [here]({{ docs_base_url }}/user/manual/en/education/program-enrollment)
<img class="screenshot" alt="Program Enrollment" src="{{docs_base_url}}/assets/img/education/lms/desk-program-enrollment.png">

---

## Course Enrollment

For a particular course in a program, a course enrollment record is automatically created for each course as shown below.
<img class="screenshot" alt="Course Enrollment List" src="{{docs_base_url}}/assets/img/education/lms/desk-course-enrollment-list.png">

For a particular program and its child course, only one course enrollment is created for a student. In case a course is added to the program later, the student will automatically be enrolled to the course when the student visits the portal next.

---

## Course Activity

For each non-quiz type content in a course, a course activity is created every time the student navigates through a content. This activity is created only once per content.

<img class="screenshot" alt="Course Activity List" src="{{docs_base_url}}/assets/img/education/lms/desk-course-activity-list.png">
<img class="screenshot" alt="Course Activity" src="{{docs_base_url}}/assets/img/education/lms/desk-course-activity.png">

---

## Quiz Activity

For each quiz attempt, till the student is allowed to attempt the quiz, a quiz activity is created. This doctype has all the information about the attempt viz. The selected options for each question, attempt date, as well as the result of the quiz.

<img class="screenshot" alt="Quiz Activity" src="{{docs_base_url}}/assets/img/education/lms/desk-quiz-activity.png">
