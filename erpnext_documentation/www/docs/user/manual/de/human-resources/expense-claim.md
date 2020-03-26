<!-- add-breadcrumbs -->
# Aufwandsabrechnung (Expense Claim)

Eine Aufwandsabrechnung (Expense Claim) wird dann erstellt, wenn ein Mitarbeiter Ausgaben für das Unternehmen aus seinem eigenen Geldbeutel tätigt. Wenn Sie beispielsweise einen Kunden zum Essen einladen, können Sie über das Formular zur Aufwandsabrechnung eine Erstattung beantragen.

## Voraussetzungen

- Mitarbeiter (Employee)
- Konten Verbindlichkeiten, Bank / Kasse, Reisekosten Arbeitnehmer
- Aufwandsabrechnungsart (Expense Claim Type)

Erstellen Sie zunächst eine Aufwandsabrechnungsart oder passen Sie eine bestehende an. Hier muss das Aufwandskonto für das jeweilige Unternehmen hinterlegt werden. Für die Aufwandsabrechnungsart "Fahrtkosten" wird beispielsweise "Reisekosten Arbeitnehmer Fahrtkosten" als Konto hinterlegt.

## Aufwandsabrechnung

Um eine neue Aufwandsabrechnung zu erstellen, gehen Sie zu:

> Personalwesen > Dokumente > Aufwandsabrechnung > Neu

<img class="screenshot" alt="Aufwandsabrechnung" src="{{ docs_base_url }}/assets/img/human-resources/expense_claim.png">

Geben Sie die Mitarbeiter-ID, das Datum und die Auflistung der Ausgaben, die Sie zurückerstattet haben möchten, ein. Als Verbindlichkeiten-Konto (Payable Account) kann beispielsweise "Sonstige Verbindlichkeiten" angegeben werden. Speichern Sie den Datensatz.

Die Person, die die Kostenerstattung beantragt, muss auch den Benutzers, der diese Ausgaben genehmigen soll, angeben und sie muss dem Ausgabengenehmiger die Anfrage über die Schaltfläche "Zuweisen zu" zuweisen, damit dieser eine Benachrichtigung über die Anfrage erhält.

### Ausgaben genehmigen

Wenn der Genehmiger das Formular erhält, kann er die genehmigten Beträge aktualisieren und den Status auf "Genehmigt" oder "Abgelehnt" setzen. Im Feld "Bemerkung" können Kommentare angelegt werden. Diese können Erklärungen enthalten, warum ein Antrag genehmigt oder abgelehnt wurde.

Anschließend schreibt er das Dokument durch einen Klick auf "Buchen" fest.

### Ausgaben erstatten

Um eine Ausgabe zu erstatten klicken Sie rechts oben auf "Erstellen > Zahlung".

<img class="screenshot" alt="Aufwandsabrechnung" src="{{ docs_base_url }}/assets/img/human-resources/expense_claim_create_payment.png">

<img class="screenshot" alt="Aufwandsabrechnung" src="{{ docs_base_url }}/assets/img/human-resources/expense_claim_payment_entry.png">

### Verbuchung der Ausgaben und der Kostenerstattung

Wenn eine Aufwandsabrechnung genehmigt und gebucht wird, ensteht eine Verbindlichkeit in der Bilanz sowie ein betrieblicher Aufwand in der Gewinn- und Verlustrechnung.

Sobald ein Zahlunseintrag (Payment Entry) für eine Spesenabrechnung verbucht wird, wird die Verbindlichkeit aufgelöst. Ob dafür ein Bankkonto oder eine Kasse belastet wird, können Sie zum Zeitpunkt der Zahlung im Zahlungseintrag entscheiden.

### Verknüpfungen zu Aufgaben und Projekten

* Um eine Aufwandsabrechnung mit einer Aufgabe oder einem Projekt zu verknüpfen, geben Sie die Aufgabe oder das Projekt an, während Sie eine Aufwandsabrechnung erstellen.

<img class="screenshot" alt="Aufwandsabrechnung - Verknüpfung zum Projekt" src="{{ docs_base_url }}/assets/img/project/project_expense_claim_link.png">

{next}
