from pprint import pprint

from Model.data import SPHEROMETR


def get_calculations_type() -> str:
    """ Function for input from user type of calculations """

    print("  Выберите тип вычислений:")
    print("  Введите 1 - если вычисляете высоту поверхности")
    print("  Введите 2 - если вычисляете радиус поверхности")
    calculations_type = input("  1 --- 2\n  ")
    while calculations_type not in ["1", "2"]:
        print("  Введите правильные данные")
        calculations_type = input("  1 --- 2\n  ")
    return calculations_type


def get_surface_type() -> str:
    """ Function for input from user type of surface """

    print("  Выберите тип поверхности:")
    print("  Введите 1 - если поверхность вогнутая")
    print("  Введите 2 - если поверхность выпуклая")
    surface_type = input("  1 --- 2\n  ")
    while surface_type not in ["1", "2"]:
        print("  Введите правильные данные")
        surface_type = input("  1 --- 2\n  ")
    return surface_type

def get_spher_type() -> str:
    """ Function for input from user type of spherometr """

    print("  Выберите тип сферометра:")
    print("  Введите 1 - если малый сферометр")
    print("  Введите 2 - если большой сферометр")
    spher_type = input("  1 --- 2\n  ")
    while spher_type not in ["1", "2"]:
        print("  Введите правильные данные")
        spher_type = input("  1 --- 2\n  ")
    return spher_type


def get_ring_type(spher_type: str) -> str:
    """ Function for input from user number of ring """

    print("  Введите номер кольца:")
    print("  Номер обозначен на кольце")
    rings_response = "  Доступные кольца для {} сферометра:".format(
                "малого" if spher_type == "1" else "большого")
    print(rings_response)
    spherometr = (SPHEROMETR['SMALL'] if spher_type == "1"
                    else SPHEROMETR['BIG'])
    rings_list = [item[-1] for item in spherometr.keys()]
    print("  {}".format(", ".join(rings_list)))
    print("  Если хотите посмотреть параметры колец, нажмите L")
    print("  Иначе, нажмите любую клавишу.")
    user_input = input("  ").lower()
    if user_input == "l":
        pprint(spherometr)
    elif user_input in rings_list:
        return user_input
    print("  Введите номер кольца:  ")
    user_input = input("  1 --- 7\n  ")
    if user_input in rings_list:
        return user_input
    while user_input not in rings_list:
        print("  Введите правильный номер кольца")
        user_input = input("  1 --- 7\n  ")
        ring_type = user_input
    return ring_type
