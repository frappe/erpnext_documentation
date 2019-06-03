<!-- add-breadcrumbs -->

# Energy Point System
Energy Points System is a rating/karma system that you can enable for your organization. This system can be used to track the performance of each user.

> To enable Energy Point System go to **Energy Point Settings**
 > check **Enabled**.


## 1. How to use the Energy Point System?
To start using this system you need to create some Energy Point Rules (see section 3. How to create Energy Point Rules?) so that users can get energy points based on their activities.

## 2. What are Energy Point Rules?
Energy Point Rules store the information about the activity and the value of points to be alloted.

Energy Point Rule have the following fields:

| Field        | Description  |
| ------------- |:-------------|
| Reference DocType| Document Type you want to apply rule on eg. Task, ToDo, Issue, etc. |
| Condition| Condition for the point allocation. <br>eg. `doc.status == 'Closed'`<br>The above condition will check whether the `status` field in the document is 'Closed' and if yes then the points will be alloted to the user.       |
| Points | Points to be alloted.|
| User Field | Field from which user will be selected eg. `Resolved By`, `Modified By`, `Owner`, etc. can be used.      |
| Multiplier Field | Field which stores value for multiplier. This field can take numeric and decimal values which will be multiplied with points defined in the rule. <br> For example: 2 (multiplier) * 10 (points set in the rule) = 20 points     |

> **Note:** User Field and Multiplier Field are fetched from the reference doctype.

## 3. How to create Energy Point Rules?

> Search for **Energy Point Rule** > create new Energy Point Rule

Take a look at the following example rule:
<img class="screenshot" src="/docs/assets/img/energy-point-system/issue-closed-rule.png">
The screenshot above is the rule for **Issue Closing**.
So when any user closes the issue he/she will be rewarded with **10** points.

Other cases can be covered similarly.

Suppose, you want to create a rule where user gets points on completing a task,
you can do so by creating following rule
<img class="screenshot" src="/docs/assets/img/energy-point-system/task-complete-rule.png">


## 4. Features:

### 4.1 Auto Point allocation
Based on energy point rules created, users will automatically get points when they complete activities which are tracked using the Energy Point System.

### 4.2 Review System
Review system can be used to "Appreciate" or "Criticize" someone's work.

Check out the following GIF for the review process.
<img class="screenshot" src="/docs/assets/img/energy-point-system/review-system.gif">
For reviewing, user needs to have review points which can be assigned by System Manager through **Energy Point Settings**.

You can also setup auto review point allocation from 'Energy Point Settings':
<img class="screenshot" src="/docs/assets/img/energy-point-system/auto-review-point-allocation.png">

### 4.3 Leaderboard
Go to Social Home > Leaderboard (side navigation bar)

Leaderboard shows user's standing in the organization.

<img class="screenshot" src="/docs/assets/img/energy-point-system/leaderboard.png">
