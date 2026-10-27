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

## Procedimento Passo a Passo de Execução

### Passo 1: Dissecação da Ideia de Negócio (Intake & Diagnóstico)
Ao receber uma ideia de negócio (mesmo que em poucas frases, áudio transcrito, e-mail ou rascunho):
1. Extraia os **7 Vetores Fundacionais**:
   - **Setor Inicial (*Beachhead*)**: Onde a dor é mais urgente, regulada, volumosa e com orçamento disponível?
   - **Paradoxo do Mercado**: O que os clientes já contratam hoje que continua falhando na "última milha"?
   - **Objeto Econômico Real**: O que a empresa realmente monitora, decide ou orquestra (além do insumo aparente)?
   - **Core Platform (Motor Horizontal)**: Quais são as 6 camadas técnicas reutilizáveis?
   - **Produto 1 (*Wedge Product*)**: Qual problema cirúrgico abre a porta do cliente no Dia 1?
   - **Comprador Econômico e Multiplicadores**: Quem são os agregadores de volume e os decisores (CEO/CFO/CRO/CTO)?
   - **North Star**: Qual infraestrutura padrão de mercado a empresa se torna em 5 a 10 anos?
2. Consulte o template mestre preenchível em [master-30bb-template.md](./resources/master-30bb-template.md) e o mapa de consolidação em [architecture-map-30-sections.md](./references/architecture-map-30-sections.md).

### Passo 2: Síntese Modular pelos 8 Pilares Estratégicos
Construa o documento respeitando rigorosamente a numeração romana (`### I.` até `### XXX.`) e acionando as skills especializadas de cada domínio:

1. **Pilares 1 e 4 (`modern-30bb-thesis-and-brand`)**:
   - Redija as **Seções I, II e III** (Paradoxo, Matriz do Status Quo, Ciclo de 6 etapas, Antiposicionamento, Categoria, Cadeia de Valor `INSUMO BRUTO → SINAL → CONTEXTO → DECISÃO → AÇÃO → EVIDÊNCIA`, Verdadeiro Objeto Econômico e Mantra).
   - Redija as **Seções XIV e XV** (Públicos da marca, Restrição semântica proibindo termos do nicho inicial no nome corporativo, Territórios de Naming avaliados + 1 descartado por conflito + validação INPI/USPTO, Elevator Pitch e Taglines).
2. **Pilar 2 (`modern-30bb-product-and-expansion`)**:
   - Redija as **Seções IV a XI** (Diagrama em 3 níveis `CORPORATE BRAND → CORE PLATFORM → SOLUTIONS`, Beachhead com os 4 critérios raros e cálculo de SOM/SAM/TAM, Produto 1 e dinâmica operacional, Precauções tecnológicas e Matriz de 3 riscos operacionais, Land & Expand com Módulos 2 a 6, Tabela de Expansão Horizontal com 5+ novas verticais, Motor de Otimização de Custos em cascata + Equação de ROI Anual + 6 Pilares de Valor, e Visão de Longo Prazo / Marketplace).
3. **Pilares 3 e 7 (`modern-30bb-monetization-and-gtm`)**:
   - Redija as **Seções XII e XIII** (Tabela de 6 componentes de receita — *Platform Fee, Monitoring/Entity Fee, Usage/Decision Fee, Consumption Margin, Additional Modules, Implementation Fee* — e as 2 modalidades de empacotamento comercial: *Monitoramento Contínuo* e *Motor Transacional via API*).
   - Redija as **Seções XXIV a XXVII** (Prioridade de ICP começando por Agregadores + Segunda Onda, *Founder-Led Sales*, 50 *Target Accounts*, Comitê de Compra, Esteira de 14 etapas no CRM, 3 Ondas de Canais, Marketing de Autoridade `CREDIBILITY → EDUCATION → DEMAND` e CS Escalável com a Lei Fundamental de Escalabilidade Operacional).
4. **Pilares 5 e 6 (`modern-30bb-governance-ops-and-legal`)**:
   - Redija as **Seções XVI a XVIII** (Propriedade Integral 100% IP, Governança sobre Parceiros de Desenvolvimento `[PARCEIRO] desenvolve; [COMPANHIA] possui`, Linha de Comando sem Conselho Ornamental, Rito Mensal de 10 blocos encerrando em `Decisão → Responsável Nominal → Prazo Fatal`, e Acordo de Acionistas assinado no Mês 0 cobrindo os 5 blocos societários).
   - Redija as **Seções XIX a XXIII** (Organograma enxuto com Produto 100% interno, Política de sede híbrida, Cultura empresarial de alta performance + Remuneração Fixo/Variável/SOP seletivo, Esteira formal de SDLC de 10 etapas + Regra Anti-Customização Zero-Forks, Cibersegurança com prontidão LGPD/ISO 27001/SOC 2 Tipo II, e Checklist de Blindagem Jurídica).
5. **Pilar 8 (`modern-30bb-economics-roadmap-and-moat`)**:
   - Redija as **Seções XXVIII a XXX** (DRE Gerencial segregando Receita Bruta, COGS e Margem Bruta como termômetro Software vs. Revenda, Painel Mensal de KPIs em 6 dimensões, Financiamento em 4 Gates de Redução de Risco com 12–18m de Runway, Master Roadmap Integrado de 18 Meses em 5 Fases M0–M18, Renúncias Estratégicas Inegociáveis, Fotografia de 18 Meses, Flywheel de 7 efeitos da Tese de Investimento, Moat de 8 fatores e Manifesto Empresarial).

### Passo 3: Verificação e Auditoria Automatizada
Sempre que gerar ou atualizar um arquivo de Blueprint em disco, execute o script validador oficial da skill para garantir que nenhuma das 30 seções, 8 pilares, tabelas ou fórmulas obrigatórias foi omitida ou deixada com placeholders (`[...]`):

```bash
python3 ~/.gemini/config/plugins/modern-30bb-plugin/skills/modern-30bb-orchestrator/scripts/validate_30bb_blueprint.py <caminho/para/blueprint.md>
```

> [!TIP]
> Se o objetivo for gerar um **Template em Branco Preenchível**, passe a flag `--allow-placeholders` para o script validador:
> `python3 ~/.gemini/config/plugins/modern-30bb-plugin/skills/modern-30bb-orchestrator/scripts/validate_30bb_blueprint.py <caminho/para/template.md> --allow-placeholders`

---

## Recursos, Referências e Scripts da Skill

- **Template Mestre Oficial (30 Seções / 8 Pilares)**: [resources/master-30bb-template.md](./resources/master-30bb-template.md)
- **Mapa de Arquitetura e Consolidação (46 Tópicos → 30 Seções Mestras)**: [references/architecture-map-30-sections.md](./references/architecture-map-30-sections.md)
- **Validador Automatizado CLI**: [scripts/validate_30bb_blueprint.py](./scripts/validate_30bb_blueprint.py)
