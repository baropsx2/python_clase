"""
Crear función que reciba 3 diccionarios, que devuelva todos los diccionarios y tiene que devolver otro diccionario con
el id del empleado y lo que se le debe pagar en total:
- El primero tiene el id del empleado y apunta a una tupla con los siguientes datos (el nombre del empleado y la
comisión por venta realizada).
- El segundo tiene (el id de la venta y el monto de la venta).
- Hay un tercero que viene el id del empleado y una lista con los id’s de las ventas que hizo.
"""


def calc_comisiones(empleados, ventas, vendedor_ventas):
    pagos = {}
    for emp_id, emp_tupla in empleados.items():
        nombre, comision = emp_tupla
        lista_ventas = vendedor_ventas.get(emp_id)
        if lista_ventas:
            pago_total = 0
            for id_venta in lista_ventas:
                valor_venta = ventas.get(id_venta)
                pago_venta = valor_venta * comision
                pago_total += pago_venta
            pagos.update({emp_id: pago_total})
    print(pagos)
    return pagos


empleados = {
    1: ("Lucero", 0.05),
    2: ("David", 0.07),
    3: ("Tony", 0.03)
}

ventas = {
    10: 227.00,
    4: 333.11,
    22: 101.00
}

vendedor_ventas = {
    1: [10, 4],
    2: [22]
}

calc_comisiones(empleados, ventas, vendedor_ventas)
