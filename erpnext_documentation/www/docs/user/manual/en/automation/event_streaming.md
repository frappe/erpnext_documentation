 <!-- add-breadcrumbs -->
# Event Streaming

> Introduced in Version 13

Event Streaming enables inter site communications between two or more sites. You can **subscribe** to Document Types and **stream** Documents between different sites.

For Example: Consider you have more than one Company hosted on different sites, one among them is the main site where you want to do ledger posting and on other sites, the Sales Invoices are generated. You can use Event Streaming in this case. For this, your child company sites can subscribe to the main company site for Item, Customer, and Supplier Document Types. The main Company in turn can subscribe to the child companies for Sales Invoices.

To access Event Streaming, go to:
> Home > Automation > Event Streaming

## 1. Prerequisites
Before creating an Event Producer, a common user needs to be created on both the sites which will be used to access the site and will act as an Event Subscriber. Make sure the user has the necessary permissions for creation, updation, and deletion of the subscribed DocTypes.

## 2. How to set up Event Streaming

### 2.1 Create an Event Producer
1. The site which you want to subscribe to, is called as the Event Producer. Create an Event Producer document for the site you wish to get the updates from.
2. Go to: **Home > Automation > Event Streaming > Event Producer**.
3. Enter the site URL of the site you want to subscribe to, in the Producer URL field.
4. Add all the Document Types you want to subscribe to, in the Event Configuration child table.
5. If you want to have the created documents with the same name as it is on the remote Event Producer site, check the 'Use Same Name' checkbox in the child table against the required Document Type.
6. Set the Event Subscriber field to a user that will be used to create the documents fetched from the Event Producer. You need to create the same user both ways, i.e on the Event Consumer as well as the Event Producer site before creating the Event Producer.
7. Save.
8. The API key and API secret are then set in the Event Producer document for Authentication.

    ![Event Producer](/docs/assets/img/automation/event-producer-doc.png)

### 2.2 Approve Event Consumer on the Event Producer site
1. After the Event Producer has been created, an Event Consumer automatically gets created on the other site. By default all the Subscribed Document Types have the status as 'Pending'. In order to enable the Event Consumer to consume the documents of these Document Types, their Status needs to be updated to 'Approved'.
2. Go to: **Home > Automation > Event Streaming > Event Consumer**.
3. Once you open the Event Consumer document you will see all the Document Types that the consumer has subscribed to. Change the status from 'Pending' to 'Approved' for all the Document Types that you want to approve to be consumed. You can change the status to 'Rejected' if you do not want the documents of that Document Type to be consumed.
4. Save.

    ![Event Consumer](/docs/assets/img/automation/event-consumer-doc.png)

>**Note**: Document updates for Subscribed Document Types won't be synced unless they are Approved.

### 2.3 Offline access with single site
If you have some places where internet connectivity is low, for example, a store in a remote area where sales invoices are generated and you want to sync these invoices from the store to the hosted account, you could setup offline syncing using the following steps:

1. Set up an ERPNext local instance. You can refer [this guide](https://github.com/frappe/bench) for local setup.
2. You need to have hosted account with your company set up.
3. Now create an Event Producer on the hosted account and set the producer URL to the URL of your local account.
4. Add whatever doctypes you want to sync in the Event Producer Document Types child table.
5. Approve the doctypes.

## 3. Features

### 3.1 Event Update Log
Event Update Log logs every create, update, and delete for documents that have consumers on the Event Producer site.
In order to view the Event Update Log:

Go to: **Home > Automation > Event Streaming > Event Update Log**.

- For 'Create' type the Update Type, Document Type, Document Name and the entire document (as JSON) is logged.
- For 'Update' type the Update Type, Document Type, Document Name and the updated data (difference between the previous state and current state of the document) is logged.
- For 'Delete' type only the Update Type, Document Type, and Document Name is logged.

![Event Update Log](/docs/assets/img/automation/event-update-log-doc.png)

### 3.2 Event Sync Log
Like the Update Log, Event Sync Log logs every document synced from the Event Producer on the Event Consumer site.
In order to view the Event Sync Log:

Go to: **Home > Automation > Event Streaming > Event Sync Log**.

![Event Sync Log](/docs/assets/img/automation/event-sync-log.png)

A successfully synced event generates a log document with:

- **Update Type**: Create, Update or Delete
- **Status**: Sync Status
- **DocType**
- **Event Producer**: The site URL from where the document was created
- **Document Name**
- **Remote Document Name**: If 'Use Same Name' is unchecked
- **Use Same Name**
- **Data**: The document data as JSON

    ![Event Sync Log](/docs/assets/img/automation/event-synced.png)

A failed event generates a log doc with the above fields along with:

- **Error**: The error because of which the document was not synced.
    ![Event Synced](/docs/assets/img/automation/event-failed-error.png)

- **Resync Button**: It also provides a 'Resync' button in order to resync the failed event.
    ![Event Failed](/docs/assets/img/automation/event-failed.png)

### 3.3 Dependency Syncing
Certain Document Types have dependencies. For example, before syncing a Sales Invoice, the Item and Customer need to be present in the current site. So, Item and Customer are dependencies for Sales Invoice. Event Streaming handles this by on-demand dependency syncing. Whenever any document is to be synced, it first checks whether the document has any dependencies (Link fields, Dynamic Link fields, Child Table fields, etc.). If that dependency is not fullfilled i.e. the dependent document (eg: Item) is not present on your consumer site, it will be synced first and then the Sales Invoice will be synced.

For example: Sales Invoice syncing with Item dependency:
    ![Event Dependency](/docs/assets/img/automation/event-dependency-sync.gif)

### 3.4 Naming Configuration
Check the 'Use Same Name' checkbox to let the documents have same name on both Event Producer and Event Consumer sites. If this is not checked, then the document will be created using the naming conventions of the current site.

![Use Same Name Config](/docs/assets/img/automation/event-use-same-name.png)

> **Note**: For Document Types that have naming series, it is advised to keep the 'Use Same Name' checkbox unchecked, to prevent naming conflicts. If this is unchecked, the Documents are created by following the naming conventions on the current site and the 'Remote Site Name' and 'Remote Document Name' custom fields are set in the synced document to store the Event Producer site URL and the document name on the remote site respectively.

![Subscribed Document](/docs/assets/img/automation/event-subscribed-doc.png)

### 3.5 Mapping Configuration

If you want to stream documents between an ERPNext instance and another Frappe app for a particular Document Type with same or different structure or fieldnames are different in both the sites, you can use Event Streaming with Mapping Configuration.
For this you need to first set up a Document Type Mapping:

Go to: **Home > Automation > Event Streaming > Document Type Mapping**.

#### 3.5.1 Mapping for DocTypes with similar structure

- **Mapping Name**: Give a unique name to the mapping
- **Local Document Type**: The Document Type in your current site
- **Remote Document Type**: The Document Type on the Event Producer site which you want to sync

In the Field Mapping child table:

- **Local Fieldname**: The fieldname in the Local Document type of your current site.
- **Remote Fieldname**: The fieldname in the Remote Document type of the Event Producer site which you want to map to the Local Fieldname. During the sync, the value of the remote fieldname gets copied to the local fieldname.

![Document Type Mapping](/docs/assets/img/automation/event-field-mapping.png)

#### 3.5.2 Default Value for some field

If your field is not mapped to any other remote fieldname and you always want the field to have the same value, set the default value field. Event if you have set the remote fieldname, in case during the sync, remote field's value is not found and the "Default Value" has been specified, it will be set.

![Child Table Mapping Link](/docs/assets/img/automation/default.png)


#### 3.5.3 Mapping for DocTypes having child tables

If the field you are trying to map is a child table, you need create another Document Type Mapping for the child table fields.

![Child Table Mapping Link](/docs/assets/img/automation/child_table_map_doc.png)

- **Mapping Type**: Select the Mapping Type as Child Table.
- **Mapping**: Select the Document Type Mapping doc you created for the child table.

![Child Table Mapping Link](/docs/assets/img/automation/event-map-is-child-table.png)

#### 3.5.4 Mapping for DocTypes having dependencies (Link, Dynamic Link fields)

If the DocTypes you are trying to map, have any kind of dependencies like Link or Dynamic Link fields you need to set up another Document Type Mapping for syncing the dependencies.

For example: The local doctype is Opportunity and remote doctype is ERPNext Opportunity. The field `party_name` (Link field for DocType Lead) in Opportunity is mapped to `full_name` (Data field) in ERPNext Opportunity. During the sync, this Lead has to be created for the main Opportunity to sync. So you need to set up a mapping for this Link Field too.

![Lead Dependency Creation](/docs/assets/img/automation/lead_dependency_creation.png)

- **Mapping Type**: In this case, the Mapping Type is Document.
- **Mapping**: Select the mapping you just created.
- **Remote Value Filters**: You need to specify the filters that will fetch the exact remote document to be mapped. Like in this case, the remote DocType is ERPNext Opportunity which can be uniquely fetched using name, phone number and country.

The format is:

{ "remote fieldname": "field or expression from where we will get the value for that fieldname"}

If you want to fetch the value from somewhere start the expression with eval:

Like in this case it is: `eval:frappe.db.get_value('Global Defaults', None, 'country')`

![Document Mapping Type](/docs/assets/img/automation/document_mapping_type.png)

At last, check the 'Has Mapping' checkbox in the Event Configuration child table in Event Producer against the required Document Type and select the Document Type Mapping you just created.

![Mapping Configuration](/docs/assets/img/automation/event-mapping-conf.png)
