---
title: Recomendações depois de instalar seu GNU/Linux 
author:
- caioau (encripta tudo unicamp)
todo:
- encriptar /boot , com luks
license: GPLv3+
---

# Recomendacoes depois de instalar seu GNU/Linux

* ta comecando agora no fedora? Veja esse excelente texto [sudo dnf install fedora](http://danielammorais.com/2016/06/19/sudo-dnf-install-fedora/). 

* deltarpm: quando vc for atualizar seu sistema , com o deltarpm ele so baixa "o que mudou", baixando menos coisas

`sudo dnf install deltarpm`

* quer que seus programas abram mais rapido? instale o preload: ele ve os programas que vc mais usa e
"precarrega" as libs que eles precisam , as carregando durante o boot, tornando assim a inicializacao deles mais rapida

```
sudo dnf install preload
sudo systemctl enable preload

```

obs.: no debian troque `dnf` por `apt`

* (fedora apenas) : habilite o [rpmfusion](https://rpmfusion.org/Configuration)

* players: sugiro que instale o mpv, smplayer e o vlc. 

* codecs, precisa? pq se vc instalou os players vc ja consegue tocar as midias

* torrent: torrent eh importante ^^ , veja esse [post](https://torrentfreak.com/top-10-most-popular-torrent-sites-of-2017-170107/) com os sites mais populares de torrent.
    + [webtorrent](https://webtorrent.io/) : programa que permite "tocar" torrents enquanto baixa.
    + [showRSS](https://showrss.info/): site que você escolhe as séries que quer acompanhar, ele gera um feed RSS com o torrent.

* Gerenciador de senhas: instale o keepassx . veja esse [texto](https://caioau.keybase.pub//senhas/senhas.html) para entender o que sao , como criar e gerenciar boas senhas.

* ntp : eh sempre bom que seu sistema esteja com a hora certa:

```
sudo dnf install ntp
sudo systemctl enable ntpd
```

* usa dropbox, googledrive, etc? tudo proprietario! recomendo o [syncthing](https://syncthing.net/):
ele eh um app pra android e um programa pra pc, no qual ele sincroniza pastas entre seus dispositivos, criando assim sua nuvem pessoal e descentralizada.

* quer melhorar a seguranca do seu firefox: [ffprofile](https://ffprofile.com/) permite que vc mude configuracoes internas do firefox, melhorando sua seguranca e privacidade.

* criptografia de disco:
    + ecryptfs: criptografa, de maneira transparente sua /home ou somente uma pasta:
seu usuario NAO PODE ESTAR LOGADO, reinicie sua maquine e rode pelo tty, como root os comandos abaixo:
```
sudo apt install ecryptfs-utils cryptsetup
sudo modprobe ecryptfs
ecryptfs-migrate-home -u <username>
sudo ecryptfs-setup-swap
```

    + ecryptfs no fedora:
    
```
authconfig --enableecryptfs --updateall
usermod -aG ecryptfs USER
ecryptfs-migrate-home -u USER
sudo ecryptfs-setup-swap
```

    
    + luks volume: vamos criar um volume luks com 1GB (sempre da pra aumentar esse tamanho)
```
sudo dd if=/dev/zero of=luks-volume.img bs=1M count=1024
sudo cryptsetup -v -y -s 512 -h sha512 -i 10000 --use-random luksFormat luks-volume.img
sudo cryptsetup luksOpen luksvolume.img luksvolume
sudo mkfs.ext4 /dev/mapper/luksvolume
```

pronto, deve aparecer uma particao em seu gerenciador de arquivos.
para "fechar" seu volume , primeiro desmonte ele depois: `sudo cryptsetup luksClose luksvolume`
daqui pra frente, para abrir seu volume, basta rodar : `sudo cryptsetup luksOpen luksvolume.img luksvolume`

[fonte](https://www.digitalocean.com/community/tutorials/how-to-use-dm-crypt-to-create-an-encrypted-volume-on-an-ubuntu-vps)


     + veracrypt: programa **queridinho** para cryptografar volumes, a vantagem dele eh que somente ele tem os [Hidden Volumes](https://veracrypt.codeplex.com/wikipage?title=Hidden%20Volume) , se vc for forcado falar sua senha do seu volume criptografado, com os hidden volumes vc tem uma segunda senha, protengendo esse outro volume.


## recomendacoes finais:

* ​[O Guia Motherboard para não ser hackeado](https://motherboard.vice.com/pt_br/article/guia-motherboard-para-nao-ser-hackeado) basicamente:
    + mantenha seu sistema e seus programas atualizados.
    + use um gerenciador de senhas.
    + habilite 2FA.
    + faca backups.
    + fique tranquilao.

* [quidsup-LinuxAV](https://youtu.be/3HY62oA1R6E) : Ele mostra alguns passos para manter seu PC com GNU/Linux seguro sem precisar de um antivírus.

* VPN do riseup : https://black.riseup.net/

* Freed-ora : http://www.fsfla.org/ikiwiki/selibre/linux-libre/freed-ora.en.html

## coisas especificas do debian (que provavelmente nao "precisa" no fedora):

* driver wifi: de seus pulos para conectar sua maquina na internet 
(dica: use seu celular como "wifi usb": conecte seu celular no wifi e no seu pc, va em configuracoes -> mais -> tethering e acesso portatil -> habilite vinculo usb)
abra o terminal e rode `lspci` e procure uma linha como essa:

> 03:00.0 Network controller: Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter

por fim, procure na wiki do debian qual pacote desse wifi: nesse caso [rtl819x](https://wiki.debian.org/rtl819x)

* habilitar "sudo" : 

rode como root (para logar como root rode `su`)

```
apt install sudo
usermoad -aG sudo <username>
```

* firewallzinho basico, no fedora ja vem
```
sudo apt install ufw
sudo ufw enable
```

* [apparmor](https://wiki.debian.org/AppArmor/HowToUse) no fedora ja vem com o selinux

* atualizacoes automaticas: veja [aqui](https://martin.hoppenheit.info/blog/2015/automatic-updates-in-debian/)
