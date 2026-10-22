"""Detecta fichas generadas de preprints que ya no están en preprints.json.

Por defecto solo muestra las candidatas. Usar --eliminar para borrarlas tras
revisar con Git los cambios. Nunca borra archivos que no parezcan generados.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eliminar', action='store_true', help='Eliminar candidatas comprobadas')
    args = parser.parse_args()

    vigentes = {str(x['id_preprint']) for x in json.loads(
        (DOCS / 'data/preprints.json').read_text(encoding='utf-8'))}
    carpeta = DOCS / 'preprints'
    candidatas = []
    for archivo in sorted(carpeta.glob('*.md')):
        if archivo.stem in vigentes:
            continue
        contenido = archivo.read_text(encoding='utf-8')
        if ('preprint-detail-hero' in contenido and
                ('Preprint' in contenido or 'preprint' in contenido)):
            candidatas.append(archivo)
        else:
            print(f'NO se toca archivo que no parece generado: {archivo.name}')

    for ruta in candidatas:
        print(('Eliminando: ' if args.eliminar else 'Candidata: ') + str(ruta.relative_to(ROOT)))
        if args.eliminar:
            ruta.unlink()
    if not args.eliminar and candidatas:
        print('Revisa la lista. Para eliminar las fichas obsoletas, ejecuta el script con --eliminar.')
    print(f'Fichas obsoletas detectadas: {len(candidatas)}')

if __name__ == '__main__':
    main()
