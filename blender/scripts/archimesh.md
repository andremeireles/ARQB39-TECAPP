### _Em construção_

![](http://www.stack.com/assets/img/loading-gears.gif)

Durante a aula de Archimesh, foi apontado pelo professor, que o add-on considera para a altura da porta, o valor de 2.10. Precisamos que esse valor seja 2.18, ou seja, 2.10 para a folha da porta, mais a altura da peça de madeira, que está entre a folha da porta e a alvenaria.

Alterar esse valor toda vez que for inserir várias portas, pode ser um trabalho a ser evitado, editando o script do add-on.
Para fazer isso, precisamos identificar onde está localizado o add-on. No menu `Editar > Preferências > Add-on`, descubro o caminho e edito o arquivo responsável pelos parâmetros da porta.

![](https://via.placeholder.com/1294x710?text=Onde+está+o+plugin)

Aqui eu descubro que a pasta está num local protegido pelo sistema operacional.
Se você estiver usando Windows, provavelmente a pasta estará dentro de `C:/Arquivos de Programas/Blender Foundation...` , que também é protegido pelo sistema. Nesse caso, é preciso abrir um editor de texto como administrador.
Escolha o programa que você mais gosta e com o clique direito do mouse, abra o editor de texto como administrador.

Com o editor de texto aberto, use-o para abrir um arquivo chamado `achm_door_maker.py`.
Ao analizar o arquivo `nome-do-arquivo.py`, descubro que o responsável pela altura da porta está na linha _293_, como ilustrado na imagem abaixo.

![](https://via.placeholder.com/1366x768?text=Linha+293+do+arquivo)

Edite o valor de 2.10 para 2.18 e tome o cuidado de escrever ponto e não vírgula. Salve o arquivo, feche o Blender e abra-o novamente.
Pronto! Agora você aprendeu a editar um script, na forma mais básica possível.

Sinta-se a vontade para experimentar outros valores, em lugares diferentes, como a largura da porta, por exemplo.

Que tal ela sempre ser inserida com 0.80 ??

**Atenção:** Sempre que você atualizar para outra versão do Blender, as modificações serão perdidas
