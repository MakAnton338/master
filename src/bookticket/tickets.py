import collections
import uuid
import random
from datetime import datetime

way = collections.namedtuple('Route', ['route_number', 'datetime', 'from_', 'to_', 'seats'])
routes = [
    way(0, datetime.strptime('2022-11-10 08:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Odesa', 45),
    way(1, datetime.strptime('2023-11-11 10:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Poltava', 3),
    way(2, datetime.strptime('2022-11-12 12:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Zhytomyr', 5),
    way(3, datetime.strptime('2022-11-13 15:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Lviv', 23),
    way(4, datetime.strptime('2022-11-10 09:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Dnipro', 43),
    way(5, datetime.strptime('2022-11-11 11:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Nicopol', 14),
    way(6, datetime.strptime('2023-11-12 14:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Kharkiv', 40),
    way(7, datetime.strptime('2023-11-13 18:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Hutir', 12),
    way(8, datetime.strptime("2023-11-10 07:00", "%Y-%m-%d %H:%M"), 'Kyiv', 'Chernivsi', 2),
    way(9, datetime.strptime('2023-11-11 09:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Bucha', 14),
    way(10, datetime.strptime('2022-11-12 11:00', "%Y-%m-%d %H:%M"), 'Kyiv', 'Chernigiv', 11),
]


tickets = []



def buy_tickets(route_choose):
    route = [item for item in routes if item.route_number == route_choose]
    road_tickets = [item for item in tickets if item[1] == route_choose]
    numb_seats = (max(1, len(road_tickets) if road_tickets else 0)) + 1
    if route[0][1] <= datetime.today():
        print('time_check')
        return
    rem_seats = set()
    for item in range(1, (route[0][4]) + 1):
        rem_seats.add(item)
    rem_seats = rem_seats - {item[2] for item in road_tickets}
    seats_rem = int(input(f'Выберите номер места: {rem_seats}'))
    if seats_rem not in rem_seats:
        return
    if numb_seats > route[0][4]:
        print('Извините, все билеты проданы')
        return
    return len(tickets), route_choose, seats_rem, uuid.uuid4()



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
                ticket = buy_tickets(route_choose)
                if ticket:
                    tickets.append(ticket)
                    print(tickets[-1])
                else:
                    return
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

