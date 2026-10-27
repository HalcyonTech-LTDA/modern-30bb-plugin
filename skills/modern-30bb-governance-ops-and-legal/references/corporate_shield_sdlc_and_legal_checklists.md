# Checklists de Blindagem Societária, Acordo de Acionistas, SDLC e Contratos (Seções XVI a XXIII)

Este documento fornece as matrizes de verificação para redigir e auditar os Pilares 5 e 6 do **Modern 30BB Business Blueprint**.

---

## 1. Matriz de Due Diligence de Propriedade Intelectual e Parceiros Técnicos (Seção XVI)

Em rodadas institucionais (Seed / Series A) ou processos de M&A, qualquer ambiguidade sobre quem detém o código-fonte ou sobre a dependência de uma *software house* ligada a um fundador pode inviabilizar o negócio (*deal breaker*). Verifique sempre:

| Ativo Crítico | Titularidade Obrigatória | Trava Contratual e Operacional |
| :--- | :--- | :--- |
| **Código-Fonte, Motor de Regras e Algoritmos** | 100% Companhia Operacional | Cláusula de cessão patrimonial presente e irrevogável (*Work-for-Hire* / Lei 9.609/98) + renúncia a direitos morais oponíveis. |
| **Organização Git (GitHub/GitLab) e CI/CD** | 100% Companhia Operacional | Repositórios criados dentro da conta corporativa da companhia desde o Commit 0; revogação imediata de acessos ao fim de contratos. |
| **Contas de Cloud (AWS/GCP/Azure) e KMS** | 100% Companhia Operacional | Faturamento, chaves criptográficas e *root accounts* sob custódia exclusiva da companhia. |
| **Marcas (INPI/USPTO) e Domínios DNS** | 100% Companhia Operacional | Registro protocolado em nome do CNPJ da companhia operacional (nunca em CPF de sócio ou CNPJ de parceiro). |
| **Parceiro Técnico / Software House de Sócio** | Prestador Contratado sem Direito sobre IP | Regra `[PARCEIRO] desenvolve; [COMPANHIA] possui` + SLA + Cláusula de Transição Assistida (*Handover* sem interrupção). |

---

## 2. Term Sheet do Acordo de Acionistas — Os 5 Blocos do Mês 0 (Seção XVIII)

1. **Bloco 1 — Matérias Reservadas (*Reserved Matters*)**:
   - Quórum qualificado (ex: 75% a 85% do capital votante) para: alteração do objeto social, emissão de novas quotas/títulos conversíveis, endividamento acima da alçada do CEO, alienação/oneração de IP, distribuição extraordinária de dividendos e contratação com partes relacionadas.
2. **Bloco 2 — Capital, Aportes e Diluição**:
   - Cronograma de integralização vinculado aos *Capital Gates* e mecanismo claro de diluição para o acionista inadimplente (*Defaulting Shareholder*).
3. **Bloco 3 — Liquidez e Transferência**:
   - *Lock-up* de 36 a 48 meses para fundadores executivos; *Right of First Refusal (ROFR)* em favor dos demais sócios; *Tag Along* de 100% em caso de alienação de controle; *Drag Along* mediante aprovação da maioria qualificada.
4. **Bloco 4 — Vesting e Regras de Saída (*Good vs. Bad Leaver*)**:
   - *Reverse Vesting* de 36 a 48 meses com *Cliff* de 12 meses.
   - **Good Leaver** (morte, invalidez permanente, dispensa sem justa causa): recompra das quotas *vested* pelo valor justo/patrimonial parcelado em 24 a 36 meses para preservar o *runway*.
   - **Bad Leaver** (abandono de funções, fraude, falta grave, violação de não-competição ou de confidencialidade): recompra forçada da totalidade das quotas por valor nominal/simbólico (R$ 1,00).
5. **Bloco 5 — Conflito de Interesses e Impasses**:
   - *Non-compete* e *Non-solicitation* durante o vínculo e por 24 meses após a saída;
   - **Abstenção Obrigatória em Partes Relacionadas**: O sócio que possua participação em empresa fornecedora/parceira fica impedido de votar na aprovação, renovação, aplicação de multa ou rescisão daquele contrato.

---

## 3. Regra Anti-Customização e Proteção de Margem Bruta (Seção XXI)

Sempre que um grande cliente Enterprise solicitar uma funcionalidade durante a fase de negociação ou implantação, aplique o **Filtro de Plataforma Horizontal**:
- **Pergunta 1**: *Essa capacidade pode ser abstraída como um parâmetro declarativo, regra de política ou módulo ativável para outros clientes?*
  - **Sim** → Entra no *roadmap* do Core Platform como módulo configurável.
  - **Não (é um fluxo idiossincrático exclusivo daquele cliente)** → Deve ser resolvido via Webhook/API na ponta do cliente, jamais criando uma *branch* ou *fork* customizado do produto.
