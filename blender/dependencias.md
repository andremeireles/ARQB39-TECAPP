 # Instalando dependências do sverchok
 


## Instalar o Pip

Encontrar a pasta python no Blender:
1. Vá para o workspace script 
1. No editor *python console* digite:

```Python
import sys
sys.exec_prefix
```
O conssole ira imprimir o caminho para a pasta python do Blender.

1. Copie o endereço (ctrl + c)

1. Abra o Windows Power Shell (como administrador)
digite cd e cole o endereço copiado no passo anterior.

```shell
cd "C:/Program Files/Blender Foundation/Blender/2.80/python/"
```

1. Para habilitar o pip, copie e cole as linhas de comando abaixo. 

```shell
.\bin\python -m ensurepip
.\bin\python -m pip install --upgrade pip setuptools wheel
```

1. Volte para O console do Python do Blender e digite:

```Python
import site
site.getsitepackages()
```

1. Copie (ctrl + c) o segundo endereço impresso

2. Substitua o endereço abaixo pelo último endereço 

```shell
 .\Scripts\pip install --upgrade scipy geomdl SciKit-Image PyMCubes Circlify ladybug-core -t 'C:\\Program Files\\Blender Foundation\\Blender 2.90\\2.90\\python\\lib\\site-packages'
```