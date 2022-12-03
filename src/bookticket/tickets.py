import collections
import uuid
import random
from collections import namedtuple
from datetime import datetime

way = collections.namedtuple('route', ['route_number', 'date', 'time', 'from_', 'to_', 'seats'])
routes = [
    way(0, datetime.fromisoformat('2022-11-10 08:00'), 'Kyiv', 'Odesa', 45),
    way(1, datetime.fromisoformat('2022-11-11 10:00'), 'Kyiv', 'Poltava', 3),
    way(2, datetime.fromisoformat('2022-11-12 12:00'), 'Kyiv', 'Zhytomyr', 5),
    way(3, datetime.fromisoformat('2022-11-13 15:00'), 'Kyiv', 'Lviv', 23),
    way(4, datetime.fromisoformat('2022-11-10 09:00'), 'Kyiv', 'Dnipro', 43),
    way(5, datetime.fromisoformat('2022-11-11 11:00'), 'Kyiv', 'Nicopol', 14),
    way(6, datetime.fromisoformat('2022-11-12 14:00'), 'Kyiv', 'Kharkiv', 40),
    way(7, datetime.fromisoformat('2022-11-13 18:00'), 'Kyiv', 'Hutir', 12),
    way(8, datetime.fromisoformat('2022-11-10 07:00'), 'Kyiv', 'Chernivsi', 13),
    way(9, datetime.fromisoformat('2022-11-11 09:00'), 'Kyiv', 'Bucha', 14),
    way(10, datetime.fromisoformat('2022-11-12 11:00'), 'Kyiv', 'Chernigiv', 11),
]


tickets = []




def main():

    while True:
        ch = int(input('Введите действие'))
        match ch:
            case 0:
                break
            case 1:
                print('Exit')
            case 2:
                route_choose = int(input("Выберите маршрут:"))
                route = ([item for item in routes if item.route_number == route_choose])
                if not route:
                    print('Вы выбрали не верный маршурт')
                road_tickets = [item for item in tickets if item[1] == route_choose]
                numb_seats = (max(1, len(road_tickets) if road_tickets else 0)) + 1
                if numb_seats > route[0][4]:
                    print('Извините, все билеты проданы')
                    continue
                else:
                    tickets.append((len(tickets), route_choose, numb_seats, uuid.uuid4()))
                    print(tickets[-1])
            case 3:
                random_ticket = random.choice(routes)
                print(f' Поздравляю ваш маршрут:', random_ticket)
                road_tickets = [item for item in tickets if item[1] == random_ticket]
                numb_seats = (max(1, len(road_tickets) if road_tickets else 0)) + 1
                tickets.append((len(tickets), random_ticket, numb_seats, uuid.uuid4()))
            case 4:
                print('Free ticket')
            case 5:
                choose_city = input(str('Введите город в который хотите отправиться'))
                city = [item for item in routes if choose_city in item.to_]
                if not city:
                    print('Вы указали не верный город прибытия')
                    continue
                else:
                    print(city)

            case _:
                print('Wrong way')



if __name__ == '__main__':
    main()


