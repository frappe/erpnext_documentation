<!-- add-breadcrumbs -->
# BOM Update Tool

**From the BOM Update Tool, you can replace a sub-assembly BOM and update costs of all parent BOMs.**

Using this utility, you can replace an existing BOM of a sub-assembly item which is linked to a parent BOM. The system will update the new BOM in all the parent BOMs where it was used. You need to create a new BOM first.

To use the BOM Update Tool, go to:

> Home > Manufacturing > Tools > BOM Update Tool

## 1. How to use the BOM Update Tool
Let's consider a scenario to understand this better.

Suppose a company manufactures computers, Bill of Materials for the computer will look like this:

1. Monitor
1. Key Board
1. Mouse
1. CPU

Out of all the items above, CPU is assembled separately. Hence separate BOM will be created for the CPU. Following are the items from the BOM of CPU.

1. 250 GB Hard Disk
1. MotherBoard
1. Processor
1. SMTP
1. DVD player

If more items need to be added, or existing items to be edited in the CPU BOM, then create new BOM for it.

1. _950 GB Hard Disk_
1. MotherBoard
1. Processor
1. SMTP
1. DVD player

Select Current BOM and New BOM of the **sub-assembly** Item:

<img class="screenshot" alt="BOM Update Tool" src="{{docs_base_url}}/assets/img/manufacturing/bom-update-tool.png">

To update the new BOM in all the parent BOMs, where CPU is selected as sub-assembly, you can use the **Replace** button. 

On clicking Replace button, old BOM of CPU will be replaced with the new BOM in the BOM of finished Item (Computer).

**Will BOM Replace Tool work for replacing the exploded Items in the parent BOM?**

No, exploded Items which do not have any BOMs of their own cannot be replaced in the parent BOM. For example, consider if the Item Monitor does not have a sub-assembly and it cannot be updated using this tool. For updating exploded Items you should Cancel and Amend current BOM, or create a new BOM for the finished item.

## Update BOM Cost
Using the button **Update latest price in all BOMs**, you can update the cost of all Bill of Materials, based on the latest purchase price/price list rate/valuation rate of raw materials. This is useful if your updated BOM has materials with different Rates.

On clicking this button, the system will create a background process to update all the BOM's cost. It is processed via background jobs because this process can take a few minutes (depending on the number of BOMs) to update all the BOMs.

This functionality can also be executed automatically daily. For that, you need to enable "Update BOM Cost Automatically" from Manufacturing Settings.

{next}
