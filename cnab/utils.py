from .models import Cnab


def total_value_1():
    cnab_list = Cnab.objects.filter(shop_name="BAR DO JOÃO")
    value_total = 0

    for transation in cnab_list:
        if (
            transation.type == "Boleto"
            or transation.type == "Financiamento"
            or transation.type == "Aluguel"
        ):
            value_total -= transation.value
        else:
            value_total += transation.value
    return value_total


def total_value_2():
    cnab_list = Cnab.objects.filter(shop_name="LOJA DO Ó - MATRIZ")
    value_total = 0

    for transation in cnab_list:
        if (
            transation.type == "Boleto"
            or transation.type == "Financiamento"
            or transation.type == "Aluguel"
        ):
            value_total -= transation.value
        else:
            value_total += transation.value
    return value_total


def total_value_3():
    cnab_list = Cnab.objects.filter(shop_name="MERCADO DA AVENIDA")
    value_total = 0

    for transation in cnab_list:
        if (
            transation.type == "Boleto"
            or transation.type == "Financiamento"
            or transation.type == "Aluguel"
        ):
            value_total -= transation.value
        else:
            value_total += transation.value
    return value_total


def total_value_4():
    cnab_list = Cnab.objects.filter(shop_name="MERCEARIA 3 IRMÃOS")
    value_total = 0

    for transation in cnab_list:
        if (
            transation.type == "Boleto"
            or transation.type == "Financiamento"
            or transation.type == "Aluguel"
        ):
            value_total -= transation.value
        else:
            value_total += transation.value
    return value_total


def total_value_5():
    cnab_list = Cnab.objects.filter(shop_name="LOJA DO Ó - FILIAL")
    value_total = 0

    for transation in cnab_list:
        if (
            transation.type == "Boleto"
            or transation.type == "Financiamento"
            or transation.type == "Aluguel"
        ):
            value_total -= transation.value
        else:
            value_total += transation.value
    return value_total
