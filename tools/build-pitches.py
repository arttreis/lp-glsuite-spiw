"""Gera as pages de pitch /produtos/<slug>/index.html a partir do template LPMaker.

Edita PRODUCTS abaixo e roda: python tools/build-pitches.py
Sobrescreve os arquivos /produtos/<slug>/index.html exceto LPMaker (que serve como template/spec).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "produtos" / "lpmaker" / "index.html").read_text(encoding="utf-8")


PRODUCTS = [
    {
        "slug": "brandmeup",
        "nome": "BrandMeUp",
        "frente": "Criação",
        "meta_title": "BrandMeUp — Identidade visual com IA · GL Suite",
        "meta_desc": "BrandMeUp da GL Suite: marca com arquétipo, tom de voz, manifesto e paleta — não logo solto. Pitch em 6 slides.",
        "og_title": "BrandMeUp — Identidade visual com IA",
        "og_desc": "Marca com densidade: arquétipo, tom, manifesto e sistema visual completo, em dias e não em meses.",
        # Slide 1
        "s1_headline": "BrandMeUp.",
        "s1_accent": "Marca com densidade.",
        "s1_lead": "Identidade visual construída com IA: arquétipo, tom de voz, manifesto e sistema visual — não logo solto.",
        # Slide 2
        "s2_title_pre": "Sua marca soa",
        "s2_title_accent": "igual à concorrência.",
        "s2_bullets": [
            ("Logo bonito não fecha venda", "Sem arquétipo nem posicionamento, sua marca compete só no preço. Quem decide na hora não tem âncora pra te escolher."),
            ("Time fala em tons diferentes", "Cada peça (post, e-mail, anúncio, vendedor) tem voz própria — porque ninguém documentou como a marca fala."),
            ("Manual ficou na gaveta", "Pesquisa de marca cara, manual no Drive que ninguém abre. Brand é tratado como entrega, não como sistema vivo."),
        ],
        # Slide 3
        "s3_title_pre": "Marca decidida",
        "s3_title_accent": "como sistema.",
        "s3_body": "BrandMeUp é o módulo de marca da GL Suite. Diagnóstico, construção e ativação de identidade num único fluxo, com IA acelerando cada etapa.",
        "s3_bullets": [
            ("Arquétipo e persona de marca", "Diagnóstico de mercado e do seu negócio define o arquétipo que cabe — base pra todo posicionamento."),
            ("Tom de voz documentado", "Vocabulário, ritmo, exemplos do que falar e do que evitar. Aplicável por qualquer pessoa do time."),
            ("Sistema visual completo", "Paleta, tipografia, grid, ícones e fundo. Tudo coerente, pronto pra usar em LP, deck, social e anúncio."),
        ],
        # Slide 4
        "s4_title_pre": "3 etapas.",
        "s4_title_accent": "Em dias.",
        "s4_steps": [
            ("Briefing guiado com IA", "Você responde perguntas estratégicas em ~30 min. A IA cruza com pesquisa de mercado e concorrência."),
            ("Construção de identidade", "Arquétipo, manifesto, tom e sistema visual entregues como artefatos editáveis — não PDFs estáticos."),
            ("Ativação no time", "Manual vivo, exemplos de aplicação e plug-and-play com LPMaker, Atlas e GL Forms."),
        ],
        # Slide 5
        "s5_title_pre": "De meses",
        "s5_title_accent": "pra dias.",
        "s5_stat": "~7d",
        "s5_label": "Tempo médio do briefing à entrega completa do sistema de marca.",
        "s5_body": "Sua marca para de ser \"projeto eterno da agência\" e vira ativo aplicável. Toda comunicação passa a sair com a mesma densidade — orgânica, paga, comercial e produto.",
        # Slide 6
        "s6_title_pre": "Quer ver sua marca",
        "s6_title_accent": "ganhar densidade?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente identifica o que falta no seu posicionamento atual e propõe o caminho mais curto pra fechar.",
        "wa_msg": "Olá! Vi o pitch do BrandMeUp no estande do SPIW e quero entender como construir uma marca com mais densidade. Quero agendar a call de 30 min.",
    },
    {
        "slug": "gomarketer",
        "nome": "Go to Marketer",
        "frente": "Criação",
        "meta_title": "Go to Marketer — Go-to-market com dados · GL Suite",
        "meta_desc": "Go to Marketer da GL Suite: lançamento estruturado ponta a ponta — posicionamento, persona, canais, funil, cronograma. Pitch em 6 slides.",
        "og_title": "Go to Marketer — Go-to-market com método",
        "og_desc": "Lançamento previsível com IA. Posicionamento, persona, canais e cronograma sem improviso.",
        "s1_headline": "Go to Marketer.",
        "s1_accent": "Lançamento com método.",
        "s1_lead": "Go-to-market estruturado ponta a ponta — posicionamento, persona, canais, funil e cronograma, em vez de improviso.",
        "s2_title_pre": "Cada lançamento",
        "s2_title_accent": "é improviso novo.",
        "s2_bullets": [
            ("Posicionamento na cabeça do fundador", "Persona muda a cada call, mensagem muda a cada peça. O time não consegue replicar porque ninguém escreveu."),
            ("Canal pelo que dá", "Roda Meta Ads porque \"todo mundo roda\". Sem hipótese de canal, dinheiro queima na descoberta cara."),
            ("Cronograma na agenda", "Lançamento marcado pra \"semana que vem\" há 4 semanas. Sem milestone claro, prazo escorrega e momentum some."),
        ],
        "s3_title_pre": "Lançamento como",
        "s3_title_accent": "playbook replicável.",
        "s3_body": "Go to Marketer é o módulo de planejamento de lançamento da GL Suite. Cobre diagnóstico, estratégia, execução e acompanhamento.",
        "s3_bullets": [
            ("Análise de mercado e ICP", "Diagnóstico de mercado, concorrência e segmento ideal. Persona com gatilhos reais, não demográfica genérica."),
            ("Estratégia de canais", "Mix orgânico e pago com hipótese declarada por canal e métrica de validação. Sem \"vamos rodar e ver\"."),
            ("Cronograma de execução", "Milestones, responsável, entregável e dependência. Conecta com Atlas pra acompanhar o passo-a-passo."),
        ],
        "s4_title_pre": "4 etapas.",
        "s4_title_accent": "Lançamento previsível.",
        "s4_steps": [
            ("Diagnóstico inicial", "Quem é seu cliente, o que ele já compra, por que escolhe você. Calibrado com IA + sua entrada."),
            ("Estratégia gerada", "Posicionamento, persona e canais saem documentados. Editáveis, versionáveis, fáceis de revisar."),
            ("Cronograma e execução", "Plano com prazo, responsável e dependência — exportável pro Atlas, ClickUp ou planilha."),
        ],
        "s5_title_pre": "De improviso",
        "s5_title_accent": "pra playbook.",
        "s5_stat": "1×",
        "s5_label": "Você escreve o playbook uma vez. Os próximos lançamentos só ajustam variáveis.",
        "s5_body": "Lançar produto novo deixa de ser sprint heróica. O time roda do diagnóstico até o pós-lançamento com clareza de o que sai, quando, por qual canal e com qual métrica de validação.",
        "s6_title_pre": "Quer transformar lançamento",
        "s6_title_accent": "em playbook?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente mapeia seu próximo lançamento e mostra como rodar com método em vez de improviso.",
        "wa_msg": "Olá! Vi o pitch do Go to Marketer no estande do SPIW e quero estruturar meu próximo lançamento com método. Quero agendar a call de 30 min.",
    },
    {
        "slug": "gl-forms",
        "nome": "GL Forms",
        "frente": "Produtividade",
        "meta_title": "GL Forms — Formulários inteligentes · GL Suite",
        "meta_desc": "GL Forms da GL Suite: captura com lógica condicional, qualificação automática e integração nativa com CRM e Dora IA. Pitch em 6 slides.",
        "og_title": "GL Forms — Formulários inteligentes",
        "og_desc": "Pare de perder lead na primeira porta. Form que se adapta, qualifica e conecta direto no CRM.",
        "s1_headline": "GL Forms.",
        "s1_accent": "Captura que qualifica.",
        "s1_lead": "Formulários inteligentes com lógica condicional, qualificação automática e integração nativa com CRM e Dora IA.",
        "s2_title_pre": "Seu form perde lead",
        "s2_title_accent": "na primeira porta.",
        "s2_bullets": [
            ("8 campos pra preencher", "Lead bom abandona antes do meio. Lead ruim termina e chega ao time sem qualificação nenhuma."),
            ("Vendas afoga em lead frio", "Tudo cai na mesma fila. Vendedor gasta tempo descobrindo se o lead tem fit — quando o form já podia ter perguntado."),
            ("Integração quebrada", "Form em um lugar, CRM em outro, planilha de exportação no e-mail. Lead some entre uma etapa e outra."),
        ],
        "s3_title_pre": "Form que se adapta",
        "s3_title_accent": "ao lead.",
        "s3_body": "GL Forms é o builder de formulários da GL Suite. Cada campo aparece em função das respostas anteriores, e o lead já entra qualificado no seu CRM.",
        "s3_bullets": [
            ("Lógica condicional nativa", "Mostra só o que importa para aquele perfil. Form curto pra lead pouco engajado, completo pra lead quente."),
            ("Qualificação automática", "Pontuação por resposta. Lead qualificado é roteado pra vendas, lead pouco maduro vai pra nutrição."),
            ("Integração CRM + Dora IA", "RD Station, HubSpot, Pipedrive — e Dora IA chama o lead no WhatsApp em segundos com a mensagem certa."),
        ],
        "s4_title_pre": "3 passos.",
        "s4_title_accent": "Form no ar.",
        "s4_steps": [
            ("Criar com builder visual", "Arrasta campo, define lógica de exibição, pontua resposta. Sem código, sem fórmula escondida."),
            ("Integrar com sua stack", "CRM, e-mail marketing, Dora IA, Atlas — em poucos cliques. O lead chega no destino certo já etiquetado."),
            ("Publicar e embutir", "URL pública, embed em LP do LPMaker, ou pop-up no seu site. Mobile-first por padrão."),
        ],
        "s5_title_pre": "Menos atrito.",
        "s5_title_accent": "Mais lead bom.",
        "s5_stat": "+conv.",
        "s5_label": "Form condicional converte mais porque pergunta só o que faz sentido pra aquele lead.",
        "s5_body": "Captura sobe porque o form fica curto. Qualidade sobe porque o lead já vem etiquetado. E vendas só recebe o que vale a ligação — o resto é nutrido automático.",
        "s6_title_pre": "Quer trocar seu form",
        "s6_title_accent": "por um que qualifica?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente revisa seu funil de captura atual e propõe o GL Forms onde dá mais retorno.",
        "wa_msg": "Olá! Vi o pitch do GL Forms no estande do SPIW e quero parar de perder lead na captura. Quero agendar a call de 30 min.",
    },
    {
        "slug": "dora",
        "nome": "Dora IA",
        "frente": "Produtividade",
        "meta_title": "Dora IA — Atendimento WhatsApp 24/7 · GL Suite",
        "meta_desc": "Dora IA da GL Suite: agente de IA no WhatsApp que qualifica, atende e faz pós-venda 24/7. Pitch em 6 slides.",
        "og_title": "Dora IA — Atendimento que não dorme",
        "og_desc": "Lead nunca esfria por horário. IA de WhatsApp qualifica, atende e escala para humano só quando precisa.",
        "s1_headline": "Dora IA.",
        "s1_accent": "Atendimento que não dorme.",
        "s1_lead": "IA de WhatsApp 24/7 que qualifica, atende e faz pós-venda — com handoff humano só quando precisa.",
        "s2_title_pre": "Lead chega 22h.",
        "s2_title_accent": "Esfria até amanhã.",
        "s2_bullets": [
            ("Horário comercial mata pipeline", "Cliente decide à noite, no domingo, no feriado. Se ninguém responde em minutos, a venda foi para o concorrente."),
            ("Time afoga em DM repetitiva", "70% das perguntas são as mesmas. Atendente gasta dia inteiro respondendo \"qual o preço?\" — em vez de fechar venda."),
            ("Pós-venda fica esquecido", "Cliente pago some do radar. Sem follow-up automático, churn sobe e LTV cai sem ninguém perceber."),
        ],
        "s3_title_pre": "IA que",
        "s3_title_accent": "atende como humano.",
        "s3_body": "Dora IA é o módulo de atendimento da GL Suite. Agentes especializados em qualificação, suporte e pós-venda, rodando no seu WhatsApp Business.",
        "s3_bullets": [
            ("Qualificação inicial automática", "Capta intenção, contexto e fit em segundos. Lead quente vai pra vendedor; lead morno entra em nutrição."),
            ("Suporte 24/7 com base de conhecimento", "Treinada com seu material. Responde em linguagem natural, escala dúvida que sai do escopo pro humano."),
            ("Handoff humano com contexto", "Quando passa pra pessoa, vai com histórico completo da conversa e a recomendação da IA. Zero re-trabalho."),
        ],
        "s4_title_pre": "3 etapas.",
        "s4_title_accent": "Rodando essa semana.",
        "s4_steps": [
            ("Treinar com seu material", "FAQ, política, scripts comerciais, base de produtos. A Dora ingere tudo e aprende seu tom."),
            ("Conectar WhatsApp Business", "Oficial, via Meta Business. Mensagens entram no número que você já usa, sem trocar contato."),
            ("Monitorar e iterar", "Dashboard mostra conversas, conversão e onde a Dora pediu ajuda humana. Você refina sem reset."),
        ],
        "s5_title_pre": "Resposta",
        "s5_title_accent": "em segundos.",
        "s5_stat": "<30s",
        "s5_label": "Tempo médio de primeira resposta — 24h por dia, 7 dias por semana.",
        "s5_body": "Lead bom não esfria mais por horário. Time de vendas recebe lead pré-qualificado com contexto da conversa, e o atendente humano fica livre pra o que exige humano.",
        "s6_title_pre": "Quer parar de perder",
        "s6_title_accent": "lead por horário?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente mapeia onde a Dora IA gera retorno mais rápido na sua operação.",
        "wa_msg": "Olá! Vi o pitch da Dora IA no estande do SPIW e quero atendimento 24/7 sem afogar o time. Quero agendar a call de 30 min.",
    },
    {
        "slug": "atlas",
        "nome": "Atlas",
        "frente": "Produtividade",
        "meta_title": "Atlas — Gestão interna com IA · GL Suite",
        "meta_desc": "Atlas da GL Suite: tasks, reuniões, lembretes e status do time num lugar só, com IA. Pitch em 6 slides.",
        "og_title": "Atlas — Gestão sem perder coisa em DM",
        "og_desc": "Centro único de comando. Tasks, reuniões e status do time consolidados, com IA gerando pauta e ata.",
        "s1_headline": "Atlas.",
        "s1_accent": "Gestão sem ruído.",
        "s1_lead": "Tasks, reuniões, lembretes e status do time num lugar só — com IA gerando pauta, ata e follow-up automático.",
        "s2_title_pre": "Tarefa some",
        "s2_title_accent": "em DM e planilha.",
        "s2_bullets": [
            ("Operação espalhada em 6 ferramentas", "ClickUp, Slack, planilha, WhatsApp, e-mail, Notion. Cada um abre a sua, e nada conversa direito."),
            ("Reunião pra falar de outra reunião", "Sem pauta clara nem ata, o time volta a discutir o que já foi decidido. Decisão evapora entre encontros."),
            ("Lembrete que ninguém lembra", "Tarefa marcada pra terça, esquecida na quinta. Sem alerta contextual, o time vira detetive de prazo."),
        ],
        "s3_title_pre": "Centro único",
        "s3_title_accent": "de comando.",
        "s3_body": "Atlas é o módulo de gestão interna da GL Suite. Substitui o pacote de ferramentas operacionais com IA acelerando cada etapa.",
        "s3_bullets": [
            ("Kanban com status automatizado", "Task muda de status conforme regra (PR mergeado → done, prazo vencendo → alerta). Menos clique, mais ação."),
            ("Reunião com pauta + ata por IA", "Você grava ou conecta a chamada. A IA gera resumo, decisões e tarefas — atribuídas direto no quadro."),
            ("Lembrete contextual no WhatsApp", "O Atlas te chama no WhatsApp pelo que importa hoje. Sem notificação ruim, sem fadiga de app."),
        ],
        "s4_title_pre": "3 passos.",
        "s4_title_accent": "Time alinhado.",
        "s4_steps": [
            ("Importar equipe", "Convida o time, define áreas e cargos. Atlas mapeia quem faz o quê automaticamente."),
            ("Conectar ferramentas", "Slack, Google Calendar, Meet, Zoom, GitHub. Eventos viram dados consolidados, sem migrar nada."),
            ("Deixar IA cuidar do operacional", "Atlas roda os rituais: pauta, follow-up, lembrete e relatório de status semanal — sem o time pedir."),
        ],
        "s5_title_pre": "Time alinhado.",
        "s5_title_accent": "Reunião curta.",
        "s5_stat": "1 lugar",
        "s5_label": "Tudo o que o time precisa pra operar — sem trocar de aba seis vezes por hora.",
        "s5_body": "Reunião vira decisão, não discussão. Tarefa fica visível pra quem precisa ver. Status sai automático pro time inteiro — e o líder para de virar repassador de informação.",
        "s6_title_pre": "Quer seu time",
        "s6_title_accent": "operando alinhado?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente mapeia seu fluxo atual e mostra onde o Atlas substitui ferramenta hoje.",
        "wa_msg": "Olá! Vi o pitch do Atlas no estande do SPIW e quero consolidar a gestão do meu time num lugar só. Quero agendar a call de 30 min.",
    },
    {
        "slug": "seo-insights",
        "nome": "SEO Insights",
        "frente": "Performance",
        "meta_title": "SEO Insights — Inteligência de SEO com IA · GL Suite",
        "meta_desc": "SEO Insights da GL Suite: auditoria contínua, monitoramento de palavra-chave e alertas técnicos com IA. Pitch em 6 slides.",
        "og_title": "SEO Insights — SEO que IA monitora",
        "og_desc": "Você corrige antes da queda virar perda de receita. Auditoria diária, monitor de keywords e alerta técnico em tempo real.",
        "s1_headline": "SEO Insights.",
        "s1_accent": "SEO que IA monitora.",
        "s1_lead": "Auditoria contínua, monitoramento de palavra-chave e alerta técnico em tempo real — em vez de relatório mensal.",
        "s2_title_pre": "Seu SEO cai.",
        "s2_title_accent": "Você descobre por relatório.",
        "s2_bullets": [
            ("Erro técnico passa despercebido", "Sitemap quebrado, indexação caindo, redirect em loop — descoberto semanas depois, quando o tráfego já evaporou."),
            ("Palavra-chave perdida em silêncio", "Concorrente sobe, você cai. Sem monitoramento ativo, o time descobre quando a receita já mostrou impacto."),
            ("Relatório mensal de agência", "Você paga pra receber um PDF com o que aconteceu, não com o que está acontecendo. Decisão sempre atrasada."),
        ],
        "s3_title_pre": "SEO em tempo real,",
        "s3_title_accent": "não em PDF.",
        "s3_body": "SEO Insights é o módulo de inteligência de SEO da GL Suite. Auditoria diária + monitoramento contínuo + alertas onde você está.",
        "s3_bullets": [
            ("Auditoria técnica diária", "Crawl automático verifica Core Web Vitals, status code, schema, indexação e mobile. Você só vê o que mudou."),
            ("Monitor de keywords + concorrentes", "Posição diária por palavra-chave e por concorrente. Tendência semanal mostra pra onde a SERP está indo."),
            ("Alerta em tempo real", "Queda de ranking, broken link, página de-indexada, schema quebrado — alerta no WhatsApp em vez de e-mail mensal."),
        ],
        "s4_title_pre": "3 passos.",
        "s4_title_accent": "SEO sob controle.",
        "s4_steps": [
            ("Conectar Search Console", "Liga em segundos. SEO Insights puxa histórico e começa a monitorar a partir do dia 1."),
            ("Definir keywords e concorrentes", "Você lista palavra-chave e domínio que importa. A IA sugere mais com base em volume e relevância."),
            ("Receber alertas direcionados", "WhatsApp, e-mail, ou Slack — só o que mudou de fato. Sem ruído, sem PDF de 40 páginas."),
        ],
        "s5_title_pre": "Corrija antes",
        "s5_title_accent": "da queda doer.",
        "s5_stat": "24h",
        "s5_label": "Alerta de problema técnico ou queda de posição em até 24h.",
        "s5_body": "Você troca relatório mensal por sinal contínuo. Concorrente sobe, você sabe. Erro técnico aparece, você corrige antes do Google decidir penalizar.",
        "s6_title_pre": "Quer SEO",
        "s6_title_accent": "sem PDF mensal?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente revisa seu cenário SEO atual e mostra onde o SEO Insights gera retorno mais rápido.",
        "wa_msg": "Olá! Vi o pitch do SEO Insights no estande do SPIW e quero parar de descobrir queda de SEO em relatório mensal. Quero agendar a call de 30 min.",
    },
    {
        "slug": "gl-data",
        "nome": "GL Data",
        "frente": "Análise / BI",
        "meta_title": "GL Data — Métricas em tempo real · GL Suite",
        "meta_desc": "GL Data da GL Suite: dashboards que conectam Meta, Google, GA4 e CRM com atribuição real e relatório automático. Pitch em 6 slides.",
        "og_title": "GL Data — Dado em tempo real, não planilha",
        "og_desc": "Decisão de marketing com dado de hoje, não de mês passado. Atribuição multi-touch e relatório no WhatsApp.",
        "s1_headline": "GL Data.",
        "s1_accent": "Dado em tempo real.",
        "s1_lead": "Dashboards que conectam Meta Ads, Google Ads, GA4 e CRM — com atribuição real e relatório automático no e-mail ou WhatsApp.",
        "s2_title_pre": "Reunião de quinta",
        "s2_title_accent": "com planilha de quarta.",
        "s2_bullets": [
            ("Atribuição quebrada", "Meta diz que converteu, Google também, GA4 mostra outro número. Ninguém sabe o que de fato deu resultado."),
            ("Planilha que ninguém mantém", "Estagiário consolida toda segunda. Quando o dado chega, a campanha já queimou orçamento na hipótese errada."),
            ("Decisão atrasada em uma semana", "Marketing roda anúncio sem visibilidade, vendas reclama de lead frio, finanças cobra ROI — todos olhando dado diferente."),
        ],
        "s3_title_pre": "Dashboard",
        "s3_title_accent": "que decide.",
        "s3_body": "GL Data é o módulo de BI da GL Suite. Conecta as plataformas que você já usa, consolida e entrega o número certo onde você decide.",
        "s3_bullets": [
            ("Integração com Meta, Google, GA4 e CRM", "Conexão nativa. Histórico puxado de uma vez, atualização em tempo real, sem ETL manual."),
            ("Atribuição multi-touch", "Modelo que conta toda a jornada (não só last-click). Mostra qual canal abre, qual nutre, qual fecha."),
            ("Relatório no canal que você usa", "Semanal no e-mail, diário no WhatsApp, ao vivo no dashboard. Fim do PowerPoint mensal de agência."),
        ],
        "s4_title_pre": "3 passos.",
        "s4_title_accent": "Dado no lugar certo.",
        "s4_steps": [
            ("Conectar contas", "Meta, Google, GA4, RD Station, HubSpot, Pipedrive. Login OAuth, sem chave de API manual."),
            ("Definir métricas e alertas", "ROAS, CAC, LTV, CPL — você escolhe o que importa e o limite que dispara alerta."),
            ("Receber o número onde decide", "Dashboard ao vivo, e-mail semanal e mensagem diária no WhatsApp com os 3 números que importam hoje."),
        ],
        "s5_title_pre": "Decisão",
        "s5_title_accent": "com dado de hoje.",
        "s5_stat": "real-time",
        "s5_label": "Atualização contínua das plataformas — sem espera por consolidação mensal.",
        "s5_body": "Reunião deixa de discutir número e passa a discutir decisão. Marketing investe no canal que tem comprovação. Vendas e finanças olham para o mesmo dado, na mesma hora.",
        "s6_title_pre": "Quer o GL Data",
        "s6_title_accent": "conectado nos seus canais?",
        "s6_body": "30 minutos com um especialista da GuessLess. A gente vê quais plataformas você usa e mostra como o GL Data consolida sua decisão.",
        "wa_msg": "Olá! Vi o pitch do GL Data no estande do SPIW e quero decisão com dado em tempo real, não planilha mensal. Quero agendar a call de 30 min.",
    },
]


def render(p):
    html = TEMPLATE

    # <title>
    html = html.replace(
        "<title>LPMaker — Landing pages que convertem · GL Suite</title>",
        f"<title>{p['meta_title']}</title>",
    )

    # meta description
    html = html.replace(
        '<meta name="description" content="LPMaker da GL Suite: landing pages publicadas em horas, com A/B nativo e integração direta com CRM. Veja o pitch em 6 slides.">',
        f'<meta name="description" content="{p["meta_desc"]}">',
    )
    html = html.replace(
        '<meta property="og:title" content="LPMaker — Landing pages que convertem">',
        f'<meta property="og:title" content="{p["og_title"]}">',
    )
    html = html.replace(
        '<meta property="og:description" content="Página nova no ar em horas, sem dev, sem fila. Tráfego pago para de queimar em LP fraca.">',
        f'<meta property="og:description" content="{p["og_desc"]}">',
    )

    # SLIDE 1
    html = html.replace(
        '<span class="tag">Frente Criação</span>',
        f'<span class="tag">Frente {p["frente"]}</span>',
    )
    html = html.replace(
        '<h1 class="slide-title">LPMaker.<br><span class="accent">Páginas que convertem.</span></h1>',
        f'<h1 class="slide-title">{p["s1_headline"]}<br><span class="accent">{p["s1_accent"]}</span></h1>',
    )
    html = html.replace(
        '<p class="slide-lead">Landing pages publicadas em horas — sem dev, sem fila, com A/B nativo e integração direta com CRM.</p>',
        f'<p class="slide-lead">{p["s1_lead"]}</p>',
    )

    # SLIDE 2
    html = html.replace(
        '<h2 class="slide-title">Sua LP fica presa no <span class="accent">vai-e-volta com dev.</span></h2>',
        f'<h2 class="slide-title">{p["s2_title_pre"]} <span class="accent">{p["s2_title_accent"]}</span></h2>',
    )
    s2_bullets_html = "\n        ".join(
        f'<li><span class="marker">!</span><span><b>{b}</b>{t}</span></li>'
        for (b, t) in p["s2_bullets"]
    )
    s2_old = '''<ul class="bullets">
        <li><span class="marker">!</span><span><b>Cada campanha espera semana de fila</b>até a página subir. O momentum do lançamento evapora antes do anúncio rodar.</span></li>
        <li><span class="marker">!</span><span><b>Tráfego pago queima orçamento em LP fraca</b>— CPL inflado porque a página não converte, não porque o criativo é ruim.</span></li>
        <li><span class="marker">!</span><span><b>A/B test virou luxo</b>— você publica uma versão e reza. Sem experimento, não há como saber o que vende.</span></li>
      </ul>'''
    s2_new = f'<ul class="bullets">\n        {s2_bullets_html}\n      </ul>'
    html = html.replace(s2_old, s2_new)

    # SLIDE 3
    html = html.replace(
        '<h2 class="slide-title">Você publica. <span class="accent">Hoje.</span></h2>',
        f'<h2 class="slide-title">{p["s3_title_pre"]} <span class="accent">{p["s3_title_accent"]}</span></h2>',
    )
    html = html.replace(
        '<p class="slide-body">LPMaker é o editor de páginas da GL Suite — feito pra time de marketing operar sem depender de TI.</p>',
        f'<p class="slide-body">{p["s3_body"]}</p>',
    )
    s3_bullets_html = "\n        ".join(
        f'<li><span class="marker">✓</span><span><b>{b}</b>{t}</span></li>'
        for (b, t) in p["s3_bullets"]
    )
    s3_old = '''<ul class="bullets">
        <li><span class="marker">✓</span><span><b>Builder visual</b>Escolhe template otimizado por categoria, edita texto e imagem no canvas, publica no seu domínio.</span></li>
        <li><span class="marker">✓</span><span><b>A/B nativo</b>Testa headline, CTA, hero — sem plugar ferramenta externa nem código.</span></li>
        <li><span class="marker">✓</span><span><b>Integração com CRM e formulários</b>Lead cai direto no RD Station, no Atlas, ou onde sua operação já vive.</span></li>
      </ul>'''
    s3_new = f'<ul class="bullets">\n        {s3_bullets_html}\n      </ul>'
    html = html.replace(s3_old, s3_new)

    # SLIDE 4
    html = html.replace(
        '<h2 class="slide-title">3 passos. <span class="accent">Sem código.</span></h2>',
        f'<h2 class="slide-title">{p["s4_title_pre"]} <span class="accent">{p["s4_title_accent"]}</span></h2>',
    )
    s4_steps_html = "\n        ".join(
        f'<li><span class="step-num">0{i+1}</span><div><b>{b}</b><p>{t}</p></div></li>'
        for i, (b, t) in enumerate(p["s4_steps"])
    )
    s4_old = '''<ol class="steps">
        <li><span class="step-num">01</span><div><b>Escolha o template</b><p>Biblioteca por categoria: SaaS, e-commerce, serviços, infoproduto, evento. Cada template já vem otimizado pra conversão.</p></div></li>
        <li><span class="step-num">02</span><div><b>Edite no canvas visual</b><p>Texto, imagem, cor, CTA, formulário. Em mobile e desktop, com preview ao vivo.</p></div></li>
        <li><span class="step-num">03</span><div><b>Publique com SSL automático</b><p>No seu domínio, com clean URLs e cache CDN. Sem deploy, sem build, sem dev.</p></div></li>
      </ol>'''
    s4_new = f'<ol class="steps">\n        {s4_steps_html}\n      </ol>'
    html = html.replace(s4_old, s4_new)

    # SLIDE 5
    html = html.replace(
        '<h2 class="slide-title">De semanas <span class="accent">pra horas.</span></h2>',
        f'<h2 class="slide-title">{p["s5_title_pre"]} <span class="accent">{p["s5_title_accent"]}</span></h2>',
    )
    html = html.replace(
        '<div class="stat-num"><span class="accent">~3h</span></div>',
        f'<div class="stat-num"><span class="accent">{p["s5_stat"]}</span></div>',
    )
    html = html.replace(
        '<div class="stat-label">Tempo médio para publicar uma LP nova, do briefing ao ar.</div>',
        f'<div class="stat-label">{p["s5_label"]}</div>',
    )
    html = html.replace(
        '<p class="slide-body">Cada campanha vira oportunidade de teste. Publica duas variações de hero, deixa o tráfego decidir, escala a vencedora. ROAS sobe sem trocar criativo — só trocando a porta de entrada.</p>',
        f'<p class="slide-body">{p["s5_body"]}</p>',
    )

    # SLIDE 6
    html = html.replace(
        '<h2 class="slide-title">Quer ver o LPMaker <span class="accent">rodando ao vivo?</span></h2>',
        f'<h2 class="slide-title">{p["s6_title_pre"]} <span class="accent">{p["s6_title_accent"]}</span></h2>',
    )
    html = html.replace(
        '<p class="slide-body">30 minutos com um especialista da GuessLess. A gente entende sua operação e te mostra como montar a primeira LP nessa semana.</p>',
        f'<p class="slide-body">{p["s6_body"]}</p>',
    )

    # PRODUCT object no JS
    html = html.replace(
        "    slug:'lpmaker',",
        f"    slug:'{p['slug']}',",
    )
    html = html.replace(
        "    nome:'LPMaker',",
        f"    nome:'{p['nome']}',",
    )
    html = html.replace(
        "    waMsg:'Olá! Vi o pitch do LPMaker no estande do SPIW e quero entender como aplicar pra publicar LPs sem depender de dev. Quero agendar a call de 30 min.'",
        f"    waMsg:'{p['wa_msg']}'",
    )

    return html


def main():
    produtos_dir = ROOT / "produtos"
    for p in PRODUCTS:
        out_dir = produtos_dir / p["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "index.html"
        out_path.write_text(render(p), encoding="utf-8")
        print(f"wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
