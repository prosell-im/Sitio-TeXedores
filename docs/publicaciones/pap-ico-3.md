---
title: "Concursos Nacionales de la Olimpiada Mexicana de Matemáticas:1987-2016"
---

<div class="oficial-detalle">
<section class="libro-hero">
  <div class="libro-hero-portada"><img src="../../portadas_preprints/pap-ico-3.png" alt="Portada de Concursos Nacionales de la Olimpiada Mexicana de Matemáticas:1987-2016" loading="lazy"></div>
  <div class="libro-hero-contenido">
    <p class="libro-eyebrow">Ficha bibliográfica · Publicación oficial</p>
    <h1 class="libro-titulo">Concursos Nacionales de la Olimpiada Mexicana de Matemáticas:1987-2016</h1>
    <p class="oficial-hero-autores">Jose Antonio Gómez Ortega · Carlos Jacob Rubio Barrios · Rogelio Valdez Delgado</p>
    <div class="chips"><span class="chip">Papirhos</span><span class="chip">Icosaedro</span><span class="chip">Núm. 3</span></div>
  </div>
</section>

<section class="libro-seccion libro-resumen">
  <h2>Resumen</h2>
  <p>Resumen no disponible por el momento.</p>
</section>


<section class="libro-seccion libro-ediciones" id="ediciones-pap-ico-3">
  <h2>Ediciones disponibles</h2>
  <div class="edition-selector">
    <div class="edition-buttons" role="group" aria-label="Seleccionar edición">
      <button type="button" class="edition-button active" data-target="oficial-edicion-pap-ico-3-0" aria-controls="oficial-edicion-pap-ico-3-0" aria-expanded="true">Datos bibliográficos</button>
    </div>
    <div class="edition-content">
<div class="edition-panel" id="oficial-edicion-pap-ico-3-0">
  <section class="libro-subseccion libro-metadatos">
    <h3>Metadatos</h3>
    
    <div class="oficial-tabla-contenedor"><table><tbody><tr><th scope="row">Autores</th><td>Jose Antonio Gómez Ortega, Carlos Jacob Rubio Barrios, Rogelio Valdez Delgado</td></tr><tr><th scope="row">Colección</th><td>Papirhos</td></tr><tr><th scope="row">Serie</th><td>Icosaedro</td></tr><tr><th scope="row">Número de serie</th><td>3</td></tr><tr><th scope="row">Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr></tbody></table></div>
  </section>
  <section class="libro-subseccion libro-cita">
    <h3>Cómo citar</h3>
    <div class="citation-box">
      <blockquote id="oficial-cita-pap-ico-3-0">Jose Antonio Gómez Ortega, Carlos Jacob Rubio Barrios, Rogelio Valdez Delgado. (s. f.). <em>Concursos Nacionales de la Olimpiada Mexicana de Matemáticas:1987-2016</em>. Instituto de Matemáticas, UNAM.</blockquote>
      <button type="button" class="citation-copy-button" data-copy-id="oficial-cita-pap-ico-3-0" data-copy-type="text">Copiar cita</button>
    </div>
    <details class="oficial-bibtex">
      <summary>BibTeX</summary>
      <textarea readonly id="oficial-bibtex-pap-ico-3-0" rows="9" class="verbatim">@book{ed-008,
  title = {Concursos Nacionales de la Olimpiada Mexicana de Matemáticas:1987-2016},
  author = {Jose Antonio Gómez Ortega and Carlos Jacob Rubio Barrios and Rogelio Valdez Delgado},
  publisher = {Instituto de Matemáticas, UNAM},
  series = {Icosaedro},
  number = {3}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-copy-id="oficial-bibtex-pap-ico-3-0" data-copy-type="value">Copiar BibTeX</button>
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
    <a href="../../archivos_preprints/pap-ico-3-v1.pdf" class="md-button md-button--primary" target="_blank" rel="noopener noreferrer">Abrir PDF</a>
    <a href="../../archivos_preprints/pap-ico-3-v1.pdf" class="md-button preprint-secondary-button" download>Descargar PDF</a>
  </div>
  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/pap-ico-3-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/pap-ico-3-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
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

