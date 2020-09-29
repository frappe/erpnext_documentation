<!-- add-breadcrumbs -->
# Error de correo electrónico al enviar o recibir

En ERPNext, puede personalizar la puerta de enlace de correo electrónico entrante y saliente. Al guardar una cuenta de correo electrónico, ERPNext intenta establecer una conexión con su puerta de enlace de correo electrónico. Si su cuenta de ERPNext puede conectarse bien, la cuenta de correo electrónico se guardará correctamente. De lo contrario, es posible que reciba un error como se muestra a continuación.

<img class="screenshot" alt="Email Error" src="{{docs_base_url}}/assets/img/articles/email-error.png">

This indicates that using login credentials and other email gateway details provided in the Email Account, ERPNext is not able to connect to your email server. Please ensure that you have entered valid email credentials for your Email Gateway. Once you have configured Email Account successfully, you should be able to send and receive emails from your ERPNext account fine.

Nota: Su cuenta ERPNext está conectada con un servidor de correo electrónico ERPNext de forma predeterminada. Si no desea utilizar su propio servidor de correo electrónico, puede continuar enviando correos electrónicos utilizando el servidor de correo electrónico ERPNext, sin que se requiera ninguna configuración en la cuenta de correo electrónico.
