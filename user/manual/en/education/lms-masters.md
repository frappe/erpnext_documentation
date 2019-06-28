# Setting up Masters

LMS uses the following masters to show content on the portal.

<img class="screenshot" alt="LMS Masters" src="{{docs_base_url}}/assets/img/education/lms/lms-masters-tree.png">

LMS uses the existing programs and courses, additional doctypes for Topics and content have been added in v12.

<img alt="LMS Masters" src="{{docs_base_url}}/assets/img/education/lms/masters.png">

---

## Programs
To make the Program accessible on the portal, tick the 'Is Published' checkbox in the Program form. You can also tick the 'Is Featured' checkbox, that will show it on the portal landing page. The portal will automatically fetch the courses from the course table in the program.

### Portal Settings
One the portal, in order for students to be able to view the programs on the portal, a program has to be marked as Published. On the portal students will be able to see only those courses they are enrolled to or they are allowed to enroll into.

If 'Allow Self Enroll' is not checked, the program will be visible to only those students who are already enrolled in the program, this way you can host private programs on your portal.

<img class="screenshot" alt="Program Settings" src="{{docs_base_url}}/assets/img/education/lms/desk-program.png">

---

## Courses

For each of the courses in a particular program, you can set a course intro and a course hero image to be used on the portal. There is a table to add topics to, these topics will be displayed on the LMS to all enrolled students.
<img class="screenshot" alt="Course Settings" src="{{docs_base_url}}/assets/img/education/lms/desk-course.png">

---

## Topics
Similar to the course, topic has a table where you can add the content. You can add three different types of content viz. Video, Article and a Quiz.

<img class="screenshot" alt="Topic Settings" src="{{docs_base_url}}/assets/img/education/lms/desk-topic.png">

---

## Content Masters
Articles, Quizzes & Videos are all categorized under Content Masters, to add any article or video, you can simply navigate to the list view of that master and click on the `New` button

> Education > Content Masters > Article > New Article

### Articles
Adding articles is pretty straight forward, the content field is a rich-text field, you can add images, tables, links etc to your articles. There is a title field that is used as the name of the article to be used in links, this title will be displayed on the portal.
Other details include Author and Publish Date, these are optional fields and can be used for attributing resources.

<img class="screenshot" alt="Article" src="{{docs_base_url}}/assets/img/education/lms/desk-article.png">

The article is published if its parent program is published, it looks as follows on the portal.
<img class="screenshot" alt="Portal Article" src="{{docs_base_url}}/assets/img/education/lms/article.png">

### Videos
Videos can be added from both Vimeo and YouTube, the appropriate provider has to be set, but default the provider is set to YouTube.
Title field stores the name of the document as well as the title to be displayed on the portal. You can also add a publish date as well as the duration of the video in minutes.

<img class="screenshot" alt="Video" src="{{docs_base_url}}/assets/img/education/lms/desk-video.png">
Just like articles, video is published if its parent program is published, it looks as follows on the portal.
<img class="screenshot" alt="Portal Video" src="{{docs_base_url}}/assets/img/education/lms/video.png">

### Quizzes
Insturctors can also add quizzes to the topics they publish in a program. A quiz is a collection of multiple choice questions that can be added from the Question master.

You need to set a passing score, max attempts as well as agrading basis for the quiz. The following is a description of each of these options:

1. **Passing Score**: Score out of 100 required to clear the quiz (Default: 75).
1. **Max Attempts**: Maximum number of attempts the student is allowed to take. If set to 0 it will waive off the limit and the student can attempt the quiz any number of times until the student clears the quiz.
1. **Grading Basis**: Once the max number of attempts are exhausted, the final score is taken based on the grading basis. The following are the available options:
	- Latest Highest Score: Highest Score from all attempts
	- Latest Attempt: Score from the last attempt

<img class="screenshot" alt="Quiz" src="{{docs_base_url}}/assets/img/education/lms/desk-quiz.png">

#### Questions
You can add questions to be listed in quizzes. Based on the number of options marked correct, the type of the question is automatically set to either *Single Correct Answer* or *Multiple Correct Answers*.

<img class="screenshot" alt="Question" src="{{docs_base_url}}/assets/img/education/lms/desk-question-single.png">
<img class="screenshot" alt="Question" src="{{docs_base_url}}/assets/img/education/lms/desk-question-multiple.png">

Quizzes are also automatically published with its parent program, it looks as follows on the portal.
<img class="screenshot" alt="Portal Quiz" src="{{docs_base_url}}/assets/img/education/lms/quiz.png">

{next}
