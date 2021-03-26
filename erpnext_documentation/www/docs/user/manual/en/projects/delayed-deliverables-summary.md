<!-- add-breadcrumbs -->

# Delayed Deliverables Summary

The Delayed Deliverables Summary report helps identify the tasks which have exceeded their Expected End Dates.

To view this report, you can go to:

> Home > Projects > Reports > Delayed Deliverables Summary

The report is generated based on the Task Doctype.

<img class="screenshot" src="/docs/assets/img/project/delayed-deliverables-summary.png">

### Calculation of Delay

Tasks have a date field called **Completed On**, which becomes visible when a Tasks status is changed to Completed.

##### Scenario 1

If a task is marked as Completed and the Completed On field is set, then the delay is calculated as the difference between the Completed On and the Expected End Date.

```
Delay = Completed On - Expected End Date
```

##### Scenario 2

If the Completed On field is not set, then the delay is calculated as the difference between the current date and the Expected End Date.

```
Delay = Current Date - Expected End Date
```

### Chart

The chart shows the number of tasks that are On Track or Delayed based on the report generated after applying the filters.

{next}