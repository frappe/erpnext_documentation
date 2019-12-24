<!-- add-breadcrumbs -->
# Global Search

**Global search is a powerful word-processing operation in ERPNext which will help you in searching for a particular Document Type or Document.**

For every sequence of a particuar word or a set of characters, you will have a search result. 

### Using Awesome Bar for Global Search.

![Tree Master Renaming](/docs/assets/img/using-erpnext/using-global-search-2.gif)

Global Search helps users find information quickly. It’s located in the upper right-hand corner in ERPNext.  Simply entering a few characters in the Search Bar will show results from several different record types (Contact, Customer, Issues, etc.) related to that keyword. You can also customize the fields based on which search will be shown.

You can also type in multiple keywords seperated by & operator to find your desirable results. You may refer to the following cases for examples:

- Input "apple & iPod" can return documents with one field contain Apple and the other contains iPod( PO's vendor and item).
- Input "iPhone & iPod" can return target documents that contain both item iPhone and iPod (child table items).
- Input "iPhone & black" can return the item with description contains both iPhone and black(long text field).
- Input 'foo & bar" can return any docs with both tags foo and bar assigned.(special long text field _usertags).

### Enable Global Search for fields in a Doctype.

![Tree Master Renaming](/docs/assets/img/using-erpnext/using-global-search-1.gif)

