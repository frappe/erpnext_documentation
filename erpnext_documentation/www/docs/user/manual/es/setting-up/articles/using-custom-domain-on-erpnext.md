<!-- add-breadcrumbs -->
# Uso de dominio personalizado en ERPNext

<!-- markdown -->

Si se ha suscrito a alguno de los planes en [ERPNext](https://erpnext.com), puede hacernos servir su sitio en su dominio personalizado (for example at http://example.com). Esto permite que su sitio web se publique en un dominio personalizado.

Para habilitar esta función, primero deberá editar la configuración de DNS de su dominio de la siguiente manera.

- Crea un registro CNAME para un subdominio (www en la mayoría de los casos) a {youraccountname}.erpnext.com
- Si desea servir el sitio web en un dominio simple (ie. http://example.com), establecer una redirección de URL a http://www.example.com y no un registro CNAME. En este caso, hacer un registro CNAME puede tener consecuencias inesperadas, incluido que ya no pueda recibir correos electrónicos.

Una vez que haya configurado los registros DNS, deberá generar un ticket de soporte enviando un correo electrónico a support@erpnext.com y lo tomaremos desde allí.

**Nota**: No admitimos HTTPS en dominios personalizados. HTTPS permite el cifrado de extremo a extremo (desde su navegador hasta nuestro servidor). Aunque no es fundamental para el sitio web, recomendamos encarecidamente no utilizar la aplicación ERPNext en un protocolo no cifrado. Para estar seguro, utilice siempre el ERP en su dirección erpnext.com.

