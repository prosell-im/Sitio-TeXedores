"""Genera docs/data/catalogo.json con las fuentes actuales de TeXedores.

No modifica preprints.json ni los PDFs existentes.
Ejecutar desde la raíz del repositorio:
    python tools/catalogo_qr/crea_catalogo_oficial.py
"""

import json
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', '..'))
DOCS_DIR = os.path.join(PROJECT_DIR, 'docs')


def leer_csv(nombre):
    ruta = os.path.join(BASE_DIR, nombre)
    tabla = pd.read_csv(ruta, dtype=str, keep_default_na=False)
    tabla.columns = tabla.columns.str.strip()
    for columna in tabla.columns:
        tabla[columna] = tabla[columna].str.strip()
    return tabla


# La base completa y los recursos recientes son el punto de partida.
libros = leer_csv('preprints_BD_completa.csv')
autores = leer_csv('autores.csv')
relaciones = leer_csv('preprints_autores.csv')
resumenes = leer_csv('resumenes.csv')
versiones = leer_csv('versiones.csv')

if libros['id_preprint'].duplicated().any():
    raise ValueError('Hay identificadores duplicados en preprints_BD_completa.csv')

autores['nombre_completo'] = (
    autores['nombres'] + ' ' + autores['apellidos']
).str.strip()

relaciones = relaciones.merge(
    autores[['id_autor', 'nombre_completo']],
    on='id_autor',
    how='left',
    validate='many_to_one',
)

if relaciones['nombre_completo'].isna().any():
    raise ValueError('Hay autores referenciados que no existen en autores.csv')

autores_por_libro = (
    relaciones.groupby('id_preprint', sort=False)['nombre_completo']
    .apply(list)
    .to_dict()
)
resumen_por_libro = resumenes.set_index('id_preprint')['resumen'].to_dict()

# Selecciona la versión con el número mayor solamente para encontrar el PDF.
# NO significa que sea una edición editorial.
versiones['numero_version'] = pd.to_numeric(
    versiones['version'], errors='coerce'
)
versiones_ordenadas = versiones.sort_values(
    ['id_preprint', 'numero_version'], na_position='first'
)
pdf_por_libro = (
    versiones_ordenadas.drop_duplicates('id_preprint', keep='last')
    .set_index('id_preprint')['archivo']
    .to_dict()
)

catalogo = []
for libro in libros.to_dict(orient='records'):
    identificador = libro['id_preprint']
    archivo_pdf = pdf_por_libro.get(identificador, '')
    if not archivo_pdf:
        raise ValueError(f'Falta el PDF del registro {identificador}')

    ruta_pdf = os.path.join(DOCS_DIR, 'archivos_preprints', archivo_pdf)
    if not os.path.isfile(ruta_pdf):
        raise FileNotFoundError(f'No existe el PDF: {ruta_pdf}')

    catalogo.append({
        'id': identificador,
        'titulo': libro['titulo'],
        'coleccion': libro['coleccion'],
        'serie': libro['serie'],
        'num_serie': libro['num_serie'],
        'portada': libro['portada'],
        'autores': autores_por_libro.get(identificador, []),
        'resumen': resumen_por_libro.get(identificador, ''),
        # Ruta relativa a docs/. Se actualizará cuando reorganicemos PDFs.
        'pdf': f'archivos_preprints/{archivo_pdf}',
    })

os.makedirs(os.path.join(DOCS_DIR, 'data'), exist_ok=True)
salida = os.path.join(DOCS_DIR, 'data', 'catalogo.json')
with open(salida, 'w', encoding='utf-8') as archivo:
    json.dump(catalogo, archivo, ensure_ascii=False, indent=2)

print(f'Catálogo oficial generado: {len(catalogo)} registros')
print(f'Archivo: {salida}')