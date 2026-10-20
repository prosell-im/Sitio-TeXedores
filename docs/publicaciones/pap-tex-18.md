---
title: "Métodos variacionales en ecuaciones diferenciales parciales no lineales"
---

<div class="oficial-detalle">
<section class="libro-hero">
  <div class="libro-hero-portada"><img src="../../portadas_preprints/pap-tex-18.png" alt="Portada de Métodos variacionales en ecuaciones diferenciales parciales no lineales" loading="lazy"></div>
  <div class="libro-hero-contenido">
    <p class="libro-eyebrow">Ficha bibliográfica · Publicación oficial</p>
    <h1 class="libro-titulo">Métodos variacionales en ecuaciones diferenciales parciales no lineales</h1>
    <p class="oficial-hero-autores">Mónica Clapp</p>
    <div class="chips"><span class="chip">Papirhos</span><span class="chip">Textos</span><span class="chip">Núm. 18</span></div>
  </div>
</section>

<section class="libro-seccion libro-resumen">
  <h2>Resumen</h2>
  <p>Resumen no disponible por el momento.</p>
</section>


<section class="libro-seccion libro-ediciones" id="ediciones-pap-tex-18">
  <h2>Ediciones disponibles</h2>
  <div class="edition-selector">
    <div class="edition-buttons" role="group" aria-label="Seleccionar edición">
      <button type="button" class="edition-button active" data-target="oficial-edicion-pap-tex-18-0" aria-controls="oficial-edicion-pap-tex-18-0" aria-expanded="true">Datos bibliográficos</button>
    </div>
    <div class="edition-content">
<div class="edition-panel" id="oficial-edicion-pap-tex-18-0">
  <section class="libro-subseccion libro-metadatos">
    <h3>Metadatos</h3>
    
    <div class="oficial-tabla-contenedor"><table><tbody><tr><th scope="row">Autores</th><td>Mónica Clapp</td></tr><tr><th scope="row">Colección</th><td>Papirhos</td></tr><tr><th scope="row">Serie</th><td>Textos</td></tr><tr><th scope="row">Número de serie</th><td>18</td></tr></tbody></table></div>
  </section>
  <section class="libro-subseccion libro-cita">
    <h3>Cómo citar</h3>
    <div class="citation-box">
      <blockquote id="oficial-cita-pap-tex-18-0">Mónica Clapp. (s. f.). <em>Métodos variacionales en ecuaciones diferenciales parciales no lineales</em>.</blockquote>
      <button type="button" class="citation-copy-button" data-copy-id="oficial-cita-pap-tex-18-0" data-copy-type="text">Copiar cita</button>
    </div>
    <details class="oficial-bibtex">
      <summary>BibTeX</summary>
      <textarea readonly id="oficial-bibtex-pap-tex-18-0" rows="9" class="verbatim">@book{pap-tex-18,
  title = {Métodos variacionales en ecuaciones diferenciales parciales no lineales},
  author = {Mónica Clapp},
  series = {Textos},
  number = {18}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-copy-id="oficial-bibtex-pap-tex-18-0" data-copy-type="value">Copiar BibTeX</button>
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
    <a href="../../archivos_preprints/pap-tex-18-v1.pdf" class="md-button md-button--primary" target="_blank" rel="noopener noreferrer">Abrir PDF</a>
    <a href="../../archivos_preprints/pap-tex-18-v1.pdf" class="md-button preprint-secondary-button" download>Descargar PDF</a>
  </div>
  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/pap-tex-18-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/pap-tex-18-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
      </object>
    </div>
  </details>
</div>
</section>

<div class="libro-navegacion">
  <a class="md-button md-button--primary" href="../../catalogo/">Volver al catálogo</a>
</div>


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
         href="../../preprints/pap-tex-18/">
        Consultar preprint <span aria-hidden="true">→</span>
      </a>
    </div>
  </div>
</section>
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

