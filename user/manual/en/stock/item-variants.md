<!-- add-breadcrumbs -->
# Item Variants

**An Item Variant is a version of an Item with different attributes like sizes or colors.**

Eg: Suppose t-shirt is an Item and it comes in different sizes and colors like small, medium, large and red, blue, green. In ERPNext the t-shirt will be considered as an Item template and each of the variations will be an Item Variant. 

A _blue_ t-shirt in size _small_ rather than just a t-shirt. Item variants let you treat the _small_, _medium_, and _large_ versions of a t-shirt as variations of one Item 't-shirt'.

Without Item variants, you would have to treat the _small_, _medium_ and _large_ versions of a t-shirt as three separate Items.

## 1. Using Item Variants

Variants can be based on two things:

1. Item Attributes
1. Manufacturers

> Tip: Once an item template is created, when you update this template, all the variants are also updated accordingly.

### 1.1 Creating the Item Variant Template

1. To use Item Variants in ERPNext, create an Item and tick 'Has Variants' under Variants. 

1. The Item then shall be referred to as a so-called 'Template'. Such a Template is not identical to a regular 'Item' any longer. For example, it (the Template) cannot be used directly in any transaction (Sales Order, Delivery Note, Purchase Invoice) itself.
 
1. Only the Variants of the Item (_blue_ t-shirt in size _small)_ can be practically used. Therefore it would be ideal to decide whether an item 'Has Variants' or not directly when creating it.
    <img class="screenshot" alt="Has Variants" src="{{docs_base_url}}/assets/img/stock/item-has-variants.png">

1. On selecting 'Has Variants' a table will appear. Specify the variant attributes for the Item in the table. In case the attribute has Numeric Values, you can specify the range and create intervals based on the increment values.
    <img class="screenshot" alt="Valid Attributes" src="{{docs_base_url}}/assets/img/stock/item-attributes.png">
> Note: You cannot make Transactions against a 'Template'.

### 1.2 Creating the Item Variants Based on Item Attributes
To create 'Item Variants' against a 'Template' click on 'Create'. From there, choose whether to create a single variant or multiple. Single is simple where you just one or more attributes and one item will be created. When choosing multiple variants, tick the attributes and multiple items will be created. For example, if you choose Color: Red, Green and Size: Small, Medium, Large, 6 variants will be created.

Creating multiple variants in ERPNext:

<img class="screenshot" alt="Make Variants" src="{{docs_base_url}}/assets/img/stock/make-multiple-variants.png">

To learn more about setting attributes check out [Item Attributes](/docs/user/manual/en/stock/setup/item-attribute)

### 1.3 Item Variants Based on Manufacturers

To setup variants based on Manufacturers, in your Item template, set "Variants Based On" as "Manufacturers"
In this case, to create variants, click on Create > Make Variant. The system will prompt you to select a Manufacturer. You can also optionally put in a Manufacturer Part Number.

<img class='screenshot' alt='Setup Item Variant by Manufacturer' src='{{docs_base_url}}/assets/img/stock/select-mfg-for-variant.png'>

The naming of the variant will be based on the name (ID) of the template Item with a number suffix. e.g. "Screwdriver" will have variant "Screwdriver-1".

## 2. Update Item Variants Based on Template
Go to: **Home > Stock > Items and Pricing > Item Variant Settings**. The fields displayed here will be copied over to the variants as well. By default, all fields are shown, delete any rows you don't want to be updated from the item template to the variants.

## 3. Video

### 3.1 Creating Item Variant one by one
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/kogIricF40I?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 3.2 Creating Item Variants in bulk
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/SngZtDIMdiQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 4. Related Topics
1. [Item Group](/docs/user/manual/en/stock/item-group)
1. [Item Attribute](/docs/user/manual/en/stock/item-attribute)
1. [Item Price](/docs/user/manual/en/stock/item-price)
1. [Item Codification](/docs/user/manual/en/stock/item-codification)
