<!-- add-breadcrumbs -->
# Address Template

**Address template can store different formats of addresses based on the region.**

Each region has its way of defining addresses. To manage multiple address formats for your Documents (like Quotations, Purchase Invoices, etc.), you can create country-wise **Address Templates**.

To access address template, go to:
> Home > Settings > Address Template

A default Address Template is created when you set up the system. You can either edit it or create a new template. This default template will apply to all countries not having a specific template.

Consider a customer from the United States where 'County' is a part of the address. If you set county in the address template for United States, then it'll show up in the address field and hence in the print preview. Fields like PIN code can be changed to be displayed as ZIP code and fields like county can be added by using Address Templates.

> The Address Template checks the 'Country' field in the Address master to apply different address templates to transactions.

## 1. How to create an Address Template
1. Go to the Address Template list, click on New.
1. Select a country.
1. Change the CSS and Jinja if required.
1. Save.

### 1.1 Jinja Templating
The templating engine is based on HTML and the [Jinja Templating](http://jinja.pocoo.org/docs/templates/) system. All the fields (including Custom Fields) will be available for creating the template.

Here is the default Jinja template:

    {% raw %}{{ address_line1 }}<br>
    {% if address_line2 %}{{ address_line2 }}<br>{% endif -%}
    {{ city }}<br>
    {% if state %}{{ state }}<br>{% endif -%}
    {% if pincode %}PIN:  {{ pincode }}<br>{% endif -%}
    {{ country }}<br>
    {% if phone %}Phone: {{ phone }}<br>{% endif -%}
    {% if fax %}Fax: {{ fax }}<br>{% endif -%}
    {% if email_id %}Email: {{ email_id }}<br>{% endif -%}{% endraw %}

Here is an example:

<img class="screenshot" alt="Print Heading" src="{{docs_base_url}}/assets/img/setup/print/address-format.png">

### 2. Related Topics
1. [Terms and Conditions Template](/docs/user/manual/en/setting-up/print/terms-and-conditions)
1. [Cheque Print Template](/docs/user/manual/en/setting-up/print/cheque-print-template)
