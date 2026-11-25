"""Comprueba enlaces locales del sitio generado por MkDocs.

Uso desde la raíz del repositorio:
    python tools/verifica_enlaces.py

No modifica archivos. Las URL externas no se comprueban.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
# Prefijo público definido en site_url de mkdocs.yml
SITE_PREFIX = "/Sitio-TeXedores/"


class Referencias(HTMLParser):
    ATRIBUTOS = {"a": "href", "img": "src", "link": "href", "script": "src", "object": "data", "source": "src", "iframe": "src"}

    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        atributo = self.ATRIBUTOS.get(tag)
        if atributo:
            valor = dict(attrs).get(atributo)
            if valor:
                self.refs.append((tag, valor))


def destino_local(origen, enlace):
    if "{{" in enlace or "{%" in enlace:
        return None  # Plantillas copiadas tal cual a site/; no son HTML publicado
    parsed = urlsplit(enlace)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None

    ruta = unquote(parsed.path)
    if ruta.startswith(SITE_PREFIX):
        destino = SITE / ruta[len(SITE_PREFIX):]
    elif ruta.startswith("/"):
        destino = SITE / ruta.lstrip("/")
    else:
        destino = origen.parent / ruta
    if destino.is_dir() or not destino.suffix:
        destino = destino / "index.html"
    return destino


def main():
    if not SITE.is_dir():
        raise SystemExit("No existe site/. Primero ejecuta: mkdocs build")

    total = 0
    errores = []
    htmls = list(SITE.rglob("*.html"))
    for pagina in htmls:
        # MkDocs también puede copiar fuentes de plantillas en docs/overrides.
        if "overrides" in pagina.relative_to(SITE).parts:
            continue
        parser = Referencias()
        parser.feed(pagina.read_text(encoding="utf-8", errors="replace"))
        for etiqueta, url in parser.refs:
            destino = destino_local(pagina, url)
            if destino is None:
                continue
            total += 1
            if not destino.is_file():
                errores.append((pagina.relative_to(SITE), etiqueta, url))

    print(f"Páginas HTML revisadas: {len(htmls)}")
    print(f"Referencias internas comprobadas: {total}")
    if errores:
        print(f"Enlaces internos rotos: {len(errores)}")
        for pagina, etiqueta, url in errores[:40]:
            print(f" - {pagina}: <{etiqueta}> {url}")
        raise SystemExit(1)
    print("Sin enlaces internos rotos detectados.")


if __name__ == "__main__":
    main()
