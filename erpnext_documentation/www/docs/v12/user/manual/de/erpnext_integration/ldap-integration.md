# Authentifizierung über LDAP

Das Lightweight Directory Access Protocol ist ein zentralisiertes Zugangskontrollsystem, das von vielen kleinen und mittleren Unternehmen verwendet wird. Wenn Sie einen LDAP-Dienst einrichten, können Sie sich mit LDAP-Anmeldeinformationen bei ERPNext-Konto anmelden.

Um LDAP einzurichten, navigieren Sie zu `Entdecken > Integrationen > LDAP-Einstellungen`.

#### LDAP einrichten

Um den LDAP-Dienst zu aktivieren, müssen Sie Parameter wie die LDAP-Server-URL (einschließlich `ldap://`), die Organisationseinheit, die UID, den Base Distinguished Name (DN) und das Passwort für den Base Distinguished Name konfigurieren.

<img class="screenshot" alt="LDAP-Einstellungen" src="{{ docs_base_url }}/assets/img/setup/integrations/ldap_settings.png">

Nach der Einstellung der LDAP-Parameter aktiviert das System auf dem Anmeldebildschirm die Option **Anmeldung über LDAP**.

<img class="screenshot" alt="LOGIN via LDAP" src="{{ docs_base_url }}/assets/img/setup/integrations/login_via_ldap.png">

Für die erweiterten Felder können Sie diese Einstellungen ausprobieren:

    LDAP Search String: uid={0}     
    LDAP First Name Field: cn     
    LDAP Email Field: mail     
    LDAP Username Field: uid

Die Standard-Rolle eines neuen LDAP-Benutzers ist `Blogger`. Sie können die Berechtigungen dieser Rolle mit dem Berechtigungsmanager anpassen.

##### Sichere Verbindung zu LDAP

Im Bereich LDAP-Einstellungen gibt es zwei Dropdowns.

1. SSL/TLS-Modus
   
   stellen Sie diesen auf **StartTLS**, um eine Verbindung mit Ihrem LDAP-Server über StartTLS herzustellen. Wenn Ihr LDAP-Server StartTLS nicht unterstützt, führt die Einstellung auf StartTLS zu der Fehlermeldung `StartTLS wird nicht unterstützt`. Überprüfen Sie die Konfiguration auf Ihrem LDAP-Server, wenn Sie diesen Fehler erhalten.

2. Require Trusted Certificate
   
   wenn Sie dies auf **Ja** ändern, muss das vom LDAP-Server bereitgestellte Zertifikat vom Frappe/ERPNext-Server als vertrauenswürdig eingestuft werden. Wenn Sie StartTLS lieber mit einem selbstsignierten (nicht vertrauenswürdigen) Zertifikat verwenden möchten, setzen Sie dies auf **Nein**. Wenn Sie StartTLS nicht verwenden, wird diese Einstellung ignoriert.
