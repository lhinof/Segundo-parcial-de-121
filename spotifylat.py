class Cancion:
    def __init__(self, nombre, duracion, artista):
        self.nombre = nombre
        self.duracion = duracion  
        self.artista = artista  

class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = [] 
        self.seguidores = 0  

    def agregar_cancion(self, cancion):
        """Añadir una canción a la lista del artista."""
        self.canciones.append(cancion)
        self.seguidores += 10  

    def obtener_estadisticas(self):
        """Devuelve la cantidad de canciones y seguidores."""
        return f"Artista: {self.nombre}, Canciones: {len(self.canciones)}, Seguidores: {self.seguidores}"

class Usuario:
    def __init__(self, nombre, premium=False):
        self.nombre = nombre
        self.premium = premium  
        self.estadisticas = {
            'canciones_reproducidas': 0,
            'seguimiento_artistas': {}
        }

    def reproducir_cancion(self, cancion):
        """Simula la reproducción de una canción."""
        self.estadisticas['canciones_reproducidas'] += 1
        if cancion.artista.nombre not in self.estadisticas['seguimiento_artistas']:
            self.estadisticas['seguimiento_artistas'][cancion.artista.nombre] = 0
        self.estadisticas['seguimiento_artistas'][cancion.artista.nombre] += 1
        cancion.artista.seguidores += 1 

    def obtener_estadisticas(self):
        """Devuelve las estadísticas del usuario."""
        tipo_usuario = "Premium" if self.premium else "Gratuito"
        return f"Usuario: {self.nombre} ({tipo_usuario})\nReproducciones: {self.estadisticas['canciones_reproducidas']}\nSeguimiento de artistas: {self.estadisticas['seguimiento_artistas']}"

class Spotify:
    def __init__(self):
        self.usuarios = []  
        self.artistas = [] 

    def registrar_usuario(self, nombre, premium=False):
        """Registrar un nuevo usuario en la plataforma."""
        nuevo_usuario = Usuario(nombre, premium)
        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def registrar_artista(self, nombre):
        """Registrar un nuevo artista en la plataforma."""
        nuevo_artista = Artista(nombre)
        self.artistas.append(nuevo_artista)
        return nuevo_artista

    def mostrar_estadisticas(self):
        """Mostrar estadísticas generales de la plataforma."""
        print("Estadísticas de Usuarios:")
        for usuario in self.usuarios:
            print(usuario.obtener_estadisticas())
        print("\nEstadísticas de Artistas:")
        for artista in self.artistas:
            print(artista.obtener_estadisticas())


spotify = Spotify()


usuario1 = spotify.registrar_usuario("Carlos", premium=True)
usuario2 = spotify.registrar_usuario("Ana", premium=False)


artista1 = spotify.registrar_artista("Shakira")
artista2 = spotify.registrar_artista("Bad Bunny")

cancion1 = Cancion("Hips Don't Lie", 3.35, artista1)
cancion2 = Cancion("La Canción", 4.05, artista2)
artista1.agregar_cancion(cancion1)
artista2.agregar_cancion(cancion2)

usuario1.reproducir_cancion(cancion1)
usuario2.reproducir_cancion(cancion2)
usuario1.reproducir_cancion(cancion2)

spotify.mostrar_estadisticas()
