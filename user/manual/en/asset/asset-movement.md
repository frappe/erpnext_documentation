<!-- add breadcrumbs -->
# Asset Movement

**Asset Movement refers to moving an Asset from one Location to another.**

In ERPNext, you can track the location of an asset or to whom it is issued. For tracking, you need to create an Asset Movement transaction, whenever the asset is moved from one location to another. You can also keep a track of issuance of an asset to any employee.

To access the Asset Movement list, go to:
> Home > Asset > Assets > Asset Movement

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-movement.png">

## 1. Prerequisites
Before creating and using Asset Movement, it is advised to create the following first:

* [Asset](/docs/user/manual/en/asset/asset)
* [Asset Location](/docs/user/manual/en/asset/asset-location)


## 2. How to create an Asset Movement
1. Go to the Asset Movement list, click on New.
1. Select the Asset. 
1. Select a date.
1. Enter the Quantity to be transfered.
1. Enter the source and target Locations of the Asset.
1. You can also transfer an Asset from one Employee to another by selecting the From and To Employee.
1. Save.
1. Submit.

    If the Item is Serialized, enter the Serial Number. 

There is also a **Transfer Asset** button on the top right of the Asset form to initiate Asset Movement. Enter the target location, select a date and click on Transfer.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-movement-using-button.png">
