from copy import deepcopy

import pytest

from ai.src.preparar_dados import preparar


@pytest.fixture
def leitura():
    """Leitura fictícia, sem dados pessoais."""
    return {
        "no_id": "no3",
        "divisao": "teste",
        "ts": 1700000000,
        "luz_raw": 1,
        "luz_pct": None,
        "presenca": 1,
        "led_pct": 100,
        "modo": "auto",
        "hora": "2023-11-14 22:13:20",
    }


def test_preserva_nulo_e_dados_originais(leitura):
    dados = [leitura]
    original = deepcopy(dados)

    resultado = preparar(dados)

    assert resultado[0]["luz_pct"] is None
    assert resultado[0]["data_utc"] == "2023-11-14T22:13:20+00:00"
    assert dados == original


def test_ordena_por_timestamp(leitura):
    posterior = {**leitura, "ts": leitura["ts"] + 15}

    resultado = preparar([posterior, leitura])

    assert [linha["ts"] for linha in resultado] == [
        leitura["ts"],
        posterior["ts"],
    ]


def test_rejeita_duplicados(leitura):
    with pytest.raises(ValueError, match="duplicado"):
        preparar([leitura, leitura.copy()])


@pytest.mark.parametrize(
    "campo,valor",
    [
        ("no_id", "outro_no"),
        ("divisao", " "),
        ("ts", 0),
        ("ts", True),
        ("presenca", 2),
        ("led_pct", -1),
        ("led_pct", 101),
        ("luz_pct", 101),
    ],
)
def test_rejeita_valores_invalidos(leitura, campo, valor):
    leitura[campo] = valor

    with pytest.raises(ValueError):
        preparar([leitura])


def test_rejeita_campo_em_falta(leitura):
    del leitura["presenca"]

    with pytest.raises(ValueError, match="faltam campos"):
        preparar([leitura])


def test_rejeita_lista_vazia():
    with pytest.raises(ValueError, match="lista"):
        preparar([])