<!-- add-breadcrumbs -->
# Store Landing Page

After enabling Shopping Cart for your app you can create a custom landing page for your
store using the [Web Page Builder](/docs/v13/user/manual/en/website/web-page-builder).

![Store Landing Page](/docs/v13/assets/img/website/store-landing-page.png)
*Custom Store Landing Page*

## 1. How to create a Custom Store Landing Page

1. Follow the steps mentioned here to [create a Web Page](/docs/v13/user/manual/en/website/web-page).
1. Set a Route for your page (eg. */store*).
1. Select Content Type as **Page Builder**.
1. Click on Add Row in the Page Building Blocks Table.
1. Select a Web Template.

	ERPNext comes with a great set of standard web templates that can be used to create your Web Page.

	The configuration for the page in the screenshot above looks like this:

	![Store Web Templates](/docs/v13/assets/img/website/store-web-templates.png)
	*Store Page Building Blocks*

1. Add Values.

	Click on the Edit Values button on the right of each block, and enter the values in the dialog to
	set the content for each section.

	The Web Templates that will be useful for building your store landing page are:

	- **Hero Slider:**
		Up to 5 slides can be created. The image, title, primary action, alignment, theme for each slide
		is configurable.
		![Store Hero Slider](/docs/v13/assets/img/website/store-hero-slider.png)
		*Hero Slider Configuration*

	- **Product Category Cards:**
		Up to 8 product category cards can be configured. Each product categories will link to an
		[Item Group](/docs/v13/user/manual/en/stock/item-group).
		Ensure that the **Show in Website** option is ticked in the Item Group form so that the
		route for the product category is generated.

		![Store Product Category Cards](/docs/v13/assets/img/website/store-product-category.png)
		*Product Categories Configuration*

	- **Item Card Group:**
		This section can be used to showcase your featured items. Up to 12 cards can be configured.
		Each card will link to an [Item](/docs/v13/user/manual/en/stock/item). If **featured** is checked,
		the item will take up 2 columns of space.

		![Store Item Card Group](/docs/v13/assets/img/website/store-item-card-group.png)
		*Item Cards Configuration*


1. Publish your Web Page.

	The web page will be published only when the Published option is checked.
	Once the page is published, click on **See on Website** on the sidebar or visit the configured route
	and check out the page!

	![Store Page Published](/docs/v13/assets/img/website/store-page-published.png)
	*Publish your Web Page*

1. Set as your Home Page.

	Follow the steps [here](/docs/v13/user/manual/en/website/articles/website-home-page) to set
	this page as your Website home page.
