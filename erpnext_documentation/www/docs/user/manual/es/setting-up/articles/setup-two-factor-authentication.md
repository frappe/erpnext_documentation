<!-- add-breadcrumbs -->
# Configurar la autenticación de dos factores

## Habilitar la autenticación de dos factores (2FA)

Active la autenticación de dos factores ejecutando el comando.

`bench --site [sitename] set-config enable_two_factor_auth true` 

Especifique lo siguiente en Configuración del sistema

* El método de validación de OTP (Aplicación OTP = TOTP usando token suave o duro mientras que correo electrónico / SMS = HOTP usando correo electrónico o SMS
* El tiempo de caducidad del código QR en el servidor si se especifica la aplicación OTP
* El nombre del emisor de la OTP.

<img alt="Habilitar autenticación de dos factores" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-1.png">


Al activar 2FA desde la configuración, también se activa para el rol "Todos". De esta forma, todos los usuarios, incluido el Administrador, deben realizar una autenticación de segundo nivel con un token. Al desmarcar la casilla de verificación "Autenticación de dos factores" en el rol "Todos" y habilitarla en otros roles, la necesidad de iniciar sesión con un token puede limitarse a roles específicos. 2FA no se aplica al inicio de sesión de usuarios web y al inicio de sesión de API

<img alt="Función Activar autenticación de dos factores" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-2.png">

Si usa la autenticación por SMS, asegúrese de que la configuración de SMS esté actualizada

<img alt="SMS Configuración" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-3.png">

Si usa el correo electrónico, asegúrese de que la configuración de su cuenta de correo electrónico saliente esté actualizada

<img alt="Email Configuración" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-4.png">

Cuando el nuevo usuario intenta iniciar sesión por primera vez en un sistema que tiene habilitada la autenticación de dos factores y que tiene la opción de autenticación como aplicación OTP, se envía un correo electrónico con un enlace al código QR.

<img alt="Notificación de email de dos factores" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-5.png">
<img alt="Página de código QR" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-6.png">

Escanear el código QR con una aplicación de autenticación como Google Authenticator registra el acceso del usuario y automáticamente comienza a generar tokens que se pueden usar para iniciar sesión.

<img alt="Aplicación de escaneo de dos factores" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor_app.jpeg">

Si se utiliza correo electrónico / SMS como método de autenticación, también recibirá notificaciones

<img alt="Email y SMS" class="screenshot" src="{{docs_base_url}}/assets/img/articles/twofactor/twofactor-8.png">
