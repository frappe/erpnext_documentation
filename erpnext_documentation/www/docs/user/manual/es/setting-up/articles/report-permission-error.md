<!-- add-breadcrumbs -->
# Solución de problemas de errores de permisos

**Pregunta:** El usuario tiene asignados roles como Usuario de cuenta y Administrador de cuenta. Aún así, al acceder al informe de cuentas por cobrar, el usuario recibe un mensaje de error que indica que el maestro del territorio no tiene permiso.

<img alt="Informar error de permiso" class="screenshot" src="{{docs_base_url}}/assets/img/articles/report-permission-1.png">

**Respuesta:**

Según el sistema de permisos en ERPNext, para que el Usuario pueda acceder a un formulario o informe, debe tener al menos permiso de lectura en todos los campos de enlace de ese formulario / informe. Dado que Territorio es un campo de enlace en el informe de Cuentas por cobrar, agregue una regla de permiso para permitir que el Usuario / Administrador de cuenta tenga al menos permiso de lectura en el maestro de Territorio. Siga los pasos que se indican a continuación para resolver este problema.

1.  Los roles asignados al usuario son el usuario de la cuenta y el administrador de la cuenta.

2.  Como se indica en el mensaje de error, el usuario no tenía permiso en el maestro de territorio. Según el permiso predeterminado, ninguno de los roles anteriores asignados a ese usuario tiene ningún permiso en el maestro del territorio.

3.  Para resolver este problema, he asignado el permiso de Usuario de la cuenta para leer el maestro del territorio.

    <img alt="Administrador de permisos" class="screenshot" src="{{docs_base_url}}/assets/img/articles/report-permission-2.png">

Según esta actualización de permiso, el usuario debería poder acceder al informe de cuentas por cobrar correctamente.
