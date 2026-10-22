/* Búsqueda unificada de TeXedores.
 * Lee las dos fuentes originales; NO mezcla ni reescribe sus registros ni PDFs.
 * Las URL se calculan desde este script, así funciona localmente y en GitHub Pages.
 */
(() => {
  "use strict";

  const BASE = new URL("../", document.currentScript.src).href;
  const raiz = document.querySelector(".busqueda-unificada");
  if (!raiz) return;
  const $ = selector => raiz.querySelector(selector);
  const resultados = $("#resultados");
  const contador = $("#contador");
  const aviso = $("#busqueda-aviso");
  const coleccion = $("#f-coleccion");
  const serie = $("#f-serie");
  const anio = $("#f-anio");
  const autor = $("#f-autor");
  const titulo = $("#f-titulo");
  const palabra = $("#f-palabra");
  const orden = $("#f-order");
  const limpiar = $("#btn-clear");
  let publicaciones = [];

  const texto = valor => String(valor ?? "");
  const normalizar = valor => texto(valor).normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "").toLowerCase().trim();
  const escapar = valor => texto(valor).replace(/[&<>"']/g, caracter => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[caracter]));
  const ruta = archivo => texto(archivo).split("/").map(encodeURIComponent).join("/");
  const unico = lista => [...new Set(lista.filter(Boolean))];
  const resumenHTML = valor => escapar(valor).replace(/&lt;br\s*\/?&gt;/gi, "<br>");


  // Cada documento sigue siendo un resultado distinto, aunque tenga el mismo ID.
  function normalizarOficial(x) {
    const anios = unico([
      ...(Array.isArray(x.anios_edicion) ? x.anios_edicion : []),
      x.anio,
      ...(Array.isArray(x.ediciones) ? x.ediciones.map(e => e.anio) : [])
    ].map(texto).map(s => s.trim())).filter(a => /^\d{4}$/.test(a));
    const fecha = anios.length ? [...anios].sort().at(-1) : "";
    return {
      tipo: "oficial", id: texto(x.id), titulo: texto(x.titulo),
      autores: Array.isArray(x.autores) ? x.autores.map(texto) : [],
      coleccion: texto(x.coleccion), serie: texto(x.serie),
      resumen: texto(x.resumen), portada: texto(x.portada),
      pdf: texto(x.pdf), anios, fecha,
      impreso: x.impreso_disponible === true, preprintDisponible: false,
      extra: [x.num_serie, x.isbn_libro, x.isbn_col, x.editorial, x.edicion]
        .map(texto).join(" ")
    };
  }

  function normalizarPreprint(x, oficiales) {
    const fecha = texto(x.fecha);
    const id = texto(x.id_preprint);
    const oficial = oficiales.get(id);
    // La colección y la serie pertenecen a la obra publicada, no al preprint
    // por sí solo. Si no hay publicación oficial, se dejan vacías.
    return {
      tipo: "preprint", id, titulo: texto(x.titulo),
      autores: Array.isArray(x.autores) ? x.autores.map(texto) : [],
      coleccion: oficial ? oficial.coleccion : "",
      serie: oficial ? oficial.serie : "",
      resumen: texto(x.resumen), portada: texto(x.portada),
      pdf: texto(x.pdf),
      anios: /^\d{4}/.test(fecha) ? [fecha.slice(0, 4)] : [],
      fecha, tieneOficial: !!oficial,
      extra: oficial ? oficial.extra : ""
    };
  }

  function tituloAsc(a, b) {
    return a.titulo.localeCompare(b.titulo, "es", { sensitivity: "base" }) ||
      a.tipo.localeCompare(b.tipo) || a.id.localeCompare(b.id);
  }

  function comparar(a, b) {
    if (orden.value === "titulo-asc") return tituloAsc(a, b);
    if (orden.value === "titulo-desc") return -tituloAsc(a, b);
    // Fechas ISO y años de 4 dígitos pueden compararse lexicográficamente;
    // los registros sin año quedan al final en ambos sentidos.
    if (!a.fecha && !b.fecha) return tituloAsc(a, b);
    if (!a.fecha) return 1;
    if (!b.fecha) return -1;
    const cmp = a.fecha.localeCompare(b.fecha);
    return (orden.value === "fecha-asc" ? cmp : -cmp) || tituloAsc(a, b);
  }

  function seleccionTipo() {
    return raiz.querySelector('input[name="tipo-publicacion"]:checked')?.value || "ambas";
  }
  function listaTipo() {
    const tipo = seleccionTipo();
    return publicaciones.filter(item => tipo === "ambas" || item.tipo === tipo);
  }

  // Al seleccionar tipo de publicación, solo se ofrecen filtros relevantes.
  function actualizarOpciones(selector, valores, valorPredeterminado) {
    const anterior = selector.value;
    selector.replaceChildren(new Option(valorPredeterminado, ""));
    valores.forEach(valor => selector.add(new Option(valor, valor)));
    selector.value = valores.includes(anterior) ? anterior : "";
  }

  function actualizarSelectores() {
    const base = listaTipo();
    actualizarOpciones(coleccion,
      unico(base.map(x => x.coleccion)).sort((a, b) => a.localeCompare(b, "es")),
      "Todas");
    actualizarOpciones(serie,
      unico(base.map(x => x.serie)).sort((a, b) => a.localeCompare(b, "es")),
      "Todas");
    actualizarOpciones(anio,
      unico(base.flatMap(x => x.anios)).sort((a, b) => b.localeCompare(a)),
      "Todos");
  }

  function coincide(item) {
    const eq = (valor, filtro) => !filtro || valor === filtro;
    const contiene = (valor, filtro) => !filtro || normalizar(valor).includes(normalizar(filtro));
    return eq(item.coleccion, coleccion.value) &&
      eq(item.serie, serie.value) &&
      (!anio.value || item.anios.includes(anio.value)) &&
      contiene(item.autores.join(" "), autor.value) &&
      contiene(item.titulo, titulo.value) &&
      contiene([
        item.id, item.titulo, item.resumen, item.coleccion, item.serie,
        item.autores.join(" "), item.extra
      ].join(" "), palabra.value);
  }

  function tarjeta(item) {
    const isOficial = item.tipo === "oficial";
    const ficha = `${BASE}${isOficial ? "publicaciones" : "preprints"}/${encodeURIComponent(item.id)}/`;
    const portada = item.portada ? `
      <img src="${BASE}portadas_preprints/${ruta(item.portada)}"
        alt="Portada de ${escapar(item.titulo)}" loading="lazy">` : "";
    const placeholder = `<div class="preprint-cover preprint-cover-placeholder"><span>${escapar(item.id)}</span><small>${isOficial ? "Publicación" : "Preprint"}</small></div>`;
    const cubierta = portada ? `<div class="preprint-cover">${portada}</div>` : placeholder;
    const datoFecha = isOficial
      ? (item.fecha ? `Edición: ${escapar(item.fecha)}` : "Publicación oficial")
      : (item.fecha ? `Disponible desde: ${escapar(item.fecha)}` : "Preprint");
    const descripcion = item.resumen ? `
      <div class="preprint-summary-wrapper">
        <p class="preprint-summary preprint-summary-collapsed">${resumenHTML(item.resumen)}</p>
        <button type="button" class="preprint-summary-toggle" hidden>Ver más</button>
      </div>` : "";
    const badges = [
      `<span class="tex-disponibilidad__badge ${isOficial ? '' : 'tex-disponibilidad__badge--preprint'}">${isOficial ? 'Publicación oficial' : 'Preprint'}</span>`
    ];
    if (item.pdf) badges.push('<span class="tex-disponibilidad__badge">PDF disponible</span>');
    if (isOficial && item.impreso) badges.push('<span class="tex-disponibilidad__badge">Impreso disponible</span>');
    if (isOficial && item.preprintDisponible) badges.push('<span class="tex-disponibilidad__badge tex-disponibilidad__badge--preprint">Preprint disponible</span>');
    if (!isOficial && item.tieneOficial) badges.push('<span class="tex-disponibilidad__badge">Edición oficial disponible</span>');
    const disponibilidad = `<div class="tex-disponibilidad" aria-label="Disponibilidad">${badges.join('')}</div>`;
    const botonPdf = item.pdf ? `<a class="md-button preprint-secondary-button" href="${BASE}${ruta(item.pdf)}" target="_blank" rel="noopener">Ver PDF</a>` : "";

    return `<article class="preprint-card busqueda-tarjeta ${isOficial ? "busqueda-oficial" : "busqueda-preprint"}">
      <div class="preprint-card-layout">
        ${cubierta}
        <div class="preprint-card-main">
          <div class="preprint-card-top">
            <span class="preprint-id">${escapar(item.id)}</span>
            <span class="busqueda-clase">${isOficial ? "Publicación oficial" : "Preprint"}</span>
          </div>
          <div class="preprint-card-content">
            <h3 class="preprint-title"><a href="${ficha}">${escapar(item.titulo)}</a></h3>
            <p class="preprint-authors">${escapar(item.autores.join(" · "))}</p>
            ${descripcion}
            <div class="busqueda-preprint-meta">
              ${item.coleccion ? `<span><strong>Colección:</strong> ${escapar(item.coleccion)}</span>` : ""}
              ${item.serie ? `<span><strong>Serie:</strong> ${escapar(item.serie)}</span>` : ""}
              <span>${datoFecha}</span>
            </div>
          </div>
          <div class="preprint-card-footer">
            ${disponibilidad}
            <div class="preprint-actions">
              <a class="md-button md-button--primary" href="${ficha}">Ver ficha</a>
              ${botonPdf}
            </div>
          </div>
        </div>
      </div>
    </article>`;
  }

  function prepararResumenes() {
    resultados.querySelectorAll(".preprint-summary-wrapper").forEach(wrapper => {
      const resumen = wrapper.querySelector(".preprint-summary");
      const boton = wrapper.querySelector(".preprint-summary-toggle");
      if (!resumen || !boton) return;
      boton.hidden = resumen.scrollHeight <= resumen.clientHeight + 2;
    });
  }

  function filtrar() {
    const visibles = listaTipo().filter(coincide).sort(comparar);
    const oficiales = visibles.filter(x => x.tipo === "oficial").length;
    const preprints = visibles.length - oficiales;
    contador.textContent = `${visibles.length} ${visibles.length === 1 ? "resultado" : "resultados"} · ${oficiales} ${oficiales === 1 ? "oficial" : "oficiales"} · ${preprints} ${preprints === 1 ? "preprint" : "preprints"}`;
    resultados.innerHTML = visibles.length
      ? visibles.map(tarjeta).join("")
      : '<div class="preprints-no-results"><strong>No se encontraron publicaciones.</strong><span>Prueba con otros filtros o limpia la búsqueda.</span></div>';
    requestAnimationFrame(prepararResumenes);
    resultados.setAttribute("aria-busy", "false");
  }

  resultados.addEventListener("click", event => {
    const boton = event.target.closest(".preprint-summary-toggle");
    if (!boton) return;
    const resumen = boton.closest(".preprint-summary-wrapper")?.querySelector(".preprint-summary");
    if (!resumen) return;
    const contraido = resumen.classList.toggle("preprint-summary-collapsed");
    boton.textContent = contraido ? "Ver más" : "Ver menos";
    boton.setAttribute("aria-expanded", String(!contraido));
  });

  raiz.querySelectorAll('input[name="tipo-publicacion"]').forEach(radio => {
    radio.addEventListener("change", () => { actualizarSelectores(); filtrar(); });
  });
  [coleccion, serie, anio, orden].forEach(elemento => elemento.addEventListener("change", filtrar));
  [autor, titulo, palabra].forEach(elemento => elemento.addEventListener("input", filtrar));
  limpiar.addEventListener("click", () => {
    raiz.querySelector('input[name="tipo-publicacion"][value="ambas"]').checked = true;
    [autor, titulo, palabra].forEach(input => { input.value = ""; });
    [coleccion, serie, anio].forEach(select => { select.value = ""; });
    orden.value = "fecha-desc";
    actualizarSelectores();
    filtrar();
    palabra.focus();
  });
  window.addEventListener("resize", () => requestAnimationFrame(prepararResumenes));

  async function cargar(nombre) {
    const respuesta = await fetch(`${BASE}data/${nombre}`);
    if (!respuesta.ok) throw new Error(`${nombre}: error HTTP ${respuesta.status}`);
    const datos = await respuesta.json();
    if (!Array.isArray(datos)) throw new Error(`${nombre}: se esperaba una lista`);
    return datos;
  }

  Promise.allSettled([cargar("catalogo.json"), cargar("preprints.json")]).then(([oficiales, preprints]) => {
    const mapaOficial = new Map();
    if (oficiales.status === "fulfilled") {
      oficiales.value.map(normalizarOficial).forEach(item => {
        publicaciones.push(item);
        mapaOficial.set(item.id, item);
      });
    }
    if (preprints.status === "fulfilled") {
      preprints.value.map(x => normalizarPreprint(x, mapaOficial)).forEach(item => {
        publicaciones.push(item);
        const oficial = mapaOficial.get(item.id);
        if (oficial && item.pdf) oficial.preprintDisponible = true;
      });
    }
    if (oficiales.status === "rejected" || preprints.status === "rejected") {
      const faltantes = [
        oficiales.status === "rejected" ? "catalogo.json" : null,
        preprints.status === "rejected" ? "preprints.json" : null
      ].filter(Boolean);
      aviso.textContent = `No se pudo cargar ${faltantes.join(" y ")}. Revisa los archivos en docs/data/.`;
      aviso.hidden = false;
    }
    actualizarSelectores();
    filtrar();
  });
})();
