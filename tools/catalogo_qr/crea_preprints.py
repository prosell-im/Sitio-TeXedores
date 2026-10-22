"""Genera preprints.json sin historial de versiones.

Los preprints solo pertenecen a una colección/serie si ya existe publicación
oficial con el mismo ID. El PDF se controla por pdfs_preprints.csv.
"""
import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOCS = BASE.parent.parent / "docs"


def tabla(nombre):
    with (BASE / nombre).open(encoding="utf-8-sig", newline="") as archivo:
        return [{k.strip(): (v or "").strip() for k,v in fila.items() if k}
                for fila in csv.DictReader(archivo)]


def registros_unicos(filas, campo, nombre):
    registros = {}
    for fila in filas:
        ident = fila[campo]
        if not ident or ident in registros:
            raise ValueError(f"Identificador vacío o duplicado en {nombre}: {ident!r}")
        registros[ident] = fila
    return registros


def main():
    datos = tabla("preprints.csv")
    autores = registros_unicos(tabla("autores.csv"), "id_autor", "autores.csv")
    relaciones = tabla("preprints_autores.csv")
    resumenes = {r["id_preprint"]: r["resumen"] for r in tabla("resumenes.csv")}
    pdfs = registros_unicos(tabla("pdfs_preprints.csv"), "id_preprint", "pdfs_preprints.csv")
    oficiales_path = DOCS / "data" / "catalogo.json"
    if not oficiales_path.is_file():
        raise FileNotFoundError("Primero ejecuta crea_catalogo_oficial.py")
    oficiales = {str(libro["id"]): libro
                 for libro in json.loads(oficiales_path.read_text(encoding="utf-8"))}
    autores_por_id = {}
    for r in relaciones:
        if r["id_autor"] not in autores:
            raise ValueError("Autor inexistente: " + r["id_autor"])
        a = autores[r["id_autor"]]
        nombre = (a["nombres"] + " " + a["apellidos"]).strip()
        autores_por_id.setdefault(r["id_preprint"], []).append(nombre)

    resultado = []
    ids = set()
    for fila in datos:
        ident = fila["id_preprint"]
        if ident in ids:
            raise ValueError("Preprint duplicado: " + ident)
        ids.add(ident)
        pdf_info = pdfs.get(ident, {})
        pdf = pdf_info.get("pdf", "").replace("\\", "/")
        if pdf:
            if not pdf.startswith("archivos_preprints/") or not pdf.lower().endswith(".pdf"):
                raise ValueError(f"Ruta de PDF inválida para {ident}: {pdf}")
            ruta = (DOCS / pdf).resolve()
            if not ruta.is_relative_to(DOCS.resolve()) or not ruta.is_file():
                raise FileNotFoundError(f"PDF inexistente para {ident}: {pdf}")
        oficial = oficiales.get(ident)
        resultado.append({
            "id_preprint": ident,
            "titulo": fila["titulo"],
            "coleccion": (oficial.get("coleccion", "") if oficial else ""),
            "serie": (oficial.get("serie", "") if oficial else ""),
            "num_serie": (oficial.get("num_serie", "") if oficial else ""),
            "portada": fila.get("portada", ""),
            "resumen": resumenes.get(ident, ""),
            "autores": autores_por_id.get(ident, []),
            "pdf": pdf,
            "fecha": pdf_info.get("fecha", ""),
            "oficial_disponible": oficial is not None,
        })
    salida = DOCS / "data" / "preprints.json"
    salida.parent.mkdir(exist_ok=True, parents=True)
    salida.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Preprints generados: {len(resultado)}; sin historial de versiones.")
    print(f"Preprints sin publicación oficial: {sum(not r['oficial_disponible'] for r in resultado)}")

if __name__ == "__main__":
    main()
