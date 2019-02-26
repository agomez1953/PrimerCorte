def calcular_precio_producto(coste_producto):
    """
    >>> calcular_precio_producto(50000)
    75000.0

    :param coste_producto:
    :return:
    """
    return coste_producto*1.5


def calcular_precio_servicio(cantidad_horas):
    """
    >>> calcular_precio_servicio(7)
    700000

    :param cantidad_horas:
    :return:
    """
    return cantidad_horas*100000

def calcular_precio_servicio_extras(cantidad_horas):
    """
    >>> calcular_precio_servicio_extras(5)
    625000.0

    :param cantidad_horas:
    :return:
    """
    return calcular_precio_servicio(cantidad_horas)*1.25

def calcular_costo_envio(kilometros):
    """
    >>> calcular_costo_envio(10)
    1150

    :param kilometros:
    :return:
    """
    return kilometros*115

def calcular_precio_producto_fuera(coste_producto,kilometros):
    """
    >>> calcular_precio_producto_fuera(50000,10)
    51150

    :param coste_producto:
    :param kilometros:
    :return:
    """
    return coste_producto+calcular_costo_envio(kilometros)

def calcular_iva_producto(coste_producto, tasa):
    """
    >>> calcular_iva_producto(50000,19)
    9500.0

    :param coste_producto:
    :param tasa:
    :return:
    """
    return coste_producto*(tasa/100)


def calcular_iva_servicio(cantidad_horas, tasa):
    """
    >>> calcular_iva_servicio(7,15)
    105000.0

    :param cantidad_horas:
    :param tasa:
    :return:
    """
    return calcular_precio_servicio(cantidad_horas)*(tasa/100)

def calcular_iva_envio(kilometros, tasa):
    """
    >>> calcular_iva_envio(10,15)
    172.5

    :param kilometros:
    :param tasa:
    :return:
    """
    return calcular_costo_envio(kilometros)*(tasa/100)

def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    """
    >>> calcular_iva_servicio_fuera(7,15)
    131250.0

    :param cantidad_horas:
    :param tasa:
    :return:
    """
    return calcular_precio_servicio_extras(cantidad_horas)*(tasa/100)


def calcular_recaudo_locales(coste_producto_1,coste_producto_2,coste_producto_3):
    """
    >>> calcular_recaudo_locales(2000,3000,4000)
    1330.0

    :param coste_producto_1:
    :param coste_producto_2:
    :param coste_producto_3:
    :return:
    """
    return calcular_iva_producto((coste_producto_1+coste_producto_2+coste_producto_1),19)

def calcular_recaudo_horas_extra(horas_1,horas_2,horas_3,horas_4):
    """
    >>> calcular_recaudo_horas_extra(2,3,4,5)
    262500.0

    :param horas_1:
    :param horas_2:
    :param horas_3:
    :param horas_4:
    :return:
    """
    return calcular_precio_servicio_extras(horas_1+horas_2+horas_3+horas_4)*0.15



def calcular_recaudo_mixto_local(coste_producto_1,coste_producto_2,horas_1,horas_2):
    """
    >>> calcular_recaudo_mixto_local(2000,3000,5,6)
    4200000000.0

    :param coste_producto_1:
    :param coste_producto_2:
    :param horas_1:
    :param horas_2:
    :return:
    """
    return calcular_precio_producto((coste_producto_1)*calcular_precio_servicio(horas_1))+calcular_precio_producto((coste_producto_2)*calcular_precio_servicio(horas_2))