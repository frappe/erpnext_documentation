<!-- add-breadcrumbs -->
#Letter Head

**A Letter Head contains your organization's name, logo, address, etc which appears at the top portion in documents.**

Every company has a default Letter Head. These Letter Head values are generally set as Header and Footer in the documents. In ERPNext, you can capture these details in the Letter Head master.

These details will appear in the Print Format of transactions like Sales Order, Sales Invoice, Salary Slip, Purchase Order, etc. In ERPNext, the Letter Head is only for setting up the top part of the document, other content is pre-formatted and can be configured via [Print Format](/docs/user/manual/en/setting-up/print/print-format) and [Print Headings](/docs/user/manual/en/setting-up/print/print-headings).

To access Letter Head, go to:
> Home > Settings > Letter Head

## 1. How to create a Letter Head
1. Go to the Letter Head list, click on New.
1. Enter a name for the Letter Head. You can create a separate Letter Head for different office locations.
1. Choose whether based on image or HTML.
1. You can enter details in a Letter Head by using:

  * Logo Image: Click on the Attach button to attach an image. Once the image is inserted, HTML for it will be generated automatically.
  * Other information (like Address, tax ID, etc.) that you want to put on your Letter Head.

    <img class="screenshot" alt="Print Heading" src="{{docs_base_url}}/assets/img/setup/print/letter-head.png">
  
  > If you want to make this the default Letter Head, click on "Default Letter Head".

1. After entering values in the Header and Footer section, save the Letter Head.

You can set the Letter Head based on HTML to make changes to it:

![Letter Head based on](/docs/assets/img/setup/print/letter-head-based-on.gif)

This is how the Letter Head looks in a document's print.

<img class="screenshot" alt="Print Heading" src="{{docs_base_url}}/assets/img/setup/print/letter-head-1.png">

> Note that Footer will be visible only when the document's print is seen in the PDF. Footer will not be visible in the HTML based print preview.

## 2. Video
<div class="embed-container">
  <iframe src="https://www.youtube.com/embed/cKZHcx1znMc?end=58&rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
  </iframe>
</div>

### 3. Related Topics
1. [Address Template](/docs/user/manual/en/setting-up/print/address-template)
1. [Terms and Conditions](/docs/user/manual/en/setting-up/print/terms-and-conditions)
1. [Cheque Print Template](/docs/user/manual/en/setting-up/print/cheque-print-template)
1. [Print Headings](/docs/user/manual/en/setting-up/print/print-headings)
