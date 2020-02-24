# Navigating on the Portal

## Home Page

The portal is hosted on `/lms` route. (Example. `hogwarts.erpnext.com/lms`) Here all the programs are shown in the form of cards. Each card is clickable and navigates to the corresponding program/course/topic/content. The portal is accessible even if a student has not logged in, however the content (Articles, Videos, etc) can only be accessible after login and enrolling in the program.

![LMS Navigation](/docs/assets/img/education/education-lmms-3.png)

## Program Page
On the program page, the student can see the description as well as the list of courses in the form of cards. If the student is not enrolled, a button to enroll will be shown. This will happen only if self enroll is enabled in the program doc, if not then the program won't be visible to the student at all.

After enrolling, the status of each course is added to the card footer. This status is updated based on the student's activity on the portal.

![LMS Navigation](/docs/assets/img/education/education-navigation-1.png)

---

## Course Page
Similar to the program page, it lists all the topics, as well as the status of each topic. Clicking on any card will navigate to the topic page. A list of contents is shown in each topic card, clicking on any list item will navigate to that content.

![LMS Navigation](/docs/assets/img/education/education-lms-4.png)

---

## Topic Page
The topic page lists all the content as well as their completion status. Clicking on any card will navigate to the content Page:

![LMS Navigation](/docs/assets/img/education/education-lms-13.png)

---

## Content Pages

Each type of content has its own view and a common navigation based on the content type.

<img alt="Portal Contents" src="{{docs_base_url}}/assets/img/education/lms/content.png">

When a student visits particular content page, he/she can navigate using buttons at the bottom of the content.

> Note: The activity of the student is only recorded after the student clicks on the Next button.

<img class="screenshot" alt="Portal Contents" src="{{docs_base_url}}/assets/img/education/lms/content-navigation.png">

### Navigating Quizzes

In case of a quiz, the student has to first submit the quiz, following which the result is computed and displayed, after which the student can navigate to the next content.

<img class="screenshot" alt="Quiz Pass" src="{{docs_base_url}}/assets/img/education/lms/quiz-pass.png">

The next time a student visits the quiz page, based on the previous attempts, the portal may or may not allow any quiz attempts.
In case the student has reached max limits, the quiz will be locked. The previous score based on the quiz grading basis will be displayed
<img class="screenshot" alt="Quiz Limit" src="{{docs_base_url}}/assets/img/education/lms/quiz-fail-no-attempt.png">
*Max attempt limit reached*

In case the student has cleared the quiz already, the quiz will be closed and the score will be displayed.
<img class="screenshot" alt="Quiz Already Cleared" src="{{docs_base_url}}/assets/img/education/lms/quiz-pass-cleared.png">
*Quiz already cleared*

{next}
