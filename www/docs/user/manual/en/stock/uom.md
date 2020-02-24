<!-- add-breadcrumbs -->
# Unit of Measure (UoM)

**A UoM is a unit using which an Item is measured.**

By default, there are many UoMs created in  ERPNext. However, more can be added depending on your business use case. 
In the UoM there is an option 'Must be Whole Number'. If this is checked, you cannot use fraction numbers in this UoM. To know more about fractions and UoMs, check out [this page](/docs/user/manual/en/stock/articles/managing-fractions-in-uom).

The UoM list by itself only stores the name. The actual conversion rates are stored in a document called 'UoM Conversion Factor'. If you add new UoMs and plan to use it in transactions where it'll be converted to other UoMs, it is advised that you add it to this list.

For example, here 1 Kg is approximately 2.2 Pounds and the exact conversion factor is stored:

![UoM conversion factor](/docs/assets/img/stock/uom_convert.png)
