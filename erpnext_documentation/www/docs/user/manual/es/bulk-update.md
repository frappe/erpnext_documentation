<!-- add-breadcrumbs -->
# Bulk Update

**Bulk Update allows you to update a particular field of a DocType for all documents.**

To access Bulk Update, go to:
> Home > Settings > Bulk Update

Consider that you have 20 quotations in which you had selected 'All Territories' and now you want to change the Territory to France. Instead of updating the individual quotations manually, you can use Bulk Update to update all 20 Quotations at once.

To do this,

1. Go to Bulk Update.
1. Select the Document Type, like Quotation.
1. Select the field to update, like territory.
1. Enter a **valid** new value to be updated.
1. Enter any conditions that apply, for example, status="Draft" will only affect documents in the Draft stage.
1. Select the limit, i.e. number of documents (Quotations) to be updated.
1. Click on Update.

    ![Bulk Update](/docs/assets/img/setup/bulk-update.png)

> Note: You can only update fields that can be updated normally in a particular stage. For example, valid till date cannot be updated for submitted Quotations.

### Related Topics
1. [Bulk Rename](/docs/user/manual/en/setting-up/settings/bulk-rename)
