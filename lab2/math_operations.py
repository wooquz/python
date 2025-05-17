# Возвращение суммы a + b
def add(a, b):
    return a + b

# Возвращение разности a - b"
def subtract(a, b):
    return a - b

# Возвращение произведения a * b
def multiply(a, b):
    return a * b

# Возвращение a / b, или None при делении на ноль
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None