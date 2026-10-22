---
title: "Análisis Matemático"
---
<div class="preprint-detalle">
<section class="preprint-detail-hero">
  <div class="preprint-detail-cover"><img src="../../portadas_preprints/pap-tex-2.png" alt="Portada de Análisis Matemático" loading="lazy"></div>
  <div class="preprint-detail-main">
    <p class="preprint-detail-eyebrow">Preprint · pap-tex-2</p>
    <h1>Análisis Matemático</h1>
    <p class="preprint-detail-authors">Mónica Clapp</p>
    <div class="preprint-detail-version"><span class="preprint-detail-date">Publicado: 2026-10-07</span></div>
    <div class="chips"><span class="chip">Papirhos</span></div>
    <div class="tex-disponibilidad" aria-label="Disponibilidad"><span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint</span><span class="tex-disponibilidad__badge">PDF disponible</span><span class="tex-disponibilidad__badge">Edición oficial disponible</span></div>
    <div class="preprint-detail-actions">
      <a class="md-button md-button--primary" href="../../archivos_preprints/pap-tex-2-v1.pdf" target="_blank" rel="noopener">Ver PDF</a>
      <a href="../" class="md-button preprint-secondary-button">Volver a Preprints</a>
    </div>
  </div>
</section>
<section class="libro-seccion libro-resumen preprint-resumen">
  <h2>Resumen</h2><p>Este libro tan esperado en la Facultad de Ciencias de la Universidad Nacional Autónoma de México, y en diversas universidades de México y de países hispanoparlantes, es el resultado de muchos años de experiencia docente y de investigación por parte de la autora. Reúne material clave en la formación en análisis de los estudiantes dematemáticas y de otras carreras afines.<br>Motivándolos por un problema concreto —la existencia de trayectorias de longitud mínima— la obra introduce gradualmente los conceptos básicos del análisis hasta llegar a los teoremas de punto fijo de Banach y de Arzelà-Azcoli, así como a diversas aplicaciones de ellos a la existencia de soluciones de ecuaciones diferenciales e integrales. Posteriormente presenta el concepto de diferenciabilidad en espacios de Banach y demuestra el teorema de la función implícita, que permite introducir el concepto de variedad y el estudio de problemas de minimización en variedades. La última parte de este texto se dedica a la teoría de integración de Lebesgue; introduce los espacios de Lebesgue y de Sobolev para concluir con algunas aplicaciones a la existencia de soluciones de problemas elípticos con condición de frontera.</p>
</section>
<section class="libro-seccion preprint-citation-section">
  <h2>Cómo citar</h2>
  <div class="citation-box citation-box-featured">
    <div class="citation-box-main"><p id="cita-pap-tex-2" class="citation-text">Mónica Clapp. (2026). Análisis Matemático. Preprints, pap-tex-2. https://prosell-im.github.io/Sitio-TeXedores/preprints/pap-tex-2/</p></div>
    <button type="button" class="citation-copy-button" data-target="cita-pap-tex-2">Copiar cita</button>
  </div>
  <details class="preprint-bibtex-details">
    <summary>BibTeX</summary>
    <div class="preprint-bibtex-content">
      <textarea id="bibtex-pap-tex-2" rows="7" class="verbatim preprint-bibtex-area" readonly>@misc{pap-tex-2,
  author = {Mónica Clapp},
  title = {Análisis Matemático},
  year = {2026},
  note = {Preprint: pap-tex-2},
  url = {https://prosell-im.github.io/Sitio-TeXedores/preprints/pap-tex-2/}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-target="bibtex-pap-tex-2">Copiar BibTeX</button>
    </div>
  </details>
</section>
<section class="libro-seccion preprint-pdf-seccion"><h2>Vista previa del PDF</h2><div class="pdf-mostrador">

  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/pap-tex-2-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/pap-tex-2-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
      </object>
    </div>
  </details>
</div></section>
<div class="libro-navegacion"><a href="../../preprints/" class="md-button md-button--primary">Volver al catálogo</a></div>
<section class="relacion-fichas" aria-label="Contenido relacionado">
<div class="relacion-fichas__marco">
  <p class="relacion-fichas__etiqueta">Contenido relacionado</p>
  <div class="relacion-fichas__contenido">
    <div class="relacion-fichas__descripcion">
      <h2>Publicación oficial relacionada</h2>
      <p>Este preprint incluye cambios todavía no incorporados a la edición oficial.
         Puedes consultar la publicación oficial por separado.</p>
    </div>
    <a class="md-button md-button--primary relacion-fichas__enlace"
       href="../../publicaciones/pap-tex-2/">Consultar publicación oficial →</a>
  </div>
</div>
</section>
</div>
<script>
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
</script>
