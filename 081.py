def esUnPalindromo(numero):
    if numero < 10:
        return False
    cadena = str(numero)
    inversa = int(cadena[::-1])
    return numero == inversa

palindromos = []
for i in range (100,1000):
    for j in range (i, 1000):
        mult = j *  i
        if esUnPalindromo(mult):
            palindromos.append(mult)
            
print(f"El mayor número palindrómico de tres cifra es {max(palindromos)}.")
print(palindromos)