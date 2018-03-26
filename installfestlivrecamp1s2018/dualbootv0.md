---
title: Procedimento DualBoot com Ubuntu
author: caioau
license: GPLv3+
---

# Procedimento DualBoot com Ubuntu

Com esse procedimento você poderá instalar Ubuntu junto com Windows. Dividimos a instalação em 4 partes:

1. Gravação da imagem no pendrive;
2. Desativação do Secure Boot.
3. Instalação do Ubuntu.
4. Sugestões.

Caso você queria se livrar do windows, pule o passo 2. e leia a observação no passo 3.

## Gravação em pendrive

Antes de tudo, você precisa de um pendrive para esse passo, que será formatado (todos os arquivos apagados). Portanto, faça um backup das coisas que estiverem lá.

Primeiramente para gravar a imagem no pendrive, baixe a imagem do Ubuntu: [ubuntu.com/download/desktop](https://www.ubuntu.com/download/desktop)

Escolha entre a versão mais recente ou a versão LTS que terá suporte por muito mais tempo.

Alternativamente, sugiro que você considere o [Ubuntu Budgie](https://ubuntubudgie.org) que tem uma interface linda e familiar. Ou o [Ubuntu MATE](https://ubuntu-mate.org/) que tem uma interface mais básica e leve.

Depois que o download acabar, é importante verificar a imagem baixada. 
(esse passo é importante pois mais importante que atestar se a imagem foi corrompida é verificar se a imagem foi adulterada, como quando colocaram malware no Linux mint em [fev2016](https://blog.linuxmint.com/?p=2994)) 

Vá em [releases.ubuntu.com/](http://releases.ubuntu.com/) , selecione a versão que você escolheu e baixe os arquivos SHA256SUMS e SHA256SUMS.gpg

```
sha256sum --ignore-missing -c SHA256SUMS
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys "8439 38DF 228D 22F7 B374 2BC0 D94A A3F0 EFE2 1092" "C598 6B4F 1257 FFA8 6632 CBA7 4618 1433 FBB7 5451"
gpg --verify SHA256SUMS.gpg SHA256SUMS

```
Se aparecer OK e depois Good signature from "Ubuntu CD Image Automatic Signing Key <cdimage@ubuntu.com>", então está tudo certo :)

Agora bora para a gravação em si: rode `lsblk` antes e depois de conectar o pendrive no seu pc e compare os resultados. Se surgiu o sdb, para gravar basta abrir o terminal na pasta onde a iso está e rodar o comando 

```
sudo dd if=imagem.iso of=/dev/sdb bs=4M status=progress && sync
```

**Importante**: tome cuidado para não colocar /dev/sdb1 ! É para ser apenas /dev/sdb (sem numero).

Para gravar a imagem usando o windows, você pode usar o [etcher](https://etcher.io/) ou o [rufus](https://rufus.akeo.ie/).

Pronto, a primeira parte ja foi!:D`

## Desativação do Secure Boot.

Se deseja se livrar do windows, pule este passo.

O que é o Secure Boot?

Secure boot é um mecanismo disparado durante o boot para verificar se o sistema instalado na sua maquina é o mesmo que o fabricante colocou.

Porém na mioria das vezes ele não funciona com GNU/Linux, [as chaves vazaram](http://www.zdnet.com/article/microsoft-secure-boot-key-debacle-causes-security-panic/). Portanto, não presta, é inútil anyway. 

Como desativá-lo? 

Clique na botão do windows no canto inferior esquerdo → Configurações → Recuperação → Inicialização avançada → Reiniciar agora.

Depois da sua maquina reiniciar vá em solução de problemas → opções avançadas → configurações de firmware UEFI clique reiniar.

Entre na sua bios e procure a opção de secure boot, desative-a e salve as alterações.

## Instalação em si do Ubuntu

Boote seu computador pelo pendrive que gravamos anteriormente. Quando chegar na hora de particionar o disco, identifique a partição do windows (normalmente a maior partição) e a diminua para dar espaço ao Ubuntu (botão magico)

Caso queira se livrar completamente do windows, coloque para utilizar todo o disco.

Pronto! o seu ubuntu foi instalado com sucesso :D

## Sugestões

Esse passo é completamente opcional, vou recomendar programas e coisas para fazer.

Para instalar os programas abaixo basta rodar `sudo apt install nome_do_pacote`, então daqui para frente vou colocar apenas os nomes dos pacotes.

### Gerenciador de senhas: 

Sugiro o `keepassx` , porém o [keepassxc](https://keepassxc.org/) é um excelente fork mais ativo dele.

Quer compartilhar senhas necessarias com colegas de um projeto? `pass` é um gerenciador de senhas que permite compartilhar as senhas com git e as criptografa usando pgp.

### Media Players:

Para video tem o famoso `vlc`, porém prefiro o `smplayer` ou `mpv`.

Para musicas, sugiro o excelente `clementine`

Gosta de torrents? Sugiro o [webtorrent](https://webtorrent.io/) que permite "tocar" os torrents.

### Navegadores:

Meu navegador favorito é o [brave](https://brave.com/) que bloqueia por padrão os rastreadores e cookies e já vem com webtorrent.

(obs: o brave roda numa sandbox, para fazelas funcionar veja [aqui](https://superuser.com/questions/1094597/enable-user-namespaces-in-debian-kernel#1122977) como habilitá-las) 

O navegador padrão é o firefox, sugiro que visite [ffprofile.com](https://ffprofile.com/)  para melhorar a segurança e privacidade dele.

Está acostumado com chrome? instale o `chromium`, que é o navegador no qual o google chrome é baseado, porém esse é software livre e "menos dependente" do google.

## Miscelânea:

Usa bastante o computador anoite? Le bastante pdf? use o `redshift-gtk` para ajustar a temperatura de cor de sua tela e cansar menos a vista.

O ubuntu já vem com firewall, porém desativado, para ativa-lo: `sudo ufw enable`

Quer que seus programas abram mais rapido? instale o `preload`: ele ve os programas que vc mais usa e
"precarrega" as libs que eles precisam , as carregando durante o boot, tornando assim a inicializacao deles mais rapida

Usa bastante pgp? instale o `openpgp-applet`, ele é um ícone que permite que você criptografe facilmente o que está no seu Control-C.

Usa Dropbox, Googledrive, etc? Tudo proprietario! Recomendo o `syncthing` ([syncthing.net](https://syncthing.net/)). Syncthing é um app pra android e programa pra pc, no qual sincroniza pastas entre seus dispositivos e cria sua nuvem pessoal descentralizada.

Para acompanhar seus feeds rss, sugiro o `liferea`.

### coisas para terminal: 

1. [fish shell](https://fishshell.com/) (friendly interactive shell): shell que curto: com autossugestões perfeitas.
2. [powerline](https://powerline.readthedocs.io/en/latest/): status line excelente.
3. [TLDR pages](http://tldr.sh/): man pages simplificadas e com exemplos práticos. 
4. [cheat.sh](http://cheat.sh/) : consulte opções de comandos.
5. [explainshell.com](https://explainshell.com/): referencia legal para aprender a usar shell.

