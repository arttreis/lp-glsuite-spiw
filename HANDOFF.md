# HANDOFF — LPs SPIW GL Suite

Documento pra retomar o trabalho de qualquer máquina. Última atualização: **2026-05-07**.

## TL;DR

Duas LPs estão construídas, no GitHub e no ar na Vercel. Falta substituir o `RD_TOKEN`, plugar o domínio `lp.glsuite.com.br` e configurar tracking. Tudo documentado abaixo.

| | Link |
|---|---|
| **Repo GitHub** (privado) | https://github.com/arttreis/lp-glsuite-spiw |
| **Vercel dashboard** | https://vercel.com/arthur-castilhos-projects/lp-glsuite-spiw |
| **LP1 — catálogo** | https://lp-glsuite-spiw.vercel.app/spiw |
| **LP2 — diagnóstico** | https://lp-glsuite-spiw.vercel.app/diagnostico |
| **Página obrigado LP1** | https://lp-glsuite-spiw.vercel.app/spiw/obrigado |

Auto-deploy ativo: qualquer `git push origin main` sobe automaticamente em produção em ~30s.

## Pegar de outro PC — 3 comandos

Pré-requisitos: `git`, `gh` (autenticado como `arttreis`), e qualquer editor (VS Code, etc). Não precisa Node, npm, build step, nada.

```bash
gh repo clone arttreis/lp-glsuite-spiw
cd lp-glsuite-spiw
# abre no editor — ou só clica nos arquivos pra ver no browser
```

Pra rodar local em modo preview (opcional, qualquer servidor estático serve):

```bash
# Python (geralmente já vem instalado)
python -m http.server 8000
# Depois acessa http://localhost:8000/spiw e http://localhost:8000/diagnostico
```

Pra fazer deploy manual via Vercel CLI (caso queira sem passar pelo GitHub):

```bash
npm i -g vercel    # uma vez só
vercel login       # autenticar como artwesz
vercel deploy --prod
```

Mas o caminho normal é só `git push` que a Vercel redeploya sozinha.

## Estado atual

### O que está pronto

- [x] LP1 (`spiw/index.html`) — hero, 4 frentes, catálogo das 8 ferramentas à venda, form com validação, máscara de telefone, redirect para obrigado.
- [x] Página obrigado (`spiw/obrigado.html`) — saudação personalizada via query string, botão WhatsApp pré-preenchido com nome e fase.
- [x] LP2 (`diagnostico/index.html`) — quiz de 8 perguntas, scoring ponderado, tela de captura, tela de resultado com top 3 ferramentas + CTA WhatsApp personalizado.
- [x] Design system inline herdado de glsuite.com.br (Montserrat / DM Sans / accent `#0014ff` / radius `0.5rem`).
- [x] Mobile-first com breakpoints `680px` e `980px`.
- [x] `vercel.json` com clean URLs, security headers, cache de HTML.
- [x] `index.html` raiz redireciona pra glsuite.com.br.
- [x] Repo no GitHub privado.
- [x] Deploy em produção na Vercel.
- [x] Auto-deploy GitHub → Vercel ativo.

### O que falta fazer (em ordem de prioridade)

#### 1. Substituir `RD_TOKEN` pelo token público do RD Station

Editar **dois** arquivos. Localizar a linha:

```js
RD_TOKEN: 'COLOQUE_AQUI_O_TOKEN_PUBLICO_RD',
```

Em:

- `spiw/index.html` (perto do final, dentro do `<script>`)
- `diagnostico/index.html` (mesmo lugar)

Substituir pelo token. Depois:

```bash
git add spiw/index.html diagnostico/index.html
git commit -m "config: RD Station token"
git push
```

A Vercel redeploya em ~30s.

#### 2. Apontar `lp.glsuite.com.br` na Vercel

No dashboard da Vercel:
1. Abrir o projeto `lp-glsuite-spiw`
2. **Settings → Domains**
3. Adicionar `lp.glsuite.com.br`
4. A Vercel mostra um CNAME (algo como `cname.vercel-dns.com`)
5. No painel do registrador do domínio `glsuite.com.br`, adicionar entrada CNAME `lp` apontando pro valor da Vercel
6. Em ~5 a 15 min propaga e o SSL é emitido automaticamente

#### 3. Configurar workflow no RD Station para alertar e disparar WhatsApp

No painel do RD Station:
- Criar workflow: trigger = lead recebe tag `SPIW`
- Ação 1: enviar e-mail pra `midia@guessless.com.br` com os dados do lead
- Ação 2: integrar com sua ferramenta de disparo de WhatsApp (n8n, Z-API, etc)

Alternativa: preencher `WEBHOOK_URL` no `CONFIG` de cada LP (atualmente vazio), apontando pra um webhook próprio (ex.: n8n) que faz e-mail + WhatsApp. As LPs já estão preparadas pra disparar em paralelo.

#### 4. Tracking (Meta Pixel + GA4)

Pontos de hook documentados no `README.md`. Resumindo:

- **LP1** (`spiw/index.html`): adicionar `fbq('track','Lead')` antes do `window.location.href = CONFIG.REDIRECT_URL...` no submit handler.
- **LP2** (`diagnostico/index.html`): adicionar `fbq('track','CompleteRegistration')` antes do `renderResult()` no submit handler do `captureForm`.
- **GA4**: incluir o snippet padrão no `<head>` de ambas as LPs e disparar `gtag('event','generate_lead')` nos mesmos pontos.

Adicionar o pixel no `<head>` de cada HTML se ainda não tiver script global de tag manager.

## Mapa do código — onde mexer em cada coisa

| Quero alterar... | Vai em... |
|---|---|
| Headline ou copy da LP1 | `spiw/index.html` → `<section class="hero">` |
| Lista das ferramentas (cards) | `spiw/index.html` → `<section id="ferramentas">` |
| Pergunta ou opção do quiz | `diagnostico/index.html` → array `QUESTIONS` no JS |
| Pesos do scoring do quiz | `diagnostico/index.html` → propriedade `score` ou `absent` em cada option, ou `weight` da pergunta |
| Catálogo + URLs das ferramentas no resultado | `diagnostico/index.html` → objeto `TOOLS` no JS |
| Frase justificadora do "porquê" no resultado | `diagnostico/index.html` → função `buildWhy()` |
| Cor de marca (accent) | qualquer HTML → `--accent` no `:root` (atual: `#0014ff`) |
| Tipografia | qualquer HTML → `--font-display`, `--font-body`, `--font-mono` |
| Texto do WhatsApp pré-preenchido | `spiw/obrigado.html` (LP1) ou `diagnostico/index.html` (LP2) → função que monta `waText`/`finalWa` |
| Número do WhatsApp | atual: `5511910817825`. Buscar nos 3 HTMLs e substituir |
| Página de redirect raiz | `index.html` (raiz) |
| Headers HTTP / cache / clean URLs | `vercel.json` |

## Decisões importantes que tomamos

Pra você não ter que reconstruir contexto:

1. **Slugs**: `/spiw` (LP1, campanha de tráfego do evento) e `/diagnostico` (LP2, mais reusável depois do evento). A LP2 pode virar entrada permanente fora do SPIW só trocando a tag.
2. **Catálogo só com 8 ferramentas**: UTMize e GL Content estão "em breve" no glsuite.com.br, então ficaram fora do catálogo da LP1 e da recomendação do quiz da LP2.
3. **Quiz com 8 perguntas, não 10**: menos atrito no estande. Mais perguntas não traziam resolução melhor — perguntas 2 e 4 já capturam 80% da decisão.
4. **Single-choice avança automático**: 220ms após o clique. Multi-choice exige confirmar com botão. UX otimizada pra tempo de uso de estande (~2 minutos do começo ao fim).
5. **Captura ANTES do resultado**: forma um "gate" — quem não preenche não vê diagnóstico. Mas a UX deixa claro que a entrega é instantânea na tela.
6. **CRM da skill ≠ catálogo público**: a skill `gl-suite` mencionava CRM como ferramenta da Suite, mas o site público (glsuite.com.br) não vende CRM separado. Seguimos o site público porque foi o que o brief pediu (extrair de glsuite.com.br).
7. **Nomes comerciais públicos** (do site) sobrepõem nomes da skill: `LPMaker` não `Site/LP Builder`, `Dora IA` não `Bot Dora`, `BrandMeUp` não `Branding Guide`, `GL Data` não `Dash`, `Go to Marketer` não `GTM`, `SEO Insights` não `SEO Insight`, `GL Forms` não `Forms`.
8. **Tom**: alinhado com o site (`Decisões baseadas em Inteligência`), direto e técnico, com toques de "decida com dado" — não premium rebuscado.
9. **Sem co-branding SPIW**: só GL Suite. Hero menciona "GuessLess no SPIW" como badge contextual.
10. **WhatsApp como fallback de agendamento**: nada de Calendly. Lead → RD Station → e-mail + chamada no WhatsApp.

## Estrutura de pastas

```
lp-glsuite-spiw/
├── .gitignore           → ignora .vercel, .env, etc
├── HANDOFF.md           → este arquivo
├── README.md            → documentação técnica + checklist
├── index.html           → raiz, redireciona pra glsuite.com.br
├── vercel.json          → headers, clean URLs
├── spiw/
│   ├── index.html       → LP1
│   └── obrigado.html    → pós-cadastro LP1
└── diagnostico/
    └── index.html       → LP2 (quiz + captura + resultado)
```

## Comandos úteis

```bash
# Ver últimos commits
git log --oneline -10

# Editar e fazer push (auto-deploy em ~30s)
# (edite os arquivos)
git add -A
git commit -m "descrição da mudança"
git push

# Ver últimos deploys
gh repo view arttreis/lp-glsuite-spiw --web    # abre no browser
# ou ir direto no dashboard Vercel

# Rodar localmente
python -m http.server 8000
# acessa http://localhost:8000/spiw e /diagnostico

# Ver logs de deploy da Vercel
vercel logs lp-glsuite-spiw --prod
```

## Contatos / créditos

- **GitHub**: arttreis
- **Vercel**: artwesz (org: arthur-castilhos-projects)
- **WhatsApp comercial usado nas LPs**: 5511910817825
- **E-mail de notificação configurado no RD**: midia@guessless.com.br

## Próxima sessão sugerida

Quando voltar:

1. Pegar token do RD Station e substituir nos dois HTMLs (5 min).
2. Adicionar `lp.glsuite.com.br` no Vercel Domains (5 min + propagação DNS).
3. Configurar workflow do RD Station pra alertar (15 min).
4. Adicionar pixel/GA4 (15 min).
5. Validar fluxo end-to-end no celular (preencher form, ver e-mail chegar, abrir WhatsApp do CTA).

Tempo total estimado: 1h pra deixar tudo no ar pronto pro evento.
