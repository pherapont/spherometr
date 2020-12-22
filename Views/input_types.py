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

def get_ring_type(spher_type) -> str:
    """ Function for input from user number of ring """

    print("  Введите номер кольца:")
    print("  Номер обозначен на кольце")
    if spher_type == "1":
        print("  Доступные кольца для малого сферометра:")
        print("  1, 2, 3, 4, 5, 7")
        print(" Если хотите посмотреть список колец, нажмите L")
        if input().lower() == "l":
            pprint(SPHEROMETR['SMALL'])
        ring_type = input("  1 --- 7\n  ")
        while ring_type not in ["1", "2", "3", "4", "5", "7"]:
            print("  Введите правильный номер кольца")
            ring_type = input("  1 --- 7\n  ")
    return ring_type
