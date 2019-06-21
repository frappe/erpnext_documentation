<!-- add-breadcrumbs -->
# Shopping Cart

In addition to listing your products, ERPNext also allows you to sell them via
the Shopping Cart.

To enable Shopping Cart, go to:

> Home > Website > Portal > Shopping Cart Settings

![Shopping Cart Settings](/docs/assets/img/website/shopping-cart-settings.png)
*Shopping Cart Settings*

Here are some configuration options:

1. **Show Price**: Show Item Price on the product page.
1. **Show Stock Availability**: Show whether the Item is in stock.
1. **Show Stock Quantity**: Show available stock on the product page.
1. **Show Configure Button**: Show a configure button if the Item has variants.
   It can be used to narrow down the specific item based on Attributes.
1. **Show Contact Us Button**: Show a contact us button which customers can use
   to enquire about the Item. It will create a Lead in the system.

## 1. Item Types

Shopping Cart works differently for Items with and without variants.

### 1.1 Items without variants

Items without variants have their dedicated product page and an **Add to Cart**
button. The stock information is also shown if they are enabled in Shopping Cart
Settings.

![Item without Variants](/docs/assets/img/website/item-without-variants.png)
*Item without Variants*

### 1.2 Items with variants

Since Item Templates can't be bought directly, there is a Configure button to
choose the specific variant and add it to cart.

![Item with Variants](/docs/assets/img/website/item-with-variants.gif)
*Item with Variants*

## 2. Cart Quotation

If checkout is disabled, when your customers add an item to cart, they can click
on the **Request for Quotation** button to get a quote for it. A [Quotation](/docs/user/manual/en/selling/quotation)
is generated in the system.

![Cart Quotation](/docs/assets/img/website/cart-quotation.png)
*Cart Quotation*

## 3. Cart Checkout

You can enable checkout from **Checkout Settings** section in Shopping Cart
Settings. You must have [PayPal Integration](/docs/user/manual/en/setting-up/integrations/paypal-integration)
or [Razorpay Integration](/docs/user/manual/en/setting-up/integrations/razorpay-integration)
for enabling payments.

![Cart Checkout Settings](/docs/assets/img/website/cart-checkout-settings.png)
*Cart Checkout Settings*

![Cart Checkout](/docs/assets/img/website/cart-checkout.png)
*Cart Checkout*
