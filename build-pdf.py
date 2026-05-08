#!/usr/bin/env python3
"""
build-pdf.py — Converte DIAGNOSTICO.md em PDF estilizado.

Uso: python build-pdf.py [arquivo.md]
Padrão: DIAGNOSTICO.md -> DIAGNOSTICO.pdf

Pipeline:
  1. Lê markdown
  2. Converte para HTML com extensões (tables, fenced_code, toc)
  3. Aplica CSS herdado do design system do glsuite.com.br
  4. Renderiza PDF via Chrome headless

Requer: Python 3.8+ com `markdown` instalado, Chrome instalado.
"""
import sys
import os
import subprocess
import tempfile
from pathlib import Path

import markdown

# Garante UTF-8 no stdout do Windows (cp1252 default quebra com setas/acentos)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Montserrat:wght@400;700;800;900&display=swap');

@page {
  size: A4;
  margin: 18mm 16mm 20mm 16mm;
  @bottom-right {
    content: "Página " counter(page) " / " counter(pages);
    font-family: "JetBrains Mono", monospace;
    font-size: 8pt;
    color: #6b6b75;
  }
  @bottom-left {
    content: "GL Suite · Diagnóstico · Maio 2026";
    font-family: "JetBrains Mono", monospace;
    font-size: 8pt;
    color: #6b6b75;
  }
}

:root {
  --bg: #fff;
  --ink: #0a0a0f;
  --ink-soft: #2a2a33;
  --ink-mute: #6b6b75;
  --rule: rgba(10,10,15,.12);
  --rule-soft: rgba(10,10,15,.06);
  --accent: #0014ff;
  --accent-wash: rgba(0,20,255,.06);
  --bg-deep: #f5f4ef;
  --card-bg: #fff;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: "DM Sans", -apple-system, system-ui, sans-serif;
  font-size: 10.5pt;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

.cover {
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 245mm;
  padding-top: 12mm;
}
.cover-top {
  display: flex; align-items: center; justify-content: space-between;
}
.brand {
  display: flex; align-items: center; gap: 8pt;
  font-family: "Montserrat", sans-serif; font-weight: 800; font-size: 13pt;
  letter-spacing: -0.01em;
}
.brand-mark {
  width: 22pt; height: 22pt; border-radius: 4pt;
  background: var(--ink); color: #fff;
  display: grid; place-items: center;
  font-family: "JetBrains Mono", monospace; font-size: 11pt; font-weight: 700;
}
.cover-meta {
  font-family: "JetBrains Mono", monospace;
  font-size: 8pt; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--ink-mute);
  text-align: right;
}
.cover-mid h1 {
  font-family: "Montserrat", sans-serif;
  font-weight: 900;
  font-size: 44pt;
  line-height: 1.0;
  letter-spacing: -0.035em;
  color: var(--ink);
  margin: 0 0 14pt 0;
  max-width: 90%;
}
.cover-mid h1 em { font-style: normal; color: var(--accent); }
.cover-mid p.lead {
  font-size: 13pt; color: var(--ink-soft); line-height: 1.45;
  max-width: 80%; margin: 0 0 28pt 0;
}
.cover-tags {
  display: flex; flex-wrap: wrap; gap: 6pt;
}
.cover-tag {
  font-family: "JetBrains Mono", monospace;
  font-size: 8pt; font-weight: 500;
  letter-spacing: 0.06em; text-transform: uppercase;
  padding: 4pt 9pt; border-radius: 999pt;
  background: var(--accent-wash); color: var(--accent);
}
.cover-bottom {
  border-top: 1px solid var(--rule);
  padding-top: 12pt;
  display: flex; justify-content: space-between;
  font-family: "JetBrains Mono", monospace;
  font-size: 8pt; letter-spacing: 0.05em;
  text-transform: uppercase; color: var(--ink-mute);
}

.content { padding: 0; }

h1, h2, h3, h4 {
  font-family: "Montserrat", sans-serif;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--ink);
  margin: 18pt 0 8pt;
  page-break-after: avoid;
  page-break-inside: avoid;
}
h1 { font-size: 24pt; font-weight: 900; letter-spacing: -0.03em; margin-top: 0; padding-bottom: 6pt; border-bottom: 2px solid var(--ink); page-break-before: always; }
h1:first-child { page-break-before: auto; }
h2 { font-size: 16pt; margin-top: 22pt; padding-bottom: 4pt; border-bottom: 1px solid var(--rule); }
h3 { font-size: 12.5pt; margin-top: 14pt; }
h4 { font-size: 11pt; margin-top: 10pt; color: var(--accent); text-transform: uppercase; letter-spacing: 0.04em; }

p { margin: 0 0 8pt; }
p + h2, p + h3 { margin-top: 18pt; }

strong { font-weight: 700; color: var(--ink); }
em { font-style: italic; }

code {
  font-family: "JetBrains Mono", monospace;
  font-size: 9.5pt;
  background: var(--bg-deep);
  padding: 1pt 4pt;
  border-radius: 3pt;
  color: var(--ink);
}

pre {
  background: var(--bg-deep);
  border: 1px solid var(--rule-soft);
  border-radius: 6pt;
  padding: 10pt 12pt;
  overflow-x: auto;
  page-break-inside: avoid;
  margin: 8pt 0;
}
pre code {
  background: transparent;
  padding: 0;
  font-size: 9pt;
  line-height: 1.5;
}

blockquote {
  border-left: 3px solid var(--accent);
  background: var(--accent-wash);
  margin: 8pt 0;
  padding: 8pt 12pt;
  color: var(--ink-soft);
  page-break-inside: avoid;
  border-radius: 0 4pt 4pt 0;
}
blockquote p { margin: 0; }
blockquote strong { color: var(--accent); }

ul, ol {
  margin: 6pt 0 10pt;
  padding-left: 18pt;
}
li { margin-bottom: 3pt; }
li > ul, li > ol { margin-top: 3pt; }

hr {
  border: none;
  border-top: 1px solid var(--rule);
  margin: 18pt 0;
}

a {
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid var(--accent-wash);
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 8pt 0 12pt;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
thead { background: var(--ink); }
thead th {
  color: #fff;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  text-align: left;
  padding: 6pt 8pt;
  font-size: 9pt;
  letter-spacing: 0.01em;
}
tbody tr { border-bottom: 1px solid var(--rule-soft); }
tbody tr:nth-child(even) { background: rgba(245,244,239,.5); }
tbody td {
  padding: 6pt 8pt;
  vertical-align: top;
  line-height: 1.4;
}
tbody td:first-child { font-weight: 500; }

/* Tabelas com a primeira coluna numérica destacada */
table.tight { font-size: 9pt; }

/* Avoid awkward breaks */
table, pre, blockquote { page-break-inside: avoid; }
h2 + table, h3 + table { margin-top: 4pt; }
"""

COVER_HTML = """
<section class="cover">
  <div>
    <div class="cover-top">
      <div class="brand"><span class="brand-mark">GL</span><span>Suite</span></div>
      <div class="cover-meta">
        Documento de Revisão<br>
        Maio 2026 · v1.0
      </div>
    </div>
  </div>

  <div class="cover-mid">
    <h1>Diagnóstico <em>GL Suite</em>.<br>Lógica do quiz.</h1>
    <p class="lead">Material para revisão pela diretoria. Apresenta a lógica completa do quiz da LP2, todas as perguntas com pontuação, cenários de exemplo e pontos abertos.</p>
    <div class="cover-tags">
      <span class="cover-tag">8 perguntas</span>
      <span class="cover-tag">8 ferramentas</span>
      <span class="cover-tag">3 cenários</span>
      <span class="cover-tag">12 pontos abertos</span>
    </div>
  </div>

  <div class="cover-bottom">
    <span>GuessLess · GL Suite</span>
    <span>Confidencial · Uso interno</span>
  </div>
</section>
"""


def md_to_html(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    # Remove a primeira H1 e a linha de "blockquote" introdutória do MD
    # porque já estão na capa
    lines = text.splitlines()
    out_lines = []
    skip_intro = True
    seen_first_section = False
    for line in lines:
        if skip_intro:
            # Pula até a primeira H2 (--- mantém)
            if line.startswith("## "):
                skip_intro = False
                seen_first_section = True
                out_lines.append(line)
                continue
            else:
                continue
        out_lines.append(line)
    cleaned = "\n".join(out_lines)

    body_html = markdown.markdown(
        cleaned,
        extensions=["tables", "fenced_code", "sane_lists", "smarty"],
        output_format="html5",
    )
    return body_html


def build_html_doc(body: str) -> str:
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Diagnóstico GL Suite — Documento de Revisão</title>
<style>{CSS}</style>
</head>
<body>
{COVER_HTML}
<section class="content">
{body}
</section>
</body>
</html>"""


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    if not Path(CHROME).exists():
        raise FileNotFoundError(f"Chrome não encontrado em {CHROME}")
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--no-margins",
        f"--print-to-pdf={pdf_path}",
        f"file:///{html_path.as_posix()}",
    ]
    print("→ Renderizando PDF com Chrome headless…")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print("STDERR:", result.stderr)
        raise RuntimeError("Chrome falhou ao gerar o PDF")


def main():
    md_name = sys.argv[1] if len(sys.argv) > 1 else "DIAGNOSTICO.md"
    md_path = Path(md_name).resolve()
    if not md_path.exists():
        sys.exit(f"Arquivo {md_path} não encontrado")

    pdf_path = md_path.with_suffix(".pdf")
    print(f"→ Lendo {md_path.name}…")
    body = md_to_html(md_path)
    full = build_html_doc(body)

    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".html", delete=False
    ) as f:
        f.write(full)
        html_path = Path(f.name)
    print(f"→ HTML temporário: {html_path}")

    try:
        render_pdf(html_path, pdf_path)
        size_kb = pdf_path.stat().st_size / 1024
        print(f"✓ PDF gerado: {pdf_path} ({size_kb:.1f} KB)")
    finally:
        try:
            html_path.unlink()
        except OSError:
            pass


if __name__ == "__main__":
    main()
