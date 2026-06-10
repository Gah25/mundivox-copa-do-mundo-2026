import random


times = ["Brasil", "Marrocos", "França", "Inglaterra", "Espanha", "Holanda",
         "Portugal", "Bélgica", "Croácia", "Uruguai", "Alemanha", "Colômbia",
         "Suiça", "Estados Unidos", "Coreia do Sul", "Argentina"]

estatisticas = {}
for time in times:
    estatisticas[time] = {"marcados": 0, "sofridos": 0}

partidas = []


def jogar_partida(time1, time2, fase):
    gols1 = random.randint(0, 5)
    gols2 = random.randint(0, 5)

    estatisticas[time1]["marcados"] += gols1
    estatisticas[time1]["sofridos"] += gols2
    estatisticas[time2]["marcados"] += gols2
    estatisticas[time2]["sofridos"] += gols1

    if gols1 > gols2:
        vencedor = time1
    elif gols2 > gols1:
        vencedor = time2
    else:
        vencedor = random.choice([time1, time2])

    partidas.append({
        "fase": fase, "time1": time1, "time2": time2,
        "gols1": gols1, "gols2": gols2, "vencedor": vencedor
    })

    print(f"[{fase}] {time1} {gols1} x {gols2} {time2}  |  vencedor: {vencedor}")
    return vencedor


def jogar_fase(times_da_fase, fase):
    print(f"\n===== {fase} =====")
    vencedores = []
    for i in range(0, len(times_da_fase), 2):
        vencedor = jogar_partida(times_da_fase[i], times_da_fase[i + 1], fase)
        vencedores.append(vencedor)
    return vencedores


oitavas = jogar_fase(times, "Oitavas")
quartas = jogar_fase(oitavas, "Quartas")
semis = jogar_fase(quartas, "Semifinal")
final = jogar_fase(semis, "Final")

campeao = final[0]
print(f"\nCAMPEAO: {campeao}")

print("\n----- INSERTS PARA O SQL -----")
for time in times:
    m = estatisticas[time]["marcados"]
    s = estatisticas[time]["sofridos"]
    print(f"INSERT INTO equipes (nome, gols_marcados, gols_sofridos) VALUES ('{time}', {m}, {s});")
for i, p in enumerate(partidas, start=1):
    print(f"INSERT INTO partidas (id, fase, time1, time2, gols1, gols2, vencedor) "
          f"VALUES ({i}, '{p['fase']}', '{p['time1']}', '{p['time2']}', {p['gols1']}, {p['gols2']}, '{p['vencedor']}');")  