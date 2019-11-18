<!-- add-breadcrumbs -->
# Server Script

**A Server Script lets you dynamically define a Python Script that is executed on the server on a document event or API**

> Introduced in Version 12

## 1. How to create a Server Script

To create a Server Script

1. You must set `server_script_enabled` as true in site_config.json of your site.
1. To add/edit Server Script, ensure your role is System Manager.
1. Create a new server script via "New Server Script" in the toolbar.
1. Set the type of server script (Document Event / API).
1. Set the document type and event name, or method name, script and save.

## 2. Features

### 2.1 Enabling Server Script

Server script must be enabled via site_config.json

```
bench --site site1.local set-config server_script_enabled true
```

### 2.2 Document Events

For scripts that are to be called via document events, you must set the Reference Document Type and Event Name to define the trigger

- Before Insert
- Before Save
- After Save
- Before Submit
- After Submit
- Before Cancel
- After Cancel
- Before Delete
- After Delete

### 2.3 API Scripts

You can create a new API that can be accessed via `api/method/[methodname]` by the script type "API"

If you want the guest user to access the API, you must check on "Allow Guest"

The response can be set via `frappe.response["message"]` object

### 2.3 Security

Frappe Framework uses the RestrictedPython library to restrict access to methods available for server scripts. Only the safe methods, listed below are available in server scripts

```py
json # json module
dict # internal dict
frappe._ # translator method
frappe._dict # frappe._dict internal method
frappe.flags # global flags

# FORMATTING
frappe.format # frappe.format_value(value, dict(fieldtype='Currency'))
frappe.format_value # frappe.format_value(value, dict(fieldtype='Currency'))
frappe.date_format # default date format
frappe.format_date # returns date as "1st September 2019"

# SESSION
frappe.form_dict # form / request parameters
frappe.request # request object
frappe.response # response object
frappe.session.user # current user
frappe.session.csrf_token # CSRF token of the current session
frappe.user  # current user
frappe.get_fullname # fullname of the current user
frappe.get_gravatar # frappe.utils.get_gravatar_url
frappe.full_name = # fullname of the current user

# ORM
frappe.get_meta # get metadata object
frappe.get_doc
frappe.get_cached_doc
frappe.get_list
frappe.get_all
frappe.get_system_settings

# DB
frappe.db.get_list
frappe.db.get_all
frappe.db.get_value
frappe.db.get_single_value
frappe.db.get_default
frappe.db.escape

# UTILITIES
frappe.msgprint # msgprint
frappe.get_hooks # app hooks
frappe.utils # methods in frappe.utils
frappe.render_template # frappe.render_template,
frappe.get_url # frappe.utils.get_url
socketio_port # port for socketio
style.border_color # '#d1d8dd'
guess_mimetype = mimetypes.guess_type,
html2text = html2text,
dev_server # True if in developer mode
```

## 3. Examples

### 3.1 Change the value of a property before change

Script Type: Before Save

```py
if "test" in doc.description:
	doc.status = 'Closed'
```

### 3.2 Custom validation

Script Type: "Before Save"

```py
if "validate" in doc.description:
	raise frappe.ValidationError
```

### 3.3. Auto Create To Do

Script Type: "After Save"

```py
if doc.allocted_to:
    frappe.get_doc(dict(
        doctype = 'ToDo'
        owner = doc.allocated_to,
        description = doc.subject
    )).insert()
```

### 3.4 API

- Script Type: API
- Method Name: `test_method`

```py
frappe.response['message'] = "hello"
```

Request: `/api/method/test_method`
