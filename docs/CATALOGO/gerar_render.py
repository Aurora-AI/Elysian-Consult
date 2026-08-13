#!/usr/bin/env python3
"""
Gerador de render/ a partir do registro.

P2 do ESQUEMA_PECA: o registro é dado; o documento é renderização.
Nada em render/ é escrito à mão.

Uso:  python gerar_render.py
"""
from __future__ import annotations
import os, glob, sys, re
from collections import defaultdict, Counter

try:
    import yaml
except ImportError:
    sys.exit("pyyaml não instalado:  pip install pyyaml")

BASE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(BASE, "registro")
OUT = os.path.join(BASE, "render")

# Taxonomia de NATUREZA DO TRABALHO — o que fecha a lacuna, não onde ela dói.
# É o eixo que informa esforço; a severidade informa urgência.
NATUREZA = {
    "FONTE_AUSENTE": {
        "titulo": "Fórmula que não existe em fonte nenhuma",
        "fecha_com": "escrever a fórmula — trabalho de método, não de catalogação",
        "ids": ["LAC-FOR-019", "LAC-FOR-049", "LAC-FOR-061", "LAC-FOR-025",
                "LAC-FOR-059", "LAC-FOR-077", "LAC-FOR-028"],
    },
    "DOC_X_CODIGO": {
        "titulo": "Documento e código implementado divergem",
        "fecha_com": "comparar as duas versões e ratificar uma — decisão pontual",
        "ids": ["LAC-FOR-052", "LAC-FOR-060", "LAC-FOR-074", "LAC-FOR-002",
                "LAC-FOR-039"],
    },
    "DOC_X_DOC": {
        "titulo": "Dois documentos afirmam coisas diferentes",
        "fecha_com": "escolher qual vale — decisão pontual, evidência já anexada",
        "ids": ["LAC-FOR-001", "LAC-FOR-017", "LAC-FOR-053", "LAC-FOR-062",
                "LAC-FOR-055", "LAC-FOR-064", "LAC-FOR-066"],
    },
    "ERRO_MATEMATICO": {
        "titulo": "A fórmula produz número errado como está escrita",
        "fecha_com": "corrigir a expressão — a correção candidata já está registrada",
        "ids": ["LAC-FOR-003", "LAC-FOR-006", "LAC-FOR-013", "LAC-FOR-015",
                "LAC-FOR-008", "LAC-FOR-041", "LAC-FOR-047", "LAC-FOR-069",
                "LAC-FOR-035"],
    },
    "CASO_DEGENERADO": {
        "titulo": "Comportamento indefinido em borda previsível",
        "fecha_com": "UMA política única fecha quase todas de uma vez",
        "ids": ["LAC-FOR-010", "LAC-FOR-032", "LAC-FOR-027", "LAC-FOR-043",
                "LAC-FOR-011", "LAC-FOR-012", "LAC-FOR-034", "LAC-FOR-033",
                "LAC-FOR-018", "LAC-FOR-022", "LAC-FOR-029", "LAC-FOR-036",
                "LAC-FOR-038", "LAC-FOR-068", "LAC-FOR-070", "LAC-FOR-030",
                "LAC-FOR-007", "LAC-FOR-075", "LAC-FOR-021"],
    },
    "CONTRA_GABARITO": {
        "titulo": "O Gabarito exige um comportamento que a fórmula não tem",
        "fecha_com": "a régua de veracidade já diz a resposta — é implementar",
        "ids": ["LAC-FOR-057", "LAC-FOR-067", "LAC-FOR-042", "LAC-FOR-065",
                "LAC-FOR-046", "LAC-FOR-024"],
    },
    "CONTRA_DOUTRINA": {
        "titulo": "Contradiz um princípio declarado da casa",
        "fecha_com": "decisão de método — mexe no que diferencia a Aurora",
        "ids": ["LAC-FOR-014", "LAC-FOR-023", "LAC-FOR-026"],
    },
    "NOMENCLATURA": {
        "titulo": "Higiene de símbolo e fronteira",
        "fecha_com": "renomear e declarar — meia hora, fecha reprovas do validador",
        "ids": ["LAC-FOR-004", "LAC-FOR-005", "LAC-FOR-050", "LAC-FOR-031",
                "LAC-FOR-044", "LAC-FOR-016", "LAC-FOR-051", "LAC-FOR-071",
                "LAC-FOR-072", "LAC-FOR-073", "LAC-FOR-076", "LAC-FOR-058",
                "LAC-FOR-056", "LAC-FOR-009"],
    },
    "MODELO_DE_DADOS": {
        "titulo": "A fórmula pede um dado que não existe no modelo",
        "fecha_com": "definir a captura — depende do PDV do cliente, não de nós",
        "ids": ["LAC-FOR-063", "LAC-FOR-048", "LAC-FOR-045", "LAC-FOR-020",
                "LAC-FOR-037", "LAC-FOR-040"],
    },
    "CONTRATUAL": {
        "titulo": "Pendência de estrutura comercial, não de fórmula",
        "fecha_com": "decisão de negócio",
        "ids": ["LAC-FIN-079", "LAC-CNC-080"],
    },
}
ORDEM_SEV = {"CRITICA": 0, "ALTA": 1, "MEDIA": 2, "BAIXA": 3}
MARCA = {"CRITICA": "🔴", "ALTA": "🟠", "MEDIA": "🟡", "BAIXA": "⚪"}


def carregar():
    lac, outras = [], []
    for f in sorted(glob.glob(os.path.join(REG, "*.yaml"))):
        d = yaml.safe_load(open(f, encoding="utf-8")) or {}
        for p in d.get("pecas", []) or []:
            (lac if p.get("tipo") == "LAC" else outras).append(p)
    return lac, outras


def render_lacunas(lac, fase="1-CONSULTORIA"):
    abertas = [p for p in lac
               if p.get("fase", "1-CONSULTORIA") == fase and p.get("status") == "ABERTA"]
    abertas.sort(key=lambda p: (ORDEM_SEV[p["severidade"]], p["id"]))

    idx = {}
    for nat, meta in NATUREZA.items():
        for i in meta["ids"]:
            idx[i] = nat
    porNat = defaultdict(list)
    for p in abertas:
        porNat[idx.get(p["id"], "NAO_CLASSIFICADA")].append(p)

    sev = Counter(p["severidade"] for p in abertas)
    L = []
    L.append("# LACUNAS ABERTAS — Frente 1 · CONSULTORIA\n")
    L.append("> ⚙️ **Arquivo gerado** por `gerar_render.py` a partir de `registro/*.yaml`.")
    L.append("> Não editar à mão (`ESQUEMA_PECA.md` P2). Para mudar algo, mude a peça e regenere.\n")
    L.append(f"**{len(abertas)} lacunas abertas** · "
             + " · ".join(f"{MARCA[s]} {sev[s]} {s.lower()}" for s in
                          ["CRITICA", "ALTA", "MEDIA", "BAIXA"] if sev[s]) + "\n")
    L.append("---\n")

    L.append("## Por natureza do trabalho\n")
    L.append("A severidade diz o quanto dói. A **natureza** diz quanto custa fechar — e são")
    L.append("coisas diferentes. Um grupo de 19 casos degenerados fecha com **uma** política;")
    L.append("um grupo de 7 fórmulas ausentes é semanas de escrita de método.\n")
    L.append("| Natureza | Qtd | 🔴 | O que fecha |")
    L.append("|---|---:|---:|---|")
    for nat in list(NATUREZA) + ["NAO_CLASSIFICADA"]:
        v = porNat.get(nat)
        if not v:
            continue
        crit = sum(1 for p in v if p["severidade"] == "CRITICA")
        t = NATUREZA.get(nat, {}).get("titulo", "Não classificada")
        f = NATUREZA.get(nat, {}).get("fecha_com", "—")
        L.append(f"| **{t}** | {len(v)} | {crit or ''} | {f} |")
    L.append("")

    L.append("---\n")
    L.append("## As 🔴 críticas, em detalhe\n")
    for p in [x for x in abertas if x["severidade"] == "CRITICA"]:
        L.append(f"### `{p['id']}` · {p['titulo']}\n")
        if p.get("descricao"):
            L.append(str(p["descricao"]).strip() + "\n")
        L.append("**Evidência**\n")
        for e in (p.get("evidencia") or []):
            L.append(f"- {e}")
        L.append("")
        if p.get("impacto"):
            L.append(f"**Impacto:** {str(p['impacto']).strip()}\n")
        if p.get("correcao_candidata"):
            L.append(f"**Correção candidata:** {str(p['correcao_candidata']).strip()}\n")
        b = p.get("bloqueia") or []
        if b:
            L.append(f"**Bloqueia:** {' · '.join(f'`{x}`' for x in b)}\n")
        L.append("---\n")

    L.append("## Todas as abertas\n")
    for nat in list(NATUREZA) + ["NAO_CLASSIFICADA"]:
        v = porNat.get(nat)
        if not v:
            continue
        t = NATUREZA.get(nat, {}).get("titulo", "Não classificada")
        L.append(f"### {t} · {len(v)}\n")
        L.append("| | ID | Bloqueia | Lacuna |")
        L.append("|---|---|---:|---|")
        for p in sorted(v, key=lambda p: (ORDEM_SEV[p["severidade"]], p["id"])):
            nb = len(p.get("bloqueia") or [])
            L.append(f"| {MARCA[p['severidade']]} | `{p['id']}` | {nb or ''} | {p['titulo']} |")
        L.append("")
    return "\n".join(L)


# ═══════════════════════════════════════════════════════════════
# DICIONÁRIO DO DASHBOARD — cruzamento FOR × ART
# ═══════════════════════════════════════════════════════════════

def indice_dependencias(fors):
    """Quem alimenta quem: FOR-A depende de FOR-B se B aparece em variaveis.origem ou alvo."""
    dep = defaultdict(set)
    for f in fors:
        alvos = set()
        for v in (f.get("variaveis") or []):
            o = v.get("origem") if isinstance(v, dict) else None
            if isinstance(o, str) and re.match(r"^(FOR|PAR)-", o):
                alvos.add(o)
        a = f.get("alvo")
        if isinstance(a, str) and re.match(r"^(FOR|PAR)-", a):
            alvos.add(a)
        dep[f["id"]] = alvos
    return dep


def fecho(sementes, dep):
    """Fecho transitivo: tudo que as sementes consomem, direta ou indiretamente."""
    vistos, fila = set(), list(sementes)
    while fila:
        x = fila.pop()
        if x in vistos:
            continue
        vistos.add(x)
        fila.extend(dep.get(x, ()))
    return vistos


def render_dicionario(pecas):
    fors = {p["id"]: p for p in pecas if p.get("tipo") == "FOR"}
    arts = [p for p in pecas if p.get("tipo") == "ART"]
    regs = {p["id"]: p for p in pecas if p.get("tipo") == "REG"}
    lacs = {p["id"]: p for p in pecas if p.get("tipo") == "LAC"}
    dep = indice_dependencias(fors.values())

    def cons(a, chave):
        c = a.get("consome") or {}
        if isinstance(c, list):
            return set(c)
        return set(c.get(chave) or [])

    diretas, profundas = set(), set()
    for a in arts:
        diretas |= cons(a, "superficie_e_direto") | set((a.get("superficie") or {}).get("elementos") or [])
        profundas |= cons(a, "profundidade")
    diretas = {d for d in diretas if d in fors}
    profundas = {d for d in profundas if d in fors} - diretas
    declaradas = diretas | profundas
    alcancadas = fecho(declaradas, dep) & set(fors)
    indiretas = alcancadas - declaradas
    orfas = set(fors) - alcancadas

    onde = defaultdict(list)
    for a in arts:
        sup = set((a.get("superficie") or {}).get("elementos") or [])
        for fid in cons(a, "superficie_e_direto") | sup:
            if fid in fors:
                onde[fid].append((a["id"], "superfície"))
        for fid in cons(a, "profundidade"):
            if fid in fors:
                onde[fid].append((a["id"], "profundidade"))

    L = []
    L.append("# DICIONÁRIO DO DASHBOARD — o que renderizar, onde, com que profundidade\n")
    L.append("> ⚙️ **Arquivo gerado** por `gerar_render.py` a partir de `registro/*.yaml`.")
    L.append("> Não editar à mão. É o documento que o desenvolvedor do painel consome —")
    L.append("> se ele diverge da tela, a tela está errada, não o dicionário.\n")
    L.append("> **Dois princípios (`DEC-009`):** superfície mínima, profundidade total ·")
    L.append("> o drill-down é diagnóstico, não navegação.\n")
    L.append(f"**{len(arts)} artefatos** · {len(diretas)} na superfície · {len(profundas)} no drill-down ·")
    L.append(f"{len(indiretas)} por dependência · **{len(orfas)} sem artefato declarado**\n")

    # ── mapa por DOMÍNIO: onde a fórmula RESIDE ──
    L.append("---\n")
    L.append("## Onde cada fórmula reside\n")
    L.append("O **domínio** é propriedade da fórmula — não muda com a tela. O artefato é")
    L.append("circunstância: hoje consome, amanhã pode não consumir. Esta é a leitura estável.\n")
    pordom = defaultdict(lambda: {"total": 0, "sup": 0, "prof": 0, "orfa": 0, "ids": []})
    for fid, f in fors.items():
        d = pordom[f.get("dominio", "?")]
        d["total"] += 1
        d["ids"].append(fid)
        if fid in diretas: d["sup"] += 1
        elif fid in profundas: d["prof"] += 1
        elif fid in orfas: d["orfa"] += 1
    L.append("| Domínio | Fórmulas | Na superfície | No drill-down | **Sem artefato** |")
    L.append("|---|---:|---:|---:|---:|")
    for dom in sorted(pordom, key=lambda x: -pordom[x]["total"]):
        d = pordom[dom]
        marca = " 🔴" if d["orfa"] == d["total"] else ""
        L.append(f"| **{dom}**{marca} | {d['total']} | {d['sup'] or ''} | {d['prof'] or ''} | "
                 f"{('**'+str(d['orfa'])+'**') if d['orfa'] else ''} |")
    L.append("")
    for dom in sorted(pordom, key=lambda x: -pordom[x]["total"]):
        L.append(f"### {dom} · {pordom[dom]['total']}\n")
        L.append("| Fórmula | Símbolo | Grão | Janela | Onde aparece |")
        L.append("|---|---|---|---|---|")
        for fid in sorted(pordom[dom]["ids"]):
            f = fors[fid]
            locs = onde.get(fid)
            if locs:
                onde_txt = " · ".join(f"`{a}`" for a, _ in locs)
            elif fid in indiretas:
                onde_txt = "_alimenta outra fórmula_"
            else:
                onde_txt = "**— sem artefato —**"
            L.append(f"| `{fid}` {f['nome'][:44]} | `{f.get('simbolo','—')}` | {f.get('grao')} | "
                     f"{f.get('janela')} | {onde_txt} |")
        L.append("")
    L.append("---\n")

    for a in sorted(arts, key=lambda x: x["id"]):
        sup = a.get("superficie") or {}
        prof = a.get("profundidade") or {}
        L.append(f"## `{a['id']}` · {a['nome']}\n")
        L.append(f"> {a.get('resumo','')}\n")
        L.append(f"**Quem abre:** {a['consumidor']} · **Quando:** {a['gatilho']} · "
                 f"**Cadência:** {a['cadencia']} · **Modo mínimo:** ({a['modo_minimo']}) · "
                 f"**Linguagem:** {a['lei_de_linguagem']}\n")

        L.append(f"### Superfície — teto de {sup.get('teto_elementos')} elemento(s)\n")
        if sup.get("numero_ancora"):
            L.append(f"**Âncora:** `{sup['numero_ancora']}` — o número que justifica abrir.\n")
        els = sup.get("elementos") or []
        if els and all(e in fors for e in els):
            L.append("| # | Fórmula | Símbolo | Grão | Janela | Teto | Sem base → |")
            L.append("|---|---|---|---|---|---|---|")
            for i, e in enumerate(els, 1):
                f = fors[e]
                L.append(f"| {i} | `{e}` {f['nome']} | `{f.get('simbolo','—')}` | {f.get('grao')} | "
                         f"{f.get('janela')} | {f.get('teto') if f.get('teto') is not None else '—'} | NULO+selo |")
        else:
            for e in els:
                L.append(f"- {e}")
        L.append("")
        L.append("**Não aparece ativamente:**\n")
        for x in (sup.get("o_que_NAO_aparece") or []):
            L.append(f"- {x}")
        L.append("")

        L.append("### Profundidade\n")
        ev = prof.get("eixo_vertical") or []
        L.append("**Vertical** (desagregar) — " + " → ".join(f"`{x}`" for x in ev) + "\n")
        eh = prof.get("eixo_horizontal") or []
        if eh:
            L.append("**Horizontal** (fatiar no mesmo grão)\n")
            L.append("| Grão | Dimensões |")
            L.append("|---|---|")
            for h in eh:
                L.append(f"| `{h.get('grao')}` | " + " · ".join(h.get("dimensoes") or []) + " |")
            L.append("")
        L.append(f"**Completude:** `{prof.get('completude')}`")
        if prof.get("completude") == "PARCIAL":
            L.append(f" — corta em: {prof.get('onde_corta')}")
            L.append(f"  · razão: {prof.get('por_que')}")
        L.append("")
        if prof.get("piso_declarado"):
            L.append(f"**Piso:** {prof['piso_declarado']}\n")

        ra = a.get("regras_aplicaveis") or []
        if ra:
            L.append("### Regras que o render deve obedecer\n")
            for r in ra:
                reg = regs.get(r)
                L.append(f"- `{r}` — {reg['nome'] if reg else '?'}"
                         + (f" · **{reg.get('obrigatoriedade')}**" if reg and reg.get("obrigatoriedade") else ""))
            L.append("")

        bloq = []
        for fid in set(a.get("consome") or []) | set(els):
            f = fors.get(fid)
            if not f:
                continue
            if f.get("status_canonico") == "CONFLITANTE":
                bloq.append((fid, "CONFLITANTE"))
            for l in (f.get("lacunas") or []):
                if lacs.get(l, {}).get("severidade") == "CRITICA" and lacs[l].get("status") == "ABERTA":
                    bloq.append((fid, f"{l} crítica aberta"))
        if bloq:
            L.append("### 🔴 Bloqueios ativos\n")
            for fid, m in sorted(set(bloq)):
                L.append(f"- `{fid}` — {m}")
            L.append("")
        L.append("---\n")

    L.append("## Índice reverso — onde cada fórmula aparece\n")
    L.append("| Fórmula | Aparece em | Papel |")
    L.append("|---|---|---|")
    for fid in sorted(onde):
        locs = " · ".join(f"`{a}` ({papel})" for a, papel in onde[fid])
        L.append(f"| `{fid}` {fors[fid]['nome'][:40]} | {locs} | direta |")
    L.append("")

    L.append(f"## Fórmulas sem artefato declarado — {len(orfas)}\n")
    L.append("Existem, têm domínio, e nenhum artefato as consome. Não é defeito da fórmula —")
    L.append("é ausência do entregável que a mostraria.\n")
    porb = defaultdict(list)
    for o in orfas:
        porb[fors[o].get("dominio", "?")].append(o)
    L.append("| Domínio | Qtd | Fórmulas |")
    L.append("|---|---:|---|")
    for b in sorted(porb, key=lambda x: -len(porb[x])):
        L.append(f"| **{b}** | {len(porb[b])} | " + " · ".join(f"`{x}`" for x in sorted(porb[b])) + " |")
    L.append("")
    L.append(f"## Fórmulas que alimentam por dependência — {len(indiretas)}\n")
    L.append("Não aparecem em tela, mas são consumidas por quem aparece. São intermediárias legítimas.\n")
    L.append(" · ".join(f"`{x}`" for x in sorted(indiretas)) + "\n")
    return "\n".join(L)


def main():
    os.makedirs(OUT, exist_ok=True)
    lac, _ = carregar()
    destino = os.path.join(OUT, "LACUNAS_CONSULTORIA.md")
    open(destino, "w", encoding="utf-8").write(render_lacunas(lac))
    todas = lac + _
    open(os.path.join(OUT, "DICIONARIO_DASHBOARD.md"), "w", encoding="utf-8").write(
        render_dicionario(todas))
    n = sum(1 for p in lac
            if p.get("fase", "1-CONSULTORIA") == "1-CONSULTORIA" and p.get("status") == "ABERTA")
    print(f"gerado: render/LACUNAS_CONSULTORIA.md · {n} lacunas")
    print("gerado: render/DICIONARIO_DASHBOARD.md")


if __name__ == "__main__":
    main()
