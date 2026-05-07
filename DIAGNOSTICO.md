# Diagnóstico GL Suite — Documento de Revisão

> Material para revisão pela diretoria. Apresenta a lógica completa do quiz da LP2 (`/diagnostico`), todas as perguntas com pontuação, cenários de exemplo e pontos abertos.

---

## 1. Resumo executivo

A LP2 é um quiz curto que recomenda **3 ferramentas da GL Suite** baseado na situação do negócio do lead.

- **8 perguntas** (escolha única e múltipla)
- **2 minutos** de duração média
- **3 telas**: perguntas → captura de dados → resultado na hora
- **Catálogo recomendável**: 8 ferramentas (UTMize e GL Content ficaram fora — estão "em breve" no site oficial)
- Cada resposta atribui pontos a 1 ou mais ferramentas
- A ferramenta com mais pontos é a recomendação número 1
- Pesos diferentes por pergunta refletem importância relativa

### Catálogo coberto pelo quiz

| # | Ferramenta | Frente | Headline |
|---|---|---|---|
| 1 | LPMaker | Criação | Landing pages que convertem |
| 2 | BrandMeUp | Criação | Identidade visual com IA |
| 3 | Go to Marketer | Criação | Go-to-Market com dados |
| 4 | GL Forms | Produtividade | Formulários inteligentes |
| 5 | Dora IA | Produtividade | Atendimento WhatsApp 24/7 |
| 6 | Atlas | Produtividade | Gestão interna com IA |
| 7 | SEO Insights | Performance | Inteligência de SEO com IA |
| 8 | GL Data | BI | Métricas em tempo real |

---

## 2. Lógica de pontuação — visão geral

1. Cada **opção de resposta** carrega uma ou mais entradas no formato `{ferramenta: pontos}`.
2. Cada **pergunta** tem um **peso** (x1, x2 ou x3) que multiplica esses pontos.
3. Ao final do quiz, somamos todos os pontos por ferramenta.
4. As **3 ferramentas mais pontuadas** viram a recomendação na tela de resultado.
5. A **fase de maturidade** ("Criação", "Produtividade", "Performance" ou "Análise/BI") é definida pela resposta da Pergunta 1 e exibida no resultado.

### Por que pesos diferentes

| Pergunta | Peso | Motivo |
|---|---|---|
| Pergunta 2 (maior dor) | **x3** | É a pergunta mais decisiva. A dor declarada peso direto na recomendação. |
| Pergunta 1 (momento da empresa) | **x2** | Define a fase e dá direção para o conjunto de ferramentas. |
| Demais perguntas | x1 | Refinam a pontuação sem dominar o resultado. |

---

## 3. As 8 perguntas — texto completo + pontuação

### Pergunta 1 — Peso x2

**Em qual momento sua empresa está hoje?**
*(escolha única)*

| Resposta | Pontuação (já com peso x2) | Fase definida |
|---|---|---|
| Estamos começando ou trocando posicionamento | LPMaker +4 · BrandMeUp +4 · Go to Marketer +4 | **Criação** |
| Operação rodando, mas caótica | GL Forms +4 · Atlas +4 · Dora IA +4 | **Produtividade** |
| Empresa madura querendo crescer | Dora IA +4 · GL Data +4 · SEO Insights +4 · LPMaker +2 | **Performance** |
| Quero decidir com base em dado | GL Data +4 · SEO Insights +4 | **Análise / BI** |

---

### Pergunta 2 — Peso x3 (mais decisiva)

**Qual é a maior dor agora?**
*(escolha única — a que mais te incomoda)*

| Resposta | Pontuação (já com peso x3) |
|---|---|
| Marca/identidade visual sem força | BrandMeUp +9 |
| Site ou LP que não converte | LPMaker +9 |
| Não sei lançar coisa nova com método | Go to Marketer +9 |
| Atendimento engasgado / lead esfria | Dora IA +9 |
| Time desorganizado, sem gestão | Atlas +9 |
| Captação de lead fraca | GL Forms +9 · LPMaker +3 |
| Apareço pouco no Google | SEO Insights +9 |
| Não sei o que está dando resultado | GL Data +9 |

---

### Pergunta 3 — Peso x1

**Quantas pessoas no seu time de marketing/vendas?**
*(escolha única — incluindo você)*

| Resposta | Pontuação |
|---|---|
| Só eu | (sem pontos) |
| 2 a 5 pessoas | Atlas +1 |
| 6 a 15 pessoas | Atlas +2 · GL Data +1 |
| 16 ou mais | Atlas +3 · GL Data +2 |

---

### Pergunta 4 — Peso x1 — Múltipla escolha (lógica invertida)

**O que sua empresa já tem hoje?**
*(marque tudo que se aplica — a falta indica onde a gente entra)*

> **Lógica importante**: nesta pergunta, a opção **não marcada** é que pontua. Se o usuário marca "Site/LP que converte bem", entendemos que ele já tem isso e LPMaker não pontua. Se ele não marca, LPMaker ganha pontos porque é o que resolve a falta.

| Item | Pontuação se NÃO marcado |
|---|---|
| Site ou LP que converte bem | LPMaker +2 |
| Identidade visual sólida | BrandMeUp +2 |
| Atendimento WhatsApp estruturado | Dora IA +2 |
| Forms de captura inteligentes | GL Forms +2 |
| Dashboard de marketing/vendas | GL Data +2 |
| Gestão de tarefas centralizada | Atlas +2 |

---

### Pergunta 5 — Peso x1

**Sua empresa investe em tráfego pago?**
*(escolha única — Meta, Google ou similares)*

| Resposta | Pontuação |
|---|---|
| Sim, regularmente | GL Data +2 · SEO Insights +1 |
| Esporadicamente | GL Data +1 |
| Não | SEO Insights +1 · Go to Marketer +1 |

---

### Pergunta 6 — Peso x1

**Como está sua presença orgânica (Google, blog, SEO)?**
*(escolha única)*

| Resposta | Pontuação |
|---|---|
| Forte, com ranking bom | (sem pontos) |
| Fraca, sem estratégia clara | SEO Insights +3 |
| Inexistente, nunca trabalhamos | SEO Insights +3 · Go to Marketer +1 |

---

### Pergunta 7 — Peso x1

**Quando você lança um produto ou serviço novo, o processo é:**
*(escolha única)*

| Resposta | Pontuação |
|---|---|
| Tem playbook claro | (sem pontos) |
| Improvisamos no caminho | Go to Marketer +3 |
| Quase não lançamos coisas novas | Go to Marketer +2 · BrandMeUp +1 |

---

### Pergunta 8 — Peso x1

**Quanto tempo leva pra colocar uma landing page nova no ar?**
*(escolha única)*

| Resposta | Pontuação |
|---|---|
| Em horas, sem dev | (sem pontos) |
| Em dias, com ajuda de dev | LPMaker +2 |
| Em semanas — ou nunca | LPMaker +3 · GL Forms +1 |

---

## 4. Como o resultado é montado

### Layout da tela de resultado

A tela de diagnóstico mostra:

1. **Saudação personalizada** com o primeiro nome do lead
2. **Fase identificada** (definida pela Pergunta 1)
3. **3 cards de ferramentas** ranqueados por pontuação total
4. **CTA WhatsApp personalizado** — abre o chat com mensagem pré-preenchida contendo nome, fase e top 3
5. **Botão "Refazer"** e **"Copiar diagnóstico"**

### Frase justificadora do "porquê"

Cada card de ferramenta tem uma frase explicando *por que* aquela ferramenta foi recomendada. A frase combina:

- **A dor declarada** na Pergunta 2 (frase em primeira pessoa: "você falou que sua marca precisa ganhar densidade")
- **O benefício específico** da ferramenta (frase técnica: "BrandMeUp entrega marca com arquétipo, tom e paleta — não logo solto")

#### Tabela de "porquês" disponíveis

| Ferramenta | Frase de benefício |
|---|---|
| LPMaker | monta página nova em horas, sem depender de dev |
| BrandMeUp | entrega marca com arquétipo, tom e paleta — não logo solto |
| Go to Marketer | estrutura lançamento ponta a ponta, sem improviso |
| GL Forms | capta com lógica condicional, integrado ao CRM |
| Dora IA | IA de WhatsApp 24/7 que qualifica e atende |
| Atlas | centraliza tasks, reuniões e status do time |
| SEO Insights | monitora SEO técnico e palavra-chave continuamente |
| GL Data | conecta Meta, Google, GA e CRM em dashboard único |

#### Tabela de "dores" detectadas (origem: Pergunta 2)

| Dor declarada | Frase usada no resultado |
|---|---|
| Marca/identidade fraca | "sua marca precisa ganhar densidade" |
| Site ou LP que não converte | "seu site/LP precisa converter mais" |
| Não sei lançar com método | "seu lançamento precisa de método" |
| Atendimento engasgado | "seu atendimento não pode esfriar lead" |
| Time desorganizado | "seu time precisa de gestão clara" |
| Captação fraca | "sua captação precisa subir" |
| Apareço pouco no Google | "sua presença no Google é frágil" |
| Não sei o que dá resultado | "você precisa enxergar o que dá resultado" |

### Mensagem do WhatsApp pré-preenchido

> *"Olá! Acabei de fazer o diagnóstico no estande do SPIW, meu nome é [Nome]. Minha fase é [Fase] e meu top 3 deu: [Ferramenta 1], [Ferramenta 2], [Ferramenta 3]. Quero agendar a call de 30 minutos com um especialista."*

---

## 5. Cenários — exemplos de resultado

Três personas para ilustrar como o quiz se comporta.

### Cenário A — Startup em validação

> "Acabei de abrir o negócio, não tenho marca, site converte mal, lanço produto improvisando."

**Respostas:**
- P1: Estamos começando
- P2: Marca sem força (BrandMeUp)
- P3: 2 a 5 pessoas
- P4: Não marca nenhuma opção
- P5: Esporadicamente
- P6: Inexistente
- P7: Improvisamos
- P8: Semanas ou nunca

**Pontuação calculada:**

| Ferramenta | Pontos | Origem |
|---|---|---|
| **BrandMeUp** | **15** | P1(+4) + P2(+9) + P4(+2) |
| **LPMaker** | **9** | P1(+4) + P4(+2) + P8(+3) |
| **Go to Marketer** | **8** | P1(+4) + P6(+1) + P7(+3) |
| SEO Insights | 4 | P5(+1) + P6(+3) |
| Atlas | 3 | P3(+1) + P4(+2) |
| GL Forms | 3 | P4(+2) + P8(+1) |
| GL Data | 3 | P4(+2) + P5(+1) |
| Dora IA | 2 | P4(+2) |

**Resultado exibido:**
- Fase: **Criação**
- Top 3: **BrandMeUp · LPMaker · Go to Marketer**
- Faz sentido: persona em fase 100% de Criação, recomendação 100% das ferramentas dessa frente.

---

### Cenário B — Empresa média investindo em tráfego

> "Empresa estabelecida, quer crescer, gasta em mídia mas não sabe o que dá resultado."

**Respostas:**
- P1: Empresa madura querendo crescer
- P2: Não sei o que dá resultado (GL Data)
- P3: 6 a 15 pessoas
- P4: Marca tudo menos "Dashboard de marketing"
- P5: Sim, regularmente
- P6: Forte
- P7: Tem playbook
- P8: Dias com dev

**Pontuação calculada:**

| Ferramenta | Pontos | Origem |
|---|---|---|
| **GL Data** | **18** | P1(+4) + P2(+9) + P3(+1) + P4(+2) + P5(+2) |
| **SEO Insights** | **5** | P1(+4) + P5(+1) |
| **Dora IA** | **4** | P1(+4) |
| LPMaker | 4 | P1(+2) + P8(+2) |
| Atlas | 2 | P3(+2) |
| Outras | 0 | — |

**Resultado exibido:**
- Fase: **Performance**
- Top 3: **GL Data · SEO Insights · Dora IA**
- Faz sentido: a dor "não sei o que dá resultado" combinada com "investe em tráfego regularmente" puxou GL Data com força. Os outros dois vêm da fase Performance.

> ⚠️ **Empate**: LPMaker e Dora IA empataram em 4 pontos. O sistema escolheu Dora IA pela ordem interna do catálogo. Ver "Pontos abertos" na seção 7.

---

### Cenário C — Operação caótica em escala

> "Time grande, processos quebrados, atendimento perdendo lead, marketing reativo."

**Respostas:**
- P1: Operação caótica
- P2: Time desorganizado (Atlas)
- P3: 16 ou mais
- P4: Marca "Site/LP", "Identidade", "Dashboard". Não marca os outros 3.
- P5: Sim, regularmente
- P6: Fraca
- P7: Improvisamos
- P8: Dias com dev

**Pontuação calculada:**

| Ferramenta | Pontos | Origem |
|---|---|---|
| **Atlas** | **18** | P1(+4) + P2(+9) + P3(+3) + P4(+2) |
| **GL Forms** | **6** | P1(+4) + P4(+2) |
| **Dora IA** | **6** | P1(+4) + P4(+2) |
| GL Data | 4 | P3(+2) + P5(+2) |
| SEO Insights | 4 | P5(+1) + P6(+3) |
| Go to Marketer | 3 | P7(+3) |
| LPMaker | 2 | P8(+2) |

**Resultado exibido:**
- Fase: **Produtividade**
- Top 3: **Atlas · GL Forms · Dora IA**
- Faz sentido: time grande caótico → Atlas óbvio. Marcou que tem site mas não tem forms inteligentes nem WhatsApp estruturado → GL Forms e Dora IA entram para tampar buraco operacional.

---

## 6. Fluxo completo do quiz

```
┌─────────────────────┐
│   TELA DE INTRO     │  "Em 2 minutos, você sai com o plano certo"
│                     │  3 metas: 8 perguntas · 2 min · 3 ferramentas
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   8 PERGUNTAS       │  Escolha única avança automaticamente em 220ms
│   (uma por tela)    │  Múltipla exige clicar "Próxima"
│                     │  Barra de progresso no topo
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  TELA DE CAPTURA    │  Nome · E-mail · WhatsApp · Empresa
│                     │  Gate antes do resultado
│                     │  Dispara para RD Station + webhook
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  TELA DE RESULTADO  │  Fase + 3 cards ranqueados
│                     │  CTA WhatsApp pré-preenchido
│                     │  Refazer · Copiar diagnóstico
└─────────────────────┘
```

---

## 7. Pontos abertos para a diretoria revisar

Lista de decisões que vale validar antes de subir o domínio definitivo:

### Sobre as perguntas

1. **As 8 perguntas cobrem o suficiente?** Estudei reduzir para 6 (mais rápido no estande) ou expandir para 10 (mais granularidade). 8 ficou no equilíbrio entre cobertura e fricção.
2. **A Pergunta 2 está com 8 opções de dor — virou uma lista grande.** Vale checar se queremos consolidar ou se essa granularidade é boa pra direcionar bem.
3. **A lógica invertida da Pergunta 4 é intuitiva pro lead?** Marcar o que tem (em vez do que falta) é menos comum, mas pesquisas mostram que reduz fadiga e o lead identifica melhor seus assets que suas faltas.

### Sobre o scoring

4. **Pesos x3 / x2 / x1 estão bem calibrados?** Em todos os cenários testados, as Perguntas 1 e 2 dominam o ranking, o que é o comportamento desejado. As demais refinam o top 3 mas raramente mudam o #1.
5. **Mapeamento dor → ferramenta** (tabela da Pergunta 2): essa é a tabela mais sensível. Pede revisão direta dos times de cada ferramenta para confirmar que cada dor está apontada para a ferramenta certa.
6. **Empates**: hoje o sistema desempata pela ordem interna do catálogo (LPMaker, BrandMeUp, Go to Marketer, GL Forms, Dora IA, Atlas, SEO Insights, GL Data). Vale criar regra de desempate explícita? Sugestões: priorizar a ferramenta da fase identificada, ou priorizar a mais barata, ou adicionar pergunta de tiebreaker.

### Sobre as frases justificadoras (`buildWhy`)

7. **O tom das frases de benefício** está alinhado com o jeito que vocês falam de cada ferramenta? Sugiro cada gerente de produto rever a sua linha em "Tabela de porquês".
8. **As frases de dor** soam acolhedoras? Hoje são técnicas e diretas ("seu site/LP precisa converter mais"). Pode-se humanizar mais ("você sente que perde gente que entra no seu site").

### Sobre a captura

9. **Pedimos 4 campos** (nome, e-mail, WhatsApp, empresa). Reduzir para 2 (nome + WhatsApp) aumentaria taxa de conclusão mas perderia dado para o CRM. Vale testar.
10. **A captura está antes do resultado** (gate). Funciona pra estande (lead já está engajado). Para uso pós-evento, pode valer testar o oposto: mostrar resultado e capturar para "salvar" / "receber por e-mail".

### Sobre o catálogo

11. **UTMize e GL Content ficaram fora** porque estão "em breve" no glsuite.com.br. Quando lançarem, basta adicionar entradas no objeto `TOOLS` e ajustar o scoring. Hoje a recomendação é sempre dentro das 8.
12. **CRM** aparece na visão interna da Suite, mas não está no catálogo público (glsuite.com.br). Por isso ficou fora do quiz. Se virar produto público, entra com facilidade.

---

## 8. Onde mexer no código

Para qualquer ajuste no quiz, o arquivo é único: `diagnostico/index.html`.

| Quero mudar... | Vai em... |
|---|---|
| Texto de uma pergunta | Array `QUESTIONS`, propriedade `title` |
| Texto de uma opção | Array `QUESTIONS`, dentro de `options[i].label` |
| Pontuação de uma opção | Array `QUESTIONS`, dentro de `options[i].score` |
| Peso de uma pergunta | Array `QUESTIONS`, propriedade `weight` |
| Frase de "porquê" | Função `buildWhy`, objetos `dorMap` e `reasons` |
| Adicionar ferramenta nova | Objeto `TOOLS` (adicionar entrada) |
| Mudar quantidade de perguntas | Adicionar/remover entradas no array `QUESTIONS` (o resto se ajusta sozinho) |
| Mudar para mostrar top 5 em vez de top 3 | Função `renderResult`, mudar `.slice(0, 3)` para `.slice(0, 5)` |

Toda mudança feita aqui sobe automaticamente em produção via `git push`.
