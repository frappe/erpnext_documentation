<!-- add-breadcrumbs -->

# How Valuation Rate is Calculated for an Item

When Item’s stock is let in via stock transactions (Purchase Receipt, Stock Entry, or Stock Reconciliation), valuation is calculated for an item. 

There are various sources of rates based on which valuation rate is calculated.

The following are the options that explain various cases where rates are picked from different sources for calculating the item's valuation rate.

1.  Based on the Basic Rate/Incoming Rate/Valuation Rate entered in an entry, the Valuation Rate is calculated for an item. In transactions, you can enter the item's rate, apply taxes, and other charges. Based on these values, the Valuation Rate is calculated for an item.  
      
    
2.  If the user doesn't enter any valuation rate, then it checks for the Valuation Rate from the field present in the Item master in the first section.
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/item-valuation-rate.png">

3. If both the above fail to provide a valuation rate to an Item, then it calculates the average of the old valuation rate available for the item and applies for the current Stock Entry.  
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/calculation-of-valuation-rate.png">

4. If there is no reference at all and if **Allow Zero Valuation Rate** in Stock Entry is *not* enabled, the system shows the following validation message. 
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/valuation-rate-not-found.png">