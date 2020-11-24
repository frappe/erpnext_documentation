---
title: Putaway Rule
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A Putaway Rule defines a Warehouse assignment strategy for incoming stock. This is particularly useful for purchasers with large warehouse locations and volume of purchase.
 keywords: Putaway Rule, Putaway, Put List, frappe, Warehouse Put Away, erpnext new features, WMS, Warehouse Capacity, erp, open source erp, free erp, stock, inventory
---

# Putaway Rule

**A Putaway Rule defines a Warehouse Assignment Strategy for incoming stock.**

A Putaway Rule is uniquely defined for an Item-Warehouse combination in a Company. It takes Warehouse Capacity and Priority into consideration.

While creating a **Purchase Receipt** from a **Purchase Order**, the Putaway Rules are applied and Items are **auto-assigned** to Warehouses based on the given strategy.

This is particularly useful for capacity management in large warehouses with multiple locations.

To access a Putaway Rule, go to:

> Home > Stock > Stock Transactions > Putaway Rule

## 1. Prerequisites

Before creating and using a Putaway Rule, it is advised that you create the following first:

- [Stock Item](/docs/user/manual/en/stock/item)
- [Warehouse](/docs/user/manual/en/stock/warehouse)

## 2. How to create a Putaway Rule

1. Go to the Putaway Rule list, click on New.
 <img class='screenshot' alt='Unsaved Pick List' src='{{docs_base_url}}/assets/img/stock/unsaved-putaway-rule.png'>

1. Set the Company and Select an Item.
1. Set the Warehouse on which this rule is applicable.
1. Set the Capacity. You can also select a UOM if you want to set the Capacity in a different UOM. The Capacity in Stock UOM will be set automatically.
 <img class='screenshot' alt='Unsaved Pick List' src='{{docs_base_url}}/assets/img/stock/multi-uom-putaway-rule.png'>

1. Set the Priority. This can begin from 1 onwards, 1 being the highest priority.
1. Save.
 <img class='screenshot' alt='Unsaved Pick List' src='{{docs_base_url}}/assets/img/stock/saved-putaway-rule.png'>

1. You can additionally Disable a Putaway Rule as well.

## 3. How does it work

As mentioned above the Putaway Rules are applied on the creation of a **Purchase Receipt** from a **Purchase Order**. Let us see that in action:

1. We have a Purchase Order with a requirement of 2 Bags (2000 Kgs) of Rice:
 <img class='screenshot' alt='Unsaved Pick List' src='{{docs_base_url}}/assets/img/stock/po-putaway-demo.png'>

1. We have 2 active Putaway Rules below. One has more priority than the other:
 <img class='screenshot' alt='Unsaved Pick List' src='{{docs_base_url}}/assets/img/stock/active-putaway-rules-list.png'>

1. On creating a Purchase Receipt from this Purchase Order, one row of 2 Bags is split and assigned according to the rules. First, the Item is accommodated in 'Stores - HUL'. Once this Warehouse is at capacity, it assigns the rest to 'Finished Goods - HUL':
 <img class='screenshot' alt='Unsaved Pick List' src='{{docs_base_url}}/assets/img/stock/putaway-po-to-pr.gif'>

> **Note:** When two rules having the same priority are to be applied, the Warehouse with a greater amount of vacant space will be considered first.


As of now, only Direct Putaway is supported in Purchase Receipt.