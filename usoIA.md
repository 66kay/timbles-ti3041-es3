# Uso de IA

# Consulta 1 – Entorno y nuevo repositorio

**Prompt:** Entender el repositorio anterior de mi prueba y entender el punto hacia el que vamos, me ayudaras paso a paso como hacer las cosas para entender y me explicaras todo antes de darme una respuesta o modificar algo

**Respuesta:** Reviso el PDF y mi repo de la ES2. Me dio los comandos para copiar el proyecto a una carpeta nueva, crear el venv, instalar Django, migrar, crear el .gitignore y subirlo al repo nuevo.

# Consulta 2 – CRUD desde la web

**Prompt:** Todo lenguaje o codigo que me des me debes explicar el funcionamiento completo y la finalidad de la integracion

**Respuesta:** Me dio el ProductoForm y las vistas crear, editar y eliminar con su ruta cada una. Tuve errores porque no guarde forms.py y se borro el import de Producto, lo corregimos.

# Consulta 3 – Diseno del front (formularios y panel de contacto)

**Prompt:** Quiero que rehagas el front end entendiendo la logica del proyecto para que quede visualmente mejor que antes pero sin que sea generica

**Respuesta:** Hizo los templates del formulario, la confirmacion para eliminar y un panel de contacto con WhatsApp, usando los colores de la tienda. No se veia por el cache del CSS y lo arreglo con ?v= en el link.

# Consulta 4 – Seguridad del CRUD

**Prompt:** Quiero que haya algun tipo de seguridad para que no se acceda directamente y se pueda modificar, por ende me diras exactamente como implementarlo yo

**Respuesta:** Oculto los botones si no soy admin y me explico que agregara @staff_member_required a crear, editar y eliminar. Sin sesion ahora redirige al login.

# Consulta 5 – Reportes con ORM

**Prompt:** Necesito que me indiques paso a paso como agregar el bloque de codigo para que me funcione el ORM

**Respuesta:** Reporte 1 con annotate (Count, Avg, Sum) por categoria y reporte 2 con filter(stock__lte=5) y order_by. Yo agregue las vistas y rutas, la IA los templates y el menu.

# Consulta 6 – Clientes, ModelForm y sesiones

**Prompt:** Me hace falta terminar el apartado de clientes con el form y sesiones para que todo quede bien configurado, ya me dio error anteriormente al intentar anadirlo directamente yo, por ende me indicaras paso a paso como agregarlo y como funcionaria

**Respuesta:** Modelo ConsultaCliente, su migracion y registro en admin, ConsultaForm con validacion de largo minimo, vista contacto y contador de visitas con request.session. Puse mal la ruta y borre vistas sin querer, la IA las recupero del commit anterior.
