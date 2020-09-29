<!-- add-breadcrumbs -->
# Integración de ERPNext con dispositivos de asistencia biométricos

Los registros de registro de asistencia del dispositivo biométrico son un tipo de registro de entrada y salida de un empleado.

ERPNext tiene una disposición para almacenar estos registros en un documento llamado Registro de empleados.

La asistencia se puede marcar en función de los registros de registro del empleado y el turno [Configuración de asistencia automática](/docs/user/manual/en/human-resources/shift-management#25-auto-attendance-settings) del empleado usando [Asistencia automática](/docs/user/manual/en/human-resources/auto-attendance)

Por lo tanto, la integración de su dispositivo biométrico, o cualquier sistema de control de acceso que recolecte IN / OUT, se puede realizar mediante los siguientes pasos:

  1. [Configuración del asistente automático para marcar la asistencia desde el registro del empleado](#1-setting-up-auto-attendance-to-mark-attendance-from-the-employee-checkin)
  1. [Rellenar los registros de perforaciones biométricas en ERPNext Employee Check In](#2-populating-the-biometric-punch-logs-into-erpnexts-employee-checkin)

## 1. Configuración del asistente automático para marcar la asistencia desde el registro del empleado

Antes de importar los registros de Check-in y Check-out de los empleados a su sistema ERPNext, tendría que configurar los empleados y sus turnos para poder generar asistencia utilizando la función de Asistencia automática en ERPNext.

Consulte el siguiente enlace para configurar la asistencia automática: [Configurar la asistencia automática](/docs/user/manual/en/human-resources/auto-attendance#steps-to-setup-auto-attendance)

Una vez que haya configurado el empleado y asignado turnos a los empleados, ahora está listo para continuar con el siguiente paso.

## 2. Rellenar los registros de perforaciones biométricas en registro de empleado en ERPNext 
Dependiendo de su sistema biométrico y sus características, puede haber muchas formas de importar los registros a ERPNext:

1. Utilice la herramienta de importación de datos de ERPNext:
    - La solución más simple posible (en términos de complejidad de implementación) sería generar un Excel / CSV del Check-in / Check-out y usar la herramienta de importación de datos incorporada en ERPNext para importar periódicamente a su Documento de Checkin de Empleado
    - Por favor refiérase a [Documentación de ERPNext sobre la herramienta de importación de datos](/docs/user/manual/en/setting-up/data/data-import) para obtener más información sobre cómo hacer esto.

1. Integración de API:
    - Puede automatizar el proceso de importación de registros de perforaciones biométricas integrándolo con la API disponible en ERPNext.
    - Se puede acceder a esta API en: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.
    - Este método requiere conocimientos técnicos y probablemente debería ponerse en contacto con su implementador ERPNext o proveedor de sistema biométrico.

1. Configure un script de Python en su computadora para integrar ZKTeco o dispositivos similares:
    - Este método funciona solo para ZKTeco o dispositivos similares que usan el protocolo ZK para comunicarse a través de TCP / IP.
    - Este script está disponible en: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
    - Siga las instrucciones que se dan en la página del script para configurarlo en su computadora.
    - Este script extrae registros biométricos de un dispositivo compatible y utiliza la API mencionada en el paso anterior para enviar los datos a ERPNext.
