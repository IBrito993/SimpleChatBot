print("Hello, World!")

def mi_to_km(miles):
    return miles * 1.609


print(mi_to_km(100))


def fahrenheit_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    
    return round(c, 3)


print(fahrenheit_to_celsius(451))