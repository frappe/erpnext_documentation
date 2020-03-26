<!-- add-breadcrumbs -->
# Notification

**You can configure various notifications in your system to remind you of important activities.**

1. The completion date of a Task.
2. Expected Delivery Date of a Sales Order.
3. Expected Payment Date.
4. A reminder of follow up.
5. If an Order greater than a particular value is received or sent.
6. Expiry notification for a Contract.
7. Completion/Status change of a Task.

To access notification setup, go to:

> Home > Settings > Notification

## 1. Setting Up An Alert

To set up a Notification:

1. Select the Document Type you want to watch changes on.
2. Define what events you want to watch under Send Alert On. Events are:
    1. New: When a new document of the selected type is made.
    2. Save/Submit/Cancel: When a document of the selected type is saved, submitted, or canceled.
    4. Days Before/Days After: Trigger this alert a few days before or after the **Reference Date.** To set the days, set **Days Before or After**. This can be useful in reminding you of upcoming due dates or reminding you to follow up on certain leads of quotations.
    3. Value Change: When a particular value in the selected type changes.
    1. Method: Sends notification when a specific method is triggered. Eg: before_insert.
    1. Custom: Send a notification to an [Email Account](/docs/user/manual/en/setting-up/email/email-account) selected.
3. Set additional Conditions if required.
4. Set the recipients of this alert. The recipient could either be a field of the document or a list of fixed Email Addresses.
5. Compose the message.
1. Save.


### 1.1 Setting a Subject
You can retrieve the data for a particular field by using `doc.[field_name]`. To use it in your subject/message, you have to surround it with `{% raw %}{{ }}{% endraw %}`. These are called [Jinja](http://jinja.pocoo.org/) tags. For example, to get the name of a document, you use `{% raw %}{{ doc.name }}{% endraw %}`. The following example sends an email on saving a Task with the Subject, "TASK#### has been created"

<img class="screenshot" alt="Setting Subject" src="{{docs_base_url}}/assets/img/setup/notifications/email-alert-subject.png">

### 1.2 Setting Conditions

Notifications allow you to set conditions according to the field data in your documents. For example, if you want to receive an Email if a Lead has been saved as "Interested" as it's status, you put `doc.status == "Interested"` in the conditions textbox. You can also set more complex conditions by combining them.

<img class="screenshot" alt="Setting Condition" src="{{docs_base_url}}/assets/img/setup/notifications/email-alert-condition.png">

The above example will send a Notification when a Task is saved with the status "Open" and the "Expected End Date" for the Task is the date on or before the date on which it was saved on.


### 1.3 Setting a Message

You can use both Jinja Tags (`{% raw %}{{ doc.[field_name] }}{% endraw %}`) and HTML tags in the message textbox.

    {% raw %}<h3>Order Overdue</h3>

    <p>Transaction {{ doc.name }} has exceeded Due Date. Please take necessary action.</p>

    <!-- show last comment -->
    {% if comments %}
    Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
    {% endif %}

    <h4>Details</h4>

    <ul>
    <li>Customer: {{ doc.customer }}
    <li>Amount: {{ doc.total_amount }}
    </ul>{% endraw %}


### 1.4 Setting a Value after the Alert is Set

Sometimes to make sure that the Notification is not sent multiple times, you can
define a custom property (via Customize Form) like "Notification Sent" and then
set this property after the alert is sent by setting the **Set Property After Alert**
field.

Then you can use that as a condition in the **Condition** rules to ensure emails are not sent multiple times

<img class="screenshot" alt="Setting Property in Notification" src="{{docs_base_url}}/assets/img/setup/notifications/email-alert-subject.png">

### 1.5 Example

1. Defining the Criteria
    <img class="screenshot" alt="Defining Criteria" src="{{docs_base_url}}/assets/img/setup/notifications/email-alert-1.png">

1. Setting the Recipients and Message
    <img class="screenshot" alt="Set Message" src="{{docs_base_url}}/assets/img/setup/notifications/email-alert-2.png">


---

## 2. Slack Notifications

If you prefer to have your notifications sent to a dedicated Slack channel, you can also choose the option "Slack" in the channel options and select the appropriate Slack Webhook URL.

### 2.1 Slack Webhook URL

A Slack webhook URL is a URL pointing directly to a Slack channel.

To generate webhook URLs, you need to create a new Slack App:

1. Go to https://api.slack.com/slack-apps.
2. Click on "Create a Slack App".
    <img class="screenshot" alt="Set Message" src="{{docs_base_url}}/assets/img/setup/notifications/slack_notification_1.png">

3. Give your App a name and choose the right workspace.
    Once your app is created, go to the "Incoming Webhooks" section and add a new Webhook to Workspace.  
    <img class="screenshot" alt="Set Message" src="{{docs_base_url}}/assets/img/setup/notifications/slack_notification_2.png">

4. Copy the created link, go back to ERPNext and use it to create a new Slack Webhook URL in Integrations > Slack Webhook URL.
    <img class="screenshot" alt="Set Message" src="{{docs_base_url}}/assets/img/setup/notifications/slack_notification_3.png">

5. Select Slack and your Slack channel in the channel and Slack channel fields within your notification
    

### 2.2 Message Format

Unlike Email messages, Slack doesn't allow HTML formatting.

Instead, you can use markdown formatting: [Slack Documentation](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages)

Example:
    {% raw %}
    *Order Overdue*

    Transaction {{ doc.name }} has exceeded Due Date. Please take the necessary action.


    {% if comments %}
    Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
    {% endif %}

    *Details*

    • Customer: {{ doc.customer }}
    • Amount: {{ doc.grand_total }}
    {% endraw %}

<img class="screenshot" alt="Set Message" src="{{docs_base_url}}/assets/img/setup/notifications/slack_notification_4.png">

### 3. Related Topics
1. [SMS Settings](/docs/user/manual/en/setting-up/sms-setting)
1. [Document Follow](/docs/user/manual/en/setting-up/email/document-follow)
