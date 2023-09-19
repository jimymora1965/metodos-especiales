class Persona:
    def __init__(self,nombre, edad):
        self.n = nombre
        self.e = edad

    # def __str_(self):
    #     return f'Persona(nombre={self.n}, edad= {self.e})'
    
    def __repr__(self):
        return f'Persona("{self.n}",{self.e})'
    
persona = Persona("Jimy","58")
repre = repr(persona)    
resultado = eval(repre)
print(resultado.n,resultado.e)

