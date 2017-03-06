import convert as c

x=1
eu=1

def interpolacion(xa, xb,xrAnt,eu,fun):
	#xr = (xa+xb)/2
	mko = c.f(fun,xa)-c.f(fun,xb)
	ep =100
	xr=1
	if (mko!=0):
		xr = xb-(c.f(fun,xb)*(xa-xb)/(c.f(fun,xa)-c.f(fun,xb)))
	if (xr!=0):
		ep = abs((xr-xrAnt)/xr)*100

	alv = c.f(fun,xa)*c.f(fun,xr)

	if ep>eu:
		if(alv>0):
			interpolacion(xr, xb,xr,eu,fun)
		elif (alv<0):
			interpolacion(xa,xr,xr,eu,fun)
		elif (alv==0):
			print ("Con el método de falsa posición (de inverpolación):")
			print ("la raíz es %s"%xr)
	else:
		print ("Con el método de falsa posición (de inverpolación):")
		print ("La raíz es"+str(xr)+" con un error de "+str(ep)+"%")

#(lim inf,lim sup, xranterior, e porcentual del usuario,funcion)
def biseccion(xa, xb,xrAnt,eu,fun):
	xr = (xa+xb)/2
	ep =100

	if (xr!=0):
		ep = abs((xr-xrAnt)/xr)*100

	#alv = f(xa)*f(xr)
	alv = c.f(fun,xa)*c.f(fun,xr)

	if ep>eu:
		if(alv>0):
			biseccion(xr, xb,xr,eu,fun)
		elif (alv<0):
			biseccion(xa,xr,xr,eu,fun)
		elif (alv==0):
			print ("Con el método de bisección:")
			print ("la raíz es %s"%xr)
	else:
		print ("Con el método de bisección:")
		print ("La raíz es"+str(xr)+" con un error de "+str(ep)+"%")

fun = c.convertAsPy(input("Ingrese una función\n f(x)="))
xl = float(input("Ingrese el limite inferior\n"))
xu = float(input("Ingrese el limite superior\n"))
eu = float(input("Ingrese el error\n"))
biseccion(xl,xu,0,eu,fun)
interpolacion(xl,xu,0,eu,fun)