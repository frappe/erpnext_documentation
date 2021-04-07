<!-- add-breadcrumbs -->
# Member

The Member doctype allows you to record the Member details for a **Membership**.

Members are simply contacts in your ERPNext database with one or more memberships. The contact may be an individual, a household, an organization, or some other contact sub-type, but it is always a contact to which a membership is applied.

To create new Member go to:

> Home > Non Profit > Member > New

## 1. How to Create a Member

<img class="screenshot" alt="Member" src="{{docs_base_url}}/assets/img/non_profit/membership/member.png">

**Email Address:** You can capture the member's email address here. This will be used while sending membership acknowledgments.

**Membership Type:** Select the Membership Type here.

**Membership Expiry Date:** This Field fetches the membership end date details from the member's corresponding Membership record.

## 2. Features


### 2.1 Member linking with Customer or Supplier

<img class="screenshot" alt="Member" src="{{docs_base_url}}/assets/img/non_profit/membership/member-details.png">

ERPNext gives you the provision to link your members to customers or suppliers or both.

**Customer**: If the members of your NGO are paying membership fees and donations, you might want to generate invoices and track receivables for them. In this case, you can link a member to a customer record.

**Supplier**: Members can also be treated as Suppliers when they are offering goods and services to the NGO in some form or the other. You might want to create Purchase Invoices and maintain payables for the same. In this case, you can link a member to a supplier record.

**Address and Contact Section:** This Section allows you to link existing or add new address and contact records for the member.

### 2.2 Razorpay Details

If _Enable RazorPay For Memberships_ has been enabled in Membership Settings, then, the subscription details will be shown in the Razorpay Details section.


{next}
