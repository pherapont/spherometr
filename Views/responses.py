def check_response(calc_type: str, surface_type: str,
    surface_param: float, spher_type: str, ring_type: str) -> None:

    """ The function that output data for checking by user """

    print("\n  Проверка введеных данных:")

    calc_type_resp = "стрелку" if calc_type == "1" else "радиус"
    print("  Вычисляем {} поверхности.".format(calc_type_resp))

    surface_type_resp = "вогнутая" if surface_type == "1" else "выпуклая"
    print("  Поверхность {}".format(surface_type_resp))

    if calc_type == "1":
        print("  Радиус поверхности: {}мм".format(surface_param))
    elif calc_type == "2":
        print("  Высота поверхности: {}мм".format(surface_param))

    spher_type_response = ("Сферометр малый" if spher_type == "1"
        else "Сферометр большой")
    print("  {}".format(spher_type_response))

    print("  Номер кольца {}\n".format(ring_type))


def result_response(res: float) -> str:

    """ The function that output result of calculations """

    print("  Результат:\n\t", res, "мм\n")
