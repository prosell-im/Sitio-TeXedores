"""Genera el catálogo y las fichas de publicaciones oficiales de TeXedores.

Entrada: docs/data/catalogo.json (creado con crea_catalogo_oficial.py).
Salidas: docs/catalogo.md y docs/publicaciones/<id>.md.

No modifica docs/preprints/, docs/data/preprints.json ni los PDF.
Ejecutar desde la raíz del repositorio:
    python tools/catalogo_qr/crea_paginas_oficiales.py
"""

import html
import csv
import json
import re
from pathlib import Path
from urllib.parse import quote
import sys

# Reutilizamos el visor PDF del directorio tools/.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mostrador_PDF import bloque_pdf

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR.parent.parent / "docs"
JSON_PATH = DOCS_DIR / "data" / "catalogo.json"
OUTPUT_DIR = DOCS_DIR / "publicaciones"
CATALOG_PATH = DOCS_DIR / "catalogo.md"
METADATA_PATH = BASE_DIR / "metadatos_ediciones_oficiales.csv"
PREPRINTS_JSON_PATH = DOCS_DIR / "data" / "preprints.json"


def texto(valor):
    """Escapa texto para usarlo sin riesgos dentro del HTML."""
    return html.escape(str(valor or ""), quote=True)


def resumen_html(valor):
    """Conserva solamente los saltos <br> de los resúmenes existentes."""
    contenido = texto(valor)
    return re.sub(r"&lt;br\s*/?&gt;", "<br>", contenido, flags=re.IGNORECASE)


def ruta_recurso(valor):
    """Codifica la ruta relativa que ya viene en el JSON."""
    return quote(str(valor), safe="/-_.")


def portada_html(libro, prefijo, clase):
    imagen = str(libro.get("portada", "") or "").strip()
    titulo = texto(libro["titulo"])
    identificador = texto(libro["id"])
    if imagen and (DOCS_DIR / "portadas_preprints" / imagen).is_file():
        return (
            f'<div class="{clase}">'
            f'<img src="{prefijo}portadas_preprints/{ruta_recurso(imagen)}" '
            f'alt="Portada de {titulo}" loading="lazy">'
            "</div>"
        )
    # Algunos registros pueden carecer de portada.
    return (
        f'<div class="{clase} preprint-detail-cover-placeholder">'
        f'<span>{identificador}</span><small>Publicación</small></div>'
    )


def validar_y_leer():
    if not JSON_PATH.is_file():
        raise FileNotFoundError(f"No se encontró {JSON_PATH}. Ejecuta primero crea_catalogo_oficial.py")
    libros = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(libros, list):
        raise ValueError("catalogo.json debe contener una lista de publicaciones")
    vistos = set()
    for libro in libros:
        identificador = str(libro.get("id", ""))
        if not re.fullmatch(r"[A-Za-z0-9_-]+", identificador):
            raise ValueError(f"Identificador inválido: {identificador!r}")
        if identificador in vistos:
            raise ValueError(f"Identificador duplicado: {identificador}")
        vistos.add(identificador)
        if not str(libro.get("titulo", "")).strip():
            raise ValueError(f"Falta el título de {identificador}")
        pdf = str(libro.get("pdf", "")).replace("\\", "/")
        if not pdf.startswith("archivos_preprints/") or not pdf.endswith(".pdf"):
            raise ValueError(f"Ruta PDF inesperada para {identificador}: {pdf}")
        archivo_pdf = (DOCS_DIR / pdf).resolve()
        if not archivo_pdf.is_relative_to(DOCS_DIR.resolve()) or not archivo_pdf.is_file():
            raise FileNotFoundError(f"No existe el PDF de {identificador}: {archivo_pdf}")
    return libros


def cargar_preprints_relacionados():
    """IDs que tienen una ficha de preprint con PDF disponible.

    Solo consultamos el JSON; no mezclamos ni sobrescribimos los PDF oficiales.
    """
    if not PREPRINTS_JSON_PATH.is_file():
        print("Aviso: no se encontró preprints.json; las fichas oficiales no mostrarán vínculos.")
        return set()
    registros = json.loads(PREPRINTS_JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(registros, list):
        raise ValueError("preprints.json debe contener una lista")
    return {
        str(preprint["id_preprint"])
        for preprint in registros
        if preprint.get("id_preprint") and preprint.get("pdf")
    }


def badges_disponibilidad(libro, preprints_relacionados):
    """Solo muestra las disponibilidades afirmativas, sin inventar existencias."""
    badges = []
    if libro.get("pdf"):
        badges.append('<span class="tex-disponibilidad__badge">PDF disponible</span>')
    if libro.get("impreso_disponible") is True:
        badges.append('<span class="tex-disponibilidad__badge">Impreso disponible</span>')
    if libro["id"] in preprints_relacionados:
        badges.append('<span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint disponible</span>')
    if not badges:
        return ""
    return '<div class="tex-disponibilidad" aria-label="Disponibilidad">' + ''.join(badges) + '</div>'


def cargar_ediciones():
    """Lee metadatos editoriales de un CSV independiente del catálogo y los PDF."""
    por_libro = {}
    if not METADATA_PATH.is_file():
        print(f"Advertencia: falta {METADATA_PATH}; las fichas mostrarán solo datos básicos.")
        return por_libro
    with METADATA_PATH.open(newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        if not lector.fieldnames or "id_libro" not in lector.fieldnames:
            raise ValueError("El archivo de metadatos necesita la columna id_libro")
        for fila in lector:
            limpia = {str(k).strip(): (v or "").strip() for k, v in fila.items() if k}
            ident = limpia.get("id_libro", "")
            if ident:
                por_libro.setdefault(ident, []).append(limpia)
    return por_libro


def fila_metadato(etiqueta, valor):
    valor = str(valor or "").strip()
    if not valor:
        return ""
    return f'<tr><th scope="row">{texto(etiqueta)}</th><td>{texto(valor)}</td></tr>'


def citar(libro, edicion):
    """Cita orientativa con datos comprobables, sin suponer edición ni año."""
    autores = ", ".join(str(a).strip() for a in libro.get("autores", []) if str(a).strip())
    anio = edicion.get("anio") or "s. f."
    partes = []
    if autores:
        partes.append(f"{texto(autores)}.")
    partes.append(f"({texto(anio)}).")
    partes.append(f"<em>{texto(libro['titulo'])}</em>.")
    if edicion.get("editorial"):
        partes.append(f"{texto(edicion['editorial'])}.")
    if edicion.get("edicion"):
        partes.append(f"Edición {texto(edicion['edicion'])}.")
    return " ".join(partes)


def generar_bibtex(libro, edicion):
    clave = re.sub(r"[^A-Za-z0-9:_-]", "-", edicion.get("id_edicion") or libro["id"])
    autores = " and ".join(str(a).strip() for a in libro.get("autores", []) if str(a).strip())
    campos = {
        "title": libro.get("titulo", ""),
        "author": autores,
        "year": edicion.get("anio", ""),
        "publisher": edicion.get("editorial", ""),
        "edition": edicion.get("edicion", ""),
        "isbn": edicion.get("isbn_libro", ""),
        "series": libro.get("serie", ""),
        "number": libro.get("num_serie", ""),
    }
    lineas = []
    for campo, valor in campos.items():
        valor = str(valor or "").replace("\r", " ").replace("\n", " ").strip()
        if valor:
            lineas.append(f"  {campo} = {{{valor}}}")
    return "@book{" + clave + ",\n" + ",\n".join(lineas) + "\n}"


def seccion_ediciones(libro, ediciones):
    """Muestra metadatos y citas por edición, sin relacionar esas ediciones con versiones PDF."""
    ident = texto(libro["id"])
    autor = ", ".join(str(a).strip() for a in libro.get("autores", []) if str(a).strip())

    if not ediciones:
        ediciones = [{}]

    def ordenar(fila):
        try:
            n = int(fila.get("edicion") or -1)
        except ValueError:
            n = -1
        return n, fila.get("anio", "")

    ediciones = sorted(ediciones, key=ordenar, reverse=True)
    botones = []
    paneles = []
    for i, ed in enumerate(ediciones):
        panel_id = f"oficial-edicion-{ident}-{i}"
        nombre = f"Edición {ed['edicion']}" if ed.get("edicion") else "Datos bibliográficos"
        botones.append(
            f'<button type="button" class="edition-button{" active" if i == 0 else ""}" '
            f'data-target="{panel_id}" aria-controls="{panel_id}" '
            f'aria-expanded="{"true" if i == 0 else "false"}">{texto(nombre)}</button>'
        )
        filas = "".join([
            fila_metadato("Autores", autor),
            fila_metadato("Colección", libro.get("coleccion")),
            fila_metadato("Serie", libro.get("serie")),
            fila_metadato("Número de serie", libro.get("num_serie")),
            fila_metadato("Tomo", ed.get("tomo")),
            fila_metadato("Año", ed.get("anio")),
            fila_metadato("Editorial", ed.get("editorial")),
            fila_metadato("Edición", ed.get("edicion")),
            fila_metadato("ISBN (colección)", ed.get("isbn_col")),
            fila_metadato("ISBN (libro)", ed.get("isbn_libro")),
            fila_metadato("Reimpresiones", ed.get("reimpresiones")),
        ])
        aviso = ""  # Los datos del catálogo se muestran tal como fueron proporcionados.
        cita = citar(libro, ed)
        bib = texto(generar_bibtex(libro, ed))
        paneles.append(f'''
<div class="edition-panel" id="{panel_id}"{' hidden' if i else ''}>
  <section class="libro-subseccion libro-metadatos">
    <h3>Metadatos</h3>
    {aviso}
    <div class="oficial-tabla-contenedor"><table><tbody>{filas}</tbody></table></div>
  </section>
  <section class="libro-subseccion libro-cita">
    <h3>Cómo citar</h3>
    <div class="citation-box">
      <blockquote id="oficial-cita-{ident}-{i}">{cita}</blockquote>
      <button type="button" class="citation-copy-button" data-copy-id="oficial-cita-{ident}-{i}" data-copy-type="text">Copiar cita</button>
    </div>
    <details class="oficial-bibtex">
      <summary>BibTeX</summary>
      <textarea readonly id="oficial-bibtex-{ident}-{i}" rows="9" class="verbatim">{bib}</textarea>
      <button type="button" class="bibtex-copy-button" data-copy-id="oficial-bibtex-{ident}-{i}" data-copy-type="value">Copiar BibTeX</button>
    </details>
  </section>
</div>''')

    return f'''
<section class="libro-seccion libro-ediciones" id="ediciones-{ident}">
  <h2>Ediciones disponibles</h2>
  <div class="edition-selector">
    <div class="edition-buttons" role="group" aria-label="Seleccionar edición">
      {''.join(botones)}
    </div>
    <div class="edition-content">{''.join(paneles)}</div>
  </div>
</section>'''


JS_FICHA = r'''
<script>
(() => {
  const area = document.querySelector(".oficial-detalle");
  if (!area) return;
  area.querySelectorAll(".edition-selector").forEach(selector => {
    const botones = selector.querySelectorAll(".edition-button");
    const paneles = selector.querySelectorAll(".edition-panel");
    botones.forEach(boton => boton.addEventListener("click", () => {
      botones.forEach(b => { b.classList.remove("active"); b.setAttribute("aria-expanded", "false"); });
      paneles.forEach(p => p.hidden = true);
      boton.classList.add("active");
      boton.setAttribute("aria-expanded", "true");
      const panel = area.querySelector("#" + boton.dataset.target);
      if (panel) panel.hidden = false;
    }));
  });
  area.querySelectorAll("[data-copy-id]").forEach(boton => {
    boton.addEventListener("click", async () => {
      const fuente = area.querySelector("#" + boton.dataset.copyId);
      if (!fuente) return;
      const valor = boton.dataset.copyType === "value" ? fuente.value : fuente.innerText;
      try {
        await navigator.clipboard.writeText(valor);
        const anterior = boton.textContent;
        boton.textContent = "Copiado";
        setTimeout(() => boton.textContent = anterior, 1500);
      } catch (err) {
        if (fuente.tagName === "TEXTAREA") { fuente.focus(); fuente.select(); }
        boton.textContent = "Selecciona y copia el texto";
      }
    });
  });
})();
</script>
'''


def ficha(libro, ediciones, preprints_relacionados):
    identificador = texto(libro["id"])
    titulo = texto(libro["titulo"])
    autores = " · ".join(texto(a) for a in libro.get("autores", []) if a)
    resumen = resumen_html(libro.get("resumen") or "Resumen no disponible.")
    pdf = "../../" + ruta_recurso(libro["pdf"])
    portada = portada_html(libro, "../../", "libro-hero-portada")
    visor_pdf = bloque_pdf(pdf)
    coleccion = texto(libro.get("coleccion") or "")
    serie = texto(libro.get("serie") or "")
    numero = texto(libro.get("num_serie") or "")
    ediciones_html = seccion_ediciones(libro, ediciones)
    disponibilidad = badges_disponibilidad(libro, preprints_relacionados)
    # Una ficha de preprint solo existe mientras haya cambios pendientes.
    # Su presencia en preprints.json es la condición para mostrar el enlace.
    seccion_preprint = ""
    if libro["id"] in preprints_relacionados:
        seccion_preprint = f'''
<section class="relacion-fichas" aria-label="Contenido relacionado">
  <div class="relacion-fichas__marco">
    <p class="relacion-fichas__etiqueta">Contenido relacionado</p>
    <div class="relacion-fichas__contenido">
      <div class="relacion-fichas__descripcion">
        <h2>Preprint relacionado</h2>
        <p>Esta obra tiene un preprint con cambios que todavía no se han
           incorporado a la publicación oficial. Puedes consultar esa
           versión por separado.</p>
      </div>
      <a class="md-button md-button--primary relacion-fichas__enlace"
         href="../../preprints/{identificador}/">
        Consultar preprint <span aria-hidden="true">→</span>
      </a>
    </div>
  </div>
</section>'''
    chips = "".join(
        f'<span class="chip">{valor}</span>'
        for valor in (coleccion, serie, ("Núm. " + numero if numero else ""))
        if valor
    )
    return f'''---
title: {json.dumps(libro['titulo'], ensure_ascii=False)}
---

<div class="oficial-detalle">
<section class="libro-hero">
  {portada}
  <div class="libro-hero-contenido">
    <p class="libro-eyebrow">Ficha bibliográfica · Publicación oficial</p>
    <h1 class="libro-titulo">{titulo}</h1>
    <p class="oficial-hero-autores">{autores}</p>
    <div class="chips">{chips}</div>
    {disponibilidad}
  </div>
</section>

<section class="libro-seccion libro-resumen">
  <h2>Resumen</h2>
  <p>{resumen}</p>
</section>

{ediciones_html}

<section class="libro-seccion libro-seccion-descargas oficial-pdf-seccion">
  <h2>Descargas</h2>
  <p>Abre, descarga o consulta el PDF de la publicación desde aquí.</p>
  {visor_pdf}
</section>

<div class="libro-navegacion">
  <a class="md-button md-button--primary" href="../../catalogo/">Volver al catálogo</a>
</div>

{seccion_preprint}
</div>
{JS_FICHA}
'''

def tarjeta(libro, preprints_relacionados):
    identificador = texto(libro["id"])
    titulo = texto(libro["titulo"])
    autores = " · ".join(texto(a) for a in libro.get("autores", []) if a)
    resumen = resumen_html(libro.get("resumen") or "Resumen no disponible.")
    pdf = "../" + ruta_recurso(libro["pdf"])
    portada = portada_html(libro, "../", "preprint-cover")
    coleccion = texto(libro.get("coleccion") or "Publicación")
    serie = texto(libro.get("serie") or "")
    disponibilidad = badges_disponibilidad(libro, preprints_relacionados)
    return f'''
<article class="preprint-card oficial-card">
  <div class="preprint-card-layout">
    {portada}
    <div class="preprint-card-main">
      <div class="preprint-card-top">
        <span class="preprint-id">{identificador}</span>
        <span class="preprint-date">{coleccion}{' · ' + serie if serie else ''}</span>
      </div>
      <div class="preprint-card-content">
        <h3 class="preprint-title"><a href="../publicaciones/{identificador}/">{titulo}</a></h3>
        <p class="preprint-authors">{autores}</p>
        <div class="preprint-summary-wrapper">
          <p class="preprint-summary preprint-summary-collapsed">{resumen}</p>
          <button type="button" class="preprint-summary-toggle">Ver más</button>
        </div>
      </div>
      <div class="preprint-card-footer">
        {disponibilidad}
        <div class="preprint-actions">
          <a href="../publicaciones/{identificador}/" class="md-button md-button--primary">Ver ficha</a>
          <a href="{pdf}" target="_blank" rel="noopener" class="md-button preprint-secondary-button">Ver PDF</a>
        </div>
      </div>
    </div>
  </div>
</article>'''


JS_CATALOGO = r'''
<script>
(() => {
  const pagina = document.querySelector(".oficiales-page");
  if (!pagina) return;
  const input = pagina.querySelector("#oficiales-search-input");
  const tarjetas = Array.from(pagina.querySelectorAll(".oficial-card"));
  const contador = pagina.querySelector("#oficiales-results-count");
  const vacio = pagina.querySelector("#oficiales-no-results");

  function normalizar(valor) {
    return String(valor).toLowerCase().normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "").trim();
  }
  function filtrar() {
    const consulta = normalizar(input.value);
    let visibles = 0;
    tarjetas.forEach(tarjeta => {
      const encontrado = normalizar(tarjeta.textContent).includes(consulta);
      tarjeta.hidden = !encontrado;
      if (encontrado) visibles++;
    });
    contador.textContent = visibles === 1 ?
      "1 publicación encontrada" : `${visibles} publicaciones encontradas`;
    vacio.hidden = visibles !== 0;
  }
  pagina.querySelectorAll(".preprint-summary-toggle").forEach(boton => {
    boton.addEventListener("click", () => {
      const resumen = boton.parentElement.querySelector(".preprint-summary");
      const cerrado = resumen.classList.toggle("preprint-summary-collapsed");
      boton.textContent = cerrado ? "Ver más" : "Ver menos";
    });
  });
  input.addEventListener("input", filtrar);
  filtrar();
})();
</script>
'''


def pagina_catalogo(libros, preprints_relacionados):
    tarjetas = "\n".join(tarjeta(l, preprints_relacionados) for l in libros)
    return f'''<div class="preprints-page oficiales-page">
  <section class="preprints-hero">
    <p class="preprints-eyebrow">Repositorio académico</p>
    <h1>Publicaciones oficiales</h1>
    <p class="preprints-lead">Consulta el catálogo de publicaciones del Instituto de Matemáticas.</p>
    <p class="preprints-description">Explora las obras, consulta sus fichas y visualiza los PDF disponibles.</p>
  </section>
  <section class="preprints-list">
    <div class="preprints-list-header"><div>
      <p class="preprints-section-label">Catálogo general</p>
      <h2>Explora nuestras publicaciones</h2>
    </div></div>
    <div class="preprints-search">
      <label for="oficiales-search-input" class="preprints-search-label">Buscar publicaciones</label>
      <div class="preprints-search-box">
        <input type="search" id="oficiales-search-input" placeholder="Buscar por título, autor, serie o identificador..." autocomplete="off">
      </div>
      <p id="oficiales-results-count" class="preprints-results-count"></p>
    </div>
    <div id="oficiales-no-results" class="preprints-no-results" hidden>
      <strong>No se encontraron publicaciones.</strong>
      <span>Prueba con otro título, autor, serie o identificador.</span>
    </div>
    {tarjetas}
  </section>
</div>
{JS_CATALOGO}
'''


def main():
    libros = validar_y_leer()
    ediciones = cargar_ediciones()
    preprints_relacionados = cargar_preprints_relacionados()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for libro in libros:
        salida = OUTPUT_DIR / f"{libro['id']}.md"
        salida.write_text(ficha(libro, ediciones.get(libro["id"], []), preprints_relacionados), encoding="utf-8")
    CATALOG_PATH.write_text(pagina_catalogo(libros, preprints_relacionados), encoding="utf-8")
    print(f"Catálogo oficial: {len(libros)} publicaciones")
    print(f"Página principal: {CATALOG_PATH}")
    print(f"Fichas: {OUTPUT_DIR}")
    print(f"Datos editoriales: {METADATA_PATH}")
    print("No se modificaron preprints.json ni los archivos PDF.")


if __name__ == "__main__":
    main()
