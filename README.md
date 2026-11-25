# TeXedores

Sitio editorial del **Instituto de Matemáticas, UNAM**, construido con MkDocs Material.
Reúne el catálogo de **publicaciones oficiales** y el de **preprints**.

## Entorno de trabajo

Con Python instalado, desde la raíz del repositorio:

```powershell
pip install -r requirements.txt
mkdocs serve
```

La vista local suele estar en `http://127.0.0.1:8000/`.

## Actualizar catálogos

Tras modificar los CSV correspondientes, ejecutar en este orden:

```powershell
python tools/catalogo_qr/crea_catalogo_oficial.py
python tools/catalogo_qr/crea_preprints.py
python tools/catalogo_qr/crea_paginas_oficiales.py
python tools/catalogo_qr/crea_paginas_preprints.py
mkdocs build
python tools/verifica_enlaces.py
```

**Importante:** las páginas de `docs/catalogo.md`, `docs/preprints.md`,
`docs/publicaciones/` y `docs/preprints/` se generan automáticamente.
Editar sus contenidos a mano puede hacer que los cambios se pierdan en la siguiente actualización.

- Los PDF **oficiales** se referencian en `tools/catalogo_qr/pdfs_oficiales.csv`.
- Los PDF **preprints** se referencian en `tools/catalogo_qr/pdfs_preprints.csv`.
- La disponibilidad de ejemplares impresos se indica en `tools/catalogo_qr/disponibilidad_impresa.csv`.
- Las ediciones oficiales se registran en `tools/catalogo_qr/metadatos_ediciones_oficiales.csv`.
- Los preprints ya **no manejan historial de versiones**.
- Un preprint sin edición oficial no se considera perteneciente a una colección editorial.

Para examinar fichas antiguas de preprints:

```powershell
python tools/catalogo_qr/limpia_preprints_obsoletos.py
```

El modo `--eliminar` debe ejecutarse solo tras revisar la lista mostrada por el comando sin argumentos.

## Estructura principal

- `mkdocs.yml`: navegación, tema y hojas de estilo.
- `docs/`: contenido fuente, catálogos y archivos consultables.
- `docs/stylesheets/`: personalizaciones visuales.
- `docs/js/`: navegación, pestañas y búsqueda.
- `docs/overrides/`: plantilla de encabezado, pestañas y pie de página.
- `tools/catalogo_qr/`: bases de datos CSV y generadores.
- `site/`: archivos HTML de salida. **No editarlos manualmente**; volver a construir con `mkdocs build`.

## Antes de publicar

Comprobar la navegación superior y móvil, filtros, enlaces entre fichas,
metadatos, descarga y vista previa de PDF; después ejecutar `mkdocs build`.
Si el despliegue depende de `site/`, incluir también los archivos regenerados en el commit.
