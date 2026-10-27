# Modern 30BB Business Blueprint Plugin (`modern-30bb-plugin`)

Um plugin profissional para o **Antigravity** projetado para estruturar, redigir, refinar e auditar **Planos Mestres de Negócios (Master Business Blueprints)** completos a partir de qualquer nova ideia de negócio, tese de investimento ou rascunho executivo, utilizando a arquitetura canônica de **30 Seções Mestras (I a XXX)** distribuídas em **8 Pilares Estratégicos**.

---

## Instalação / Installation

### Antigravity

Instale diretamente no Antigravity via CLI:

```bash
agy plugin install https://github.com/HalcyonTech-LTDA/modern-30bb-plugin
```

Verifique se o plugin está instalado e ativo:

```bash
agy plugin list
```

### Claude Code

Adicione o marketplace da Halcyon Tech uma única vez e instale o plugin:

```text
/plugin marketplace add HalcyonTech-LTDA/halcyon-plugins
/plugin install modern-30bb-plugin@halcyon-plugins
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

## Componentes do Plugin

### 1. Regra de Guardrails e Roteamento (`rules/modern-30bb-blueprint-standards.md`)
Carregada sob demanda (`trigger: model_decision`) para preservar a janela de contexto do agente, impondo os **9 Invariantes Inegociáveis** do padrão 30BB e roteando automaticamente cada tarefa para a skill especializada correspondente.

### 2. Squad Multi-Agentes de Especialistas (`agents/`)
Define a equipe especializada de agentes para orquestração ponta a ponta e redação de cada pilar com rigor institucional:
- **`modern-30bb-architect-agent`** (`agents/modern_30bb_architect_agent.md`): Orquestrador Líder e Integrador Raiz, coordena o pipeline em 6 etapas e executa a homologação final.
- **`modern-30bb-thesis-agent`** (`agents/modern_30bb_thesis_agent.md`): Subagente de Tese e Marca (Pilares 1 e 4: Seções I a III e XIV a XV).
- **`modern-30bb-product-agent`** (`agents/modern_30bb_product_agent.md`): Subagente de Plataforma, Wedge, Expansão e Precificação (Pilares 2 e 3: Seções IV a XIII).
- **`modern-30bb-gtm-agent`** (`agents/modern_30bb_gtm_agent.md`): Subagente de Go-To-Market Enterprise, CRM de 14 etapas e CS Escalável (Pilar 7: Seções XXIV a XXVII).
- **`modern-30bb-governance-agent`** (`agents/modern_30bb_governance_agent.md`): Subagente de Blindagem Societária 100% IP, Acordo de Acionistas, SDLC Zero-Forks e Compliance (Pilares 5 e 6: Seções XVI a XXIII).
- **`modern-30bb-finance-agent`** (`agents/modern_30bb_finance_agent.md`): Subagente de DRE Gerencial, Painel de KPIs, Financiamento por 4 Gates e Moat (Pilar 8: Seções XXVIII a XXX).

### 3. As 6 Skills Especializadas (`skills/`)

1. **`modern-30bb-orchestrator`**:
   - Orquestrador mestre ponta a ponta para transformar qualquer ideia de negócio nas 30 Seções Mestras (I a XXX).
   - Inclui o template canônico completo em `resources/master-30bb-template.md`, a matriz de rastreabilidade dos 46 tópicos originais para as 30 seções em `references/architecture-map-30-sections.md`, e o validador automatizado em Python `scripts/validate_30bb_blueprint.py`.
2. **`modern-30bb-thesis-and-brand`**:
   - Especializada no **Pilar 1 (Seções I–III)** e **Pilar 4 (Seções XIV–XV)**.
3. **`modern-30bb-product-and-expansion`**:
   - Especializada no **Pilar 2 (Seções IV–XI)**.
4. **`modern-30bb-monetization-and-gtm`**:
   - Especializada no **Pilar 3 (Seções XII–XIII)** e **Pilar 7 (Seções XXIV–XXVII)**.
5. **`modern-30bb-governance-ops-and-legal`**:
   - Especializada no **Pilar 5 (Seções XVI–XVIII)** e **Pilar 6 (Seções XIX–XXIII)**.
6. **`modern-30bb-economics-roadmap-and-moat`**:
   - Especializada no **Pilar 8 (Seções XXVIII–XXX)**.

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

## Estrutura de Diretórios

```text
modern-30bb-plugin/
├── plugin.json
├── installed_version.json
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
├── .claude-plugin/
│   └── plugin.json
├── claude/
│   └── skills/
│       └── modern-30bb-blueprint-standards/
│           └── SKILL.md
├── assets/
│   └── logo.svg
├── agents/
│   ├── modern_30bb_architect_agent.md
│   ├── modern_30bb_thesis_agent.md
│   ├── modern_30bb_product_agent.md
│   ├── modern_30bb_gtm_agent.md
│   ├── modern_30bb_governance_agent.md
│   └── modern_30bb_finance_agent.md
├── rules/
│   └── modern-30bb-blueprint-standards.md
└── skills/
    ├── modern-30bb-orchestrator/
    │   ├── SKILL.md
    │   ├── references/
    │   │   └── architecture-map-30-sections.md
    │   ├── resources/
    │   │   └── master-30bb-template.md
    │   └── scripts/
    │       └── validate_30bb_blueprint.py
    ├── modern-30bb-thesis-and-brand/
    │   ├── SKILL.md
    │   └── references/
    │       └── thesis_category_and_naming_playbooks.md
    ├── modern-30bb-product-and-expansion/
    │   ├── SKILL.md
    │   └── references/
    │       └── platform_wedge_and_roi_engineering.md
    ├── modern-30bb-monetization-and-gtm/
    │   ├── SKILL.md
    │   └── references/
    │       └── pricing_packaging_and_enterprise_gtm.md
    ├── modern-30bb-governance-ops-and-legal/
    │   ├── SKILL.md
    │   └── references/
    │       └── corporate_shield_sdlc_and_legal_checklists.md
    └── modern-30bb-economics-roadmap-and-moat/
        ├── SKILL.md
        └── references/
            └── dre_kpis_gates_and_manifesto_guide.md
```
