<!-- add-breadcrumbs -->
# Druckformat

Druckformate sind die Erscheinungsbilder der Ausdrucke, wenn Sie eine E-Mail oder eine Transaktion wie eine Ausgangsrechnung drucken. Es gibt zwei Arten von Druckformaten:

* Das automatisch generierte "Standard"-Druckformat: Diese Art der Formatierung folgt den Vorgaben von ERPNext.
* Das auf dem Dokument "Druckformat" basierende Format: Hier gibt es HTML-Vorlagen, die  mit Daten gefüllt werden.

ERPNext bringt eine bestimmte Menge von vordefinierten Vorlagen in drei Stilarten mit: Modern, Classic und Standard.

Sie können die Vorlagen verändern und eigene erstellen. Die ERPNext-Vorlagen zu bearbeiten, ist nicht erlaubt, weil Sie bei einem Update auf eine neuere Programmversion überschrieben werden können.

Um Ihre eigenen Versionen zu erstellen, öffnen Sie eine bereits vorhandene Vorlage über:

> Einstellungen > Druck > Druckformate

![Druckformat]({{docs_base_url}}/v12/assets/img/customize/print-settings.png)

Wählen Sie den Typ des Druckformats, welches Sie bearbeiten wollen, und klicken Sie auf die Schaltfläche "Kopieren" in der rechten Spalte. Es öffnet sich ein neues Druckformat mit der Einstellung NEIN für "für "Ist Standard" und Sie kännen das Druckformat bearbeiten.

Ein Druckformat zu bearbeiten ist eine langwierige Angelegenheit und Sie müssen etwas Grundwissen über HTML, CSS und Python mitbringen, um dies verstehen zu können. Wenn Sie Hilfe benötigen, erstellen Sie bitte im Forum eine Anfrage.

Printformate werden auf der Serverseite über die [Programmiersprache Jinja Templating](http://jinja.pocoo.org/docs/templates/) erstellt. Alle Formulare haben Zugriff auf doc object, das Informationen über das Dokument enthält, welches formatiert wird. Sie können über das Frappe-Modul auch auf oft verwendete Hilfswerkzeuge zugreifen.

Zum Bearbeiten des Erscheinungsbildes bietet sich das [Bootstrap CSS Framework](http://getbootstrap.com/)  an und Sie können die volle Bandbreite dieses Werkzeuges nutzen.

> Anmerkung: Vorgedrucktes Briefpapier zu verwenden ist normalerweise keine gute Idee, weil Ihre Ausdrucke unfertig (inkonsistent) aussehen, wenn Sie per E-mail verschickt werden.

### Referenzen

1. [Programmiersprache Jinja Templating: Referenz](http://jinja.pocoo.org/docs/templates/)
2. [Bootstrap CSS Framework](http://getbootstrap.com/)

### Druckeinstellungen

Um Ihre Druck- und PDF-Einstellungen zu bearbeiten/zu aktualisieren, gehen Sie zu:

> Einstellungen > Druck und Branding > Druckeinstellungen

![Druckformat]({{docs_base_url}}/v12/assets/img/customize/print-settings.png)

### Beispiel

```jinja
{% raw %}
 <h3>{{ doc.select_print_heading or "Invoice" }}</h3>
 <div class="row">
    <!-- Kunde XYZ GmbH -->
    <div class="col-md-3 text-right">{{ _("Customer Name") }}</div>
    <div class="col-md-9">{{ doc.customer_name }}</div>
 </div>
 <div class="row">
    <!-- Date 09.09.1999 -->
    <div class="col-md-3 text-right">{{ _("Date") }}</div>
    <div class="col-md-9">{{ doc.get_formatted("invoice_date") }}</div>
 </div>
 <table class="table table-bordered">
    <tbody>
        <tr>
            <!--
            Pos  Artikel                  Art.Nr.   Menge     Preis     Summe
            -->
            <th>{{ _("Sr") }}</th>
            <th>{{ _("Item Name") }}</th>
            <th>{{ _("Item Code") }}</th>
            <th class="text-right">{{ _("Qty") }}</th>
            <th class="text-right">{{ _("Rate") }}</th>
            <th class="text-right">{{ _("Amount") }}</th>
        </tr>
        {%- for row in doc.items -%}
        <tr>
            <!-- 
            1  Schraube                    s123     € 10,00   € 0,10   € 1,00
               Halbrundkopf Kreuzschlitz
            2  ...
            -->
            <td>{{ row.idx }}</td>
            <td>
                {{ row.item_name }}<br>
                {{ row.description }}
            </td>
            <td style="width: 37%;">
                <div>{{ row.item_code}}</div></td>
            <td class="text-right">{{ row.qty }} {{ row.uom or row.stock_uom }}</td>
            <td class="text-right">{{ row.get_formatted("rate", doc) }}</td>
            <td class="text-right">{{ row.get_formatted("amount", doc) }}</td>
        </tr>
        {%- endfor -%}
    </tbody>
   </table>
{% endraw %}
```

### Anmerkungen

1. Um nach Datum und Währung formatiert Werte zu erhalten, verwenden Sie: `doc.get_formatted("fieldname")`
1. Für übersetzbare Zeichenfolgen verwenden Sie: `{{ '{{ _("This string is translated") }}' }}`

{next}
