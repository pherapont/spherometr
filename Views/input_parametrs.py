def get_surface_radius() -> float:
    """ Function for input from user radius of surface """

    print("  Введите радиус поверхности( дробная часть отделяется точкой")
    print("  Пример: 1.001")
    radius = input("  ")
    try:
        res = float(radius)
    except:
        print("  Введите правильные данные")
        return get_surface_radius()
    return res


def get_surface_height() -> float:
    """ Function for input from user height of surface """

    print("  Введите высоту поверхности:")
    print("  (разность между показаниями сферометра на детали и эталонной\
        плоскости)")
    print("  (дробная часть отделяется точкой)")
    print("  Пример: 1.001")
    height = input("  ")
    try:
        height = float(height)
    except:
        print("  Введите правильные данные")
        return get_surface_height()
    return height
