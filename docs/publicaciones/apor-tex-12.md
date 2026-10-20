---
title: "Introducción a la teoría de redes"
---

<div class="oficial-detalle">
<section class="libro-hero">
  <div class="libro-hero-portada"><img src="../../portadas_preprints/apor-tex-12.png" alt="Portada de Introducción a la teoría de redes" loading="lazy"></div>
  <div class="libro-hero-contenido">
    <p class="libro-eyebrow">Ficha bibliográfica · Publicación oficial</p>
    <h1 class="libro-titulo">Introducción a la teoría de redes</h1>
    <p class="oficial-hero-autores">María del Carmen Hernández Ayuso</p>
    <div class="chips"><span class="chip">Aportaciones Matemáticas</span><span class="chip">Textos</span><span class="chip">Núm. 12</span></div>
  </div>
</section>

<section class="libro-seccion libro-resumen">
  <h2>Resumen</h2>
  <p>Este libro está enfocado a los temas básicos de teoría de redes. Se presentan tanto teoría general y características de los problemas de optimización de esta rama como algoritmos para resolverlos.<br>Se exponen cuatro problemas básicos: árbol de peso mínimo, ruta más corta, flujo máximo y flujo a costo mínimo; estos problemas han sido resueltos principalmente mediante dos enfoques generales. Uno consiste en especializar los algoritmos de programación lineal aprovechando la estructura de cada problema y el otro en aplicar resultados de teoría de gráficas. En los primeros cinco capítulos se presentan algunos algoritmos para resolver problemas de flujo en redes según el enfoque clásico de la programación lineal. En los últimos dos capítulos se presentan generalizaciones de dos de estos problemas según el enfoque de coloración en gráficas.<br>La teoría de dualidad ha sido estudiada para el caso de los modelos de redes; con esto se han generado algoritmos de solución simultánea para el par de problemas duales. Este es el caso de los problemas de flujo máximo y de cadena mínima.<br>En cada capítulo se incluyen conceptos, resultados teóricos rigurosamente demostrados, técnicas, ejemplos numéricos y una series de ejercicios propuestos.</p>
</section>


<section class="libro-seccion libro-ediciones" id="ediciones-apor-tex-12">
  <h2>Ediciones disponibles</h2>
  <div class="edition-selector">
    <div class="edition-buttons" role="group" aria-label="Seleccionar edición">
      <button type="button" class="edition-button active" data-target="oficial-edicion-apor-tex-12-0" aria-controls="oficial-edicion-apor-tex-12-0" aria-expanded="true">Datos bibliográficos</button>
    </div>
    <div class="edition-content">
<div class="edition-panel" id="oficial-edicion-apor-tex-12-0">
  <section class="libro-subseccion libro-metadatos">
    <h3>Metadatos</h3>
    
    <div class="oficial-tabla-contenedor"><table><tbody><tr><th scope="row">Autores</th><td>María del Carmen Hernández Ayuso</td></tr><tr><th scope="row">Colección</th><td>Aportaciones Matemáticas</td></tr><tr><th scope="row">Serie</th><td>Textos</td></tr><tr><th scope="row">Número de serie</th><td>12</td></tr></tbody></table></div>
  </section>
  <section class="libro-subseccion libro-cita">
    <h3>Cómo citar</h3>
    <div class="citation-box">
      <blockquote id="oficial-cita-apor-tex-12-0">María del Carmen Hernández Ayuso. (s. f.). <em>Introducción a la teoría de redes</em>.</blockquote>
      <button type="button" class="citation-copy-button" data-copy-id="oficial-cita-apor-tex-12-0" data-copy-type="text">Copiar cita</button>
    </div>
    <details class="oficial-bibtex">
      <summary>BibTeX</summary>
      <textarea readonly id="oficial-bibtex-apor-tex-12-0" rows="9" class="verbatim">@book{apor-tex-12,
  title = {Introducción a la teoría de redes},
  author = {María del Carmen Hernández Ayuso},
  series = {Textos},
  number = {12}
}</textarea>
      <button type="button" class="bibtex-copy-button" data-copy-id="oficial-bibtex-apor-tex-12-0" data-copy-type="value">Copiar BibTeX</button>
    </details>
  </section>
</div></div>
  </div>
</section>


<section class="libro-seccion relacion-fichas">
  <h2>Preprint relacionado</h2>
  <p>Esta publicación cuenta con una versión preliminar que incluye cambios
     todavía no incorporados a la publicación oficial.</p>
  <a class="md-button md-button--primary" href="../../preprints/apor-tex-12/">
    Consultar preprint
  </a>
</section>

<section class="libro-seccion libro-seccion-descargas oficial-pdf-seccion">
  <h2>Descargas</h2>
  <p>Abre, descarga o consulta el PDF de la publicación desde aquí.</p>
  <div class="pdf-mostrador">

  <div class="pdf-mostrador__acciones">
    <a href="../../archivos_preprints/apor-tex-12-v1.pdf" class="md-button md-button--primary" target="_blank" rel="noopener noreferrer">Abrir PDF</a>
    <a href="../../archivos_preprints/apor-tex-12-v1.pdf" class="md-button preprint-secondary-button" download>Descargar PDF</a>
  </div>
  <details class="pdf-mostrador__desplegable">
    <summary>Ver en línea (vista previa)</summary>
    <div class="pdf-mostrador__contenido">
      <object data="../../archivos_preprints/apor-tex-12-v1.pdf" type="application/pdf" class="pdf-mostrador__visor" aria-label="Vista previa del PDF">
        <p>Tu navegador no permite mostrar PDF dentro de la página. <a href="../../archivos_preprints/apor-tex-12-v1.pdf" target="_blank" rel="noopener noreferrer">Abrir PDF en otra pestaña</a>.</p>
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

