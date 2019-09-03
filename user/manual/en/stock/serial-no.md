<!-- add-breadcrumbs -->
# Serial Number

As discussed in the [Item]([Item](/docs/user/manual/en/stock/item)) page, if an **Item** is _serialized_, a
**Serial Number** (Serial No) record is maintained for each quantity of that
**Item**. This information helps track the location of the Serial
No, its warranty and end-of-life (expiry) information.

**Serial Nos** are also useful to maintain fixed assets. [Maintenance Schedules](/docs/user/manual/en/support/maintenance-schedule) can also be created against Serial Numbers for planning and scheduling maintenance activity for these assets (if they require maintenance).

You can also track from which **Supplier** you purchased the **Serial No** and
to which **Customer** you have sold it. The **Serial No** status will tell you
its current inventory status.

If your Item is _serialized_ you will have to enter the Serial Nos in the
related column with each Serial No in a new line.
You can maintain single units of serialized items using Serial Number.

To access the Serial Number list, go to:
> Home > Stock > Serial No and Batch > Serial No

## 1. Prerequisites
Before creating and using a Serial Number, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)
* Enable 'Has Serial No' in the Item master
    ![Serial No Enabled](/docs/assets/img/stock/serial-no-enabled.png)


## 2. How to create a Serial Number
Usually, Serial Numbers are auto-created when transactions are made against a serialized Item. This works only when 'Has Serial No' is enabled and a series is set in the Item master.

For example, a series was set for the following Item as 'PB2L.#####'. Then a Stock Entry was submitted to receive the Item. The Serial Numbers were created accordingly.

![Serial No Created](/docs/assets/img/stock/serial-no-created.png)

However, if you want to create a Serial No _manually_ follow these steps:

1. Go to the Serial Number list, click on New.
1. Enter a Serial Number.
1. Enter the Item Code and details will be fetched.
1. If any transaction is done with an item, Serial No cannot be set or unset.
1. Save.

Inventory of an Item can only be affected if the Serial No is transacted via a
Stock transaction (Stock Entry, Purchase Receipt, Delivery Note, Sales
Invoice). When a new Serial No is created directly, its Warehouse cannot be
set.

<img class="screenshot" alt="Serial Number" src="{{docs_base_url}}/assets/img/stock/serial-no.png">

### 2.1 Notes about Serial Number

* The Status is set based on Stock Entry.
* Only Serial Numbers with status 'Available' can be delivered.
* Serial Nos can automatically be created from a Stock Entry or Purchase Receipt. If you mention Serial No in the Serial Nos column, it will automatically create those serial Nos.
* If in the Item Master, the Serial No Series is mentioned, you can leave the Serial No column blank in a Stock Entry / Purchase Receipt. Serial Nos will automatically be set from that series.

## 3. Features
### 3.1 Purchase/Manufacture details
The document from which the Serial No was created will be shown. If you purchased it from a Supplier, it'll be linked here.

### 3.2 Delivery Details
If the Serial No was generated from a Sales Order, the Customer will be linked here.

### 3.3 Warranty/AMC Details
If the Item is under warranty or AMC (Annual Maintenance Contract), the expiry dates for these can be set.

### 3.4 More Information
Any additional information about this specific Item unit can be set under 'Serial No Details'.

## 4. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Q4tYKYTbVek" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 5. Related Topics
1. [Item Codification](/docs/user/manual/en/stock/item-codification)
1. [Item Variants](/docs/user/manual/en/stock/item-variants)
1. [Serial Number Naming](/docs/user/manual/en/stock/articles/serial-no-naming)

