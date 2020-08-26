from electrodomesticos import *

laverrap = Lavarropas(4500, "blanco", 35, 60, 5, 12)
laverrap.funcionar(15)
laverrap.funcionar(10)
laverrap.cargarJabon(100)
print ("laverrap tiene cargado ", laverrap.get_jabon(), " grs de jabon")

atmaMicro = Microondas(15000, "blanco", 5, 640, 8)
atmaMicro.funcionar(9,120)
atmaMicro.funcionar(5, 120)
atmaMicro.abrirPuerta()

phillipsLic = LicuadoraDefectuosa(7600, "negra", 2, 600, 5000, 600)
phillipsLic.agregarLiquido(2000)
phillipsLic.agregarLiquido(3500)
phillipsLic.usar(3)
print(phillipsLic.get_uso())