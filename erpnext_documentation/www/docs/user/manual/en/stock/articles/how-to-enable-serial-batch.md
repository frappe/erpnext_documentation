<!-- add-breadcrumbs -->

# How to enable Serial and Batch number 

The options **Has Serial No** and **Has Batch No** will be unselectable if there is any Stock Transaction linked. 

<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/no-serial-batch.png">

To *enable* it, you can either:

1.  Duplicate the Item, enable Serial or Batch, and create stock entries to reflect the stock. *(Recommended)*

 **OR**

2.  **Cancel** and **Delete** all Stock Transactions related to the Item and then enable it.
    
For the recommended option, refer the steps below:

1.  Make current stock zero either by using [Stock Reconciliation](https://docs.erpnext.com/docs/user/manual/en/stock/stock-reconciliation) or via Stock Entry of type **Material Issue**.
    
2.  Create a Stock Entry of type **Material Receipt**, select the new Item, and Submit. This step will assign Serial and Batch numbers to the stock coming in.  
[Click here](https://docs.erpnext.com/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item) to know more about this entry.

3.  Now, disable the old Item since we won’t be using it in any transactions.
   
**Note:** To have the same Item Code, rename the old Item Code to something else and then create the new Item as per the actual Item Code.