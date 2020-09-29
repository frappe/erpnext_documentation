<!-- add-breadcrumbs -->
# Diferencia entre el usuario del sistema y el usuario del sitio web

**Pregunta:** He añadido a mi empleado como usuario y también les he asignado roles. Aún así, no pueden ver Dashboard en el inicio de sesión.

**Respuesta:**

Hay dos tipos de usuarios en ERPNext.

* **Usuario del sistema**: Son empleados de su empresa. Ejemplo de roles asignados a los usuarios del sistema son Usuario de cuenta, Gerente de ventas, Usuario de compra, Equipo de soporte, etc.

* **Usuario del sitio web**: Son a partes (como Clientes y Proveedores) de su Empresa. 

Ejemplo de roles de usuario del sitio web son Cliente y Proveedores.

¿Cómo comprobar si el rol es para el usuario del sistema o el usuario del sitio web?

En el maestro de roles, si se marca el campo "Acceso de escritorio", ese rol es para el usuario del sistema. Si el campo Acceso a escritorio está desactivado, ese rol es para el usuario del sitio web.

<img alt="Role Desk Permission" class="screenshot" src="{{docs_base_url}}/assets/img/articles/role-deskperm.png">
