<!-- add-breadcrumbs -->

# Workflow Actions

> Introduced in Version 11

**Workflow Actions is a single place to manage all the pending actions you can take on Workflows.**

Workflow Actions will send email notifications only if the 'Send Email Alert' checkbox is ticked in the Workflow that you've created.

To access Workflow Actions, go to:
> Home > Settings > Workflow Actions

If a User is eligible to take action on some workflows, emails will be sent to the user with the relevant document as attachment. From there the user can `Approve` or `Reject` the Workflow.
<img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-actions-email.png">

Also the users will see entries in their Workflow Action list:
<img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-actions-list.png">

**Note:**

- You can set email template for Workflow Actions on each state. The template might consist of a message for users to proceed with the next Workflow Actions.
- Workflow Actions will not be created for a transition to optional states.

### Related Topics
1. [Workflows](/docs/user/manual/en/setting-up/workflows)
1. [Assignment Rule](/docs/user/manual/en/setting-up/automation/assignment-rule)
