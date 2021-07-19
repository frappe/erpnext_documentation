<!-- add-breadcrumbs -->
# Arbeitsauftrag


Der Arbeitsauftrag (auch als Arbeitsauftrag bezeichnet) ist ein Dokument welches vom Produktionsplaner als Startsignal in die Fertigung gegeben wird, um eine bestimmte Anzahl eines bestimmten Artikels zu produzieren. Der Arbeitsauftrag unterstützt Sie auch dabei den Materialbedarf (Lagerbuchung) für diesen Artikel aus der **Stückliste** zu generieren.

Der **Arbeitsauftrag** wird aus dem **Werkzeug zur Fertigungsplanung** generiert, basierend auf den Kundenaufträgen. Sie können weiterhin direkt einen Arbeitsauftrag erstellen über:

> Fertigung > Dokumente > Arbeitsauftrag > Neu

<img class="screenshot" alt="Arbeitsauftrag" src="{{docs_base_url}}/v12/assets/img/manufacturing/work-order.png">

### Einen Arbeitsauftrag erstellen

* Wählen Sie den Artikel aus, der gefertigt werden soll.
* Die Standard-Stückliste für diesen Artikel wird aus dem System gezogen. Sie können die Stückliste auch ändern.
* Wenn die ausgewählte Stückliste auch Arbeitsgänge mit berücksichtigt, sollte das System alle Arbeitsgänge aus der Stückliste übernehmen.
* Geben Sie das geplante Startdatum an (ein geschätztes Datum zu dem die Produktion beginnen soll).
* Wählen Sie das Lager aus. Das Fertigungslager ist der Ort zu dem die Artikel gelangen, wenn Sie mit der Herstellung beginnen, und das Eingangslager ist der Ort, wo fertige Erzeugnisse lagern, bevor sie versandt werden.

> Anmerkung: Sie können einen Arbeitsauftrag abspeichern ohne ein Lager auszuwählen. Lager sind jedoch zwingend erforderlich um einen Arbeitsauftrag zu übertragen.

### Arbeitsplätze neu zuordnen/Dauer von Arbeitsgängen

* Als Voreinstellung zieht das System Arbeitsplätze und die Dauer von Arbeitsgängen aus der gewählten Stückliste.

<img class="screenshot" alt="Arbeitsauftrag - Arbeitsgänge" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-operations.png">

* Wenn Sie den Arbeitsplatz für einen bestimmten Arbeitsgang im Arbeitsauftrag neu zuordnen möchten, können Sie das tun, bevor Sie den Arbeitsauftrag übertragen.

<img class="screenshot" alt="Arbeitsauftrag - Arbeitsgänge neu zuordnen" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-reassigning-operations.png">

* Wählen Sie den betreffenden Arbeitsgang aus und ändern Sie seinen Arbeitsplatz.
* Sie können auch die Dauer des Arbeitsgangs ändern.

### Kapazitätsplanung im Arbeitsauftrag

* Wenn ein Arbeitsauftrag basierend auf dem geplanten Startdatum und der Verfügbarkeit des Arbeitsplatzes übertragen wird, plant das System alle Arbeitsgänge für den Arbeitsauftrag ein (wenn der Arbeitsauftrag selbst Arbeitsgänge enthält).

### Material der Fertigung übergeben

* Wenn Sie Ihren Arbeitsauftrags übertragen haben, müssen Sie das Rohmaterial übertragen um den Fertigungsprozess zu starten.
* Das erstellt eine Lagerbuchung mit allen Artikeln, die benötigt werden, um diesen Arbeitsauftrag abzuschliessen. Die Artikel werden an das Fertigungslager übertragen (dieser Prozess fügt basierend auf Ihren Einstellungen Unterbaugruppen mit Stückliste als EINEN Artikel hinzu oder löst die Unterpunkte auf).
* Klicken Sie auf "Material der Fertigung übergeben".

<img class="screenshot" alt="Materialübertrag" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-material-transfer.png">

* Geben Sie die Menge des Materials an, das übertragen werden soll.

<img class="screenshot" alt="Materialübertrag - Menge" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-material-transfer-qty.png">

* Übertragen Sie die Lagerbuchung.

<img class="screenshot" alt="Lagerbuchung zum Kundenauftrag" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-SE-for-material-transfer.png">

* Das an die Fertigung übertragene Material wird basierend auf der Lagerbuchung im Arbeitsauftrag aktualisiert.

<img class="screenshot" alt="Lagerbuchung zum Arbeitsauftrag" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-material-transfer-updated.png">

### Zeitprotokoll erstellen

* Der Fortschritt des Arbeitsauftrages kann über ein [Zeitprotokoll]<img class="screenshot" alt="Make TL against PO" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-operations-make-tl.png"> mitprotokolliert werden.
* Zeitprotokolle werden zu den Arbeitsgängen des Arbeitsauftrages erstellt.
* Vorlagen für Zeitprotokolle werden für die eingeplanten Arbeitsgänge zum Zeitpunkt des Übertragens des Arbeitsauftrages erstellt.
* Um weitere Zeitprotokolle zu einem Arbeitsgang zu erstellen, wählen Sie "Zeitprotokoll erstellen" im betreffenden Arbeitsgang aus.

<img class="screenshot" alt="Zeitprotokoll zum Arbeitsauftrag erstellen" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-operations-make-tl.png">

### Fertige Erzeugnisse aktualisieren

* Wenn Sie den Arbeitsauftrag fertiggestellt haben, müssen Sie die Fertigen Erzeugnisse aktualisieren.
* Das erstellt eine Lagerbuchung, welche alle Unterartikel vom Fertigungslager abzieht und dem Lager "Fertige Erzeugnisse" gutschreibt.
* Klicken Sie auf "Fertige Erzeugnisse aktualisieren".

<img class="screenshot" alt="Fertigerzeugnisse aktualiseren" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-FG-update.png">

* Geben Sie die Menge des übertragenen Materials an.

<img class="screenshot" alt="Menge der Fertigerzeugnisse aktualisieren" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-FG-update-qty.png">

>Tipp: Sie können einen Arbeitsauftrag auch teilweise fertig stellen, indem Sie über eine Lagerbuchung das Lager Fertige Erzeugnisse aktualisieren.

### Einen Arbeitsauftrag anhalten

* Wenn Sie einen Arbeitsauftrag anhalten, wird sein Status auf "Angehalten" gesetzt, mit der Folge, dass alle Herstellungsprozesse für diesen Arbeitsauftrag eingestellt werden.
* Um den Arbeitsauftrag anzuhalten klicken Sie auf die Schaltfläche "Anhalten".

1. Wenn Sie den Arbeitsauftrag übertragen, reserviert das System für jeden Arbeitsgang des Arbeitsauftrags in Serie gemäß dem geplanten Startdatum basierend auf der Verfügbarkeit des Arbeitsplatzes ein Zeitfenster. Die Verfügbarkeit des Arbeitsplatzes hängt von den Arbeitszeiten des Arbeitsplatzes und der Urlaubsliste ab und davon, ob ein anderer Arbeitsgang des Arbeitsauftrages in diesem Zeitfenster eingeplant wurde. Sie können in den Fertigungseinstellungen die Anzahl der Tage angeben, in denen das System versucht den Arbeitsgang einzuplanen. Standardmäßig ist dieser Wert auf 30 Tage eingestellt. Wenn der Arbeitsgang über das verfügbare Zeitfenster hinaus Zeit benötigt, fragt Sie das System, ob der Arbeitsgang pausieren soll. Wenn das System die Terminplanung erstellen konnte, legt es Zeitprotokolle an und speichert sie. Sie können diese verändern und später übertragen.
2. Sie können außerdem zusätzliche Zeitprotokolle für einen Arbeitsgang erstellen. Hierzu wählen Sie den betreffenden Arbeitsgang aus und klicken Sie auf "Zeitprotokoll erstellen".
3. Rohmaterial übertragen: Dieser Schritt erstellt eine Lagerbuchung mit allen Artikeln, die benötigt werden, um dem Arbeitsauftrag abzuschliessen, und dem Fertigungslager hinzugefügt werden müssen (Unterartikel werden entweder als EIN Artikel mit Stücklister ODER in aufgelöster Form gemäß Ihren Einstellungen hinzugefügt).
4. Fertigerzeugnisse aktualisieren: Dieser Schritt erstellt eine Lagerbuchung, welche alle Unterartikel vom Fertigungslager abzieht und dem Lager Fertige Erzeugnisse hinzufügt.
5. Um die zum Arbeitsauftrag erstellten Zeitprotokolle anzusehen, klicken Sie auf "Zeitprotokolle anzeigen".

<img class="screenshot" alt="Arbeitsauftrag anhalten" src="{{docs_base_url}}/v12/assets/img/manufacturing/PO-stop.png">

* Sie können auch einen angehaltenen Arbeitsauftrag wieder weiter laufen lassen.

> Anmerkung: Um einen Arbeitsauftrag zu einem Artikel zu erstellen müssen Sie auf dem Artikelformular das Feld "Arbeitsauftrag zulassen" ankreuzen.

{next}
