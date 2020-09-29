<!-- add-breadcrumbs -->
# Managing Perm Level in Permission Manager

Perm Level es una forma de reducir la cantidad de información visible o modificable en un DocType específico para ciertos grupos de usuarios. Mientras que puede definir la visibilidad o la posibilidad de cambios para cada DocType personalizando la Regla de permisos específica de DocType, con el Nivel de permiso puede cambiarlos para Secciones o Campos específicos.

En cada documento, puede agrupar campos por "niveles". Cada grupo de campos o grupo de campos se indica con un número único (0, 1, 2, 3, etc.). Se puede aplicar un conjunto separado de reglas de permisos a cada grupo de campos. Por defecto, todos los campos son de nivel 0.

El nivel de permiso (forma abreviada de nivel de permiso) para un campo se puede definir en el [Personalizar formulario](/docs/user/manual/en/customize-erpnext/customize-form.html).

<img alt="Campo de nivel permanente" class="screenshot" src="{{docs_base_url}}/assets/img/articles/perm-level-1.gif">

Si necesita asignar diferentes permisos de un campo en particular a diferentes usuarios, puede lograrlo a través de Perm Level. Consideremos un ejemplo para una mejor comprensión.

La nota de entrega es accesible tanto para Stock Manager como para Stock User. No desea que el usuario de existencias acceda al campo relacionado con la cantidad en la nota de entrega, pero otro campo debe estar visible al igual que el administrador de existencias.

Para todos los campos relacionados, que no deberían verse, puede establecer el Nivel de permanente como (digamos) 2.

Para los gerentes de stock, tendrán permiso en los campos de la nota de entrega con Perm Nivel 2, mientras que un usuario de existencias no tendrá ningún permiso en el nivel de permanente 2 para la nota de entrega, porque su función no ha sido asignada con una regla que les permita leer o leer. escriba en el campo con Nivel de permanente de 2, como se muestra a continuación.

<img alt="Regla del nivel de permanente" class="screenshot" src="{{docs_base_url}}/assets/img/articles/perm-level-2.png">

Teniendo en cuenta el mismo escenario, si desea que un usuario de stock acceda a un campo en el nivel de permanente 2, pero no desea dar permiso para editarlo, se le asignará el permiso al usuario de stock para que solo pueda leer en el nivel de permanente 2, pero no para escribir / editar.

<img alt="Perm Level Rule 2" class="screenshot" src="{{docs_base_url}}/assets/img/articles/perm-level-3.png">

Los niveles de permanente (1, 2, 3 o 2, 1, 3 o 3,2,1) no necesitan estar en ningún orden en particular. No implican jerarquía. El nivel de permanente se utiliza principalmente para agrupar un número de campos y luego asignar permisos a los roles para ese grupo. Por lo tanto, puede establecer cualquier nivel de permiso para un elemento y luego configurar el permiso para él.

Si desea cambiar los permisos para todos los campos de una sección, simplemente puede cambiar el nivel de permiso para el campo de la sección y se aplicará a todos los campos de la sección.

<!-- markdown -->
