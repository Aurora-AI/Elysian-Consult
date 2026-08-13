#!/usr/bin/env python3
"""
Validador do registro Aurora — implementa V1..V11 do ESQUEMA_PECA.md §7.

Não julga conteúdo. Só verifica se o contrato de extração foi cumprido.
Uso:  python validar.py [--registro registro/]
Saída: relatório no stdout; exit code 1 se houver REPROVA.
"""
from __future__ import annotations
import sys, glob, os, re, argparse
from collections import defaultdict

try:
    import yaml
except ImportError:
    sys.exit("pyyaml não instalado:  pip install pyyaml")

REPROVA, FILA, AVISO = "REPROVA", "FILA", "AVISO"

# Campos obrigatórios por tipo (ESQUEMA_PECA §2 e §5)
# NOTA: LAC tem forma própria — usa titulo/evidencia/status no lugar de
# nome/procedencia/status_canonico. Ver ESQUEMA_PECA §5.6.
COMUNS = ["id", "tipo", "nome", "procedencia", "status_canonico", "confianca"]
COMUNS_LAC = ["id", "tipo"]
POR_TIPO = {
    "FOR": ["expressao", "grao", "janela", "natureza", "casos_degenerados",
            "onde", "quando", "quem", "entra", "sai"],
    "LAC": ["severidade", "titulo", "evidencia", "quem_decide", "status"],
    "REG": ["gatilho", "acao", "obrigatoriedade", "quem_executa"],
    "AXI": ["enunciado", "o_que_falsificaria"],
    "MEC": ["funcao", "fase", "executor"],
    "EVI": ["fato", "fonte_dado", "o_que_prova"],
}
NATUREZAS = {"CRUA", "NORMALIZADA", "DERIVADA", "PARAMETRO", "SUBJETIVA"}
STATUS = {"CANONICO", "CANDIDATO", "SUPERADO", "CONFLITANTE", "NAO_UTILIZADO", "IMPORTADO"}

# Símbolos matemáticos e operadores que não são variáveis
RUIDO = set("+-*/÷×=()[]{},;:.<>≤≥|Σ∈∩∪ 0123456789")
PALAVRAS_RUIDO = {"mín", "máx", "min", "max", "se", "e", "ou", "P75", "P50",
                  "onde", "SE", "ENTÃO", "caso", "contrário", "TRAVA", "RISCO", "OK",
                  # conectivos de prosa que aparecem em notação de índice
                  "do", "da", "de", "no", "na", "por", "com", "sem", "em", "ao",
                  "vendas", "vendedor", "gestor", "loja", "lojas", "equipe", "cat",
                  "semana", "atual", "anterior", "todos", "cada"}


def carregar(pasta):
    pecas, arquivos = [], sorted(glob.glob(os.path.join(pasta, "*.yaml")))
    for f in arquivos:
        try:
            d = yaml.safe_load(open(f, encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            print(f"  ✗ {os.path.basename(f)}: YAML inválido — {str(e)[:120]}")
            continue
        for p in d.get("pecas", []) or []:
            p["_arquivo"] = os.path.basename(f)
            pecas.append(p)
    return pecas, arquivos


def simbolos_da_expressao(expr: str) -> set[str]:
    """Extrai candidatos a variável de uma expressão, filtrando ruído."""
    if not expr:
        return set()
    corpo = expr.split("=", 1)[1] if "=" in expr else expr
    # remove grupos de índice de somatório — Σ (i ∈ conjunto) — que são prosa, não variável
    corpo = re.sub(r"Σ\s*\([^)]*\)", " Σ ", corpo)
    # remove o argumento de percentis — P75(...) — idem
    corpo = re.sub(r"P\d{2}\s*\([^)]*\)", " P75 ", corpo)
    brutos = re.findall(r"[A-Za-zÀ-ÿα-ω][A-Za-zÀ-ÿα-ω_%]*(?:_[A-Za-zÀ-ÿ0-9]+)?", corpo)
    return {b for b in brutos if b not in PALAVRAS_RUIDO and len(b) > 1}


def validar(pecas):
    achados = []
    def add(sev, regra, pid, msg):
        achados.append((sev, regra, pid, msg))

    ids = {p.get("id") for p in pecas if p.get("id")}
    inventario_shas = set()
    inv = os.path.join(os.path.dirname(__file__), "INVENTARIO.csv")
    if os.path.exists(inv):
        for linha in open(inv, encoding="utf-8").read().splitlines()[1:]:
            campos = linha.split(",")
            if len(campos) > 5:
                inventario_shas.add(campos[5].strip())

    # índice de símbolos declarados
    sym2pecas = defaultdict(set)
    sym2natureza = defaultdict(set)
    numeros = defaultdict(set)

    for p in pecas:
        pid = p.get("id", "<sem id>")
        tipo = p.get("tipo", "")

        # --- campos obrigatórios ---
        base = COMUNS_LAC if tipo == "LAC" else COMUNS
        for c in base + POR_TIPO.get(tipo, []):
            if c not in p or p[c] in (None, [], ""):
                regra = {"grao": "V2", "janela": "V2", "casos_degenerados": "V3",
                         "procedencia": "V6"}.get(c, "V0")
                add(REPROVA, regra, pid, f"campo obrigatório ausente: '{c}'")

        # --- V6 procedência com sha rastreável ---
        for pr in (p.get("procedencia") or []):
            if not isinstance(pr, dict):
                add(REPROVA, "V6", pid, "procedência mal formada")
                continue
            if not pr.get("fonte") and not pr.get("arquivo"):
                add(REPROVA, "V6", pid, "procedência sem fonte/arquivo")

        # --- V7 referências órfãs ---
        for campo in ("ver_tambem", "bloqueia", "lacunas"):
            for ref in (p.get(campo) or []):
                if isinstance(ref, str) and re.match(r"^(FOR|LAC|REG|MEC|AXI|APA|GAT|ART|EVI|PAR)-", ref):
                    if ref not in ids:
                        add(REPROVA, "V7", pid, f"{campo} → '{ref}' não existe no registro")

        # --- status válido ---
        st = p.get("status_canonico")
        if st and st not in STATUS:
            add(REPROVA, "V0", pid, f"status_canonico inválido: '{st}'")

        # --- V9 conflitante sem lacuna ---
        if st == "CONFLITANTE" and not p.get("lacunas"):
            add(FILA, "V9", pid, "CONFLITANTE sem LAC associada")

        if tipo != "FOR":
            continue

        # --- V5 natureza declarada ---
        nat = p.get("natureza")
        if nat and nat not in NATUREZAS:
            add(REPROVA, "V5", pid, f"natureza inválida: '{nat}'")

        # --- V4 variáveis da expressão declaradas ---
        declaradas = set()
        for v in (p.get("variaveis") or []):
            if isinstance(v, dict) and v.get("simbolo"):
                s = str(v["simbolo"])
                declaradas.add(s)
                declaradas.update(re.split(r"[.\s]", s))
                sym2pecas[s].add(pid)
                if v.get("natureza"):
                    sym2natureza[s].add(v["natureza"])
                elif v.get("origem") not in (None, "—"):
                    add(REPROVA, "V5", pid, f"variável '{s}' sem 'natureza' declarada")
        # peça de PARÂMETRO define valores por tabela, não por expressão algébrica
        usadas = set() if p.get("tabela") else simbolos_da_expressao(p.get("expressao", ""))
        proprio = {p.get("simbolo"), p.get("id")}
        orfaos = []
        for u in usadas:
            if u in proprio or u in declaradas:
                continue
            if any(u in d or d in u for d in declaradas if d):
                continue
            orfaos.append(u)

        # V12 — expressão em prosa: a fonte escreveu em linguagem natural, não em símbolos.
        # Três ou mais órfãos em minúsculas é assinatura de prosa, não de símbolo faltando.
        prosa = [o for o in orfaos if o.islower() and len(o) >= 4]
        if len(orfaos) >= 2 or any(len(o) >= 6 and o.islower() for o in orfaos) \
                or p.get("notacao") == "PROSA":
            prosa = prosa or orfaos
            add(FILA, "V12", pid,
                f"expressão em PROSA, não simbólica — não implementável sem tradução "
                f"(termos: {', '.join(sorted(prosa)[:4])}…)")
        else:
            for u in orfaos:
                add(REPROVA, "V4", pid,
                    f"símbolo '{u}' usado na expressão e não declarado em 'variaveis'")

        # --- V3 casos degenerados não vazios ---
        cd = p.get("casos_degenerados") or []
        if cd and not any(isinstance(c, dict) and c.get("condicao") for c in cd):
            add(REPROVA, "V3", pid, "casos_degenerados presente mas sem 'condicao'")

        # --- V11 hipótese ---
        if not p.get("implementado_em") and not p.get("verificado_contra"):
            add(AVISO, "V11", pid, "sem implementação e sem gabarito → HIPÓTESE")

        # --- V8 números divergentes ---
        for chave in ("teto", "piso"):
            if p.get(chave) is not None:
                numeros[(p.get("simbolo"), chave)].add(p[chave])

    # --- V1 colisão de sigla ---
    for s, natures in sym2natureza.items():
        if len(natures) > 1:
            add(REPROVA, "V1", ", ".join(sorted(sym2pecas[s])),
                f"símbolo '{s}' usado com naturezas divergentes: {sorted(natures)}")

    for p in pecas:
        for v in (p.get("variaveis") or []):
            if isinstance(v, dict) and v.get("colisao"):
                add(REPROVA, "V1", p.get("id"),
                    f"colisão declarada no símbolo '{v.get('simbolo')}': {v['colisao']}")

    # --- V8 ---
    for (sim, chave), vals in numeros.items():
        if len(vals) > 1:
            add(FILA, "V8", sim, f"'{chave}' com valores divergentes: {sorted(vals)}")

    # --- V10 axioma sem falsificador ---
    for p in pecas:
        if p.get("tipo") == "AXI" and not p.get("o_que_falsificaria"):
            add(AVISO, "V10", p.get("id"), "AXI sem 'o_que_falsificaria' → rebaixar a CANDIDATO")

    return achados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registro", default=os.path.join(os.path.dirname(__file__), "registro"))
    a = ap.parse_args()

    pecas, arquivos = carregar(a.registro)
    print("═" * 74)
    print("VALIDADOR DO REGISTRO AURORA — ESQUEMA_PECA.md §7")
    print("═" * 74)
    print(f"arquivos: {len(arquivos)} · peças: {len(pecas)}")
    por_tipo = defaultdict(int)
    por_status = defaultdict(int)
    for p in pecas:
        por_tipo[p.get("tipo", "?")] += 1
        por_status[p.get("status_canonico", "?")] += 1
    print("  por tipo:   " + " · ".join(f"{k}={v}" for k, v in sorted(por_tipo.items())))
    print("  por status: " + " · ".join(f"{k}={v}" for k, v in sorted(por_status.items())))

    achados = validar(pecas)
    ordem = {REPROVA: 0, FILA: 1, AVISO: 2}
    achados.sort(key=lambda x: (ordem[x[0]], x[1], str(x[2])))

    n = defaultdict(int)
    for sev, *_ in achados:
        n[sev] += 1

    for sev, marca in ((REPROVA, "🔴"), (FILA, "🟡"), (AVISO, "⚪")):
        grupo = [x for x in achados if x[0] == sev]
        if not grupo:
            continue
        print("\n" + "─" * 74)
        print(f"{marca} {sev} — {len(grupo)}")
        print("─" * 74)
        for _, regra, pid, msg in grupo:
            print(f"  [{regra}] {pid}\n        {msg}")

    print("\n" + "═" * 74)
    print(f"RESULTADO: {n[REPROVA]} reprova · {n[FILA]} fila · {n[AVISO]} aviso")
    if n[REPROVA]:
        print("→ Registro NÃO pode gerar código nem render/ enquanto houver REPROVA.")
    print("═" * 74)
    return 1 if n[REPROVA] else 0


if __name__ == "__main__":
    sys.exit(main())
