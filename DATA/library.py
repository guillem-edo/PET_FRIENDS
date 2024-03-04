class library:
    def __init__(self):
        self.imported_libraries = []

    def import_library(self,imported_libraries):
        try:
            import pandas as pd
            self.imported_libraries.append('pandas')
            print('[+] La librería pandas se ha importado correctamente')

            import numpy as np
            self.imported_libraries.append('numpy')
            print('[+] La librería numpy se ha importado correctamente')

            import matplotlib.pyplot as plt
            self.imported_libraries.append('matplotlib')
            print('[+] La librería matplotlib se ha importado correctamente')

        except Exception as e:
            print('[-] Error al importar librerías')
            print(e)