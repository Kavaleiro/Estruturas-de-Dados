class car:
    def __init__(self, ano, modelo):
        self.ano = ano 
        self.modelo = modelo

    def modelo_car(self):
        LongName = self.modelo
        return LongName.title()
    def ano_car(self):
        LongName = str(self.ano)
        return LongName
    
new_car = car(2013,"Civic k")
print(new_car.modelo_car())
print(new_car.ano_car())