# Introdução ao Blender

## Vídeos de apresentação

### Tour pelo Blender Studio

<iframe width="560" height="315" src="https://www.youtube.com/embed/mf2uAJepT44" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Entrevista com  Ton Roosendaal, o criador do Blender

<iframe width="560" height="315" src="https://www.youtube.com/embed/qJEWOTZnFeg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Interface

[Documentação](https://docs.blender.org/manual/en/2.90/interface/index.html#user-interface)

![interface](../figs/imgBlender/blenderInterface.jpg)

1. Menu do programa (application menu)
2. Workspaces
3. Controles de cena e camadas de visibilidade (Scene and View Layer selection)
4. Editores

Abas servem para trocar entre diferentes configurações de editores.

________________
## Editores

[Documentação](https://docs.blender.org/manual/en/2.90/editors/index.html#editors)

![Editores](../figs/imgBlender/blendeditors.jpg)


  1. 3d viewport
  2. Outliner
  3. Properties
  4. Timeline


O atalho ``ctrl + space`` maximiza o editor atual ou retorna para a vista padrão da aba.

________________

## Painéis T e N

Alguns editores possuem pequenas setas nos lados de duas áreas. Menus podem ser abertos clicando e arrastando nas setas, ou pelos atalhos ``T`` e ``N``.

Abaixo Vemos a indicação das setas no editor 3d Viewport.

![menus T e N](../figs/imgBlender/menusTeN.jpg)

No Lado esquerdo, temos o painel de ferramentas (tools panel) que pode ser visto ou escondido teclando ``T``.

![Menu T](../figs/imgBlender/menuT.jpg)

No lado direito temos o painel lateral (Sidebar panel), que pode ser mostrado ou recolhido também pela tecla ``N``(como muitos dos ajustes são numéricos, a equipe do Blender escolheu a tecla ``N`` como atalho para este painel)

![Menu N](../figs/imgBlender/menuN.jpg)

É comum encontrar estes paineis referidos como ``T`` e ``N`` nos materiais de informação sobre o blender.

Uma outra versão do painel T pode ser vista pressionando as teclas ``shift + space``. 

![shift+space](../figs/imgBlender/shifht_space.jpg)

Uma tabela com botões aparece na posição do ponteiro do mouse, apresentando os mesmos botões do painel de ferramentas. 

________________

## Modos de Trabalho do Editor 3D Viewport

Os modos de trabalho ([object modes](https://docs.blender.org/manual/en/2.90/editors/3dview/modes.html#object-modes) podem ser selecionados pela barra superior esquerda do editor 3d viewport.

![modos](../figs/imgBlender/modosobj.jpg)

Selecione um dos objetos da cena e clique na seta do seletor de modos como na figura acima.

Apenas dois modos de objeto serão apresentados neste momento, **Object Mode** e o **Edit Mode**. A tecla ``Tab`` alterna automaticamente entre estes dois modos.

**Observação:** note que, quando mudamos de modo os painéis mostram algumas opções diferentes.

_______________

## Precisão (snaps & pivots)

![snaps](../figs/imgBlender/snaps.png)

Comandos de precisão do Blender.

![pivots](../figs/imgBlender/pivot.png)

Pontos pivots de transformação do Blender.

________________

## Adições (add-ons)

![preferences](../figs/imgBlender/preferences.jpg)

Acima vemos uma das maneiras de se abrir o menu de preferências.

![addons](../figs/imgBlender/addons.jpg)

Na opção Add-ons podemos ver uma série de adições que já vem embarcadas no Blender e podemos instalar outras, baixadas da internet. Alguns são gratuitos e outros pagos.

##### Add-ons sugeridos (gratuitos - disponíveis na internet):

  1. [CAD transformations](https://github.com/s-leger/blender_cad_transforms)
  1. [Mesh Align Plus](https://github.com/egtwobits/mesh_mesh_align_plus)
  2. [Sverchok](https://github.com/nortikin/sverchok/)
  3. [Sorcar](https://github.com/aachman98/Sorcar)
  4. [Blender Gis](https://github.com/domlysz/BlenderGIS)
  5. [Blender Bim](https://blenderbim.org/)
  6. [Point Cloud vizualizer](https://github.com/uhlik/bpy#point-cloud-visualizer-for-blender-280)
  1. [QBlocker](https://blender-addons.org/qblocker-addon/)
  2. [Jmesh](https://github.com/jayanam/jmesh-tools)



_______________

## Sistemas de coordenadas

![corrdenadas_belnder](../figs/imgBlender/coordenadas_blender.jpg)

1. Global
2. Local
3. Normal
4. Gimbal
5. View
6. Cursor
7. A partir de um objeto (+)

________________