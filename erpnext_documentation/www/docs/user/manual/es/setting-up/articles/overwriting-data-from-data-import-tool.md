<!-- add-breadcrumbs -->
# Sobrescribir datos de la herramienta de importación de datos

La herramienta de importación de datos permite importar documentos (como clientes, proveedores, pedidos, facturas, etc.) desde un archivo Excel / CSV a ERPNext. La misma herramienta también se puede utilizar para sobrescribir valores en los documentos existentes.

La sobrescritura de datos de la herramienta de importación de datos solo funciona para las transacciones guardadas y no para las enviadas.

Supongamos que no hay. de elementos para los que necesitamos sobrescribir Grupo de elementos. A continuación se muestran los pasos para sobrescribir grupos de artículos para artículos existentes.


### Paso 1: Descargar la plantilla

La plantilla utilizada para sobrescribir datos será la misma que se utilizó para importar elementos nuevos. Por lo tanto, primero debe descargar la plantilla.

> Inicio > Configuración > Datos > Importar/Exportar Datos

Dado que los elementos que se sobrescribirán ya estarán disponibles en el sistema, mientras descarga la plantilla, haga clic en "Descargar con datos" para obtener todos los elementos existentes en la plantilla.

<img alt="Download Template" class="screenshot" src="{{docs_base_url}}/assets/img/articles/overwrite-1.gif">
    
### Paso 2: Preparar Data

Ingrese el nuevo valor en la columna Grupo de artículos para un artículo. Dado que el grupo de artículos es un maestro en sí mismo, asegúrese de que el grupo de artículos ingresado en el archivo de hoja de cálculo ya esté agregado en el maestro del grupo de artículos.

<img alt="Update Values" class="screenshot" src="{{docs_base_url}}/assets/img/articles/overwrite-2.png">

Dado que solo estamos sobrescribiendo el Grupo de artículos, solo las siguientes columnas serán obligatorias:

1. Columna A (ya que tiene valores principales de la plantilla)
1. Nombre (columna B)
1. Grupo de artículos

Las columnas de otros campos que no tendrán ningún impacto se pueden eliminar, incluso si son obligatorias. Esto es aplicable solo para sobrescribir y no al importar nuevos registros.

### Paso 3: Examinar plantilla

Después de actualizar los grupos de elementos en la hoja de cálculo, vuelva a la herramienta de importación de datos en ERPNext. Busque y seleccione el archivo / plantilla que tiene datos para sobrescribir.

<img alt="Browse template" class="screenshot" src="{{docs_base_url}}/assets/img/articles/overwrite-3.gif">

### Paso 4: Subir

Al hacer clic en Importar, se sobrescribirá el grupo de elementos.

<img alt="Upload" class="screenshot" src="{{docs_base_url}}/assets/img/articles/overwrite-4.png">

Si falla la validación de valores, indicará el número de fila. de la hoja de cálculo cuya validación falló y necesita corrección. En ese caso, debe corregir el valor en esa fila de la hoja de cálculo y luego importar el mismo archivo nuevamente. Si la validación falla incluso para una fila, ninguno de los registros se importa / sobrescribe.

<!-- markdown -->
