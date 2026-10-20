---
title: "Combinatoria"
---

<div class="oficial-detalle">
<section class="libro-hero">
  <div class="libro-hero-portada"><img src="../../portadas_preprints/cuad-x-1.png" alt="Portada de Combinatoria" loading="lazy"></div>
  <div class="libro-hero-contenido">
    <p class="libro-eyebrow">Ficha bibliográfica · Publicación oficial</p>
    <h1 class="libro-titulo">Combinatoria</h1>
    <p class="oficial-hero-autores">Maria Luisa Pérez Seguí</p>
    <div class="chips"><span class="chip">Cuadernos de olimpiadas de matemáticas</span><span class="chip">Núm. 1</span></div>
  </div>
</section>

<section class="libro-seccion libro-resumen">
  <h2>Resumen</h2>
  <p>Resumen no disponible por el momento.</p>
</section>


<section class="libro-seccion libro-ediciones" id="ediciones-cuad-x-1">
  <h2>Ediciones disponibles</h2>
  <div class="edition-selector">
    <div class="edition-buttons" role="group" aria-label="Seleccionar edición">
      <button type="button" class="edition-button active" data-target="oficial-edicion-cuad-x-1-0" aria-controls="oficial-edicion-cuad-x-1-0" aria-expanded="true">Edición 2</button>
    </div>
    <div class="edition-content">
<div class="edition-panel" id="oficial-edicion-cuad-x-1-0">
  <section class="libro-subseccion libro-metadatos">
    <h3>Metadatos</h3>
    
    <div class="oficial-tabla-contenedor"><table><tbody><tr><th scope="row">Autores</th><td>Maria Luisa Pérez Seguí</td></tr><tr><th scope="row">Colección</th><td>Cuadernos de olimpiadas de matemáticas</td></tr><tr><th scope="row">Número de serie</th><td>1</td></tr><tr><th scope="row">Año</th><td>2018</td></tr><tr><th scope="row">Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th scope="row">Edición</th><td>2</td></tr><tr><th scope="row">ISBN (colección)</th><td>978-968-36-8599-5</td></tr><tr><th scope="row">ISBN (libro)</th><td>978-607-02-85882</td></tr></tbody></table></div>
  </section>
  <section class="libro-subseccion libro-cita">
    <h3>Cómo citar</h3>
    <div class="citation-box">
      <blockquote id="oficial-cita-cuad-x-1-0">Maria Luisa Pérez Seguí. (2018). <em>Combinatoria</em>. Instituto de Matemáticas, UNAM. Edición 2.</blockquote>
      <button type="button" class="citation-copy-button" data-copy-id="oficial-cita-cuad-x-1-0" data-copy-type="text">Copiar cita</button>
    </div>
    <details class="oficial-bibtex">
      <summary>BibTeX</summary>
      <textarea readonly id="oficial-bibtex-cuad-x-1-0" rows="9" class="verbatim">@book{ed-002,
  title = {Combinatoria},
  author = {Maria Luisa Pérez Seguí},
  year = {2018},
  publisher = {Instituto de Matemáticas, UNAM},
  edition = {2},
  isbn = {978-607-02-85882},
  number = {1}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-copy-id="oficial-bibtex-cuad-x-1-0" data-copy-type="value">Copiar BibTeX</button>
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
    <a href="../../archivos_preprints/cuad-x-1-v1.pdf" class="md-button md-button--primary" target="_blank" rel="noopener noreferrer">Abrir PDF</a>
    <a href="../../archivos_preprints/cuad-x-1-v1.pdf" class="md-button preprint-secondary-button" download>Descargar PDF</a>
  </div>
  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/cuad-x-1-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/cuad-x-1-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
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

