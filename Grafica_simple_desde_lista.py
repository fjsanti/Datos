'''''

Grafica rapida de una lista de datos.

'''''

import pandas as pd
import matplotlib.pyplot as plt # Manipulacion de graficos

l= [43,34,41,19,21,25,37,44,19,22,20,27,32,31,20,29,62,31,41,20,21,38,25,52,19,19,18,18,35,28,18,19,
    24,45,64,30,30,18,22,24,20,21,42,39,40,54,24,22,44,62,36,39,28,21,26,21,36,47,51,45,22,31,73,49,
    42,36,35,21,20,21,66,25,24,35,21,22,44,24,24,28]

df = pd.DataFrame({'freq': l}) # funcion frecuencia, entrada l
df.groupby('freq', as_index=False).size().plot(kind='bar') # Graficar por frecuencia

#plt.show('')
plt.savefig('foo.png')
