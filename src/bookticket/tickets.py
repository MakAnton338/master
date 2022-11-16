routes = [
    (0, '2022-11-10', '08:00', 'Kyiv-Odesa', 40),
    (1, '2022-11-11', '10:00', 'Kyiv-Poltava', 38),
    (2, '2022-11-12', '12:00', 'Kyiv-Zhytomyr', 45),
    (3, '2022-11-13', '15:00', 'Kyiv-Lviv', 30),
    (4, '2022-11-10', '09:00', 'Kyiv-Odesa', 40),
    (5, '2022-11-11', '11:00', 'Kyiv-Poltava', 38),
    (6, '2022-11-12', '14:00', 'Kyiv-Zhytomyr', 45),
    (7, '2022-11-13', '18:00', 'Kyiv-Lviv', 30),
    (8, '2022-11-10', '07:00', 'Kyiv-Odesa', 40),
    (9, '2022-11-11', '09:00', 'Kyiv-Poltava', 38),
    (10, '2022-11-12', '11:00', 'Kyiv-Zhytomyr', 45),
]
def main():


    while True:
        ch = int(input('Введите действие'))
        match ch:
            case 0:
                break
            case 1:
                print('Exit')
            case 2:
                print('Route list')
            case 3:
                print('Buy ticket')
            case 4:
                print('Free ticket')
            case _:
                print('Wrong way')

if __name__ == '__main__':
    main()

    ###
