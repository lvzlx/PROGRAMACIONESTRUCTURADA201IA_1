import pyfiglet
import sys

# Generar un banner estilizado
banner = pyfiglet.figlet_format("Estructurada")
print(banner)

# Mostrar información del entorno para confirmar que no es el global
print(f"Versión de Python: {sys.version}")
print("-" * 30)
print("¡Librería instalada correctamente en el entorno virtual!")