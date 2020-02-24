<!-- add-breadcrumbs -->
# BOM Costing in different Currency

User can change the Currency in the BOM *before* submitting. The system calculates the costing based on the Price List currency. You can check the manufacturing cost in a particular Currency by changing the Currency in the BOM.

Consider that you import plastic as a raw material from Japan and the Sales Invoices are in the Yen currency. Your company Currency is INR but you want the BOM costing to be done in Yen. On setting 'Rate Of Materials Based On' to 'Price List' the raw materials used in the BOM will also have rates set in Yen. These rates are fetched from the Price List you create for Japan. In this case, it is a buying Price List called 'Import Japan'.

![BOM in different Currency](/docs/assets/img/manufacturing/bom-currency.png)

If you select 'Rate Of Materials Based On' to 'Valuation Rate' or 'Last Purchase Rate', the prices will be fetched from the Item master or the Sales Invoice respectively. In case of Item master, you'll need to enter the Valuation Rate in **your** Currency. In the BOM, Valuation Rate will be converted to the Currency set in the BOM.

![BOM in different Currency](/docs/assets/img/manufacturing/bom-currency-1.png)
