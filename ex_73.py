# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Fortaleza.
time = ('Palmeira', 'Internacional', 'Fluminence', 'Corintians','Flamengo', 'Atletico-Pr',
        'Atletico-MG', 'Fortaleza','Sao Paulo', 'Améririca-MG','Bota Fgo', 'Santos', 'Goias',
        'Bragantino', 'Coritibá', 'Cuiaba','Ceará-SC','Atletico-GO','Avai', 'Juventude')
print(f'Essa são os 20 Colocado na tabela do brasileirão 2022: {time}')
print(f'Os 5 primeros colocados são: {time[0:5]}')
print(f'Os 4 ultimos colocadosão são: {time[-4:]}')
print(f'Times em Ordem alfabetica: {sorted(time)}')
print(f"O Fortaleza esta na {time.index('Fortaleza')+1}º Posição")
