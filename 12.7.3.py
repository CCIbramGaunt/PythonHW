per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вклада '))
deposit = [money*0.01*per_cent['ТКБ'], money*0.01*per_cent['СКБ'], money*0.01*per_cent['ВТБ'], money*0.01*per_cent['СБЕР']]
#print(deposit)
max_index = deposit.index(max(deposit))
print('Максимальная сумма, которую Вы можете заработать составит ', max(deposit), 'при размещении денег в банке ', list(per_cent)[max_index])