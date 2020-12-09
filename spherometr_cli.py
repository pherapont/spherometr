def header() -> None:
    print("")
    header = "Расчет параметров оптической детали"
    print("{0:-^70}\n".format(header))

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

def get_surface_radius() -> float:
    """ Function for input from user radius of surface """

    print("  Введите радиус поверхности( дробная часть отделяется точкой")
    print("  Пример: 1.001")
    radius = input("  ")
    try:
        radius = float(radius)
    except:
        print("  Введите правильные данные")
    return radius

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

def get_ring_type() -> str:
    """ Function for input from user number of ring """

    print("  Введите номер кольца:")
    print("  Номер обозначен на кольце")
    ring_type = input("  1 --- 7\n  ")
    while ring_type not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("  Введите правильный номер кольца")
        ring_type = input("  1 --- 7\n  ")
    return ring_type

def check_response(surface_type: str, surface_radius: float, 
        spher_type: str, ring_type: str) -> None:
    """ The function that output data for checking by user """

    print("\n  Проверка введеных данных:")
    surface_type_response = "вогнутая" if surface_type == "1" else "выпуклая"
    print("  Поверхность {}".format(surface_type_response))
    print("  Радиус поверхности: {}мм".format(surface_radius))
    spher_type_response = ("Сферометр малый" if spher_type == "1"
        else "Сферометр большой")
    print("  {}".format(spher_type_response))
    print("  Номер кольца {}\n".format(ring_type))


