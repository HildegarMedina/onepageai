CREATE_ONE_PAGE = """
    Crea una one page en {lang} utilizando HTML5, CSS3, Javascript y Bootstrap 5, diseño moderno. Solo genera un solo código html con todo junto. La página es para {company_name}, cuya descripción breve es: {description} {location}. 

    **Usa los CDN de Boostrap**:
    - **CSS**: https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    - **JS**: https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js

    **Estructura la página con:**:
    - **Header**: Usa el diseño de navbar de bootstrap para asegurar que sea 100% responsive.
    - **Secciones**: Incluye las secciones: {sections}.
    - **Footer**: incluye un pie de página con el año actual, con el fondo: #1d1d1d y una etiqueta `p`, con `margin-bottom: 0` para evitar espacio extra.

    **Colores**:
    - **Color Primario**: {primary_color}. Uso: Header, Navbar, Botones, enlaces principales.
    - **Color Secundario**: {secondary_color}. Uso: Elementos destacados, botones secundarios.
    - **Color de Fondo**: {background_color}. Uso: Fondo general de la página.

    **Instrucciones adicionales**:
    - **Estilos globales**: Importa normalize.css antes de cualquier otro CSS para restablecer estilos.
    - **Imágenes**: Usa imágenes de relleno de https://placehold.co/{with}x{height} cambiar los valores de {with} y {height} para adaptarse a cada sección que necesites, ejemplo: para un banner, podrías usar https://placehold.co/1200x400. Cuando uses imágenes para productos o similares, asegúrate de usar  w-100 para asegurarte de que la imagen sea 100% responsiva.
    - **Estilos y Layout**: Aplica un diseño 100% responsive usando la grid de bootstrap. Asegúrate de que los elementos tengan espacio adecuado (padding y margin) para evitar que se vean demasiado juntos en móvil. Evita márgenes, usa padding en su lugar. Para algunas secciones que no sean (contacto, productos o servicios) intenta usar el fondo del color secundario, para generar un buen contraste.
    - **Tipografía**: Usa Roboto de Google Fonts. Para los títulos aplica `font-weight: bold`, con `margin-bottom: 2rem` y `margin-top: 1rem` para separar las secciones. Los `heading` que siguen a una imagen deben tener `margin-top: 1rem`.
    - **Header oscuro**: Si el header tiene un fondo oscuro, aplica una clase para que el menú sea de color blanco.
    - **Formularios**: Si se te pide alguna sección contacto o similar, crea allí formularios, y dale estilos también.
    - **Banners**: Si se te pide un banner, asegúrate de que tenga un botón con un enlace, y que todo el fondo del banner tenga una imágen de fondo, además de agregar una cubierta semi oscura para generar un buen contraste entre el texto y la imagen de fondo. Recuerda usar z-index para el titulo, boton, y descripción que están en el banner para que queden encima de la imágen.
    - **Productos**: Si se te pide una sección de productos, asegúrate de que cada producto tenga un título, una descripción y un precio (Con color verde). Usa un diseño de tarjeta de Bootstrap para mostrar los productos.

    Proporciona solo el código sin comentarios adicionales ni explicaciones.
"""
