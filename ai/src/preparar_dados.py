import csv
import json
from datetime import datetime, timezone
from pathlib import Path

AI_DIR = Path(__file__).resolve().parents[1]

CAMPOS = (
    "no_id", "divisao", "ts", "luz_raw", "luz_pct",
    "presenca", "led_pct", "modo", "hora",
)


def preparar(dados, no_esperado="no3"):
    """Valida e ordena leituras sem alterar os dados originais."""
    if not isinstance(dados, list) or not dados:
        raise ValueError("Esperada uma lista não vazia de leituras.")

    resultado = []
    identificadores = set()

    for numero, leitura in enumerate(dados, start=1):
        if not isinstance(leitura, dict):
            raise ValueError(f"Leitura {numero}: formato inválido.")

        if not set(CAMPOS).issubset(leitura):
            raise ValueError(f"Leitura {numero}: faltam campos.")

        if any(leitura[c] is None for c in CAMPOS if c != "luz_pct"):
            raise ValueError(f"Leitura {numero}: campo obrigatório nulo.")

        if leitura["no_id"] != no_esperado:
            raise ValueError(f"Leitura {numero}: nó inesperado.")

        if not isinstance(leitura["divisao"], str) or not leitura["divisao"].strip():
            raise ValueError(f"Leitura {numero}: divisão inválida.")

        ts = leitura["ts"]
        if type(ts) is not int or ts <= 0:
            raise ValueError(f"Leitura {numero}: timestamp inválido.")

        if type(leitura["presenca"]) not in (int, bool) or leitura["presenca"] not in (0, 1):
            raise ValueError(f"Leitura {numero}: presença inválida.")

        for campo in ("led_pct", "luz_pct"):
            valor = leitura[campo]
            if campo == "luz_pct" and valor is None:
                continue
            if type(valor) not in (int, float) or not 0 <= valor <= 100:
                raise ValueError(f"Leitura {numero}: {campo} inválido.")

        chave = (leitura["no_id"], leitura["divisao"], ts)
        if chave in identificadores:
            raise ValueError(f"Leitura {numero}: registo duplicado.")
        identificadores.add(chave)

        try:
            data_utc = datetime.fromtimestamp(ts, timezone.utc).isoformat()
        except (ValueError, OverflowError, OSError) as erro:
            raise ValueError(f"Leitura {numero}: timestamp fora do intervalo.") from erro

        linha = {campo: leitura[campo] for campo in CAMPOS}
        linha["data_utc"] = data_utc
        resultado.append(linha)

    return sorted(resultado, key=lambda linha: linha["ts"])


def main():
    origem = AI_DIR / "data/raw/no3_amostra.json"
    destino = AI_DIR / "data/processed/no3_preparado.csv"

    dados = json.loads(origem.read_text(encoding="utf-8-sig"))
    linhas = preparar(dados)

    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8", newline="") as ficheiro:
        escritor = csv.DictWriter(
            ficheiro, fieldnames=[*CAMPOS, "data_utc"]
        )
        escritor.writeheader()
        escritor.writerows(linhas)

    print(f"Leituras preparadas: {len(linhas)}")
    print(f"CSV guardado em: {destino}")
    print("Sem cálculo de consumo nem treino de modelos.")


if __name__ == "__main__":
    main()