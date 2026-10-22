---
title: "Introducción a la teoría de redes"
---
<div class="preprint-detalle">
<section class="preprint-detail-hero">
  <div class="preprint-detail-cover"><img src="../../portadas_preprints/apor-tex-12.png" alt="Portada de Introducción a la teoría de redes" loading="lazy"></div>
  <div class="preprint-detail-main">
    <p class="preprint-detail-eyebrow">Preprint · apor-tex-12</p>
    <h1>Introducción a la teoría de redes</h1>
    <p class="preprint-detail-authors">María del Carmen Hernández Ayuso</p>
    <div class="preprint-detail-version"><span class="preprint-detail-date">Publicado: 2026-09-29</span></div>
    <div class="chips"><span class="chip">Aportaciones Matemáticas</span></div>
    <div class="tex-disponibilidad" aria-label="Disponibilidad"><span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint</span><span class="tex-disponibilidad__badge">PDF disponible</span><span class="tex-disponibilidad__badge">Edición oficial disponible</span></div>
    <div class="preprint-detail-actions">
      <a class="md-button md-button--primary" href="../../archivos_preprints/apor-tex-12-v1.pdf" target="_blank" rel="noopener">Ver PDF</a>
      <a href="../" class="md-button preprint-secondary-button">Volver a Preprints</a>
    </div>
  </div>
</section>
<section class="libro-seccion libro-resumen preprint-resumen">
  <h2>Resumen</h2><p>Este libro está enfocado a los temas básicos de teoría de redes. Se presentan tanto teoría general y características de los problemas de optimización de esta rama como algoritmos para resolverlos.<br>Se exponen cuatro problemas básicos: árbol de peso mínimo, ruta más corta, flujo máximo y flujo a costo mínimo; estos problemas han sido resueltos principalmente mediante dos enfoques generales. Uno consiste en especializar los algoritmos de programación lineal aprovechando la estructura de cada problema y el otro en aplicar resultados de teoría de gráficas. En los primeros cinco capítulos se presentan algunos algoritmos para resolver problemas de flujo en redes según el enfoque clásico de la programación lineal. En los últimos dos capítulos se presentan generalizaciones de dos de estos problemas según el enfoque de coloración en gráficas.<br>La teoría de dualidad ha sido estudiada para el caso de los modelos de redes; con esto se han generado algoritmos de solución simultánea para el par de problemas duales. Este es el caso de los problemas de flujo máximo y de cadena mínima.<br>En cada capítulo se incluyen conceptos, resultados teóricos rigurosamente demostrados, técnicas, ejemplos numéricos y una series de ejercicios propuestos.</p>
</section>
<section class="libro-seccion preprint-citation-section">
  <h2>Cómo citar</h2>
  <div class="citation-box citation-box-featured">
    <div class="citation-box-main"><p id="cita-apor-tex-12" class="citation-text">María del Carmen Hernández Ayuso. (2026). Introducción a la teoría de redes. Preprints, apor-tex-12. https://prosell-im.github.io/Sitio-TeXedores/preprints/apor-tex-12/</p></div>
    <button type="button" class="citation-copy-button" data-target="cita-apor-tex-12">Copiar cita</button>
  </div>
  <details class="preprint-bibtex-details">
    <summary>BibTeX</summary>
    <div class="preprint-bibtex-content">
      <textarea id="bibtex-apor-tex-12" rows="7" class="verbatim preprint-bibtex-area" readonly>@misc{apor-tex-12,
  author = {María del Carmen Hernández Ayuso},
  title = {Introducción a la teoría de redes},
  year = {2026},
  note = {Preprint: apor-tex-12},
  url = {https://prosell-im.github.io/Sitio-TeXedores/preprints/apor-tex-12/}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-target="bibtex-apor-tex-12">Copiar BibTeX</button>
    </div>
  </details>
</section>
<section class="libro-seccion preprint-pdf-seccion"><h2>Vista previa del PDF</h2><div class="pdf-mostrador">

  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/apor-tex-12-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/apor-tex-12-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
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
       href="../../publicaciones/apor-tex-12/">Consultar publicación oficial →</a>
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
