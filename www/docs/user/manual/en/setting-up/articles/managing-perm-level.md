<!-- add-breadcrumbs -->
#Managing Perm Level in Permission Manager

Perm Level is way of reducing the amount information visible or changeable in a specific DocType for certain User Groups. Where as you can define visibility or changability for each DocType by customizing the DocType-specific Permissions Rule, with the Perm Level you can change these for specific Sections or Fields.

In each document, you can group fields by "levels". Each group of fields or field group is denoted by a unique number (0, 1, 2, 3 etc.). A separate set of permission rules can be applied to each field group. By default all fields are of level 0.

Perm Level (Abbreviated form of Permission Level) for a field can be defined in the [Customize Form](/docs/user/manual/en/customize-erpnext/customize-form.html).

<img alt="Perm Level Field" class="screenshot" src="{{docs_base_url}}/assets/img/articles/perm-level-1.gif">

If you need to assign different permission of particular field to different users, you can achieve it via Perm Level. Let's consider an example for better understanding.

Delivery Note is accessible to Stock Manager as well as Stock User. You don't wish Stock User to access Amount related field in Delivery Note, but other field should be visible just like it is visible Stock Manager.

For all related fields, that should not be seen, you can set Perm Level as (say) 2. 

For Stock Managers, they will have permission on fields on Delivery Note with Perm Level 2, whereas a Stock User will not have any permission on Perm Level 2 for Delivery Note, because their role has not been assigned with a rule allowing them to read or write in Field with Perm Level of 2, as shown below.

<img alt="Perm Level Rule" class="screenshot" src="{{docs_base_url}}/assets/img/articles/perm-level-2.png">

Considering the same scenario, if you want a Stock User to access a field at Perm Level 2, but do not want to give permission to edit it, the Stock User will be assigned with permission to only be able to read on Perm Level 2, but not to write/edit.

<img alt="Perm Level Rule 2" class="screenshot" src="{{docs_base_url}}/assets/img/articles/perm-level-3.png">

Perm Levels (1, 2, 3 or 2, 1, 3 or 3,2,1) do not need to be in any particular order. They do not imply hierarchy. Perm Level is primarily used for grouping number of fields together, and then assigning permission to Roles for that group. Hence, you can set any perm level for an item, and then do permission setting for it.

If you want to change permissions for all fields in a section, you can simply change the perm level for the section field and it will be applied to all fields in the section.

<!-- markdown -->
