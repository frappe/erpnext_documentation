<!-- add-breadcrumbs -->

# Milestone Tracking

> Introduced in Version 12

You can automatically track milestones on the lifecycle of a document if it undergoes multiple stages.

The configuration for Milestone setting can be set in **Milestone Tracking** and each milestone is updated in **Milestone**

### 1. Creating a Milestone Tracker

1. Go to Settings -> Automation -> Milestone Tracker
1. Create a new Milestone Tracker
1. Set the Document Type to track (example: "Issue")
1. Set the field that represents stages (example: "status")

Note: a milestone stage can be defined by Link or Select properties

Once this is set, a new **Milestone** record is created everytime the status of any issue is changed.

The Milestone can be viewed in the timeline of the view

<img class="screenshot" alt="Assign" src="/docs/assets/img/setup/automation/milestone-in-timeline.png">

Note: Milestones work independently of Versions

### 2. Features

Milestones can be a great source of reporting and notifications. For example if Lead Qualification is a milestone on "Lead", milestones can help generate reports on the number of leads being qualified in a period.

#### 2.1 Using Milestones with Dashboards

Used along with Dashboards, Milestones can help track the trends in milestones. For example, if "Qualification" is tracked as a "Lead Stage", a Dashboard on Milestone filterd by Qualification will show the trends of leads qualified.

#### 2.2 Using Milestones with Energy Points

Energy Point Rules can be defined to automatically give Energy Points to users who achieve a milestone. This can be used to incentivise action on transactions at various levels.

### 3. Related Topics

- [Tracking Versions](/docs/user/manual/en/using-erpnext/document-versioning)
- [Dashbaords](/docs/user/manual/en/customize-erpnext/dashboard)
