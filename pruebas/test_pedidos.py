from librerias.pedidos import procesar_venta

def test_calculo_iva():
    # Simulamos un ticket con un producto de 10€
    ticket_falso = [{'nombre': 'Pizza Test', 'precio': '10.00'}]
    # Total esperado: 10 + 10% IVA (1.00) = 11.00
    assert procesar_venta(ticket_falso) == 11.00

def test_total_cero():
    # Una lista vacía debe devolver 0
    assert procesar_venta([]) == 0