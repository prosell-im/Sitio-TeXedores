
document.addEventListener("DOMContentLoaded", function () {

  // =====================================
  // 1. MENÚ DE LA BARRA SUPERIOR
  // =====================================

  const dropdown = document.querySelector(
    ".publicaciones-dropdown"
  );

  if (dropdown) {
    const boton = dropdown.querySelector("summary");
    const menu = dropdown.querySelector(
      ".publicaciones-dropdown__menu"
    );

    if (boton && menu) {
      // Sacamos el panel de la barra para evitar
      // que los estilos de MkDocs lo recorten.
      document.body.appendChild(menu);

      menu.id = "menu-publicaciones-superior";
      boton.setAttribute("aria-controls", menu.id);
      boton.setAttribute("aria-expanded", "false");

      dropdown.open = false;

      function posicionarMenu() {
        const rect = boton.getBoundingClientRect();
        const ancho = Math.min(290, window.innerWidth - 24);

        const izquierda = Math.max(
          12,
          Math.min(rect.left, window.innerWidth - ancho - 12)
        );

        menu.style.width = ancho + "px";
        menu.style.left = izquierda + "px";
        menu.style.top = rect.bottom + 8 + "px";
        menu.style.maxHeight =
          Math.max(120, window.innerHeight - rect.bottom - 24)
          + "px";
      }

      function cerrarMenu() {
        dropdown.open = false;
        menu.classList.remove("is-open");
        boton.setAttribute("aria-expanded", "false");
      }

      function abrirMenu() {
        posicionarMenu();
        dropdown.open = true;
        menu.classList.add("is-open");
        boton.setAttribute("aria-expanded", "true");
      }

      boton.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();

        if (dropdown.open) {
          cerrarMenu();
        } else {
          abrirMenu();
        }
      });

      document.addEventListener("click", function (event) {
        if (
          !dropdown.contains(event.target) &&
          !menu.contains(event.target)
        ) {
          cerrarMenu();
        }
      });

      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
          cerrarMenu();
        }
      });

      window.addEventListener("resize", function () {
        if (dropdown.open) {
          posicionarMenu();
        }
      });

      window.addEventListener("scroll", function () {
        if (dropdown.open) {
          cerrarMenu();
        }
      }, true);
    }
  }


  // =====================================
  // 2. MENÚ LATERAL COMO ACORDEÓN
  // =====================================

  const secciones = document.querySelectorAll(
    ".md-sidebar--primary .md-nav__item--nested"
  );

  secciones.forEach((seccion) => {

    const etiqueta = seccion.querySelector(
      ":scope > label.md-nav__link"
    );

    const navegacion = seccion.querySelector(
      ":scope > nav.md-nav"
    );

    const titulo = etiqueta
      ?.querySelector(".md-ellipsis")
      ?.textContent.trim();

    if (
      titulo !== "Nuestras publicaciones" ||
      !navegacion
    ) return;

    // Recuperamos las opciones que ya creó MkDocs
    const enlaces = navegacion.querySelectorAll(
      ":scope > ul.md-nav__list > li.md-nav__item > a.md-nav__link"
    );

    if (!enlaces.length) return;

    if (seccion.classList.contains("pub-acordeon")) return;

    // Crear un botón independiente del menú de MkDocs
    const boton = document.createElement("button");
    boton.type = "button";
    boton.className = "pub-acordeon__boton";
    boton.setAttribute("aria-expanded", "false");
    boton.setAttribute("aria-controls", "pub-acordeon-opciones");

    const nombre = document.createElement("span");
    nombre.textContent = "Nuestras publicaciones";

    const flecha = document.createElement("span");
    flecha.className = "pub-acordeon__flecha";
    flecha.setAttribute("aria-hidden", "true");

    boton.append(nombre, flecha);

    // Crear la lista que aparecerá debajo
    const lista = document.createElement("ul");
    lista.id = "pub-acordeon-opciones";
    lista.className = "pub-acordeon__opciones";

    enlaces.forEach((original) => {

      const li = document.createElement("li");
      const enlace = document.createElement("a");

      enlace.href = original.href;

      enlace.textContent =
        original.querySelector(".md-ellipsis")
          ?.textContent.trim()
        || original.textContent.trim();

      // Identificar la página actual
      if (original.classList.contains("md-nav__link--active")) {
        enlace.classList.add("es-actual");
        enlace.setAttribute("aria-current", "page");
      }

      li.appendChild(enlace);
      lista.appendChild(li);

    });

    seccion.classList.add("pub-acordeon");
    seccion.append(boton, lista);

    // Abrir y cerrar sin activar la navegación de MkDocs
    boton.addEventListener("click", (evento) => {

      evento.preventDefault();
      evento.stopPropagation();

      const abrir =
        boton.getAttribute("aria-expanded") !== "true";

      boton.setAttribute("aria-expanded", String(abrir));

      seccion.classList.toggle("abierto", abrir);

    });

  });

});
