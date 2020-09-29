<!-- add-breadcrumbs -->
# Administrar maestros de estructura de árbol

Algunos de los maestros de ERPNext se mantienen en estructura de árbol. Los maestros estructurados en árbol le permiten establecer maestros principales y maestros secundarios en esos padres. La configuración de esta estructura le permite crear un informe inteligente y realizar un seguimiento del crecimiento en cada nivel de la jerarquía.

A continuación se muestra la lista parcial de maestros que se mantienen en la estructura de árbol.

* Catálogo de cuentas

* Cuadro de centros de costos

* Grupo de clientes

* Territorio

* Persona de ventas

* Grupo de artículos

Los siguientes son los pasos para administrar y crear un registro en el maestro estructurado en árbol. Consideremos Territory master para entender la gestión de árboles maestros.

### Paso 1 : Ir al maestro

`Ventas > Configuración > Territorio`

### Paso 2 : Territorio principal

<img alt="Default Territories" class="screenshot" src="{{docs_base_url}}/assets/img/articles/territory-2.png">

Cuando haga clic en Territorio principal, verá la opción para agregar territorio secundario debajo de él. Todos los grupos de territorios predeterminados se enumerarán en el grupo principal llamado "Todos los territorios". Puede agregar más grupos de territorios principales o secundarios debajo de él.

### Paso 3: Agregar nuevo territorio

Al hacer clic en Agregar hijo, un cuadro de diálogo proporcionará dos campos.

**Nombre del grupo de territorio**

El territorio se guardará con el nombre del territorio proporcionado aquí.

**Nodo de grupo**

Si Nodo de grupo seleccionado como Sí, entonces este Territorio se creará como Padre, lo que significa que puede crear más sub-territorios debajo de él. Si selecciona No, se convertirá en un Territorio hijo que podrá seleccionar en otros maestros.

<div class="well">Solo se pueden seleccionar grupos de territorios secundarios en otros maestros y transacciones.</div>

<img alt="Territorios predeterminados" class="screenshot" src="{{docs_base_url}}/assets/img/articles/territory-1.gif">

A continuación se muestra cómo se incluirán los Territorios secundarios en un Territorio principal.

<img alt="Agregar nuevos territorios" class="screenshot" src="{{docs_base_url}}/assets/img/articles/territory-3.png">

Siguiendo estos pasos, también puede administrar otros árboles maestros en ERPNext.

<!-- markdown -->
