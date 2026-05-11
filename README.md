# LPs SPIW — GL Suite

Landing pages para o evento SPIW (14–16/05). HTML/CSS/JS estático, mobile-first, design herdado de glsuite.com.br.

## Estrutura

```
lp.glsuite.com.br/
├── spiw/
│   ├── index.html          → LP1 (catálogo + form RD Station)
│   └── obrigado.html       → pós-cadastro com CTA WhatsApp
├── diagnostico/
│   └── index.html          → LP2 (quiz 8 perguntas → captura → resultado)
├── produtos/               → 8 pitches de produto (6 slides cada)
│   ├── lpmaker/index.html       (template/spec — editado à mão)
│   ├── brandmeup/index.html
│   ├── gomarketer/index.html
│   ├── gl-forms/index.html
│   ├── dora/index.html
│   ├── atlas/index.html
│   ├── seo-insights/index.html
│   └── gl-data/index.html
└── tools/
    └── build-pitches.py    → regera os 7 pitches a partir do template LPMaker
```

URLs finais:

- **LP1**: `https://lp.glsuite.com.br/spiw/` — cards do catálogo linkam para `/produtos/<slug>`
- **Obrigado**: `https://lp.glsuite.com.br/spiw/obrigado.html`
- **LP2**: `https://lp.glsuite.com.br/diagnostico/`
- **Pitches**: `https://lp.glsuite.com.br/produtos/<slug>` — slugs: `lpmaker`, `brandmeup`, `gomarketer`, `gl-forms`, `dora`, `atlas`, `seo-insights`, `gl-data`

## Pitches de produto (6 slides cada)

Cada pitch é uma página de 1 arquivo (`produtos/<slug>/index.html`) com scroll-snap vertical e rail lateral de 6 dots. Estrutura dos slides:

1. **Abertura** — nome do produto, headline com accent, lead curta, badge da frente (Criação · Produtividade · Performance · BI)
2. **Problema** — 3 dores específicas que aquela ferramenta resolve
3. **Solução** — pitch core + 3 pilares
4. **Como Funciona** — 3 passos numerados em cards
5. **Ganho Prático** — stat grande + body explicando o impacto
6. **Fechamento** — CTA WhatsApp pré-preenchido com mensagem contextual do produto + agendar call

**Para editar o conteúdo dos pitches**, edite o dict `PRODUCTS` em `tools/build-pitches.py` e rode `python tools/build-pitches.py`. O LPMaker é o template/spec e é editado à mão — qualquer mudança estrutural (CSS, JS, layout) deve começar nele e depois rodar o script pra propagar.

## Antes de subir — checklist obrigatório

Em **ambos** os HTMLs (`spiw/index.html` e `diagnostico/index.html`), localize o bloco `CONFIG` no topo do `<script>` e substitua:

```js
RD_TOKEN: 'COLOQUE_AQUI_O_TOKEN_PUBLICO_RD'
```

→ pelo token público do formulário no painel do RD Station.

Os campos de conversão usados:

| Campo enviado | Origem |
|---|---|
| `identificador` | `lp-spiw-catalogo` (LP1) / `lp-spiw-diagnostico` (LP2) |
| `tags` | SPIW, catalogo, agendamento (LP1) · SPIW, diagnostico, quiz (LP2) |
| `email`, `nome`, `telefone`, `empresa` | form |
| `cf_origem` | identificação da LP |
| `cf_momento_empresa` (LP1) | seleção do select |
| `cf_fase`, `cf_top1`, `cf_top2`, `cf_top3`, `cf_dor_principal` (LP2) | calculados pelo quiz |

**Para alertar `midia@guessless.com.br` e disparar WhatsApp**: configure no RD Station um workflow que, ao receber lead com tag `SPIW`, envie e-mail pra você + integração com seu disparador de WhatsApp (n8n / Z-API / etc). Alternativamente, preencha `WEBHOOK_URL` no `CONFIG` pra disparar em paralelo um webhook próprio (n8n com Hefesto, por exemplo).

## Quiz da LP2 — lógica de scoring

8 perguntas. Cada resposta dá pontos para 1+ ferramentas. No final, top 3 ferramentas com maior pontuação são exibidas.

| # | Pergunta | Tipo | Peso | O que mede |
|---|---|---|---|---|
| 1 | Em qual momento sua empresa está? | única | x2 | Define a **fase** (Criação / Produtividade / Performance / BI) |
| 2 | Qual a maior dor agora? | única | x3 | Mais decisiva — atribui pontos pesados a 1 ferramenta |
| 3 | Quantas pessoas no time? | única | x1 | Sinaliza necessidade de gestão (Atlas) e BI |
| 4 | O que você já tem? | múltipla | x1 | A **falta** pontua a ferramenta correspondente |
| 5 | Investe em tráfego pago? | única | x1 | Sinaliza GL Data e SEO Insights |
| 6 | Como está sua presença orgânica? | única | x1 | SEO Insights |
| 7 | Como lança coisa nova? | única | x1 | Go to Marketer |
| 8 | Quanto tempo pra subir uma LP? | única | x1 | LPMaker |

Catálogo das 8 ferramentas no quiz: `lpmaker`, `brandmeup`, `gomarketer`, `gl-forms`, `dora`, `atlas`, `seo-insights`, `gl-data` (UTMize e GL Content estão "em breve" e ficaram fora).

Para ajustar o scoring, edite o array `QUESTIONS` no JS de `diagnostico/index.html`. Cada `option` tem um `score: { tool: pontos }`. Em perguntas `multi`, há também `absent: { tool: pontos }` (pontua quando NÃO marcado).

## Fluxo do quiz

```
INTRO → 8 PERGUNTAS → CAPTURA (form) → DIAGNÓSTICO (top 3 + WhatsApp)
```

- Perguntas de escolha única **avançam automaticamente** ao clicar (UX rápida pra estande).
- Múltipla escolha exige clicar em "Próxima".
- Captura acontece **antes** do resultado (gate de e-mail).
- Resultado mostra fase + 3 cards de ferramentas + CTA WhatsApp personalizado com nome, fase e top 3.

## Design system

Tokens herdados de `glsuite.com.br`:

- **Cores**: bg `#f5f4ef`, ink `#0a0a0f`, accent `#0014ff`
- **Fontes**: Montserrat (display), DM Sans (body), JetBrains Mono (labels)
- **Radius**: `0.5rem` / `1rem`
- **Container max**: `56rem` (LP1) / `38rem` (quiz)

CSS é inline em cada HTML pra simplicidade de deploy. Sem build step.

## Tracking (Meta Pixel + GA4) — estrutura cabeada, basta plugar IDs

Os 3 HTMLs já têm loader, `PageView` e eventos de conversão prontos. Sem IDs preenchidos, nada dispara (no-op).

Pra ativar, preencher em cada arquivo:

```js
META_PIXEL_ID: 'SEU_PIXEL_ID',
GA4_MEASUREMENT_ID: 'G-XXXXXXXXXX'
```

| Arquivo | Eventos disparados |
|---|---|
| `spiw/index.html` | `PageView` no load · `Lead` no submit |
| `spiw/obrigado.html` | `PageView` + `Lead` no load (página de conversão) |
| `diagnostico/index.html` | `PageView` · `QuizStart` (custom) · `CompleteRegistration` + `Lead` no submit do captureForm |
| `produtos/<slug>/index.html` (×8) | `PageView` · `ProductPitchView` (custom) · `PitchSlideView` por slide visto · `Contact` no click do WhatsApp |

GA4 dispara `generate_lead`, `quiz_start`, `product_pitch_view`, `pitch_slide_view` e `contact` nos mesmos pontos, com metadata (`momento`, `fase`, `top1`, `product`, `slide`).

> Como o template é replicado nas 8 páginas via `tools/build-pitches.py`, depois de plugar os IDs no LPMaker basta rodar o script pra propagar para os outros 7 produtos.

UTMs são preservadas automaticamente porque nada redireciona — funciona bem com qualquer parâmetro vindo do Instagram.

## Mobile-first

Breakpoints: `680px` (tablet) e `980px` (desktop). Em mobile:

- Cards e form com padding generoso (≥1.25rem)
- Botões com altura ≥44px (toque)
- Quiz com nav fixa no rodapé respeitando `safe-area-inset-bottom`
- Sem hover essencial — toda interação é clicável
- Tipografia escalável via `clamp()`

## Deploy

Qualquer host estático serve: Vercel, Netlify, S3+CloudFront, NGINX. Basta apontar `lp.glsuite.com.br` pra raiz do projeto (sem `lp.glsuite.com.br/spiw/index.html` precisa ser acessível).
