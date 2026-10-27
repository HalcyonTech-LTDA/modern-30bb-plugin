---
name: modern-30bb-orchestrator
description: >-
  Use this skill when the user asks to create, generate, structure, expand, or audit a complete
  Master Business Blueprint ("Plano Mestre da Nova Companhia") from a new business idea, startup pitch,
  or strategic thesis using the 30 Master Sections (I to XXX) across 8 Strategic Pillars (framework 30BB).
---

# Modern 30BB Orchestrator: Master Business Blueprint Workflow

Esta skill orquestra a criação ponta a ponta, revisão e auditoria de um **Plano Mestre da Nova Companhia (Master Business Blueprint)** baseado na arquitetura de **30 Seções Mestras (I a XXX)** distribuídas em **8 Pilares Estratégicos**.

O objetivo do documento gerado nunca é ser um resumo superficial de ideias, mas sim consolidar a lógica completa e integrada do negócio: por que a empresa deve existir, qual problema estrutural resolve, qual produto vende primeiro (*Wedge*), qual ativo horizontal constrói (*Core Platform*), como ganha dinheiro em múltiplas camadas, como se diferencia, como blinda seu IP e governança, como se organiza, como entra no mercado, como escala e que empresa investível se torna ao final de 18 meses.

---

## Arquitetura dos 8 Pilares e 30 Seções Mestras

```text
┌───────────────────────────────────────────────────────────────────────────────┐
│                   PLANO MESTRE DA NOVA COMPANHIA (30BB)                       │
├───────────────────────────────────────────────────────────────────────────────┤
│ PILAR 1: Fundamentos da Tese e Proposta de Valor             (Seções I a III) │
│ PILAR 2: Arquitetura de Produto, Entrada e Expansão          (Seções IV a XI) │
│ PILAR 3: Modelo de Monetização e Empacotamento Comercial   (Seções XII e XIII)│
│ PILAR 4: Marca, Naming e Comunicação Executiva              (Seções XIV e XV) │
│ PILAR 5: Blindagem Societária, IP e Governança            (Seções XVI a XVIII)│
│ PILAR 6: Organização, Cultura, Operações e Conformidade   (Seções XIX a XXIII)│
│ PILAR 7: Go-To-Market (GTM), Vendas e Customer Success   (Seções XXIV a XXVII)│
│ PILAR 8: Economia, Finanças, Execução e Tese de Invest.  (Seções XXVIII a XXX)│
└───────────────────────────────────────────────────────────────────────────────┘
```

---

## Procedimento de Execução Multi-Agentes (Staged Handoff Pipeline)

Para evitar dependências circulares e assegurar que nenhum agente opere sem o contexto consolidado das etapas anteriores, a geração completa do Blueprint adota obrigatoriamente o **Pipeline em Fases de Entrega de Bastão (Staged Handoff)**:

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   FLUXO MULTI-AGENTES DE ENTREGA DE BASTÃO                       │
├──────────────────────────────────────────────────────────────────────────────────┤
│ Fase 0: Orquestrador Líder (Extrai os 7 Vetores Fundacionais)                     │
│                            ↓                                                     │
│ Fase 1: Subagente Tese & Marca (Pilares 1 e 4: Seções I-III e XIV-XV)             │
│         [Insumo gerado: Problema, Antiposicionamento, Categoria, Mantra e Naming]│
│                            ↓                                                     │
│ Fase 2: Subagente Produto & Monetização (Pilares 2 e 3: Seções IV-XIII)           │
│         [Insumo gerado: Core Platform, Beachhead, Wedge, Custos e Pricing 6L]    │
│                            ↓                                                     │
│ Fase 3 (Execução Paralela Segura):                                               │
│         ├─ Subagente GTM & Vendas (Pilar 7: XXIV-XXVII)                          │
│         └─ Subagente Governança & Operações (Pilares 5 e 6: XVI-XXIII)           │
│         [Insumos gerados: 50 Contas, Funil 14E, CS, 100% IP, SHA M0 e SDLC]      │
│                            ↓                                                     │
│ Fase 4: Subagente Finanças & Moat (Pilar 8: XXVIII-XXX)                          │
│         [Insumo gerado: DRE Gerencial Software/Repasse, KPIs, 4 Gates e Moat]    │
│                            ↓                                                     │
│ Fase 5: Orquestrador Líder (Compilação, Auditoria Python e Homologação)          │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Passo 0: Dissecação da Ideia de Negócio (Intake pelo Orquestrador)
O Orquestrador Líder analisa a ideia do usuário e extrai a **Ficha de Parâmetros Globais (7 Vetores Fundacionais)**:
1. **Setor Inicial (*Beachhead*)**: Onde a dor é mais urgente, regulada e volumosa?
2. **Paradoxo do Mercado**: O que os clientes já contratam que continua falhando na última milha?
3. **Objeto Econômico Real**: O que a empresa realmente decide/orquestra além do insumo bruto?
4. **Core Platform (Motor Horizontal)**: As 6 camadas técnicas reutilizáveis.
5. **Produto 1 (*Wedge Product*)**: A cunha comercial cirúrgica que abre a porta no Dia 1.
6. **Comprador Econômico e Multiplicadores**: Agregadores de volume e decisores.
7. **North Star**: A infraestrutura padrão em 5 a 10 anos.

---

### Passo 1: Disparo da Fase 1 — Tese, Categoria e Naming
Invoque o subagente especializado (`modern-30bb-thesis-agent` ou subagente `self` com a skill `modern-30bb-thesis-and-brand`):
- **Missão:** Redigir as **Seções I a III (Pilar 1)** e as **Seções XIV a XV (Pilar 4)**.
- **Insumo Passado no Prompt:** A Ficha de Parâmetros Globais do Passo 0.
- **Entrega Esperada:** O Paradoxo de Mercado, a Matriz do Status Quo, o Antiposicionamento, a Cadeia de Valor `[INSUMO BRUTO] → [SINAL] → [CONTEXTO] → [DECISÃO] → [AÇÃO] → [EVIDÊNCIA]`, a Nova Categoria, o Mantra Corporativo e o Naming Institucional validado (com restrição semântica proibindo termos do nicho inicial).

---

### Passo 2: Disparo da Fase 2 — Arquitetura de Produto e Monetização
Invoque o subagente especializado (`modern-30bb-product-agent` ou subagente `self` com as skills `modern-30bb-product-and-expansion` e `modern-30bb-monetization-and-gtm`):
- **Missão:** Redigir as **Seções IV a XI (Pilar 2)** e as **Seções XII e XIII (Pilar 3)**.
- **Insumo Passado no Prompt:** A Ficha de Parâmetros Globais + As Seções I a III e XIV a XV redigidas na Fase 1.
- **Entrega Esperada:** Desacoplamento técnico em 3 níveis (`Marca → Core Platform 6 camadas → Soluções`), Beachhead quantificado (SOM, SAM, TAM), Produto 1 Wedge, Precauções técnicas, Land & Expand vertical, Expansão horizontal, Calculadora de ROI do CFO com 6 pilares de valor, Tabela de Precificação em 6 Linhas e Empacotamento MaaS vs DaaS.

---

### Passo 3: Disparo da Fase 3 em Paralelo Seguro — GTM & Governança/Operações
Com o Produto e a Precificação formalmente congelados, dispare simultaneamente dois subagentes:

1. **Subagente GTM & Vendas (`modern-30bb-gtm-agent`):**
   - **Missão:** Redigir as **Seções XXIV a XXVII (Pilar 7)**.
   - **Insumo:** O pacote de Produto e Precificação da Fase 2.
   - **Entrega:** ICP Enterprise priorizando Agregadores, Comitê de Compra mapeado, 50 Target Accounts nominais/categorizadas, Esteira de CRM em 14 etapas, 3 Ondas de Canais, Marketing de Autoridade e CS com Lei Fundamental de Escalabilidade Operacional.

2. **Subagente Governança & Operações (`modern-30bb-governance-agent`):**
   - **Missão:** Redigir as **Seções XVI a XVIII (Pilar 5)** e as **Seções XIX a XXIII (Pilar 6)**.
   - **Insumo:** A estrutura da Core Platform e custos operacionais da Fase 2.
   - **Entrega:** Blindagem patrimonial de 100% de IP (`[PARCEIRO] desenvolve; [COMPANHIA] possui`), Rito mensal executivo de 10 blocos sem conselho ornamental, Acordo de Acionistas no Mês 0 (5 blocos), Organograma enxuto e sede híbrida, SDLC formal de 10 etapas com Regra Anti-Customização (Zero Forks), Cibersegurança e Checklist Jurídico.

---

### Passo 4: Disparo da Fase 4 — Economia, Finanças, Execução e Moat
Invoque o subagente financeiro (`modern-30bb-finance-agent` ou subagente `self` com a skill `modern-30bb-economics-roadmap-and-moat`):
- **Missão:** Redigir as **Seções XXVIII a XXX (Pilar 8)**.
- **Insumo Passado no Prompt:** A totalidade dos dados consolidados das Fases 1, 2 e 3 (tabelas de preços, custos de APIs/terceiros, volume de vendas, headcount técnico/comercial e cronograma).
- **Entrega Esperada:** DRE Gerencial segregando Software de Repasse de Terceiros (com Margem Bruta como termômetro de identidade), Painel de KPIs em 6 dimensões, Financiamento por 4 Gates de Redução de Risco (12–18m runway), Master Roadmap Integrado de 18 Meses em 5 Fases M0–M18, Renúncias Estratégicas ("O Que NÃO Faremos"), Flywheel da Tese de Investimento, Moat de 8 fatores e Manifesto Empresarial.

---

### Passo 5: Compilação, Auditoria Automatizada e Homologação
O Orquestrador Líder reúne as seções geradas, monta o documento Markdown consolidado no disco e executa o validador oficial:

```bash
python3 ~/.gemini/config/plugins/modern-30bb-plugin/skills/modern-30bb-orchestrator/scripts/validate_30bb_blueprint.py <caminho/para/blueprint.md>
```

> [!IMPORTANT]
> O Orquestrador só encerra a tarefa após o script validador retornar código de saída 0 (sucesso total). Se houver qualquer pendência, o Orquestrador solicita a retificação cirúrgica ao subagente responsável antes de finalizar a resposta ao usuário.

---

## Recursos, Referências e Scripts da Skill

- **Template Mestre Oficial (30 Seções / 8 Pilares)**: [resources/master-30bb-template.md](./resources/master-30bb-template.md)
- **Mapa de Arquitetura e Consolidação (46 Tópicos → 30 Seções Mestras)**: [references/architecture-map-30-sections.md](./references/architecture-map-30-sections.md)
- **Validador Automatizado CLI**: [scripts/validate_30bb_blueprint.py](./scripts/validate_30bb_blueprint.py)
