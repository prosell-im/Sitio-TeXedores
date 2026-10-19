"""Vista previa expandible para PDFs en fichas oficiales y de preprints.

La ruta recibida es una URL relativa a la ficha generada, por ejemplo:
    ../../archivos_preprints/pap-tex-1-v1.pdf

No busca archivos antiguos en docs/libros: el catálogo proporciona la ruta.
"""

from html import escape


def bloque_pdf(url_pdf: str, mostrar_botones: bool = True) -> str:
    """Construye botones y un visor PDF dentro de un desplegable nativo.

    mostrar_botones=False sirve para Preprints, que ya tiene su botón Ver PDF.
    """
    if not url_pdf:
        return '<p class="pdf-mostrador__vacio">PDF no disponible.</p>'

    url = escape(url_pdf, quote=True)
    botones = ""
    if mostrar_botones:
        botones = f'''
  <div class="pdf-mostrador__acciones">
    <a href="{url}" class="md-button md-button--primary" target="_blank" rel="noopener noreferrer">Abrir PDF</a>
    <a href="{url}" class="md-button preprint-secondary-button" download>Descargar PDF</a>
  </div>'''

    return f'''<div class="pdf-mostrador">
{botones}
  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="{url}" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="{url}" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
      </object>
    </div>
  </details>
</div>'''
