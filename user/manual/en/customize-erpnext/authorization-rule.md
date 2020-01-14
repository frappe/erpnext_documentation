<!-- add-breadcrumbs -->
# Authorization Rule

**Authorization Rule allows configuring a custom authorization / approval on a documents, based on conditions defined.**

Example: If a Sales Order's Grand Total exceeds $1,000, then it should be verified/Submitted by the Sales Manager only, even if Sales User has submit permission.

On the same lines, you can define authorization rule based on the fields like Net Total, Grand Total, Discount % and specify who would be document approver if authorization condition is matched.

<img class="screenshot" alt="Authorization Rule" src="{{docs_base_url}}/assets/img/customize/customize-authorization-rule-1.png">

## Creating Authorization Rule

To access Authorization Rule, go to:

> Home > Settings > Customize > Authorization Rule

Let's consider an detailed example of an Authorization Rule to learn better.

Assume that the Sales Manager needs to authorize Sales Orders, only if it's Grand Total value exceeds 10,000. If the Sales Order value is less than 10,000, then even Sales User will be able to submit it. It means Submit permission of Sales User will be restricted only up to Sales Order of Grand Total less than 10,000.

1. Go to the Authorization Rule list, click on New.
1. Select the transaction on which Authorization Rule will be applicable. This functionality is available for limited transactions only.
1. Enter the Authorized Value etc. This depends on the field you selected in Based On.
1. Select Based On. Authorization Rule will be applied based on the value selected in this field.
1. Select Applicable Role. This is the role on which this Authorization Rule will be applicable. As per the example, it'll be Sales User.
1. To be more specific you can also select Applicable To User if you wish to apply the rule to a specific Sales User, and not all Sales Users. 
1. Select Approving Role. This is the role that can approve forms over the Authorized value. It will be Sales Manager as per the example.
1. You can also select a specific Sales Manager.
1. Save.

<img class="screenshot" alt="Authorization Rule" src="{{docs_base_url}}/assets/img/customize/auth-rule.png">

If Sales User tries submitting Sales Order of value higher than 10,000, then he will get an error message.

<img class="screenshot" alt="Authorization Rule" src="{{docs_base_url}}/assets/img/customize/customize-authorization-rule-2.png">

> If you wish to restrict Sales User from submitting Sales Orders, then instead of creating Authorization Rule, you should remove submit privilege for Sales User from [Role Permission Manager](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions).

### Documents on which Authorization Rule can be applied

1. Sales Order
1. Purchase Order
1. Quotation
1. Delivery Receipt
1. Sales Invoice
1. Purchase Invoice
1. Purchase Receipt
1. Appraisal

### Fields on which Authorization Condition can be defined

1. Grand Total
1. Average Discount
1. Customer-wise Discount
1. Item-wise Discount

{next}
