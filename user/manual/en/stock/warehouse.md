<!-- add-breadcrumbs -->
# Warehouse

A warehouse is a commercial building for storage of goods. Warehouses are used
by manufacturers, importers, exporters, wholesalers, transport businesses,
customs, etc. They are usually large plain buildings in industrial areas of
cities, towns, and villages. They mostly have loading docks to load and unload
goods from trucks.

The terminology of 'Warehouse" in ERPNext is a bit broader though and maybe can be 
regarded as "storage locations". You can create a sub-Warehouse which 
practically is a shelf inside your actual location. 
This can become quite a detailed Tree like the following, for example:

*Warehouse > Room > Row > Shelf >Box*

### 1. How to create a Warehouse
1. Go to **Stock > Setup > Warehouse > New**.
1. Enter a name for the warehouse.
1. Set/check the parent warehouse. If you tick on Is Group, then this Warehouse becomes a parent group.
1. You can add additional details like address and contact details.
1. Save. 

### 2. How to navigate to a Warehouse

To go to Warehouse, click on Stock and go to Warehouse under Setup.  You
could also switch to 'Tree' View or simply type warehouse tree in the awesome bar.

<img class="screenshot" alt="Warehouse" src="{{docs_base_url}}/assets/img/stock/warehouse.png">

In ERPNext, every Warehouse must belong to a specific company, to maintain
company wise stock balance. In order to do so each Warehouse is linked with an 
Account in the Chart of Accounts (by default of the the same name as the Warehouse 
itself) which captures the monetary equivalent of the goods or materials stored 
in that specific warehouse. If you have a more detailed Warehouse Tree as the one 
described above most likely it's a good idea to link the sub-locations (>room >row >Shelf, ...)
to the account of the actual Warehouse (the root Warehouse of that Tree) as most 
scenarios do not require to account for value of stock items per Shelf or Box.

Warehouses are saved with their respective company’s abbreviations. This facilitates 
identifying which Warehouse belongs to which company, at a glance.

You can include user restrictions for these Warehouses. In case you do not
wish a particular user to operate on a particular Warehouse, you can refrain
the user from accessing that Warehouse.

> Note: ERPNext system maintains stock balance for every distinct combination
of Item and Warehouse. Thus you can get stock balance for any specific Item in
a particular Warehouse on any particular date.

#### 3. Related Topics
1. [Stock Entry Purpose](/docs/user/manual/en/stock/articles/stock-entry-purpose)
1. [Stock Level Report](/docs/user/manual/en/stock/articles/stock-level-report)
