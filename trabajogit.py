def suma_primos_hasta(limite):
    
    sieve = [True] * limite
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(limite**0.5) + 1):
        if sieve[start]:
            # Marcamos los múltiplos como no primos
            for i in range(start * start, limite, start):
                sieve[i] = False
                
    return sum(i for i, es_primo in enumerate(sieve) if es_primo)

resultado = suma_primos_hasta(2000000)
print(f"La suma de los primos menores a 2,000,000 es: {resultado}")