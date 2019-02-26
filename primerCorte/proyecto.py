from _ast import keyword


def calcular_precio_producto(coste_producto):
    """
    >>> calcular_precio_producto(3)
    1.5

    :param coste_producto:
    :return:
    """
    return (coste_producto*0.5)


def calcular_precio_servicio(cantidad_horas):
    """
    >>> calcular_precio_servicio(2)
    200000

    :param cantidad_horas:
    :return:
    """
    return cantidad_horas*100000

def calcular_precio_servicio_extras(cantidad_horas):
    """
    >>> calcular_precio_servicio_extras(2)
    125000.0

    :param cantidad_horas:
    :return:
    """
    return (calcular_precio_servicio(1)*0.25)+calcular_precio_servicio(1)

def calcular_costo_envio(kilometros):
    """
    >>> calcular_costo_envio(10)
    1150

    :param kilometros:
    :return:
    """
    return kilometros*115
def calcular_precio_producto_fuera(coste_producto, kilometros):
    """
    >>> calcular_precio_producto_fuera(200000,8)
    1600000

    :param coste_producto:
    :param kilometros:
    :return:
    """
    return coste_producto*kilometros


def calcular_iva_producto(coste_producto, tasa):
    """
    >>> calcular_iva_producto(5000,0.19)
    950.0

    :param coste_producto:
    :param tasa:
    :return:
    """
    return coste_producto*0.19

def calcular_iva_servicio(cantidad_horas, tasa):
    """
    >>> calcular_iva_servicio(calcular_precio_servicio(5),0.08)
    40000.0

    :param cantidad_horas:
    :param tasa:
    :return:
    """
    return cantidad_horas*0.08
def calcular_iva_servicio_fuera(cantidad_horas, tasa, costo_envio):
    """
        >>> calcular_iva_servicio_fuera(6*calcular_costo_envio(10),0.15)
        714150.0

        :param cantidad_horas:
        :param tasa:
        :return:
        """
    return cantidad_horas*calcular_costo_envio()
def calcular_iva_envio(kilometros, tasa):
  pass
def calcular_recaudo_locales(coste_producto_1,oste_producto_2,coste_producto_3):

    pass

def calcular_recaudo_horas_extra(hora_1,horas_2,horas_3,horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,coste_producto_2,horas_1,horas_2):
    pass