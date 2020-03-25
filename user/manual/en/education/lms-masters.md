# Setting up the Masters for Learning Management System

The ERPNext Learning Management System uses the following masters to show content on the portal.

![LMS Setting](/docs/assets/img/education/education-lms-masters.png)

---

## 1. Programs
To make the Program accessible on the portal, tick the 'Is Published' checkbox in the Program form. You can also tick the 'Is Featured' checkbox, which will show it on the portal landing page. The portal will automatically fetch the courses from the course table in the program.

## 2. Portal Settings
On the portal, for students to be able to view the programs on the portal, a program has to be marked as Published. On the portal students will be able to see only those courses they are enrolled to or they are allowed to enroll into.

If 'Allow Self Enroll' is not checked, the program will be visible to only those students who are already enrolled in the program, this way you can host private programs on your portal.

![LMS Setting](/docs/assets/img/education/education-lms-settings-1.png)

![LMS Setting](/docs/assets/img/education/education-lmms-3.png)

Learn more about Programs [here](/docs/user/manual/en/education/program).

---

## 3. Courses

For each of the courses in a particular program, you can set a course intro and a course hero image to be used on the portal. There is a table to add topics too, these topics will be displayed on the LMS to all enrolled students.

![LMS Setting](/docs/assets/img/education/education-lms-4.png)

Learn more about courses [here](/docs/user/manual/en/education/course).

---

## 4. Topics
Similar to the course, Topic has a table where you can add the content. You can add three different types of content viz. Video, Article and a Quiz.

![LMS Setting](/docs/assets/img/education/education-lms-13.png)

Learn more about topics [here](/docs/user/manual/en/education/topic.md).

---

## 5. Content Masters
Articles, Quizzes & Videos are all categorized under Content Masters, to add any article or video, you can simply navigate to the list view of that master and click on the **New** button

> Education > Content Masters > Article > New Article

### 5.1 Articles
Adding articles is pretty straight forward, the content field is a rich-text field, you can add images, tables, links, and more to your articles. There is a title field that is used as the name of the article to be used in links, this title will be displayed on the portal.
Other details include Author and Publish Date, these are optional fields and can be used for attributing resources.

![LMS Setting](/docs/assets/img/education/education-lms-8.png)

The article is published if its parent program is published, it looks as follows on the portal.

![LMS Setting](/docs/assets/img/education/education-lms-settings-8.png)

### 5.2 Videos
Videos can be added from both Vimeo and YouTube, the appropriate provider has to be set, but default the provider is set to YouTube.

Title field stores the name of the document as well as the title to be displayed on the portal. You can also add a publish date as well as the duration of the video in minutes.

![LMS Setting](/docs/assets/img/education/education-lms-9.png)

Just like articles, video is published if its parent program is published, it looks as follows on the portal.

![LMS Setting](/docs/assets/img/education/education-lms-7.png)

### 5.3 Quizzes
Instructors can also add quizzes to the topics they publish in a program. A quiz is a collection of multiple-choice questions that can be added from the Question master.

You need to set a passing score, max attempts as well as a grading basis for the quiz. The following is a description of each of these options:

1. **Passing Score**: Score out of 100 required to clear the quiz (Default: 75).
1. **Max Attempts**: Maximum number of attempts the student is allowed to take. If set to 0 it will waive off the limit and the student can attempt the quiz any number of times until the student clears the quiz.
1. **Grading Basis**: Once the max number of attempts are exhausted, the final score is taken based on the grading basis. The following are the available options:
    - Latest Highest Score: Highest Score from all attempts
    - Latest Attempt: Score from the last attempts

![LMS Setting](/docs/assets/img/education/education-lms-10.png)

#### Questions
You can add questions to be listed in quizzes. Based on the number of options marked correct, the type of the question is automatically set to either *Single Correct Answer* or *Multiple Correct Answers*.

![LMS Setting](/docs/assets/img/education/education-lms-11.png)

![LMS Setting](/docs/assets/img/education/education-lms-12.png)

Quizzes are also automatically published with its parent program, it looks as follows on the portal.

![LMS Setting](/docs/assets/img/education/education-lms-5.png)

{next}
