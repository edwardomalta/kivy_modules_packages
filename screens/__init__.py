import os
from kivy.lang import Builder

package_dir = os.path.dirname(__file__)

Builder.load_file(os.path.join(package_dir, "my_screens.kv"))
Builder.load_file(os.path.join(package_dir, "components/boton_rojo.kv"))
Builder.load_file(os.path.join(package_dir, "components/boton_naranja.kv"))

# esto no lo encuentro tan necesario (la primera linea)
from .my_screens import (MainScreen, SecondaryScreen) 
# ---
from .components.boton_rojo import BotonRojo
from .components.boton_naranja import BotonNaranja

__all__ = ['MainScreen', 'SecondaryScreen', 'BotonRojo', 'BotonNaranja']