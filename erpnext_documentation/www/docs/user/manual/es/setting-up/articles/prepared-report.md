<!-- add-breadcrumbs -->
# Uso del informe preparado

Muchas veces, al generar un informe que trata con un gran volumen de datos, por ejemplo, un informe GL para todo el año, puede terminar recibiendo el siguiente mensaje de error: ** Solicitud agotada **. Esto ocurre porque hay una gran cantidad de datos para procesar y presentar en la página del informe, pero no hay suficientes recursos del servidor, por lo que se agota el tiempo de espera.

Para un mejor procesamiento de dichos informes, ERPNext ofrece informes preparados (desde v11). Cuando un informe se establece como Informe preparado, se genera a través de un [trabajo de fondo](https://frappe.io/docs/user/en/guides/app-development/running-background-jobs), y una vez que esté listo, estará disponible para que los usuarios lo vean.

## Pasos para configurar informes preparados

1. Ir a [Role Permission for Page and Report](/docs/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report).
1. En el campo 'Establecer función para', seleccione ** Informe **.
1. En el campo 'Informe', seleccione el informe para el que desea habilitar / deshabilitar el informe preparado.
1. Utilice la casilla de verificación ** Desactivar informe preparado ** para activar / desactivar el informe preparado. Si la opción está marcada, la opción de informe preparado se desactivará para el informe seleccionado.
1. Haga clic en ** Actualizar **.

<img alt="Configurar informe preparado" class="screenshot" src="{{docs_base_url}}/assets/img/articles/set-prep-report.gif">

## Cómo utilizar un informe preparado

1. Abra dicho informe (por ejemplo, Libro mayor) y aplique todos los filtros necesarios.
1. Si la opción de informe preparado está habilitada para ese informe, verá un botón ** Generar informe **. Haga clic en el mismo.
    <img alt="Generar informe preparado" class="screenshot" src="{{docs_base_url}}/assets/img/articles/prepared-report-generate.png">
1. Verá una notificación en la parte inferior derecha de la pantalla que dice "Informe iniciado. Puede rastrear su estado _aquí_"
    <img alt="Informe preparado iniciado" class="screenshot" src="{{docs_base_url}}/assets/img/articles/prepared-report-bg.png">
1. Puede esperar en dicha pantalla o hacer clic en _aquí_ en el mensaje anterior para abrir la página del informe. Esto abrirá una nueva página para el informe:
    <img alt="Informe preparado en cola" class="screenshot" src="{{docs_base_url}}/assets/img/articles/prepared-report-queued.png">
    Como puede ver, la página del informe tiene el estado "En cola". Una vez que el informe esté listo, verá un botón ** Mostrar informe ** en el que puede hacer clic para ver el informe:
     <img alt="Informe preparado iniciado" class="screenshot" src="{{docs_base_url}}/assets/img/articles/prepared-report-page.png">
1. Dado que el Informe preparado también es un tipo de documento, para ver la lista de informes preparados, puede utilizar el [Administrador de permisos de roles](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions) Conceder acceso a los mismos.
