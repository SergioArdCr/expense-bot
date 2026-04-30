def parsear_gasto(texto: str):
    """
    "Almuerzo 15000" → ("Almuerzo", 15000.0)
    "transporte 3500" → ("transporte", 3500.0)
    """
    try:
        partes = texto.strip().split()
        monto = float(partes[-1])
        categoria = " ".join(partes[:-1])
        if not categoria or monto <= 0:
            return None, None
        return categoria, monto
    except (ValueError, IndexError):
        return None, None