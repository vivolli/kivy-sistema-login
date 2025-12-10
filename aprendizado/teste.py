from aprendizado.index import Televisor
from aprendizado.index import ControleRemoto


tv = Televisor("SONY", "SONY-123") 
controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)