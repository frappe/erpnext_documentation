<!-- add-breadcrumbs -->
#Managing Multi-level BOM

Consider a scenario where your manufacturing process involves producing sub-assembly items before the final product. In this case, how should you manage the BOM?

First of all, you need to have BOMs for the sub-assemblies, then these BOMs should be linked to the BOM of the final finished product. In the following screenshot, you can see that the BOM for Brush Bristles (subassembly) is linked to the BOM of the Shaving Brush (final product). This is seen in the Materials table in the Bill of Materials master.

![Multi-level BOM](/docs/assets/img/articles/multi-bom.png)

The 'Materials' table will only show the sub-assemblies while the 'Materials Required (Exploded)' table will show all the raw materials required to manufacture the final product.

BOM materials table where sub-assembly is shown:
![Multi-level BOM](/docs/assets/img/articles/bom-materials.png)

In the exploded view only the raw materials are shown:
![Multi-level BOM](/docs/assets/img/articles/bom-materials-exploded.png)


To use multi-level BOM in a Work Order, enable the 'Use Multi-Level BOM' checkbox. This is enabled by default. If you want to plan materials for sub-assemblies of the Item you're manufacturing leave this enabled. If you plan and manufacture the sub-assemblies separately disable this checkbox.

<!-- <img alt="Nested BOM" class="screenshot" src="{{docs_base_url}}/assets/img/articles/nested-bom-1.png"> -->

Let's consider another example to understand this better where a computer is being assembled. The hard disk and DVD drive are also being manufactured and are the sub-assemblies. The multi-level or nested BOM will look like this:

    
- Personal Computer (FG Item)
    - Mother Board
    - SMTP
    - Accessories and wires
    - Hard Disk (sub-assembly)
        - Item A
        - Item B
        - Item C
    - DVD Drive (sub-assembly)
        - Item X
        - Item Y
        - Item Z




<!-- markdown -->
