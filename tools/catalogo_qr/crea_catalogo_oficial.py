"""Genera docs/data/catalogo.json con las fuentes actuales de TeXedores.

Usa una lista independiente de PDF oficiales; no modifica preprints.json ni los PDF.
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
pdfs_oficiales = leer_csv('pdfs_oficiales.csv')

# Los años de las ediciones se usan en el filtro de búsqueda avanzada.
# Los campos pueden estar vacíos; no se inventan fechas.
metadatos = leer_csv('metadatos_ediciones_oficiales.csv')
if not {'id_libro', 'anio'}.issubset(metadatos.columns):
    raise ValueError('metadatos_ediciones_oficiales.csv debe contener id_libro y anio')
anios_por_libro = (
    metadatos.assign(anio=metadatos['anio'].str.strip())
    .loc[lambda t: t['anio'].str.fullmatch(r"\d{4}")]
    .groupby('id_libro')['anio']
    .apply(lambda valores: sorted(set(valores)))
    .to_dict()
)

# Incorporamos también datos bibliográficos al índice para permitir búsquedas
# por ISBN, editorial y edición. Los valores vacíos se mantienen vacíos.
campos_indice = ('isbn_libro', 'isbn_col', 'editorial', 'edicion')
datos_bibliograficos = {}
for identificador, filas in metadatos.groupby('id_libro'):
    datos_bibliograficos[identificador] = {
        campo: ' '.join(dict.fromkeys(
            valor.strip() for valor in filas[campo].tolist() if valor.strip()
        )) if campo in metadatos.columns else ''
        for campo in campos_indice
    }

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

# La ruta del PDF oficial se decide explícitamente y NO depende de versiones.csv.
# Aunque mañana aparezca otro preprint con una versión nueva, esta tabla
# conserva el PDF oficial hasta que alguien lo cambie expresamente.
columnas_pdf = {'id_publicacion', 'pdf'}
if not columnas_pdf.issubset(pdfs_oficiales.columns):
    raise ValueError('pdfs_oficiales.csv necesita las columnas id_publicacion y pdf')

if pdfs_oficiales['id_publicacion'].duplicated().any():
    raise ValueError('Hay identificadores duplicados en pdfs_oficiales.csv')

pdf_por_libro = pdfs_oficiales.set_index('id_publicacion')['pdf'].to_dict()

# Evitamos datos que podrían quedar desactualizados silenciosamente.
ids_libros = set(libros['id_preprint'])
ids_pdfs = set(pdf_por_libro)
faltantes = ids_libros - ids_pdfs
if faltantes:
    raise ValueError('Faltan PDF oficiales para: ' + ', '.join(sorted(faltantes)))
sobrantes = ids_pdfs - ids_libros
if sobrantes:
    print('Aviso: hay PDF oficiales sin registro de publicación: ' + ', '.join(sorted(sobrantes)))

catalogo = []
for libro in libros.to_dict(orient='records'):
    identificador = libro['id_preprint']
    # Ruta relativa a docs/, por ejemplo: archivos_preprints/pap-tex-1-v1.pdf
    ruta_relativa = pdf_por_libro[identificador].replace('\\', '/').strip()
    if not ruta_relativa.lower().endswith('.pdf'):
        raise ValueError(f'El archivo oficial debe ser un PDF ({identificador}): {ruta_relativa!r}')
    if ruta_relativa.startswith('/') or ':' in ruta_relativa:
        raise ValueError(f'Ruta PDF no permitida para {identificador}: {ruta_relativa!r}')

    ruta_pdf = os.path.realpath(os.path.join(DOCS_DIR, ruta_relativa))
    docs_real = os.path.realpath(DOCS_DIR)
    if os.path.commonpath([docs_real, ruta_pdf]) != docs_real:
        raise ValueError(f'El PDF debe estar dentro de docs/ ({identificador}): {ruta_relativa!r}')
    if not os.path.isfile(ruta_pdf):
        raise FileNotFoundError(f'No existe el PDF oficial de {identificador}: {ruta_pdf}')

    catalogo.append({
        'id': identificador,
        'titulo': libro['titulo'],
        'coleccion': libro['coleccion'],
        'serie': libro['serie'],
        'num_serie': libro['num_serie'],
        'portada': libro['portada'],
        'autores': autores_por_libro.get(identificador, []),
        'resumen': resumen_por_libro.get(identificador, ''),
        'anios_edicion': anios_por_libro.get(identificador, []),
        **datos_bibliograficos.get(identificador, {}),
        # Ruta fija, definida en pdfs_oficiales.csv.
        'pdf': ruta_relativa,
    })

os.makedirs(os.path.join(DOCS_DIR, 'data'), exist_ok=True)
salida = os.path.join(DOCS_DIR, 'data', 'catalogo.json')
with open(salida, 'w', encoding='utf-8') as archivo:
    json.dump(catalogo, archivo, ensure_ascii=False, indent=2)

print(f'Catálogo oficial generado: {len(catalogo)} registros')
print(f'Archivo: {salida}')
