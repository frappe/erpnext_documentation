<!-- add-breadcrumbs -->
# Print Style

**In Print Style you can define custom CSS styles applied to Print Formats.**

ERPNext comes with preset styles for printing documents. You can also create new styles using CSS that can be applied to all your print formats.

The standard print Styles in ERPNext are: Monochrome, Modern, and Classic.
To create a new **Print Style** go to:

> Home > Settings > Print Style

## 1. How to create a new Print Style
1. Go to the Print Style list, click on New.
1. Enter a name for the Print Style.
1. Enter the CSS that'll define how the style will look like.
1. Save.

The styles you create here apply to both standard and custom print formats. To find out the various CSS classes available, you can make a standard print format, open in a new page and see the source.

A default Print Style, can be set from [Print Settings](/docs/user/manual/en/setting-up/print/print-settings).

All Print Format styles are based on Bootstrap (Version 3) CSS Framework.

<img class="screenshot" alt="Print Style" src="{{docs_base_url}}/assets/img/setup/print/print-style.png">

If you have enabled developer mode and tick on Standard then system will generate the JSON file for the Print Style. You can contribute a default print style with this.

### 2. Related Topics
1. [Print Format](/docs/user/manual/en/setting-up/print/print-format)
1. [Print Headings](/docs/user/manual/en/setting-up/print/print-headings)
1. [Letter Head](/docs/user/manual/en/setting-up/print/letter-head)
1. [Cheque Print Template](/docs/user/manual/en/setting-up/print/cheque-print-template)
