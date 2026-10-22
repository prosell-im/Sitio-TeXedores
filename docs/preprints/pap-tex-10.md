---
title: "Curso introductorio de álgebra II"
---
<div class="preprint-detalle">
<section class="preprint-detail-hero">
  <div class="preprint-detail-cover"><img src="../../portadas_preprints/pap-tex-10.png" alt="Portada de Curso introductorio de álgebra II" loading="lazy"></div>
  <div class="preprint-detail-main">
    <p class="preprint-detail-eyebrow">Preprint · pap-tex-10</p>
    <h1>Curso introductorio de álgebra II</h1>
    <p class="preprint-detail-authors">Diana Avella · Gabriela Campero · Edith Corina Sáenz</p>
    <div class="preprint-detail-version"><span class="preprint-detail-date">Publicado: 2026-10-07</span></div>
    <div class="chips"><span class="chip">Papirhos</span></div>
    <div class="tex-disponibilidad" aria-label="Disponibilidad"><span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint</span><span class="tex-disponibilidad__badge">PDF disponible</span><span class="tex-disponibilidad__badge">Edición oficial disponible</span></div>
    <div class="preprint-detail-actions">
      <a class="md-button md-button--primary" href="../../archivos_preprints/pap-tex-10-v1.pdf" target="_blank" rel="noopener">Ver PDF</a>
      <a href="../" class="md-button preprint-secondary-button">Volver a Preprints</a>
    </div>
  </div>
</section>
<section class="libro-seccion libro-resumen preprint-resumen">
  <h2>Resumen</h2><p>El presente texto, segundo tomo de la serie, está dirigido a estudiantes del primer semestre de carreras en ciencias exactas. Contiene temas que los introducen al Álgebra y busca incorporar, a través de su tratamiento, una descripción minuciosa y rigurosa de los procedimientos de demostración y deducción necesarios para formar a los estudiantes en el pensamiento matemático abstracto. Es un texto con un grado elevado de rigor, claridad y pedagogía, que puede ser utilizado de manera autodidacta o como un complemento necesario para las clases en aula.<br> Este tomo está conformado por cuatro capítulos; cada capítulo contiene bloques de ejercicios cuidadosamente seleccionados. En ellos se desarrolla la construcción de los números enteros y temas relacionados con esta estructura numérica. Una vez expuesta dicha construcción, se describen a detalle las características que lo llevan a ser un dominio entero. Posteriormente damos una introducción a estructuras algebraicas como son un grupo, un anillo y un dominio entero. El tercer capítulo versa sobre la noción de divisibilidad en los enteros, que incluye una exposición del algoritmo de la división, los conceptos de máximo común divisor, de mínimo común múltiplo, y de número primo. El cuarto capítulo expone el tema de congruencias en los enteros, visitando el anillo formado por las clases de equivalencia de los enteros módulo un entero positivo, además de explorar las ecuaciones con congruencias y sistemas formados con estas ecuaciones.</p>
</section>
<section class="libro-seccion preprint-citation-section">
  <h2>Cómo citar</h2>
  <div class="citation-box citation-box-featured">
    <div class="citation-box-main"><p id="cita-pap-tex-10" class="citation-text">Diana Avella, Gabriela Campero, Edith Corina Sáenz. (2026). Curso introductorio de álgebra II. Preprints, pap-tex-10. https://prosell-im.github.io/Sitio-TeXedores/preprints/pap-tex-10/</p></div>
    <button type="button" class="citation-copy-button" data-target="cita-pap-tex-10">Copiar cita</button>
  </div>
  <details class="preprint-bibtex-details">
    <summary>BibTeX</summary>
    <div class="preprint-bibtex-content">
      <textarea id="bibtex-pap-tex-10" rows="7" class="verbatim preprint-bibtex-area" readonly>@misc{pap-tex-10,
  author = {Diana Avella and Gabriela Campero and Edith Corina Sáenz},
  title = {Curso introductorio de álgebra II},
  year = {2026},
  note = {Preprint: pap-tex-10},
  url = {https://prosell-im.github.io/Sitio-TeXedores/preprints/pap-tex-10/}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-target="bibtex-pap-tex-10">Copiar BibTeX</button>
    </div>
  </details>
</section>
<section class="libro-seccion preprint-pdf-seccion"><h2>Vista previa del PDF</h2><div class="pdf-mostrador">

  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/pap-tex-10-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/pap-tex-10-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
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
       href="../../publicaciones/pap-tex-10/">Consultar publicación oficial →</a>
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
