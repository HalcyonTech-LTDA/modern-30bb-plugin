<div align="center">

# Modern 30BB Business Blueprint Plugin
### 30-Day Business Blueprint Engine & Strategic Formulation Architecture

[![Antigravity Plugin](https://img.shields.io/badge/Antigravity-Plugin%20v1.0.0-4F46E5.svg)](https://antigravity.google)
[![License: MIT](https://img.shields.io/badge/License-MIT-10B981.svg)](./LICENSE)
[![Organization](https://img.shields.io/badge/Organization-HalcyonTech--LTDA-black.svg)](https://github.com/HalcyonTech-LTDA)

<p align="center">
  <b>Framework executivo e orquestrador para construção de Planos Mestres de Negócios (Master Business Blueprints) estruturados em 30 Seções Mestras (I a XXX) distribuídas em 8 Pilares Estratégicos: Fundamentos da Tese e Categoria, Arquitetura de Plataforma Horizontal, Cunha de Entrada (Beachhead & Wedge) e Expansão (Land & Expand / Horizontal), Monetização em 6 Camadas e Empacotamento (MaaS / DaaS), Branding e Naming Institucional, Blindagem Societária (100% IP e Acordo de Acionistas de 5 Blocos), Organização Enxuta, SDLC Anti-Customização e Cibersegurança (LGPD/SOC 2/ISO 27001), Go-To-Market Enterprise (50 Target Accounts, Funil de 14 Etapas e 3 Ondas de Canais), DRE Gerencial, Painel de KPIs, Financiamento por 4 Gates, Master Roadmap de 18 Meses, Fosso Competitivo (Moat) e Manifesto Empresarial.</b>
</p>

</div>

---

## Installation & Verification

### Antigravity CLI (`agy`)

Install directly into your Antigravity environment via the CLI:

```bash
agy plugin install https://github.com/HalcyonTech-LTDA/modern-30bb-plugin
```

Verify that the plugin is active and adheres to the strict official schema:

```bash
agy plugin list
agy plugin validate --strict ./modern-30bb-plugin
```

---

## Visão Geral: O Padrão 30BB (30 Seções Mestras em 8 Pilares)

Planos de negócios tradicionais costumam falhar por dois extremos: ou são resumos superficiais de *pitch deck* que ignoram blindagem societária, arquitetura técnica, limites de fornecedores e *unit economics*, ou são documentos prolixos e repetitivos com dezenas de tópicos desconexos.

O **Modern 30BB Plugin** consolida os 46 tópicos executivos clássicos de concepção empresarial em **30 Seções Mestras (I a XXX)** sem nenhuma redundância e agrupadas em **8 Pilares Estratégicos**:

| Pilar Estratégico | Seções Mestras | Escopo Executivo |
| :--- | :--- | :--- |
| **1. Fundamentos da Tese e Proposta de Valor** | **I a III** | Paradoxo do mercado, Matriz do Status Quo, Ciclo de 6 etapas da última milha, Antiposicionamento, Definição de Categoria, Cadeia de Valor (`INSUMO BRUTO → ... → EVIDÊNCIA`), Verdadeiro Objeto Econômico e Mantra. |
| **2. Arquitetura de Produto, Entrada e Expansão** | **IV a XI** | Core Platform horizontal (6 camadas) vs. Soluções, Beachhead (4 critérios raros + TAM/SAM/SOM), Produto 1 (*Wedge*), Precauções Tecnológicas e Mitigação de Riscos, Land & Expand (Módulos 2–6), Expansão Horizontal (5+ indústrias), Motor de Otimização de Custos + Calculadora de ROI e Visão de Marketplace (*North Star*). |
| **3. Modelo de Monetização e Empacotamento Comercial** | **XII e XIII** | Arquitetura híbrida de receitas em 6 linhas (*Platform, Monitoring, Usage, Consumption Margin, Modules, Implementation*) e duplo empacotamento (*Monitoring-as-a-Service* e *Decisioning-as-a-Service via API*). |
| **4. Marca, Naming e Comunicação Executiva** | **XIV e XV** | Públicos de autoridade da marca, Restrição Semântica horizontal, Territórios de Naming (com análise de conflito e validação INPI/USPTO), *Elevator Pitch* e *Taglines*. |
| **5. Blindagem Societária, Propriedade Intelectual e Governança** | **XVI a XVIII** | Propriedade integral (100% IP na companhia), Governança sobre parceiros técnicos (`[PARCEIRO] desenvolve; [COMPANHIA] possui`), Governança executiva sem conselho ornamental (10 blocos mensais) e Acordo de Acionistas de 5 blocos no Mês 0. |
| **6. Organização, Cultura, Operações e Conformidade** | **XIX a XXIII** | Organograma enxuto (Produto 100% interno) e sede híbrida, Cultura adulta de alta performance e remuneração (Fixo + Variável + SOP seletivo), Esteira formal de SDLC (10 etapas + Regra Anti-Customização *Zero Forks*), Cibersegurança (LGPD, ISO 27001, SOC 2 Tipo II) e Checklist Jurídico. |
| **7. Go-To-Market (GTM), Máquina de Vendas e Customer Success** | **XXIV a XXVII** | ICP Enterprise (Agregadores/Multiplicadores em 1º lugar), *Founder-Led Sales*, 50 *Target Accounts*, Comitê de Compra, Funil CRM de 14 etapas, 3 Ondas de Canais (*Direct, Referrals, OEM/Embedded*), *Thought Leadership* (`CREDIBILITY → EDUCATION → DEMAND`) e CS Escalável. |
| **8. Economia, Finanças, Execução e Tese de Investimento** | **XXVIII a XXX** | DRE Gerencial (separando Software de Repasse/COGS com Margem Bruta como termômetro), Painel Mensal de KPIs (6 dimensões), Financiamento em 4 Capital Gates (12–18m *runway*), Master Roadmap de 18 Meses (5 Fases M0–M18), Renúncias Estratégicas, Flywheel da Tese de Investimento, Moat e Manifesto Empresarial. |

---

---

## Validação Automatizada de Blueprints

O plugin inclui um script CLI de verificação estrutural que inspeciona qualquer documento Markdown e valida a presença dos 8 Pilares, das 30 Seções Mestras (`I.` a `XXX.`), das tabelas/equações obrigatórias e de eventuais placeholders pendentes:

```bash
# Validar um Blueprint preenchido (reprova com exit code 1 se faltar seção, trava estrutural ou se restarem placeholders):
python3 ~/.gemini/config/plugins/modern-30bb-plugin/skills/modern-30bb-orchestrator/scripts/validate_30bb_blueprint.py caminho/para/meu-blueprint.md

# Validar um Template em branco preenchível (exit code 0 se as 30 seções, 8 pilares e 13 travas estiverem íntegros):
python3 ~/.gemini/config/plugins/modern-30bb-plugin/skills/modern-30bb-orchestrator/scripts/validate_30bb_blueprint.py ~/.gemini/config/plugins/modern-30bb-plugin/skills/modern-30bb-orchestrator/resources/master-30bb-template.md --allow-placeholders
```

---

---

## What's Included (Component Catalog)

### Contextual Rules (`rules/`)
Automatically loaded to govern and protect project contexts:
- **[`modern-30bb-blueprint-standards.md`](rules/modern-30bb-blueprint-standards.md)**: >-

### Procedural Skills (`skills/`)
On-demand actionable workflows and runbooks:
- **[`/modern-30bb-economics-roadmap-and-moat`](skills/modern-30bb-economics-roadmap-and-moat/SKILL.md)**: Use this skill when structuring or refining Pillar 8 (Sections XXVIII to XXX) of a Modern 30BB Business Blueprint: Managerial DRE (segregating Software Revenue from Data/Third-Party COGS & Gross Margin thermometer), 6-Dimension Partner KPI Panel, 4-Gate Risk-Reduction Funding Strategy (12-18m Runway), 5-Phase 18-Month Master Roadmap, Strategic Renunciations ("What We Will NOT Do"), Investment Thesis Flywheel, 8-Factor Cumulative Moat, and Corporate Manifesto.
- **[`/modern-30bb-governance-ops-and-legal`](skills/modern-30bb-governance-ops-and-legal/SKILL.md)**: Use this skill when structuring or refining Pillar 5 (Sections XVI to XVIII: 100% Unencumbered IP Ownership, Technical Partner Governance, Anti-Ornamental Executive Governance & 10-Block Monthly Ritual, Month-0 Shareholders' Agreement) and Pillar 6 (Sections XIX to XXIII: Lean Org & Hybrid HQ, High-Performance Adult Culture, 10-Stage Anti-Customization SDLC, Cybersecurity Moat & 4-Front Legal Shield) of a Modern 30BB Business Blueprint.
- **[`/modern-30bb-monetization-and-gtm`](skills/modern-30bb-monetization-and-gtm/SKILL.md)**: Use this skill when structuring or refining Pillar 3 (Sections XII and XIII: 6-Component Revenue & Pricing Model, Dual Commercial Packaging — Continuous Monitoring vs. Transactional API Decisioning) and Pillar 7 (Sections XXIV to XXVII: Aggregator-First Enterprise ICP, 50 Target Accounts, 14-Stage CRM Sales Funnel, 3 Distribution Waves, Thought Leadership & Scalable CS) of a Modern 30BB Business Blueprint.
- **[`/modern-30bb-orchestrator`](skills/modern-30bb-orchestrator/SKILL.md)**: Use this skill when the user asks to create, generate, structure, expand, or audit a complete Master Business Blueprint ("Plano Mestre da Nova Companhia") from a new business idea, startup pitch, or strategic thesis using the 30 Master Sections (I to XXX) across 8 Strategic Pillars (framework 30BB).
- **[`/modern-30bb-product-and-expansion`](skills/modern-30bb-product-and-expansion/SKILL.md)**: Use this skill when designing or refining Pillar 2 (Sections IV to XI) of a Modern 30BB Business Blueprint: Horizontal Core Platform Architecture (6 layers), Beachhead Market Selection & TAM/SAM/SOM Sizing, Product 1 (Wedge Product), Technical Ecosystem Limits & Operational Risk Mitigation, Vertical Land & Expand (Modules 2-6), Horizontal Expansion across New Industries, Cascading Cost Optimization Engine & Customer ROI Equation, and Long-Term Marketplace Vision.
- **[`/modern-30bb-thesis-and-brand`](skills/modern-30bb-thesis-and-brand/SKILL.md)**: Use this skill when structuring or refining Pillar 1 (Sections I to III: Central Thesis, Market Gap, Corporate Identity, Anti-Positioning, Category Design, True Economic Object & Company Mantra) and Pillar 4 (Sections XIV and XV: Brand Principles, Horizontal Semantic Restrictions, Naming Territories, Elevator Pitch & Taglines) of a Modern 30BB Business Blueprint.

### Specialized Subagents (`agents/`)
Autonomous personas delegated for in-depth execution:
- **[`modern_30bb_architect_agent`](agents/modern_30bb_architect_agent.md)**: Arquiteto Estrategista Líder (Lead Business Blueprint Architect & Master Orchestrator) especializado em liderar a construção do Plano Mestre da Nova Companhia (Master Business Blueprint) estruturado rigorosamente nas 30 Seções Mestras (I a XXX) e 8 Pilares Estratégicos do framework 30BB, orquestrando subagentes especialistas via pipeline em fases (Staged Handoff).
- **[`modern_30bb_finance_agent`](agents/modern_30bb_finance_agent.md)**: Subagente Especialista em DRE Gerencial, Financiamento por Gates, Roadmap de 18 Meses, Moat e Manifesto (Pilar 8). Responsável por modelar a DRE segregada (Software vs. Repasse de Terceiros), o painel de KPIs em 6 dimensões, a estratégia de 4 Gates de capital, o Master Roadmap M0-M18, Renúncias Estratégicas, Fosso Competitivo e Manifesto (Seções XXVIII a XXX).
- **[`modern_30bb_governance_agent`](agents/modern_30bb_governance_agent.md)**: Subagente Especialista em Blindagem Societária, Governança, Cultura, SDLC Anti-Customização e Cibersegurança (Pilar 5 e Pilar 6). Responsável por definir a titularidade 100% de IP, governança de parceiros técnicos, Acordo de Acionistas, organograma enxuto, esteira SDLC de 10 etapas, cibersegurança e compliance (Seções XVI a XXIII).
- **[`modern_30bb_gtm_agent`](agents/modern_30bb_gtm_agent.md)**: Subagente Especialista em Go-To-Market Enterprise, Estratégia Comercial e Sucesso do Cliente (Pilar 7). Responsável por mapear o ICP inicial de agregadores, listar as 50 contas-alvo, estruturar o funil de CRM de 14 etapas, as 3 ondas de distribuição, autoridade executiva e CS escalável (Seções XXIV a XXVII).
- **[`modern_30bb_product_agent`](agents/modern_30bb_product_agent.md)**: Subagente Especialista em Plataforma Horizontal, Beachhead, Wedge, Expansão e Modelo de Monetização (Pilar 2 e Pilar 3). Responsável por definir a Core Platform de 6 camadas, o dimensionamento TAM/SAM/SOM, o Produto 1 (Wedge), Land & Expand, Calculadora de ROI, Precificação em 6 Linhas e Empacotamento MaaS vs DaaS (Seções IV a XIII).
- **[`modern_30bb_thesis_agent`](agents/modern_30bb_thesis_agent.md)**: Subagente Estrategista de Tese, Categoria e Naming Corporativo (Pilar 1 e Pilar 4). Responsável por definir o Paradoxo do Mercado, a Matriz do Status Quo, o Antiposicionamento, a Cadeia de Valor de 6 etapas, o Verdadeiro Objeto Econômico, o Mantra e o Naming Institucional (Seções I a III e XIV a XV).

---

## Directory Hierarchy

```text
modern-30bb-plugin/
├── plugin.json              # Official Antigravity manifest (schema v1)
├── LICENSE                  # MIT License (Copyright 2026 HalcyonTech LTDA)
├── .gitignore               # System ignores & installed_version.json exclusions
├── .gitattributes           # Deterministic line endings (* text=auto eol=lf)
├── README.md                # Golden Standard documentation & runbook
├── assets/
│   └── logo.svg             # Official Halcyon Tech corporate vector symbol
├── rules/                   # Contextual rules discovered automatically
│   └── modern-30bb-blueprint-standards.md
├── skills/                  # Actionable procedural skills (Progressive Disclosure)
│   └── modern-30bb-economics-roadmap-and-moat/
│       └── SKILL.md
│   └── modern-30bb-governance-ops-and-legal/
│       └── SKILL.md
│   └── modern-30bb-monetization-and-gtm/
│       └── SKILL.md
│   └── modern-30bb-orchestrator/
│       └── SKILL.md
│   └── modern-30bb-product-and-expansion/
│       └── SKILL.md
│   └── modern-30bb-thesis-and-brand/
│       └── SKILL.md
└── agents/                  # Specialized autonomous subagents
    └── modern_30bb_architect_agent.md
    └── modern_30bb_finance_agent.md
    └── modern_30bb_governance_agent.md
    └── modern_30bb_gtm_agent.md
    └── modern_30bb_product_agent.md
    └── modern_30bb_thesis_agent.md
```

---

## 💡 Prompt Recipes & Use Cases

```markdown
- "Crie um Master Business Blueprint completo nas 30 Seções Mestras (I a XXX) e 8 Pilares para a seguinte ideia de negócio:"
- "Aplique o framework 30BB para transformar este rascunho em uma Tese de Investimento e Plano Mestre de Implantação de 18 meses"
- "Estruture o Pilar 1 e Pilar 4 (Tese Central, Antiposicionamento, Categoria, Mantra e Naming) para uma nova plataforma B2B"
- "Desenhe o Pilar 2 (Core Platform de 6 camadas, Beachhead TAM/SAM/SOM, Produto 1 Wedge, Land & Expand e Calculadora de ROI)"
- "Modele o Pilar 3 e Pilar 7 (Precificação em 6 linhas, Empacotamento API/Monitoramento, ICP de 50 Contas, Funil de 14 etapas e CS Escalável)"
- "Elabore o Pilar 5 e Pilar 6 (Blindagem 100% IP, Governança de 10 blocos, Acordo de Acionistas, SDLC Zero-Forks, Cibersegurança e Contratos)"
- "Construa o Pilar 8 (DRE Gerencial Software vs. Repasse, Painel de KPIs, 4 Gates de Capital, Roadmap de 18 Meses, Moat e Manifesto)"
- "Valide se o meu documento de Business Blueprint cumpre rigorosamente todas as 30 Seções Mestras do padrão 30BB"
```

---

## 📄 License & Corporate Governance

Distributed under the **MIT License**. Copyright (c) 2026 **HalcyonTech LTDA**.  
Engineered with precision and excellence by [Halcyon Tech](https://github.com/HalcyonTech-LTDA).
