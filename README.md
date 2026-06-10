# Teste Técnico Mundivox - Copa do Mundo 2026

Programa em Python que simula a fase eliminatória da Copa do Mundo, das oitavas de final
até o campeão, com scripts SQL para guardar e consultar os dados da competição.

## Arquivos

- main.py - código da simulação dos resultados em Python
- create_table.sql - cria as tabelas no banco
- insert.sql - insere os dados gerados pela simulação
- consultas.sql - as consultas pedidas

## Como rodar o Python

Só precisa ter o Python 3 instalado (não usa nenhuma biblioteca externa).

No terminal, dentro da pasta do projeto:

```
python main.py
```

Ele mostra os jogos de cada fase, o campeão e, no final, imprime os comandos INSERT
prontos pra colar no banco.

## Como rodar o SQL

Usei o Oracle Live SQL (livesql.oracle.com) pra testar.

1. Roda o create_table.sql pra criar as tabelas.
2. Roda o insert.sql pra inserir os dados.
3. Roda o consultas.sql pra ver os resultados.

## Como funciona a simulação

- Tem 16 times nas oitavas. Os confrontos são os times em pares na lista (o 1 joga com o 2, o 3 com o 4, e assim por diante).
- O placar de cada jogo é sorteado de 0 a 5 gols pra cada time (usando random).
- Se empatar, sorteia o vencedor (como se fosse a decisão por pênalti).
- Os vencedores vão passando de fase: oitavas (8 jogos), quartas (4), semifinal (2), final (1), e sobra o campeão.

## Exemplo de saída

Os placares mudam toda vez que roda, porque são sorteados. Um exemplo:

```
===== Oitavas =====
[Oitavas] Brasil 0 x 1 Marrocos  ->  vencedor: Marrocos
[Oitavas] França 3 x 2 Inglaterra  ->  vencedor: França
[Oitavas] Espanha 1 x 4 Holanda  ->  vencedor: Holanda
[Oitavas] Portugal 3 x 3 Bélgica  ->  vencedor: Bélgica
[Oitavas] Croácia 2 x 3 Uruguai  ->  vencedor: Uruguai
[Oitavas] Alemanha 0 x 3 Colômbia  ->  vencedor: Colômbia
[Oitavas] Suiça 4 x 0 Estados Unidos  ->  vencedor: Suiça
[Oitavas] Coreia do Sul 1 x 0 Argentina  ->  vencedor: Coreia do Sul

===== Quartas =====
[Quartas] Marrocos 4 x 4 França  ->  vencedor: França
[Quartas] Holanda 0 x 3 Bélgica  ->  vencedor: Bélgica
[Quartas] Uruguai 5 x 3 Colômbia  ->  vencedor: Uruguai
[Quartas] Suiça 2 x 5 Coreia do Sul  ->  vencedor: Coreia do Sul

===== Semifinal =====
[Semifinal] França 2 x 0 Bélgica  ->  vencedor: França
[Semifinal] Uruguai 4 x 4 Coreia do Sul  ->  vencedor: Uruguai

===== Final =====
[Final] França 4 x 3 Uruguai  ->  vencedor: França

CAMPEAO: França
```

## Resultado das consultas

- Time que marcou mais gols: Uruguai (15)
- Time que sofreu menos gols: Brasil (1)
- Partidas por fase: Oitavas 8, Quartas 4, Semifinal 2, Final 1
- Campeão: França

## Observações

- O enunciado pedia pra começar nas oitavas de final, então comecei com 16 times. Só pra
  registrar, a Copa de 2026 mudou de formato e o mata-mata agora começa antes, com 32 times.
- Como os placares são sorteados, cada execução dá um resultado diferente.
- Deixei o Python e o SQL separados: o Python gera os comandos INSERT com os dados da
  simulação e eu uso eles no script SQL.