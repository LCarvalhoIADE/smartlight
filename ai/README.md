# Componente de IA — SmartLight AI

## Objetivo

Prever o consumo energético da iluminação a partir do histórico
dos nós e de dados meteorológicos da Open-Meteo.

Está prevista a comparação de:
- Referência simples: consumo da mesma hora do dia anterior.
- Regressão Linear.
- Random Forest.

A avaliação será feita com MAE (Erro Médio Absoluto),
respeitando a ordem temporal dos dados de treino e teste.

## Estado atual

- Ambiente Python e dependências configurados.
- Amostra local de 50 leituras reais do nó no3.
- Script de validação e preparação dos dados implementado.
- CSV gerado com as leituras ordenadas cronologicamente.
- 13 testes automáticos aprovados.
- Sem cálculo de consumo ou treino de modelos nesta etapa.

## Organização

- data/raw/: dados originais, apenas locais.
- data/processed/: dados preparados, apenas locais.
- src/: scripts Python.
- tests/: testes automáticos com dados fictícios.
- outputs/: futuros resultados, métricas e gráficos.
- requirements.txt: dependências do ambiente.

Os dados reais, credenciais e o ambiente virtual não devem
ser publicados no Git.

## Executar

Executar os comandos na raiz do repositório,
com o ambiente virtual ai/.venv ativo.

Preparar a amostra:

```powershell
python ai/src/preparar_dados.py
```

Executar os testes:

```powershell
python -m pytest ai/tests/test_preparar_dados.py -v
```

## Entrada e saída

Entrada local:
data/raw/no3_amostra.json

Saída local:
data/processed/no3_preparado.csv

O script preserva o JSON original, valida os campos obrigatórios
e algumas regras de valores, rejeita duplicados pelo conjunto
(no_id, divisao, ts), ordena as leituras e acrescenta data_utc.

O CSV de saída é substituído em cada execução.

## Limitações atuais

- A amostra é pequena e destina-se a validar o processamento.
- luz_pct é nulo porque o sensor atual é digital.
- Os valores nulos são preservados, ficando vazios no CSV.
- led_pct indica a intensidade comandada ao LED, não energia medida.
- Ainda não existem medições energéticas nesta amostra.
- Ainda não existe agregação por hora ou integração meteorológica.
- Os testes verificam regras do código, não a precisão dos sensores.

## Implementação e testes

O projeto segue o Modelo em V.

Nesta componente, os testes unitários verificam:
- Preservação dos dados originais e de luz_pct nulo.
- Conversão do timestamp para UTC.
- Ordenação cronológica.
- Rejeição de duplicados.
- Rejeição de determinados valores inválidos.
- Rejeição de campos em falta e de uma lista vazia.

## Próximas etapas

1. Obter e analisar um histórico maior de leituras.
2. Identificar falhas de recolha e preparar resumos por hora.
3. Integrar meteorologia por localização e instante.
4. Definir e validar o consumo usado como alvo da previsão.
5. Treinar e comparar os modelos.
6. Integrar as previsões com a API e o dashboard.

Os endpoints e o formato de envio das previsões serão
combinados com os responsáveis pelo servidor, BD e dashboard.