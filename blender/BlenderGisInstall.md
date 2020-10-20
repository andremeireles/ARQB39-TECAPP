# Instalando o BlenderGis

## Baixando o add-on

Acesse o repositório do Github do [BlenderGis](https://github.com/domlysz/BlenderGIS)

![github_BenderGis](../figs/imgBlender/BlenderGisGitHub.jpg)


## Instalando

Baixe o arquivo .zip e, pela tela de Edit->Preferences->Add-ons, clique na opção **Install**

![bgis_install](../figs/imgBlender/INSTALL_ADDONS.JPG)

navegue até o local onde baixou o arquivo .zip, selecione o arquivo e aperte o botão **install add-on**

![bgis_install_2](../figs/imgBlender/INSTALL_ADDONS_2.JPG)

De volta à tela de Add-ons, clique na seta para visualizar as propriedades do Add-on instalado. Em todos os plug-ins vamos encontrar ao menos um botão que leva para o site da documentação (Help e informações de funcionamento do Plug-in) e um botão para remover o Add-on instalado. Em alguns casos, mais configurações vão aparecer.

Ative a **checkbox** ao lado da seta para instalar o Add-on. 

![bgis_install_2](../figs/imgBlender/INSTALL_ADDONS_3.JPG)


Dependendo da complexidade do Add-on a instalação pode ser muita rápida ou demorar um pouco. Aguarde. O Blender esta descompactando o arquivo .zip e copiando o conteúdo para a pasta de Add-ons da sua instalação. No caso do Windows 10, esta pasta fica no caminho:

```
C:\Users\<seu nome de usuário do windows>\AppData\Roaming\Blender Foundation\Blender\<número da versão do Blender instalada e.g. \2.90\>\scripts\addons
```

Que também pode ser acessado digitando a lina abaixo na barra de endereço do **Explorador de Arquivos** do Windows (apenas mudando o número da versão do Blender):

```
%AppData%\Blender Foundation\Blender\2.90\scripts\addons
```

No fim desta execução, a **checkbox** aparecerá marcada e a instalação concluída. Alguns Add-ons, contudo, exigem configurações adicionais que aparecerão nesta mesma tela, assim que a **checkbox** aparecer como marcada.

## Configurações Adicionais do BlenderGis

No BlenderGis é necessário configurar uma pasta de cash e é recomendável adicionar o sistema de coordenadas geoespaciais mais utilizado na sua região.

### Cash Folder

Crie uma pasta para o cash do BlenderGis em algum lugar do seu drive e clique no ícone para definir o caminho, conforme figura abaixo:

![cash](../figs/imgBlender/BlenderGisCashFolder.jpg)

Navegue até a pasta criada e clique no botã para aceitar.

![cash_2](../figs/imgBlender/BlenderGisCashFolder_2.jpg)


### Sistema de Projeção Sirgas 2000

O sistema de corrdenadas de referência Sirgas 2000 é o mais utilizado no Brasil. Informações sobre este sistema e seu código EPSG podem ser conferidas no [link](https://epsg.io/4674).

Na seção **spatial reference systems** das configurações do BlenderGis, clique no botão **Add**

![cash_2](../figs/imgBlender/BlenderGisCRS.jpg)

Em seguida preencha a caixa de diálogo conforme indicado. 

![cash_2](../figs/imgBlender/BlenderGisCRS_2.jpg)

```
EPSG:4674
SIRGAS 2000
```

Para configurar qualquer outro sistema de coordenadas, pasta pesquisar o nome e o EPSG na internet e repetir as operações descritas acima.

## Vídeo com instruções de instalação e uso:

__________________________________
### Canal [Nicko16](https://www.youtube.com/channel/UCIldsycnma5sHR1VRP38vhg)

<iframe width="560" height="315" src="https://www.youtube.com/embed/YNtKnmRXVlo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

__________________________________

## Mais sobre o BlenderGis

### [Modelagem de terrenos a partir de arquivos dxf](./blenderGis_dxf.md)