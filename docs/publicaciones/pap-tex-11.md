---
title: "Curso breve de geometría proyectiva"
---

<div class="oficial-detalle">
<section class="libro-hero">
  <div class="libro-hero-portada"><img src="../../portadas_preprints/pap-tex-11.png" alt="Portada de Curso breve de geometría proyectiva" loading="lazy"></div>
  <div class="libro-hero-contenido">
    <p class="libro-eyebrow">Ficha bibliográfica · Publicación oficial</p>
    <h1 class="libro-titulo">Curso breve de geometría proyectiva</h1>
    <p class="oficial-hero-autores">Felipe Cano · Beatriz Molina-Samper · Fernando Sanz</p>
    <div class="chips"><span class="chip">Papirhos</span><span class="chip">Textos</span><span class="chip">Núm. 11</span></div>
  </div>
</section>

<section class="libro-seccion libro-resumen">
  <h2>Resumen</h2>
  <p>Resumen no disponible por el momento.</p>
</section>


<section class="libro-seccion libro-ediciones" id="ediciones-pap-tex-11">
  <h2>Ediciones disponibles</h2>
  <div class="edition-selector">
    <div class="edition-buttons" role="group" aria-label="Seleccionar edición">
      <button type="button" class="edition-button active" data-target="oficial-edicion-pap-tex-11-0" aria-controls="oficial-edicion-pap-tex-11-0" aria-expanded="true">Datos bibliográficos</button>
    </div>
    <div class="edition-content">
<div class="edition-panel" id="oficial-edicion-pap-tex-11-0">
  <section class="libro-subseccion libro-metadatos">
    <h3>Metadatos</h3>
    <p class='oficial-aviso-revision'>Estos datos editoriales proceden de Papirhos Digital y deben verificarse. No necesariamente describen el PDF actual.</p>
    <div class="oficial-tabla-contenedor"><table><tbody><tr><th scope="row">Autores</th><td>Felipe Cano, Beatriz Molina-Samper, Fernando Sanz</td></tr><tr><th scope="row">Colección</th><td>Papirhos</td></tr><tr><th scope="row">Serie</th><td>Textos</td></tr><tr><th scope="row">Número de serie</th><td>11</td></tr><tr><th scope="row">Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr></tbody></table></div>
  </section>
  <section class="libro-subseccion libro-cita">
    <h3>Cómo citar</h3>
    <p class="oficial-nota-cita">Cita orientativa: confirma la edición y los datos antes de utilizarla.</p>
    <div class="citation-box">
      <blockquote id="oficial-cita-pap-tex-11-0">Felipe Cano, Beatriz Molina-Samper, Fernando Sanz. (s. f.). <em>Curso breve de geometría proyectiva</em>. Instituto de Matemáticas, UNAM.</blockquote>
      <button type="button" class="citation-copy-button" data-copy-id="oficial-cita-pap-tex-11-0" data-copy-type="text">Copiar cita</button>
    </div>
    <details class="oficial-bibtex">
      <summary>BibTeX</summary>
      <textarea readonly id="oficial-bibtex-pap-tex-11-0" rows="9" class="verbatim">@book{ed-014,
  title = {Curso breve de geometría proyectiva},
  author = {Felipe Cano and Beatriz Molina-Samper and Fernando Sanz},
  publisher = {Instituto de Matemáticas, UNAM},
  series = {Textos},
  number = {11}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-copy-id="oficial-bibtex-pap-tex-11-0" data-copy-type="value">Copiar BibTeX</button>
    </details>
  </section>
</div></div>
  </div>
</section>

<section class="libro-seccion libro-seccion-descargas oficial-pdf-seccion">
  <h2>Descargas</h2>
  <p>Abre, descarga o consulta el PDF de la publicación desde aquí.</p>
  <div class="pdf-mostrador">

  <div class="pdf-mostrador__acciones">
    <a href="../../archivos_preprints/pap-tex-11-v1.pdf" class="md-button md-button--primary" target="_blank" rel="noopener noreferrer">Abrir PDF</a>
    <a href="../../archivos_preprints/pap-tex-11-v1.pdf" class="md-button preprint-secondary-button" download>Descargar PDF</a>
  </div>
  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/pap-tex-11-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/pap-tex-11-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
      </object>
    </div>
  </details>
</div>
</section>

<div class="libro-navegacion">
  <a class="md-button md-button--primary" href="../../catalogo/">Volver al catálogo</a>
</div>
</div>

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

