import uuid

Routes = [
    (0, '2022-11-10', '08:00', 'Kyiv-Odesa', 2),
    (1, '2022-11-11', '10:00', 'Kyiv-Poltava', 5),
    (2, '2022-11-12', '12:00', 'Kyiv-Zhytomyr', 3),
    (3, '2022-11-13', '15:00', 'Kyiv-Lviv', 4),
    (4, '2022-11-10', '09:00', 'Kyiv-Odesa', 40),
    (5, '2022-11-11', '11:00', 'Kyiv-Poltava', 38),
    (6, '2022-11-12', '14:00', 'Kyiv-Zhytomyr', 45),
    (7, '2022-11-13', '18:00', 'Kyiv-Lviv', 30),
    (8, '2022-11-10', '07:00', 'Kyiv-Odesa', 40),
    (9, '2022-11-11', '09:00', 'Kyiv-Poltava', 38),
    (10, '2022-11-12', '11:00', 'Kyiv-Zhytomyr', 45),
]
Tickets = []


def main():


    while True:
        ch = int(input('Введите действие'))
        match ch:
            case 0:
                break
            case 1:
                print('Exit')
            case 2:
                RouteChoose = int(input("Выберите маршрут:")) #Стандартный инпут для выбора маршрута
                # print([item for item in Routes if item[0] == RouteChoose])
                Route = ([item for item in Routes if item[0] == RouteChoose]) #Достаем маршрут из списка.
                                                                              #Предмет для предмета в Маршрутах если он равен инпуту
                if not Route: #Если выбор маршрута выходит за рамки item[0] == RouteChoose. Т.е. если запрос маршрута больше, чем их в кортеже
                    print('Вы выбрали не верный маршурт')
                RoadTicket = [item for item in Tickets if item[1] == RouteChoose] #Делаем билет. Предмет для предмета в Билетах если
                NumbSeats = (max(1, len(RoadTicket) if RoadTicket else 0)) + 1 # 1 - ??? +1 потому что отсчёт шел с 0
                if NumbSeats > Route[0][4]: # число билетов не должно быть больше чем индекс маршрута с индексом кол-ва билетов
                    print('Извините, все билеты проданы')
                    continue # продолжить
                else:
                    Tickets.append((len(Tickets), RouteChoose, NumbSeats, uuid.uuid4())) # добавить в билеты кол-во билетов, выбор маршрута номер места(пока кол-во мест) персональный индекс
                    print(Tickets[-1])
            case 3:
                print('123')
            case 4:
                print('Free ticket')
            case _:
                print('Wrong way')



if __name__ == '__main__':
    main()




