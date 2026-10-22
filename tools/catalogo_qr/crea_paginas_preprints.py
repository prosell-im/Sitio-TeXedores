"""Genera fichas y catálogo de Preprints sin historial de versiones.

Entradas: docs/data/preprints.json y docs/data/catalogo.json.
Salidas: docs/preprints.md y docs/preprints/<id>.md.
Conserva la portada, resumen, citas, PDF y enlaces relacionados.
"""
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mostrador_PDF import bloque_pdf

BASE = Path(__file__).resolve().parent
PROJECT = BASE.parent.parent
DOCS = PROJECT / "docs"
PREPRINTS_PATH = DOCS / "data" / "preprints.json"
OFFICIAL_PATH = DOCS / "data" / "catalogo.json"
OUT = DOCS / "preprints"


def esc(v):
    return html.escape(str(v or ""), quote=True)


def urlpath(s):
    return quote(str(s or ""), safe="/-_.")


def resumen_html(s):
    """Admite etiquetas editoriales básicas; escapa el resto."""
    x = esc(s)
    x = re.sub(r"&lt;br\s*/?&gt;", "<br>", x, flags=re.I)
    x = re.sub(r"&lt;(/?)i&gt;", r"<\1i>", x, flags=re.I)
    return x


def sitio():
    archivo = PROJECT / "mkdocs.yml"
    for linea in archivo.read_text(encoding="utf-8-sig").splitlines():
        if linea.strip().startswith("site_url:"):
            return linea.split(":", 1)[1].strip().strip("'\"").rstrip("/")
    return ""


def cubierta(item, prefix, clase):
    portada = item.get("portada") or ""
    if portada and (DOCS / "portadas_preprints" / portada).is_file():
        return (f'<div class="{clase}">'
                f'<img src="{prefix}portadas_preprints/{urlpath(portada)}" '
                f'alt="Portada de {esc(item["titulo"])}" loading="lazy"></div>')
    return (f'<div class="{clase} preprint-detail-cover-placeholder preprint-cover-placeholder">'
            f'<span>{esc(item["id_preprint"])}</span><small>Preprint</small></div>')


def badges(item, oficiales):
    partes = ['<span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint</span>']
    if item.get("pdf"):
        partes.append('<span class="tex-disponibilidad__badge">PDF disponible</span>')
    if item["id_preprint"] in oficiales:
        partes.append('<span class="tex-disponibilidad__badge">Edición oficial disponible</span>')
    return '<div class="tex-disponibilidad" aria-label="Disponibilidad">'+''.join(partes)+'</div>'


def relacionado(item, oficiales):
    if item["id_preprint"] not in oficiales:
        return ""
    ident = esc(item["id_preprint"])
    return f'''<section class="relacion-fichas" aria-label="Contenido relacionado">
<div class="relacion-fichas__marco">
  <p class="relacion-fichas__etiqueta">Contenido relacionado</p>
  <div class="relacion-fichas__contenido">
    <div class="relacion-fichas__descripcion">
      <h2>Publicación oficial relacionada</h2>
      <p>Este preprint incluye cambios todavía no incorporados a la edición oficial.
         Puedes consultar la publicación oficial por separado.</p>
    </div>
    <a class="md-button md-button--primary relacion-fichas__enlace"
       href="../../publicaciones/{ident}/">Consultar publicación oficial →</a>
  </div>
</div>
</section>'''

JS_COPIA = r'''<script>
(() => {
  document.querySelectorAll('.preprint-detalle [data-target]').forEach(b => {
    b.addEventListener('click', async () => {
      const fuente = document.getElementById(b.dataset.target);
      if (!fuente) return;
      const contenido = fuente.tagName === 'TEXTAREA' ? fuente.value : fuente.innerText.trim();
      try {
        await navigator.clipboard.writeText(contenido);
        const texto = b.textContent;
        b.textContent = 'Copiado';
        setTimeout(() => { b.textContent = texto; }, 1400);
      } catch (_) {
        if (fuente.tagName === 'TEXTAREA') { fuente.focus(); fuente.select(); }
        b.textContent = 'Selecciona y copia el texto';
      }
    });
  });
})();
</script>'''


def ficha(item, oficiales, site_url):
    ident = esc(item["id_preprint"])
    titulo = esc(item["titulo"])
    autores = item.get("autores", [])
    anio = str(item.get("fecha", ""))[:4] or "s. f."
    fecha = esc(item.get("fecha") or "")
    pdf = str(item.get("pdf") or "")
    url = f'{site_url}/preprints/{urlpath(item["id_preprint"])}/' if site_url else ''
    cita = (f'{", ".join(autores)}. ({anio}). {item["titulo"]}. '
            f'Preprints, {item["id_preprint"]}. {url}')
    bib = '@misc{' + item['id_preprint'] + ',\n' + ',\n'.join([
        '  author = {' + ' and '.join(autores) + '}',
        '  title = {' + item['titulo'] + '}',
        '  year = {' + (anio if anio != 's. f.' else '') + '}',
        '  note = {Preprint: ' + item['id_preprint'] + '}',
        '  url = {' + url + '}',
    ]) + '\n}'
    pdf_btn = (f'<a class="md-button md-button--primary" href="../../{urlpath(pdf)}" '
               f'target="_blank" rel="noopener">Ver PDF</a>') if pdf else ''
    preview = (f'<section class="libro-seccion preprint-pdf-seccion">'
               f'<h2>Vista previa del PDF</h2>'
               f'{bloque_pdf("../../"+urlpath(pdf), mostrar_botones=False)}'
               f'</section>') if pdf else ''
    fecha_tag = f'<span class="preprint-detail-date">Publicado: {fecha}</span>' if fecha else ''
    coleccion_tag = ''
    if item.get('coleccion'):
        coleccion_tag = f'<div class="chips"><span class="chip">{esc(item["coleccion"])}</span></div>'
    return f'''---
title: {json.dumps(item['titulo'], ensure_ascii=False)}
---
<div class="preprint-detalle">
<section class="preprint-detail-hero">
  {cubierta(item, '../../', 'preprint-detail-cover')}
  <div class="preprint-detail-main">
    <p class="preprint-detail-eyebrow">Preprint · {ident}</p>
    <h1>{titulo}</h1>
    <p class="preprint-detail-authors">{esc(' · '.join(autores))}</p>
    <div class="preprint-detail-version">{fecha_tag}</div>
    {coleccion_tag}
    {badges(item, oficiales)}
    <div class="preprint-detail-actions">
      {pdf_btn}
      <a href="../" class="md-button preprint-secondary-button">Volver a Preprints</a>
    </div>
  </div>
</section>
<section class="libro-seccion libro-resumen preprint-resumen">
  <h2>Resumen</h2><p>{resumen_html(item.get('resumen'))}</p>
</section>
<section class="libro-seccion preprint-citation-section">
  <h2>Cómo citar</h2>
  <div class="citation-box citation-box-featured">
    <div class="citation-box-main"><p id="cita-{ident}" class="citation-text">{esc(cita)}</p></div>
    <button type="button" class="citation-copy-button" data-target="cita-{ident}">Copiar cita</button>
  </div>
  <details class="preprint-bibtex-details">
    <summary>BibTeX</summary>
    <div class="preprint-bibtex-content">
      <textarea id="bibtex-{ident}" rows="7" class="verbatim preprint-bibtex-area" readonly>{esc(bib)}</textarea>
      <button type="button" class="bibtex-copy-button" data-target="bibtex-{ident}">Copiar BibTeX</button>
    </div>
  </details>
</section>
{preview}
<div class="libro-navegacion"><a href="../../preprints/" class="md-button md-button--primary">Volver al catálogo</a></div>
{relacionado(item, oficiales)}
</div>
{JS_COPIA}
'''

JS_CATALOGO = r'''<script>
(() => {
  const pagina = document.querySelector('.preprints-page');
  if (!pagina) return;
  const input = pagina.querySelector('#preprints-search-input');
  const tarjetas = [...pagina.querySelectorAll('.preprint-card')];
  const contador = pagina.querySelector('#preprints-results-count');
  const vacio = pagina.querySelector('#preprints-no-results');
  const normalizar = x => String(x).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function filtrar() {
    const texto = normalizar(input.value).trim();
    let n = 0;
    tarjetas.forEach(card => {
      const ok = normalizar(card.textContent).includes(texto);
      card.hidden = !ok;
      if (ok) n++;
    });
    contador.textContent = `${n} ${n === 1 ? 'preprint encontrado' : 'preprints encontrados'}`;
    vacio.hidden = n > 0;
  }
  pagina.querySelectorAll('.preprint-summary-toggle').forEach(b => {
    b.addEventListener('click', () => {
      const p = b.parentElement.querySelector('.preprint-summary');
      const cerrado = p.classList.toggle('preprint-summary-collapsed');
      b.textContent = cerrado ? 'Ver más' : 'Ver menos';
    });
    const text = b.parentElement.querySelector('.preprint-summary');
    if (text && text.scrollHeight <= text.clientHeight + 2) b.hidden = true;
  });
  input.addEventListener('input', filtrar);
  filtrar();
})();
</script>'''


def tarjeta(item, oficiales):
    ident = esc(item['id_preprint'])
    titulo = esc(item['titulo'])
    pdf = item.get('pdf') or ''
    fecha = esc(item.get('fecha') or '')
    ver_pdf = (f'<a href="../{urlpath(pdf)}" class="md-button preprint-secondary-button" '
               f'target="_blank" rel="noopener">Ver PDF</a>') if pdf else ''
    descripcion = (f'<div class="preprint-summary-wrapper">'
                   f'<p class="preprint-summary preprint-summary-collapsed">{resumen_html(item.get("resumen"))}</p>'
                   f'<button type="button" class="preprint-summary-toggle">Ver más</button>'
                   f'</div>')
    return f'''<article class="preprint-card">
  <div class="preprint-card-layout">
    {cubierta(item, '../', 'preprint-cover')}
    <div class="preprint-card-main">
      <div class="preprint-card-top"><span class="preprint-id">{ident}</span>
      {f'<span class="preprint-date">{fecha}</span>' if fecha else ''}</div>
      <div class="preprint-card-content">
        <h3 class="preprint-title"><a href="{ident}/">{titulo}</a></h3>
        <p class="preprint-authors">{esc(' · '.join(item.get('autores', [])))}</p>
        {descripcion}
      </div>
      <div class="preprint-card-footer">
        {badges(item, oficiales)}
        <div class="preprint-actions">
          <a href="{ident}/" class="md-button md-button--primary">Ver ficha</a>
          {ver_pdf}
        </div>
      </div>
    </div>
  </div>
</article>'''


def indice(preprints, oficiales):
    cards = '\n'.join(tarjeta(x, oficiales) for x in preprints)
    return f'''<div class="preprints-page">
<section class="preprints-hero">
  <p class="preprints-eyebrow">Repositorio académico</p>
  <h1>Preprints</h1>
  <p class="preprints-lead">Consulta prepublicaciones y materiales académicos disponibles.</p>
  <p class="preprints-description">Los preprints pueden contener cambios que aún no forman parte de una edición oficial. Una obra sin publicación oficial todavía no pertenece a una colección editorial.</p>
</section>
<section class="preprints-list">
  <div class="preprints-list-header"><div>
    <p class="preprints-section-label">Preprints</p>
    <h2>Prepublicaciones recientes</h2>
  </div></div>
  <div class="preprints-search">
    <label for="preprints-search-input" class="preprints-search-label">Buscar preprints</label>
    <div class="preprints-search-box">
      <input type="search" id="preprints-search-input" autocomplete="off" placeholder="Buscar por título, autor, identificador o palabra clave...">
    </div>
    <p id="preprints-results-count" class="preprints-results-count"></p>
    <div class="preprints-advanced-link"><a href="../explorar/">Búsqueda avanzada →</a></div>
  </div>
  <div id="preprints-no-results" class="preprints-no-results" hidden>
    <strong>No se encontraron preprints.</strong>
    <span>Intenta con otro título, autor o palabra clave.</span>
  </div>
  {cards}
</section>
</div>
{JS_CATALOGO}'''


def main():
    preprints = json.loads(PREPRINTS_PATH.read_text(encoding='utf-8'))
    oficiales = {str(x['id']):x for x in json.loads(OFFICIAL_PATH.read_text(encoding='utf-8'))}
    OUT.mkdir(exist_ok=True, parents=True)
    sitio_url = sitio()
    for x in preprints:
        ident = str(x['id_preprint'])
        if not re.fullmatch(r'[A-Za-z0-9_-]+', ident):
            raise ValueError(f'ID de preprint no válido: {ident}')
        (OUT / (ident+'.md')).write_text(ficha(x, oficiales, sitio_url), encoding='utf-8')
    (DOCS / 'preprints.md').write_text(indice(preprints, oficiales), encoding='utf-8')
    print(f'Preprints generados: {len(preprints)}; sin historial de versiones')
    print('Fichas: ' + str(OUT))

if __name__ == '__main__':
    main()
