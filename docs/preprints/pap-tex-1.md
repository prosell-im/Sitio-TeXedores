---
title: "Grupos I"
---
<div class="preprint-detalle">
<section class="preprint-detail-hero">
  <div class="preprint-detail-cover"><img src="../../portadas_preprints/pap-tex-1.png" alt="Portada de Grupos I" loading="lazy"></div>
  <div class="preprint-detail-main">
    <p class="preprint-detail-eyebrow">Preprint · pap-tex-1</p>
    <h1>Grupos I</h1>
    <p class="preprint-detail-authors">Diana Avella · Octavio Mendoza · Edith Corina Sáenz · María José Souto</p>
    <div class="preprint-detail-version"><span class="preprint-detail-date">Publicado: 2026-09-29</span></div>
    <div class="chips"><span class="chip">Papirhos</span></div>
    <div class="tex-disponibilidad" aria-label="Disponibilidad"><span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint</span><span class="tex-disponibilidad__badge">PDF disponible</span><span class="tex-disponibilidad__badge">Edición oficial disponible</span></div>
    <div class="preprint-detail-actions">
      <a class="md-button md-button--primary" href="../../archivos_preprints/pap-tex-1-v1.pdf" target="_blank" rel="noopener">Ver PDF</a>
      <a href="../" class="md-button preprint-secondary-button">Volver a Preprints</a>
    </div>
  </div>
</section>
<section class="libro-seccion libro-resumen preprint-resumen">
  <h2>Resumen</h2><p>Grupos I es el primero de dos libros dedicados a uno de los hitos que revolucionaron el pensamiento matemático de su época, y que hasta nuestros días juega un papel esencial en el estudio sistemático de las ciencias: la Teoría de Grupos.<br>En este tomo, los autores se dirigen al público en general al explicar de manera accesible algunos de los resultados clásicos de dicha teoría. Con años de experiencia docente, introducen también a los lectores en la abstracción y el arte de las demostraciones rigurosas. Además, el texto contiene una gran cantidad de notas históricas, ejemplos trabajados y ejercicios: inicia al revisar el conjunto de los números enteros que forman un grupo con la suma usual y, de manera paulatina, desarrolla una travesía por este apasionante tema.<br>El presente volumen abarca la aritmética en el conjunto de los números enteros, por ejemplo, la divisibilidad, el algoritmo de la división y el de Euclides, las congruencias y la función φ de Euler. Asimismo, se analizan los grupos de permutaciones, los cíclicos, los normales y el grupo cociente. Finalmente, se introduce el concepto de homomorfismo de grupos y se demuestran los —tan usados en matemáticas— teoremas de isomorfismo.</p>
</section>
<section class="libro-seccion preprint-citation-section">
  <h2>Cómo citar</h2>
  <div class="citation-box citation-box-featured">
    <div class="citation-box-main"><p id="cita-pap-tex-1" class="citation-text">Diana Avella, Octavio Mendoza, Edith Corina Sáenz, María José Souto. (2026). Grupos I. Preprints, pap-tex-1. https://prosell-im.github.io/Sitio-TeXedores/preprints/pap-tex-1/</p></div>
    <button type="button" class="citation-copy-button" data-target="cita-pap-tex-1">Copiar cita</button>
  </div>
  <details class="preprint-bibtex-details">
    <summary>BibTeX</summary>
    <div class="preprint-bibtex-content">
      <textarea id="bibtex-pap-tex-1" rows="7" class="verbatim preprint-bibtex-area" readonly>@misc{pap-tex-1,
  author = {Diana Avella and Octavio Mendoza and Edith Corina Sáenz and María José Souto},
  title = {Grupos I},
  year = {2026},
  note = {Preprint: pap-tex-1},
  url = {https://prosell-im.github.io/Sitio-TeXedores/preprints/pap-tex-1/}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-target="bibtex-pap-tex-1">Copiar BibTeX</button>
    </div>
  </details>
</section>
<section class="libro-seccion preprint-pdf-seccion"><h2>Vista previa del PDF</h2><div class="pdf-mostrador">

  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/pap-tex-1-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/pap-tex-1-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
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
       href="../../publicaciones/pap-tex-1/">Consultar publicación oficial →</a>
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
