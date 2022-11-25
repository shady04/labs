money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    delta = spend - salary     # находим кол-во потраченных денег, которые необходимо взять из капитала
    if delta > money_capital:     # условие прерывания цикла: потраченных денег > чем сумма капитала
        break

    month += 1                      # каждый круг прибавляют 1 месяц
    money_capital -= delta          # из капитала вычитается потраченны деньги
    spend *= 1 + increase           # траты с каждым циклом увеличиваются

print(month)  # 8
