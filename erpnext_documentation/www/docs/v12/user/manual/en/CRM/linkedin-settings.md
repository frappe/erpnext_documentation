---
title: LinkedIn Settings
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: LinkedIn Settings for Social Media Post
 keywords: Social Media Post Scheduling, CRM, frappe, erpnext new features, erp, open source erp, free erp, security
---

# LinkedIn Settings

LinkedIn related settings like OAuth can be configured here. ERPNext needs access to the API through which the post is shared and achieved using OAuth 2.0 Authentication Protocol.

## 1. How to set up LinkedIn Developer App

You must have LinkedIn Developer App for your company. ERPNext interacts with this App for sharing the post.

### 1.1 Create LinkedIn Developer App

Create App by link `https://www.linkedin.com/developers` fill all the details and verify it. And that App has the following products.

1. Share on LinkedIn
2. Sign In with LinkedIn
3. Marketing Developer Platform
![LinkedIn Developer App Product](/docs/v12/assets/img/crm/linkedin-dev-products.png)

### 1.2 Configure Redirect URLs:

1. Goto your LinkedIn Developers App then **Auth** tab.
2. In **OAuth 2.0 settings** section add **Redirect URLs**:
`https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Click **Update** to make changes. 
![LinkedIn Redirect URL](/docs/v12/assets/img/crm/linkedin-redirect-urls.png)

## 2. How to set up LinkedIn Settings

To access LinkedIn Settings, go to:
> Home > CRM > Settings > LinkedIn Settings

![LinkedIn Settings](/docs/v12/assets/img/crm/linkedin-settings.png)

### Company ID
You get the Company ID from your LinkedIn Company URL.
![LinkedIn Company ID](/docs/v12/assets/img/crm/linkedin-company-id.png)

### Consumer Key and Consumer Secret
You get **Consumer Key** and **Consumer Secret** from your LinkedIn Developer account go to:
> `https://www.linkedin.com/developers/` > My Apps > `{Your App}` > Auth

![LinkedIn Client](/docs/v12/assets/img/crm/linkedin-client.png)

Once you save the doc by filling **Company ID**, **Consumer Key**, and **Consumer Secret** it will redirect to LinkedIn's sign-in page by providing valid LinkedIn credentials and clicking Allow, the member approves your application's request to access their member data and interact with LinkedIn on their behalf. 
![Authorize LinkedIn](/docs/v12/assets/img/crm/authorize-linkedin.jpg)

{next}