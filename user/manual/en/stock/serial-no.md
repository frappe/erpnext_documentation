<!-- add-breadcrumbs -->
# Serial Number

As we discussed in the **Item** section, if an **Item** is _serialized_, a
**Serial Number** (Serial No) record is maintained for each quantity of that
**Item**. This information is helpful in tracking the location of the Serial
No, its warranty and end-of-life (expiry) information.

**Serial Nos** are also useful to maintain fixed assets. **Maintenance Schedules** can also be created against serial numbers for planning and scheduling maintenance activity for these assets (if they require maintenance).

You can also track from which **Supplier** you purchased the **Serial No** and
to which **Customer** you have sold it. The **Serial No** status will tell you
its current inventory status.

If your Item is _serialized_ you will have to enter the Serial Nos in the
related column with each Serial No in a new line.
You can maintain single units of serialized items using Serial Number.

### 1. How to create a Serial Number
1. Go to: **Stock > Serial No and Batch > Serial No > New**.
1. Enter a Serial Number.
1. Enter the Item Code and details will be fetched.
1. If any transaction is done with an item, Serial No cannot be set or unset.
1. Save.

Inventory of an Item can only be affected if the Serial No is transacted via a
Stock transaction (Stock Entry, Purchase Receipt, Delivery Note, Sales
Invoice). When a new Serial No is created directly, its warehouse cannot be
set.

<img class="screenshot" alt="Serial Number" src="{{docs_base_url}}/assets/img/stock/serial-no.png">

* The Status is set based on Stock Entry.
* Only Serial Numbers with status 'Available' can be delivered.
* Serial Nos can automatically be created from a Stock Entry or Purchase Receipt. If you mention Serial No in the Serial Nos column, it will automatically create those serial Nos.
* If in the Item Master, the Serial No Series is mentioned, you can leave the Serial No column blank in a Stock Entry / Purchase Receipt and Serial Nos will automatically be set from that series.

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Q4tYKYTbVek" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

#### 2. Related Topics
1. [Item Codification](/docs/user/manual/en/stock/item-codification)
1. [Item Variants](/docs/user/manual/en/stock/item-variants)
1. [Serial Number Naming](/docs/user/manual/en/stock/articles/serial-no-naming)

