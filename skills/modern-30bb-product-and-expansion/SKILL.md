---
name: modern-30bb-product-and-expansion
description: >-
  Use this skill when designing or refining Pillar 2 (Sections IV to XI) of a Modern 30BB Business Blueprint:
  Horizontal Core Platform Architecture (6 layers), Beachhead Market Selection & TAM/SAM/SOM Sizing,
  Product 1 (Wedge Product), Technical Ecosystem Limits & Operational Risk Mitigation, Vertical Land & Expand (Modules 2-6),
  Horizontal Expansion across New Industries, Cascading Cost Optimization Engine & Customer ROI Equation, and Long-Term Marketplace Vision.
---

# Modern 30BB: Arquitetura de Produto, Entrada, Expansão e ROI (Pilar 2)

Esta skill orienta o desenho completo do **Pilar 2 (Seções IV a XI)** do Plano Mestre da Nova Companhia. Ela resolve a tensão clássica entre construir um ativo tecnológico horizontal escalável e entrar no mercado com foco cirúrgico em uma única dor aguda.

---

## Princípios Inegociáveis das Seções IV a XI

1. **Uma Plataforma Horizontal, Vários Produtos Configuráveis (Seção IV)**:
   - Estruture a arquitetura em 3 camadas hierárquicas:
     - `CORPORATE BRAND` (Marca e Assinatura da Categoria)
     - `CORE PLATFORM` (O Motor Tecnológico Único dividido em 6 camadas: *1. Ingestão/Orquestração, 2. Monitoramento Contínuo/Sinais, 3. Motor de Regras/Políticas/Decisão, 4. Automação de Workflows/Ações, 5. Trilha de Auditoria e Evidência Imutável, 6. APIs/Webhooks/Conectores*)
     - `SOLUTIONS` (Soluções 1 a 6 configuradas por vertical/caso de uso sem reescrever o Core).

2. **Beachhead Racional e Dimensionamento TAM/SAM/SOM (Seção V)**:
   - Justifique a escolha do setor inicial pelas **4 Características Raras**:
     1. *Obrigatoriedade / Urgência*;
     2. *Volume Massivo*;
     3. *Alto Custo do Erro*;
     4. *Capacidade Econômica*.
   - Calcule de forma *bottom-up* o **SOM** (contas-alvo de 18–24 meses × ACV), o **SAM** (total de empresas da vertical inicial × ACV) e o **TAM** (mercado total somando as novas verticais horizontais).

3. **Produto 1 — A Cunha Comercial / Wedge Product (Seção VI)**:
   - Especifique o nome do Produto 1, o caso de uso cirúrgico no *Beachhead* e o fluxo operacional em 5 estágios:
     `[ALTERAÇÃO/EVENTO DETECTADO] → [MOTOR DE REGRAS] → [DECISÃO AUTOMÁTICA] → [AÇÃO/WORKFLOW] → [TRILHA DE EVIDÊNCIA]`.

4. **Realismo Técnico e Matriz de Mitigação de Riscos (Seção VII)**:
   - Alinhe a promessa comercial à latência real das fontes externas (prometendo *Monitoramento Contínuo + Decisão Orientada a Eventos* em vez de promessas irreais sobre sistemas governamentais/terceiros).
   - Mapeie a mitigação dos 3 riscos operacionais críticos: (1) *Indisponibilidade/lentidão de fornecedor externo* (multi-provedor + *fallback* + filas assíncronas), (2) *Inconsistência de dados* (higienização + *cross-check*), e (3) *Fricção de integração no cliente* (APIs, Webhooks e ingestão simplificada por lote/SFTP/API).

5. **Expansão Vertical (Seção VIII) e Expansão Horizontal (Seção IX)**:
   - **Seção VIII (Land and Expand)**: Liste os **Módulos Verticais 2 a 6** que serão vendidos para a mesma base já integrada (elevando ARPU e NRR sem novo CAC).
   - **Seção IX (Expansão Horizontal)**: Construa a tabela com no mínimo **5 novas verticais** demonstrando o nome da solução configurada, a entidade monitorada e a passagem de *Fotografia Estática → Processo Contínuo*.

6. **Motor de Otimização de Custos e Calculadora de ROI (Seção X)**:
   - Demonstre a orquestração inteligente em cascata (consulta fonte `A` mais barata → aciona `B` só se condição `X` → aciona `C` só se risco exigir → usa `D` como *fallback*).
   - Apresente a **Equação do Business Case Comercial**:
     $$\text{ROI Anual do Cliente} = \frac{(\text{Economia de Insumos} + \text{Horas Manuais Poupadas} + \text{Perdas/Multas Evitadas}) - \text{Custo Anual da Plataforma}}{\text{Custo Anual da Plataforma}}$$
   - Explicite os **6 Pilares de Valor para o Comprador** (*risco regulatório, perdas/fraudes, trabalho manual, conta de insumos, velocidade de decisão, auditabilidade total*).

7. **Visão de Longo Prazo: Do Produto ao Marketplace / Hub (Seção XI)**:
   - Descreva a evolução em que o cliente integra apenas a API da companhia em vez de gerir 10 contratos separados, transformando a plataforma em um *Data & Decision Marketplace* com poder de barganha e margem transacional, encerrando com a **North Star**.

---

## Guia de Referência Detalhado

- **Engenharia de Plataforma, Dimensionamento e Calculadora de ROI**: [references/platform_wedge_and_roi_engineering.md](./references/platform_wedge_and_roi_engineering.md)
