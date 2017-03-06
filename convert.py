
import math
def convertAsPy(cadena):
    cadena2=""
    cin = 0;
    for i in range (0,len(cadena)-1):
        if(i==0):
            if(cadena[i+1]=="^"):
                cadena2+="math.pow(x,%s"%cadena[i+2]
                cadena2+=")"
            #elif(cadena[i]=="x"):
            #    cadena2+=cadena[i]
            elif(cadena[i+1]=="x" ):
                cadena2+=cadena[i]
                cadena2+="*"
            else:
                cadena2+=cadena[i]
            i+=1
        else:
            if(cadena[i+1]=="^"):
                cadena2+="math.pow(x,%s"%cadena[i+2]
                cadena2+=")"
                i+=3
            elif(cadena[i+1]=="x"):
                cadena2+=cadena[i]
                cadena2+="*"
            elif(cadena[i-1]=="^" or cadena[i]=="^"):
                i+=1
            else:
                cadena2+=cadena[i]
    if not(cadena[-2]=="^"):
        cadena2+=cadena[-1]
    return cadena2

def f(fun, x1):
    x= x1
    exec("y=%s"%fun)
    y1 = locals()["y"]
    return (locals()["y"])
