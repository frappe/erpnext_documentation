<!-- add-breadcrumbs -->
# Authorization Rule

**Authorization Rule allows configuring a custom authorization / approval on a documents, based on conditions defined.**

Example: If a Sales Order's Grand Total exceeds $1,000, then it should be verified/submitted by the Sales Manager only, even if the Sales User has "Submit" permission.

On the same lines, you can define Authorization Rule based on the fields like Net Total, Grand Total, Discount % and specify who would be the document approver if the authorization condition is matched.

![Authorization Rule](/docs/v13/assets/img/customize/authorization-rule.png)

Let's consider a detailed example of an Authorization Rule to learn better.

Assume that the Sales Manager needs to authorize Sales Orders, only if it's Grand Total value exceeds 10,000. If the Sales Order value is less than 10,000, then even the Sales User will be able to submit it. This means that the Submit permission of Sales User will be restricted only up to Sales Order of Grand Total less than 10,000.

## 1. How to create an Authorization Rule

1. Go to the Authorization Rule list, click on New.
1. Select the transaction on which Authorization Rule will be applicable. This functionality is available for limited transactions only.
1. Enter the Authorized Value, etc. This depends on the field you selected in Based On.
1. Select Based On. Authorization Rule will be applied based on the value selected in this field.
1. Select Applicable Role. This is the role on which this Authorization Rule will be applicable. As per the example, it'll be Sales User.
1. To be more specific, you can also select Applicable To User if you wish to apply the rule to a specific Sales User, and not to all Sales Users.
1. Select Approving Role. This is the role that can approve forms over the Authorized value. As per our example, it is the Sales Manager.
1. You can also select a specific Sales Manager.
1. Save.

![Authorization Rule](/docs/v13/assets/img/customize/new-authorization-rule.png)

If the Sales User tries submitting the Sales Order of value higher than 10,000, then he will get an error message.

![Authorization Rule Validation Message](/docs/v13/assets/img/customize/authorization-rule-validation-message.png)

> If you wish to restrict Sales User from submitting Sales Orders, then instead of creating Authorization Rule, you should remove submit privilege for Sales User from [Role Permission Manager](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions).

### Documents on which Authorization Rule can be applied

1. Sales Order
1. Purchase Order
1. Quotation
1. Delivery Note
1. Sales Invoice
1. Purchase Invoice
1. Purchase Receipt
1. Appraisal

### Fields on which Authorization Condition can be based on

1. Grand Total
1. Average Discount
1. Customer-wise Discount
1. Item-wise Discount



{next}
