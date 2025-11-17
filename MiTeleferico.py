# tenemos la siguiente clase persona que es agrgacion de la clase cabina con los siguientes atributos : nombre :String, edad:int , pesodepersona:float y los siguientes metodos publicos: +persona (nombre, edad,peso)
class Persona:
    def __init__(self, nombre: str, edad: int, peso: float):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad}, peso={self.peso})"


# tenemos la clase cabina que es composicion de la clase linea con los siguientes atributos : nro de cabina : int , personasAbordo: persona que es aguegacion [] y los siguientes metodos publicos : +cabina (nrocabina), + agregarpersona (persona p)
class Cabina:
    def __init__(self, nroCabina: int):
        self.nroCabina = nroCabina
        self.personasAbordo = []
    
    def agregar_persona(self, persona: Persona):
        self.personasAbordo.append(persona)
    
    def __str__(self):
        personas = ', '.join(str(p) for p in self.personasAbordo)
        return f"Cabina(nroCabina={self.nroCabina}, personasAbordo=[{personas}])"


# tenemos la siguiente clase Linea que es composicion de la clase miteleferico con atributos color :String, FilaPersonas: Clase persona que es aguegacion [] y por ultimo cantidfad de cabinas que es un int con los siguientes metodos publicos : +linea(color), +agregarpersona (persona p), +agregarcabina (nrocabina)
class Linea:
    def __init__(self, color: str):
        self.color = color
        self.filaPersonas = []  
        self.cabinas = []
    
    def agregar_persona(self, persona: Persona):
        self.filaPersonas.append(persona)
    
    def agregar_cabina(self, nroCabina: int):
        cabina = Cabina(nroCabina)
        self.cabinas.append(cabina)
    
    def __str__(self):
        personas = ', '.join(str(p) for p in self.filaPersonas)
        cabinas = ', '.join(str(c) for c in self.cabinas)
        return f"Linea(color={self.color}, filaPersonas=[{personas}], cabinas=[{cabinas}])"


#tenemos cuatro clases MiTeleferico atributos: composiscion clase Linea [] cantidad dingresos:que es un float los metodos de esta clase son + miteleferico()que seria su constructor, otro metodo + agregarPersonaFila (persona p, String linea), Otro metodo publico , tenemos Agregarcabina (String linea
class MiTeleferico:
    def __init__(self):
        self.lineas = []  
        self.cantidadDeIngresos = 0.0  
    
    def agregar_linea(self, linea: Linea):
        self.lineas.append(linea)

    def buscar_linea(self, color: str):
        for linea in self.lineas:
            if linea.color == color:
                return linea
        return None
    
    def agregar_persona_fila(self, persona: Persona, linea_color: str):
        linea = self.buscar_linea(linea_color)
        if linea:
            linea.agregar_persona(persona)
        else:
            print(f"ERROR: Línea {linea_color} no existe.")
    
    def agregar_cabina(self, linea_color: str, nroCabina: int):
        linea = self.buscar_linea(linea_color)
        if linea:
            linea.agregar_cabina(nroCabina)
        else:
            print(f"ERROR: Línea {linea_color} no existe.")
    
    def __str__(self):
        lineas = ', '.join(str(l) for l in self.lineas)
        return f"MiTeleferico(lineas=[{lineas}], cantidadDeIngresos={self.cantidadDeIngresos})"


# pesonas de prueba 
persona1 = Persona("Jhonny Felipez", 30, 75.5)
persona2 = Persona("Ana", 25, 60.0)

mi_teleferico = MiTeleferico()

linea_roja = Linea("Roja")
linea_amarilla = Linea("Amarilla")

mi_teleferico.agregar_linea(linea_roja)
mi_teleferico.agregar_linea(linea_amarilla)

mi_teleferico.agregar_persona_fila(persona1, "Roja")
mi_teleferico.agregar_persona_fila(persona2, "Amarilla")

mi_teleferico.agregar_cabina("Roja", 101)
mi_teleferico.agregar_cabina("Amarilla", 102)

print(mi_teleferico)
