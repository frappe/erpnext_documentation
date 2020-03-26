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
1. Select the Purpose from 'Issue', 'Receipt', or 'Transfer'. Mandatory fields will be changed based on purpose.
1. Select a date.
1. Select Assets you want to move. Currenct Location / Custodian will be automatically fetched.
1. Select Reference Document Type (Optional).
1. Select Reference Document Name (Optional).
1. Save.
1. Submit.

To make an Asset Movement of a number of assets, it is advised to go to Asset List, select assets to be moved and click on **Make Asset Movement** from Actions menu on the top left. 

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-movement-using-button.png">

There is also a **Transfer Asset** button on the top right of the Asset form to initiate Asset Movement. It auto fills available fields from Asset Form.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-movement-using-transfer-asset-button.png">
