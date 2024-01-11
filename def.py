class calculs:

    def comparar_numeros(x,y):
        """Aquesta funció compara dos números i retorna el més gran o 0 si són iguals"""
        if x > y:
            return x
        elif x == y:
            return 0
        else:
            return y
        
    z=comparar_numeros(1,2)
    print(z)
        
    def suma_3_numeros(a,b,c):
        """Aquesta funció suma els 3 números donats"""
        return(a+b+c)
    
    resultat=suma_3_numeros(1,2,3)
    print(resultat)
    
help(calculs.comparar_numeros)
help(calculs.suma_3_numeros)

print(calculs.comparar_numeros.__doc__)