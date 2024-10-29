CREATE_ONE_PAGE = """
    Crea una one page completa {lang}, usa {technologies} con un diseño moderno. Se trata de un {description} ubicado en {location}, con la empresa {company_name}.

    Incluye: Header, {sections} y un pie de página simple con el año actual. No olvides resetear los estilos del navegador con normalize o reset.css, y debes importarlo antes de cualquier otro CSS. Si el pie de pagina tiene una etiqueta p, asegurate que tenga margin-bottom: 0, para que no quede espacio extra.

    Para el header, intenta usar la misma estructura de su navbar, para que sea 100% responsive. Usa imágenes de relleno usando esta URL: https://placehold.co/200x200, cambia los valores de 200x200 por la resolución que creas conveniente.

    La página debe ser 100% responsive, usa grid o flexbox y recuerda usar espaciados (padding y margin) correctamente para que los elementos no queden pegados en mobile, además de definir bien las separaciones entre secciones.

    Intenta jugar con los colores para crear contrastes entre cada sección, por ejemplo, si una sección es blanca, la próxima debe ser del color primario. Nunca uses más de dos colores para definir secciones.

    Los títulos deben estar en bold y usar fuentes de Google Fonts, preferiblemente Montserrat o Roboto. Todo título debe tener margin-bottom: 2rem y margin-top: 1rem al menos. Los h3 siempre deben tener un margin-top: 1rem si tienen una imagen anterior.

    Cuando uses grid, no uses márgenes porque puedes romper la estructura de la grid, usa padding en su lugar.

    Usa los colores: {colors}. No expliques nada, solo proporciona el código sin ningún tipo de descripción adicional ni comentario.
    Si el header tiene un color medio o oscuro, asegurate de usar la clase correcta para que los items del menu sean blanco.
"""
