valores = ["123","100","abc"]
for v in valores:
    try:
        numero = int(v)
        print(f"2 x {numero} é igaul a {numero * 2}")
    except ValueError:
        print(f"{v} não é númerico")