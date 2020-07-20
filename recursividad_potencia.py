
def pot( n, m ):

    if m == 0 :
        return 1
    elif m == 1 :
        return n
    else:
        return pot( n, m-1 ) * n

n = int( input( "Ingrese base para calcular potencia: " ) )
m = int( input( "Ingrese exponente para calcular potencia: " ) )

numero_pot = pot( n, m )
print( "La potencia " + repr( n ) + " elevado a la " + repr( m ) + " es " + repr( numero_pot ) )