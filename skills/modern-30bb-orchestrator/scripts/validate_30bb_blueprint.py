#!/usr/bin/env python3
"""
Validador Automatizado para documentos Master Business Blueprint (Padrão Modern 30BB).
Verifica a presença e a ordem cronológica dos 8 Pilares Estratégicos (PT/EN),
das 30 Seções Mestras (I a XXX), das 13 travas estruturais obrigatórias
(Cadeia de Valor, Core Platform, TAM/SAM/SOM em qualquer ordem, Equação de ROI,
6 Componentes de Receita, API Decisioning Metadata, 100% IP / Work-for-Hire,
5 Blocos do Acordo de Acionistas, SDLC Anti-Customização, LGPD/ISO 27001/SOC 2,
DRE Gerencial com COGS/Margem Bruta, 4 Capital Gates + 5 Fases do Roadmap de 18m,
e Flywheel + Manifesto Empresarial) e detecta placeholders não preenchidos.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Callable, List, Tuple

ROMAN_SECTIONS: List[Tuple[str, str]] = [
    ("I", "A TESE CENTRAL / CENTRAL THESIS"),
    ("II", "IDENTIDADE CORPORATIVA / CORPORATE IDENTITY & CATEGORY"),
    ("III", "A GRANDE MUDANÇA DE PERSPECTIVA / PERSPECTIVE SHIFT & MANTRA"),
    ("IV", "A ARQUITETURA DO NEGÓCIO / BUSINESS ARCHITECTURE"),
    ("V", "O BEACHHEAD / BEACHHEAD MARKET & SIZING"),
    ("VI", "PRODUTO 1 / PRODUCT 1 (WEDGE)"),
    ("VII", "PRECAUÇÕES TECNOLÓGICAS / TECHNICAL PRECAUTIONS & RISK MITIGATION"),
    ("VIII", "EXPANSÃO VERTICAL / VERTICAL EXPANSION (LAND & EXPAND)"),
    ("IX", "A EXPANSÃO HORIZONTAL / HORIZONTAL EXPANSION"),
    ("X", "O SEGUNDO DIFERENCIAL ECONÔMICO / COST OPTIMIZATION & ROI"),
    ("XI", "A VISÃO DE LONGO PRAZO / LONG-TERM MARKETPLACE VISION"),
    ("XII", "ARQUITETURA DE RECEITAS / REVENUE & PRICING ARCHITECTURE"),
    ("XIII", "MODALIDADES DE EMPACOTAMENTO / COMMERCIAL PACKAGING"),
    ("XIV", "PRINCÍPIOS DE MARCA / BRAND PRINCIPLES"),
    ("XV", "TERRITÓRIOS DE NAMING / NAMING TERRITORIES & TAGLINES"),
    ("XVI", "TITULARIDADE PATRIMONIAL / IP OWNERSHIP & TECH PARTNERS"),
    ("XVII", "GOVERNANÇA EXECUTIVA / EXECUTIVE GOVERNANCE"),
    ("XVIII", "ACORDO DE ACIONISTAS / SHAREHOLDERS' AGREEMENT"),
    ("XIX", "ESTRUTURA ORGANIZACIONAL / ORGANIZATIONAL STRUCTURE & HQ"),
    ("XX", "FILOSOFIA CULTURAL / CULTURE, HR & COMPENSATION"),
    ("XXI", "GOVERNANÇA DE PRODUTO / PRODUCT & ENGINEERING SDLC"),
    ("XXII", "CIBERSEGURANÇA / CYBERSECURITY & CONTINUITY"),
    ("XXIII", "ARCABOUÇO JURÍDICO / LEGAL & REGULATORY FRAMEWORK"),
    ("XXIV", "ICP INICIAL / INITIAL ICP & ENTERPRISE SALES"),
    ("XXV", "FUNIL DE VENDAS / SALES FUNNEL & DISTRIBUTION WAVES"),
    ("XXVI", "MARKETING DE AUTORIDADE / THOUGHT LEADERSHIP MARKETING"),
    ("XXVII", "CUSTOMER SUCCESS / SCALABLE CUSTOMER SUCCESS"),
    ("XXVIII", "ECONOMIA DA COMPANHIA / MANAGERIAL P&L (DRE) & KPIS"),
    ("XXIX", "FINANCIAMENTO POR GATES / STAGED GATES, 18M ROADMAP & RENUNCIATIONS"),
    ("XXX", "A TESE DE INVESTIMENTO / INVESTMENT THESIS, MOAT & MANIFESTO"),
]

PILLAR_NUMBERS: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]


def _has_all_patterns(content: str, patterns: List[str]) -> bool:
    return all(re.search(p, content, flags=re.IGNORECASE | re.DOTALL) for p in patterns)


REQUIRED_CONCEPTS: List[Tuple[str, Callable[[str], bool]]] = [
    (
        "Cadeia de Valor Central (Seção II)",
        lambda c: _has_all_patterns(
            c,
            [
                r"INSUMO BRUTO|RAW INPUT|DATA",
                r"SINAL|SIGNAL",
                r"CONTEXTO|CONTEXT",
                r"DECISÃO|DECISION",
                r"EVIDÊNCIA|EVIDENCE",
            ],
        ),
    ),
    (
        "Core Platform & Solutions (Seção IV)",
        lambda c: _has_all_patterns(c, [r"CORE PLATFORM", r"SOLUTIONS|SOLUÇÕES"]),
    ),
    (
        "Dimensionamento SOM / SAM / TAM (Seção V)",
        lambda c: _has_all_patterns(c, [r"\bSOM\b", r"\bSAM\b", r"\bTAM\b"]),
    ),
    (
        "Equação ou Calculadora de ROI (Seção X)",
        lambda c: bool(
            re.search(
                r"ROI Anual do Cliente|Calculadora de ROI|Annual Customer ROI|ROI Calculator",
                c,
                flags=re.IGNORECASE,
            )
        ),
    ),
    (
        "Arquitetura dos 6 Componentes de Receita (Seção XII)",
        lambda c: _has_all_patterns(
            c,
            [
                r"Platform Fee|Platform SaaS Fee",
                r"Monitoring\s*/?\s*Entity Fee|Monitoring Fee",
                r"Usage\s*/?\s*Decision Fee|Usage Fee|Decision Fee",
                r"Consumption Margin",
                r"Additional Modules",
                r"Implementation Fee",
            ],
        ),
    ),
    (
        "Empacotamento API Decisioning & Audit Metadata (Seção XIII)",
        lambda c: _has_all_patterns(
            c,
            [
                r"APPROVE\s*\|\s*REVIEW\s*\|\s*BLOCK",
                r"Reason Code",
            ],
        ),
    ),
    (
        "Titularidade 100% IP & Cessão Work-for-Hire (Seção XVI)",
        lambda c: _has_all_patterns(
            c,
            [
                r"100%",
                r"Work-for-Hire|cessão total|cessão patrimonial|hereby assigns",
            ],
        ),
    ),
    (
        "Acordo de Acionistas — 5 Blocos Societários (Seção XVIII)",
        lambda c: _has_all_patterns(
            c,
            [
                r"Reserved Matters|Matérias Reservadas",
                r"Lock-up",
                r"Tag Along",
                r"Drag Along",
                r"Vesting",
                r"Good Leaver",
                r"Bad Leaver",
                r"Non-compete|Não-Competição",
            ],
        ),
    ),
    (
        "Esteira SDLC & Regra Anti-Customização Zero-Forks (Seção XXI)",
        lambda c: bool(
            re.search(r"Anti-Customiza|Zero[- ]Forks|\bforks\b", c, flags=re.IGNORECASE)
        ),
    ),
    (
        "Prontidão LGPD / ISO 27001 / SOC 2 (Seção XXII)",
        lambda c: _has_all_patterns(c, [r"ISO 27001", r"SOC 2"]),
    ),
    (
        "DRE Gerencial — COGS e Margem Bruta (Seção XXVIII)",
        lambda c: _has_all_patterns(
            c, [r"\bCOGS\b", r"Margem Bruta|Gross Margin"]
        ),
    ),
    (
        "4 Capital Gates & Master Roadmap de 18 Meses — Fases 1 a 5 (Seção XXIX)",
        lambda c: _has_all_patterns(
            c,
            [
                r"(?:Capital\s+)?Gate\s+1[\s\S]*?(?:Capital\s+)?Gate\s+4",
                r"(?:FASE|PHASE)\s+1[\s\S]*?(?:FASE|PHASE)\s+5",
            ],
        ),
    ),
    (
        "Tese de Investimento (Flywheel / Switching Cost) & Manifesto (Seção XXX)",
        lambda c: _has_all_patterns(
            c,
            [
                r"Flywheel|Switching Cost|Custo de Troca",
                r"Manifesto Empresarial|Corporate Manifesto|Manifesto da Companhia",
            ],
        ),
    ),
]


def find_placeholders(content: str) -> List[str]:
    """
    Detecta placeholders de template não preenchidos:
    1. Placeholders entre crases: `[...]`
    2. Placeholders em diagramas/blocos de texto: `[MARCA]`, `[Camada 1: ...]`,
       `[Solução 1]`, `[Ex: ...]`, `[TBD]`, `[TODO]`, `[Assinatura da Categoria]`,
       `[Termômetro: ...]`, etc., ignorando links Markdown `[texto](url)`,
       referências `[texto][id]`, notas `[^1]` e checkboxes `[x]`/`[ ]`.
    """
    found: List[str] = []

    # 1. Placeholders entre crases `[...]`
    backtick_matches = re.findall(r"`\[[^\]\n]+\]`", content)
    found.extend(backtick_matches)

    # Remover temporariamente os matches entre crases e links markdown para buscar colchetes residuais de template
    scrubbed = re.sub(r"`\[[^\]\n]+\]`", "", content)
    scrubbed = re.sub(r"!?\[[^\]\n]+\]\([^\)\n]+\)", "", scrubbed)
    scrubbed = re.sub(r"\[[^\]\n]+\]\[[^\]\n]*\]", "", scrubbed)

    # 2. Placeholders típicos de template sem crases (ex: em blocos ```text)
    raw_bracket_pattern = re.compile(
        r"\[(?:"
        r"MARCA|BRAND|PARCEIRO|COMPANHIA|"
        r"Camada\s*\d+[^\]\n]*|Layer\s*\d+[^\]\n]*|"
        r"Solução\s*\d+[^\]\n]*|Solution\s*\d+[^\]\n]*|"
        r"Assinatura[^\]\n]*|Termômetro[^\]\n]*|"
        r"Ex:[^\]\n]*|ex:[^\]\n]*|TBD[^\]\n]*|TODO[^\]\n]*|"
        r"inserir[^\]\n]*|preencher[^\]\n]*"
        r")\]",
        flags=re.IGNORECASE,
    )
    found.extend(raw_bracket_pattern.findall(scrubbed))
    return found


def validate_blueprint(filepath: Path, allow_placeholders: bool = False) -> int:
    if not filepath.exists():
        print(f"[ERRO] Arquivo não encontrado: {filepath}", file=sys.stderr)
        return 2

    content = filepath.read_text(encoding="utf-8")
    errors: List[str] = []
    warnings: List[str] = []

    # 1. Verificar os 8 Pilares Estratégicos (PT: PILAR N / EN: PILLAR N) e ordem
    found_pillars = 0
    pillar_positions: List[Tuple[int, int]] = []
    for num in PILLAR_NUMBERS:
        pattern = rf"^##\s+.*\b(?:PILAR|PILLAR)\s+{num}\b"
        matches = list(re.finditer(pattern, content, flags=re.IGNORECASE | re.MULTILINE))
        if not matches:
            errors.append(
                f"Pilar Estratégico ausente no cabeçalho H2 (`##`): PILAR {num} / PILLAR {num}"
            )
        else:
            found_pillars += 1
            pillar_positions.append((num, matches[0].start()))
            if len(matches) > 1:
                errors.append(
                    f"Pilar Estratégico duplicado no cabeçalho H2 (`##`): PILAR {num} ({len(matches)} ocorrências)"
                )

    for idx in range(1, len(pillar_positions)):
        prev_num, prev_pos = pillar_positions[idx - 1]
        curr_num, curr_pos = pillar_positions[idx]
        if curr_pos < prev_pos:
            errors.append(
                f"Ordem incorreta de Pilares Estratégicos: PILAR {curr_num} aparece antes de PILAR {prev_num}"
            )

    # 2. Verificar as 30 Seções Mestras (I a XXX), unicidade e ordem cronológica
    found_sections = 0
    section_positions: List[Tuple[str, int]] = []
    for roman, expected_topic in ROMAN_SECTIONS:
        pattern = rf"^###\s+{roman}\.\s+"
        matches = list(re.finditer(pattern, content, flags=re.MULTILINE))
        if not matches:
            errors.append(
                f"Seção Mestra ausente (`### {roman}.`): esperado tópico '{expected_topic}'"
            )
        else:
            found_sections += 1
            section_positions.append((roman, matches[0].start()))
            if len(matches) > 1:
                errors.append(
                    f"Seção Mestra duplicada (`### {roman}.`): {len(matches)} ocorrências encontradas"
                )

    for idx in range(1, len(section_positions)):
        prev_roman, prev_pos = section_positions[idx - 1]
        curr_roman, curr_pos = section_positions[idx]
        if curr_pos < prev_pos:
            errors.append(
                f"Ordem incorreta de Seções Mestras: `### {curr_roman}.` aparece antes de `### {prev_roman}.`"
            )

    # 3. Verificar as 13 travas e estruturas obrigatórias do 30BB
    found_concepts = 0
    for label, check_fn in REQUIRED_CONCEPTS:
        if check_fn(content):
            found_concepts += 1
        else:
            errors.append(f"Elemento estrutural obrigatório ausente: {label}")

    # 4. Verificar placeholders não preenchidos
    placeholder_matches = find_placeholders(content)
    if placeholder_matches:
        sample = ", ".join(placeholder_matches[:5])
        msg = (
            f"Detectados {len(placeholder_matches)} placeholders de template não preenchidos "
            f"(ex: {sample}). Substitua-os pelos dados concretos do negócio ou use --allow-placeholders se for um template."
        )
        if allow_placeholders:
            warnings.append(msg)
        else:
            errors.append(msg)

    print("=" * 72)
    print(f"RELATÓRIO DE VALIDAÇÃO MODERN 30BB: {filepath.name}")
    print("=" * 72)
    print(f"• Pilares Estratégicos verificados : {found_pillars}/{len(PILLAR_NUMBERS)}")
    print(
        f"• Seções Mestras verificadas       : {found_sections}/{len(ROMAN_SECTIONS)} (I a XXX)"
    )
    print(
        f"• Travas Estruturais verificadas   : {found_concepts}/{len(REQUIRED_CONCEPTS)}"
    )
    print(f"• Placeholders detectados          : {len(placeholder_matches)}")
    print("-" * 72)

    if warnings:
        for w in warnings:
            print(f"[INFO] {w}")

    if errors:
        for e in errors:
            print(f"[FALHA] {e}")
        print("-" * 72)
        print(
            f"RESULTADO: REPROVADO ({len(errors)} erro(s) encontrado(s))."
        )
        return 1

    if allow_placeholders and placeholder_matches:
        print(
            "RESULTADO: TEMPLATE 30/30 VÁLIDO (estrutura 100% completa com placeholders permitidos)."
        )
        return 0

    print("RESULTADO: APROVADO COM EXCELÊNCIA (100% aderente ao padrão Modern 30BB).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida se um documento Markdown cumpre as 30 Seções Mestras e 8 Pilares do Modern 30BB."
    )
    parser.add_argument(
        "file", type=Path, help="Caminho para o arquivo Markdown do Blueprint"
    )
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Permite placeholders de template (útil ao validar templates em branco)",
    )
    args = parser.parse_args()
    return validate_blueprint(args.file, allow_placeholders=args.allow_placeholders)


if __name__ == "__main__":
    sys.exit(main())
