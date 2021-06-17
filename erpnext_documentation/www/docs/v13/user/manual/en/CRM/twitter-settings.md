---
title: Twitter Settings
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Twitter Settings for Social Media Post
 keywords: Social Media Post Scheduling, CRM, frappe, erpnext new features, erp, open source erp, free erp, security
---

# Twitter Settings

Twitter related settings like OAuth can be configured here. ERPNext needs access to the API through which the post is shared and achieved using OAuth 2.0 Authentication Protocol.

## 1. How to set up Twitter App

You must have Twitter App for your company. ERPNext interacts with this App for sharing Tweet.

### 1.1 Create Twitter Developer App

Create App by link `https://developer.twitter.com/` and check that the App has **Read and write** Access permission.
![Twitter App Permission](/docs/v13/assets/img/crm/twitter-app-permission.png)

### 1.2. Configure Callback URL
1. Select your App and go to **App Details**.
2. Then go to **Edit** and click **Edit Details**.
3. Add your website URL in **Callback URLs** like:
`https://{yoursite}/api/method/erpnext.crm.doctype.twitter_settings.twitter_settings.callback`
4. Click **Save** to make changes.

![Twitter App Callback URL](/docs/v13/assets/img/crm/twitter-callback-url.png)


## 2. How to set up Twitter Settings

To access Twitter Settings, go to:
> Home > CRM > Settings > Twitter Settings

![Twitter Settings](/docs/v13/assets/img/crm/twitter-settings.png)

### 2.1 API Key and API Key Secret

You get **API Key** and **API Key Secret** from your Twitter Developer account go to:
> `https://developer.twitter.com/` > My Apps > `{Your App}` > Keys and tokens

![Twitter Keys Tokens](/docs/v13/assets/img/crm/twitter-key-token.png)

Once you save the doc by filling **API Key** and **API Key Secret** it will redirect to Twitter's sign-in page by providing valid Twitter credentials and clicking **Authorize app**, the member approves your application's request to access their member data and interact with Twitter.
![Twitter Authorize App](/docs/v13/assets/img/crm/twitter-authorize-app.png)

{next}