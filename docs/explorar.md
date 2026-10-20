<section class="catalogo-hero catalogo-hero-busqueda">
  <p class="catalogo-eyebrow">Explorar</p>
  <h1>Búsqueda avanzada</h1>
  <p>Consulta publicaciones oficiales y preprints. Combina filtros por colección, serie, año, autor, título o palabra clave.</p>
</section>

<div class="busqueda-unificada">
  <fieldset class="busqueda-tipos">
    <legend>Tipo de publicación</legend>
    <div class="busqueda-tipos__opciones">
      <label class="busqueda-tipo">
        <input type="radio" name="tipo-publicacion" value="ambas" checked>
        <span>Todas las publicaciones</span>
      </label>
      <label class="busqueda-tipo">
        <input type="radio" name="tipo-publicacion" value="oficial">
        <span>Publicaciones oficiales</span>
      </label>
      <label class="busqueda-tipo">
        <input type="radio" name="tipo-publicacion" value="preprint">
        <span>Preprints</span>
      </label>
    </div>
  </fieldset>

  <div id="filtros" class="busqueda-filtros">
    <label for="f-coleccion">Colección
      <select id="f-coleccion"><option value="">Todas</option></select>
    </label>
    <label for="f-serie">Serie
      <select id="f-serie"><option value="">Todas</option></select>
    </label>
    <label for="f-anio">Año (publicación o actualización)
      <select id="f-anio"><option value="">Todos</option></select>
    </label>
    <label for="f-autor">Autor
      <input id="f-autor" type="search" placeholder="Ej. Brasselet" autocomplete="off">
    </label>
    <label for="f-titulo">Título
      <input id="f-titulo" type="search" placeholder="Buscar por título" autocomplete="off">
    </label>
    <label for="f-palabra">Palabra clave
      <input id="f-palabra" type="search" placeholder="ID, resumen, ISBN..." autocomplete="off">
    </label>
    <label for="f-order">Ordenar por
      <select id="f-order">
        <option value="fecha-desc">Más recientes</option>
        <option value="fecha-asc">Más antiguos</option>
        <option value="titulo-asc">Título (A → Z)</option>
        <option value="titulo-desc">Título (Z → A)</option>
      </select>
    </label>
    <button id="btn-clear" type="button" class="md-button">Limpiar filtros</button>
  </div>

  <div class="busqueda-resultados-header" aria-live="polite">
    <span id="contador">Cargando publicaciones…</span>
  </div>
  <p id="busqueda-aviso" class="busqueda-aviso" role="status" hidden></p>
  <div id="resultados" aria-live="polite" aria-busy="true"></div>
</div>

<link rel="stylesheet" href="../stylesheets/busqueda-unificada.css">
<script defer src="../js/busqueda-unificada.js"></script>
