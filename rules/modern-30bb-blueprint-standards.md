---
description: >-
  Automatically enforces Modern 30BB Business Blueprint standards when structuring, authoring, auditing, or refactoring
  business ideas, investment theses, and company conception plans into the 30 Master Sections (I to XXX) across 8 Strategic Pillars:
  (1) Thesis & Value Proposition, (2) Horizontal Core Platform, Beachhead, Wedge & Expansion, (3) 6-Line Monetization & Packaging,
  (4) Brand & Executive Naming, (5) 100% IP Shield & Corporate Governance, (6) Lean Org, Anti-Customization SDLC, Cybersecurity & Legal,
  (7) Enterprise GTM, 14-Stage CRM Funnel & Scalable CS, and (8) Managerial DRE, KPIs, 4 Capital Gates, 18-Month Roadmap, Moat & Manifesto.
trigger: model_decision
---

# Modern 30BB Business Blueprint Guardrails & Skill Router

When transforming raw business ideas, founder notes, or partial strategic drafts into institutional-grade **Master Business Blueprints ("Plano Mestre da Nova Companhia")**, strictly adhere to the **Modern 30BB Standard (30 Master Sections across 8 Strategic Pillars)** and activate the corresponding specialized skills or subagents:

| When working on... | Consult Skill / Subagent | Key Focus Areas & Sections Covered |
| :--- | :--- | :--- |
| **End-to-End Orchestration & Multi-Agent Pipeline** | `modern-30bb-orchestrator`<br/>(`modern-30bb-architect-agent`) | Full 30-Section (I–XXX) / 8-Pillar blueprint orchestration, intake dissection, staged multi-agent pipeline handoff, and automated completeness validation (`validate_30bb_blueprint.py`). |
| **Thesis, Category Design, Mantra & Executive Branding** | `modern-30bb-thesis-and-brand`<br/>(`modern-30bb-thesis-agent`) | **Pilares 1 & 4 (Seções I–III, XIV–XV)**: Paradoxo de mercado, Matriz do Status Quo, Antiposicionamento, Cadeia de Valor (`INSUMO BRUTO → ... → EVIDÊNCIA`), Objeto Econômico Real, Mantra, Filtros Semânticos de Marca, Territórios de Naming e Taglines. |
| **Platform Architecture, Beachhead, Wedge, Expansion & Pricing** | `modern-30bb-product-and-expansion`<br/>`modern-30bb-monetization-and-gtm`<br/>(`modern-30bb-product-agent`) | **Pilares 2 & 3 (Seções IV–XIII)**: Core Platform horizontal de 6 camadas, Beachhead (4 critérios + TAM/SAM/SOM), Produto 1 (Wedge), Limites Técnicos e Mitigação de Riscos, Land & Expand (Módulos 2–6), Expansão Horizontal, Cost Optimization Engine + Equação de ROI, 6 linhas de receita e duplo empacotamento MaaS/DaaS. |
| **100% IP Shield, Governance, SHA, Lean Org, SDLC & Legal** | `modern-30bb-governance-ops-and-legal`<br/>(`modern-30bb-governance-agent`) | **Pilares 5 & 6 (Seções XVI–XXIII)**: Propriedade integral (100% IP) e regra de parceiros técnicos (`[PARCEIRO] desenvolve; [COMPANHIA] possui`), Governança sem conselho ornamental (10 blocos mensais), Acordo de Acionistas (5 blocos no M0), Organização enxuta e sede híbrida, Cultura de alta performance, SDLC formal Zero-Forks, Cibersegurança (LGPD/ISO 27001/SOC 2) e Checklist Jurídico. |
| **Enterprise GTM, 14-Stage CRM & Scalable CS** | `modern-30bb-monetization-and-gtm`<br/>(`modern-30bb-gtm-agent`) | **Pilar 7 (Seções XXIV–XXVII)**: ICP Enterprise (Agregadores + 50 Target Accounts), Comitê de Compra, Funil CRM de 14 etapas, 3 Ondas de Canais, Thought Leadership e CS Escalável (Lei Fundamental de Escalabilidade Operacional). |
| **Managerial DRE, KPIs, 4 Capital Gates, 18m Roadmap & Moat** | `modern-30bb-economics-roadmap-and-moat`<br/>(`modern-30bb-finance-agent`) | **Pilar 8 (Seções XXVIII–XXX)**: DRE Gerencial (segregando Software de Repasse/COGS), Painel Mensal de KPIs (6 dimensões), Financiamento por 4 Gates de redução de risco (12–18m runway), Master Roadmap Integrado de 18 Meses (5 Fases M0–M18), Renúncias Estratégicas, Flywheel da Tese de Investimento, Fosso Competitivo (Moat) e Manifesto Empresarial. |

---

## Architectural Blueprint Map (30 Master Sections across 8 Pillars)

Every complete Master Business Blueprint must preserve the canonical 8-Pillar, 30-Section Roman-numeral hierarchy:

1. **PILAR 1: FUNDAMENTOS DA TESE E PROPOSTA DE VALOR**
   - `### I. A TESE CENTRAL E A LACUNA DE MERCADO (O Problema Identificado)`
   - `### II. IDENTIDADE CORPORATIVA, ANTIPOSICIONAMENTO E DEFINIÇÃO DE CATEGORIA`
   - `### III. A GRANDE MUDANÇA DE PERSPECTIVA E O MANTRA DA COMPANHIA`
2. **PILAR 2: ARQUITETURA DE PRODUTO, ENTRADA E EXPANSÃO**
   - `### IV. A ARQUITETURA DO NEGÓCIO (Uma Plataforma, Vários Produtos)`
   - `### V. O BEACHHEAD (Mercado de Entrada) E DIMENSIONAMENTO INICIAL`
   - `### VI. PRODUTO 1 (A Cunha Comercial / Wedge Product)`
   - `### VII. PRECAUÇÕES TECNOLÓGICAS, LIMITES DO ECOSSISTEMA E MITIGAÇÃO DE RISCOS`
   - `### VIII. EXPANSÃO VERTICAL (Land and Expand no Mercado Inicial)`
   - `### IX. A EXPANSÃO HORIZONTAL (Novas Verticais de Mercado)`
   - `### X. O SEGUNDO DIFERENCIAL ECONÔMICO (Otimização de Custos e Calculadora de ROI)`
   - `### XI. A VISÃO DE LONGO PRAZO (Do Produto ao Ecossistema / Marketplace)`
3. **PILAR 3: MODELO DE MONETIZAÇÃO E EMPACOTAMENTO COMERCIAL**
   - `### XII. ARQUITETURA DE RECEITAS E PRECIFICAÇÃO (Pricing Model)`
   - `### XIII. MODALIDADES DE EMPACOTAMENTO COMERCIAL`
4. **PILAR 4: MARCA, NAMING E COMUNICAÇÃO EXECUTIVA**
   - `### XIV. PRINCÍPIOS DE MARCA E FILTROS DE BRANDING`
   - `### XV. TERRITÓRIOS DE NAMING, FRASE DE SUSTENTAÇÃO E TAGLINES`
5. **PILAR 5: BLINDAGEM SOCIETÁRIA, PROPRIEDADE INTELECTUAL E GOVERNANÇA**
   - `### XVI. TITULARIDADE PATRIMONIAL, PROPRIEDADE INTELECTUAL E PARCEIROS TÉCNICOS`
   - `### XVII. GOVERNANÇA EXECUTIVA E RITOS DE GESTÃO`
   - `### XVIII. ACORDO DE ACIONISTAS E REGRAS SOCIETÁRIAS CRÍTICAS`
6. **PILAR 6: ORGANIZAÇÃO, CULTURA, OPERAÇÕES E CONFORMIDADE**
   - `### XIX. ESTRUTURA ORGANIZACIONAL INICIAL E SEDE`
   - `### XX. FILOSOFIA CULTURAL, RH E REMUNERAÇÃO`
   - `### XXI. GOVERNANÇA DE PRODUTO, ENGENHARIA E QUALIDADE (SDLC)`
   - `### XXII. CIBERSEGURANÇA, CONFIABILIDADE E CONTINUIDADE`
   - `### XXIII. ARCABOUÇO JURÍDICO, CONTRATUAL E REGULATÓRIO`
7. **PILAR 7: GO-TO-MARKET (GTM), MÁQUINA DE VENDAS E SUCESSO DO CLIENTE**
   - `### XXIV. ICP INICIAL E ESTRATÉGIA DE VENDAS ENTERPRISE`
   - `### XXV. FUNIL DE VENDAS E ONDAS DE CANAIS DE DISTRIBUIÇÃO`
   - `### XXVI. MARKETING DE AUTORIDADE (Thought Leadership)`
   - `### XXVII. CUSTOMER SUCCESS E IMPLANTAÇÃO ESCALÁVEL`
8. **PILAR 8: ECONOMIA, FINANÇAS, EXECUÇÃO E TESE DE INVESTIMENTO**
   - `### XXVIII. ECONOMIA DA COMPANHIA (DRE GERENCIAL) E PAINEL DE KPIs`
   - `### XXIX. FINANCIAMENTO POR GATES, PLANO DE 18 MESES E RENÚNCIAS ESTRATÉGICAS`
   - `### XXX. A TESE DE INVESTIMENTO, O MOAT (FOSSO COMPETITIVO) E O MANIFESTO`

---

## Non-Negotiable Guardrails (Absolute Invariants)

1. **Complete 6-Stage Value Chain & Dynamic Economic Object (Sections I–III)**:
   - Never position the company as a commodity input reseller, software house, or manual consultancy. Express the core value chain strictly as:
     `[INSUMO BRUTO] → [SINAL] → [CONTEXTO] → [DECISÃO] → [AÇÃO] → [EVIDÊNCIA]`
   - Contrast the static legacy market question against the company's dynamic, continuous, and actionable mantra.
2. **Horizontal Core Platform vs. Ultra-Focused Beachhead Entry (Sections IV–VI)**:
   - Architecture must decouple the **Corporate Brand**, the **Core Platform** (6 reusable horizontal layers: Ingestion, Continuous Monitoring, Rules/Decision Engine, Workflow Automation, Immutable Audit Trail, APIs/Webhooks), and **Configurable Vertical Solutions**.
   - Never start by selling horizontally: justify the **Beachhead** via 4 mandatory criteria (*Obrigatoriedade/Urgência, Volume Massivo, Alto Custo do Erro, Capacidade Econômica*) and quantify **SOM, SAM, and TAM**.
3. **Technical Honesty & Cascading Cost Optimization ROI (Sections VII & X)**:
   - Calibrate commercial promises to external ecosystem limits (e.g., *Monitoramento Contínuo + Decisão Orientada a Eventos* rather than false "zero latency at third-party source"), backed by multi-provider fallback and normalization.
   - Prove the platform is *self-funding* via a cascading **Cost Optimization Engine** and explicit CFO **ROI Equation**:
     $$\text{ROI Anual do Cliente} = \frac{(\text{Economia de Insumos} + \text{Horas Manuais Poupadas} + \text{Perdas/Multas Evitadas}) - \text{Custo Anual da Plataforma}}{\text{Custo Anual da Plataforma}}$$
4. **Hybrid 6-Line Revenue Architecture & Dual Packaging (Sections XII–XIII)**:
   - Structure monetization across 6 distinct economic functions: *Platform Fee, Monitoring/Entity Fee, Usage/Decision Fee, Consumption Margin, Additional Modules,* and *Implementation Fee*.
   - Package commercially both as **Continuous Monitoring-as-a-Service** (exception management) and **Transactional API Decisioning-as-a-Service** (`INPUT → [MARCA] → OUTPUT` with *Reason Code, Consulted Sources, Timestamp, Applied Policy, Audit Evidence*).
5. **Horizontal Brand Hygiene & Validated Naming (Sections XIV–XV)**:
   - Prohibit niche-restrictive words in the corporate name (so the brand never traps the company in Product 1). Require INPI/USPTO trademark and domain availability verification before public launch.
6. **100% Unencumbered IP Ownership & Month-0 Shareholders' Agreement (Sections XVI–XVIII)**:
   - The operating company must hold 100% of IP, code, Git repositories, cloud accounts, rules, derived data, and contracts. For technical partners (including related-party software houses): **`[PARCEIRO]` desenvolve; `[COMPANHIA]` possui** under strict *Work-for-Hire* assignment.
   - Ban premature ornamental Boards of Directors; enforce a 10-block monthly executive ritual ending every item with `Decisão → Responsável Nominal → Prazo Fatal`.
   - Mandate a Month-0 Shareholders' Agreement covering 5 blocks: *Reserved Matters, Capital/Dilution, Lock-up/ROFR/Tag/Drag, Vesting & Good/Bad Leaver,* and *Non-Compete/Deadlock/Related-Party Voting Abstention*.
7. **Lean Organization, Anti-Customization SDLC & Security as a Sales Lever (Sections XIX–XXI, XXII–XXIII)**:
   - Keep Product 100% internal and real estate hybrid/lean (`Produto + Segurança + Pessoas + Clientes`, never ostentatious offices).
   - Enforce a 10-stage formal SDLC across segregated `Development | Staging | Production` environments and the **Anti-Customization Rule (Zero Forks)**: every client request must become a configurable parameter or module in the Core Platform.
   - Treat Cybersecurity as *Operational Requirement + Competitive Barrier + Sales Lever* (LGPD, ISO 27001, SOC 2 Type II readiness) alongside the 4-pillar Legal Shield Checklist.
8. **Aggregator-First Enterprise GTM, 14-Stage CRM & Scalable CS (Sections XXIV–XXVII)**:
   - Target high-volume aggregators/multipliers first via *Founder-Led Enterprise Sales* and 50 named *Target Accounts*, mapping Economic Buyers, Internal Champions, and Technical Evaluators.
   - Enforce the 14-stage CRM funnel from Day 1, the 3 distribution waves (*Direct → Strategic Referrals → OEM/Embedded*), the `CREDIBILITY → EDUCATION → DEMAND` authority marketing sequence, and the **Fundamental Law of Operational Scalability** (each new customer onboarding must require fewer manual hours than the previous one).
9. **Software-Segregated Managerial DRE, 4 Capital Gates & 18-Month Master Roadmap (Sections XXVIII–XXX)**:
   - Separate Gross Revenue lines from direct **COGS** (third-party data/inputs, production cloud, inline processing, direct CS) so **Gross Margin (%)** acts as the explicit thermometer proving software economics vs. input reselling.
   - Structure financing across **4 Risk-Reduction Capital Gates** (12–18 months runway: *Gate 1 Build M0–M5, Gate 2 Validation M5–M8, Gate 3 Commercial Validation M8–M12, Gate 4 Scale M12–M18+*), paired with the 5-Phase 18-Month Roadmap, explicit Strategic Renunciations (*O Que NÃO Faremos*), the 7-effect Investment Flywheel, the 8-factor Cumulative Moat, and the Corporate Manifesto.
10. **Staged Multi-Agent Pipeline & Context Dependency Assurance**:
   - In multi-agent executions, agents must NEVER be launched in an uncoordinated, flat parallel broadcast.
   - Strictly follow the **Staged Handoff Protocol (Fases 0 → 1 → 2 → [3A + 3B em paralelo] → 4 → 5)**, ensuring every specialist receives the preceding stages' frozen outputs in its prompt to prevent circular hallucinations, metric mismatches between Pricing/DRE, and semantic branding drift.
   - The Lead Orchestrator must run `validate_30bb_blueprint.py` upon completion to certify complete, uncompromised delivery.

Consult the specialized skills in `skills/` for complete fillable structures, reference playbooks, and automated validation scripts.
