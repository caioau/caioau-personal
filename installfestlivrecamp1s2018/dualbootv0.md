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

Adicionar usuario no grupo sudo (debian): Para usar o sudo no seu usuario use o comando `su` digite a senha de root então o $ na linha de comando virá o # então instale o sudo caso não tenha `apt install sudo` por fim `usermod -aG nome_usuario sudo`

Para instalar os programas abaixo basta rodar `sudo apt install nome_do_pacote`, então daqui para frente vou colocar apenas os nomes dos pacotes.

Icone de atualizações: instale o pacote `pk-update-icon` para ter um icone que te notifica se seu sistema precisa ser atualizado.

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

### Otimizações:

Sua maquina é um laptop? Otimize o gerenciamento de energia para salvar bateria instalando os pacotes `tlp tlp-rdw linux-cpupower`

Tem SSD? Adicione a opção noatime na fstab para reduzir o numero de escritas no seu disco, crie um arquivo em `/etc/cron.hourly/cron-fstrim` com o seguinte conteudo: depois `sudo chmod +x /etc/cron.hourly/cron-fstrim` e verique o arquivo /var/log/fstrim.log se o script está rodando.

```
#!/bin/bash

logf=/var/log/fstrim.log

echo "<------------------------->" >> $logf
date >> $logf
fstrim -v / >> $logf
```

criptografou seu disco com LUKS? modifique o campo GRUB_CMDLINE_LINUX_DEFAULT em /etc/default/grub adicionando a opção rd.luks.options=discard

zram: Uma alternativa ao swap tradicional em disco é usar o zram que é o swap em RAM: baixe o [pacote](https://apt.galliumos.org/pool/main/z/zram-config/zram-config_0.5-galliumos2_all.deb) e instale ele com `sudo dpkg -i <arquivo>`

desativar serviços não essenciais: Rode `systemd-analyze` e veja quanto tempo seu computador demora para ligar, rode `systemd-analyze blame` para listar quanto cada serviço demora para ligar. Quais serviços posso desativar? Em [Cleaning Up Your Linux Startup Process](https://www.linux.com/learn/cleaning-your-linux-startup-process) use `sudo systemctl disable <nome_servico>` para desativar e `sudo systemctl mask <nome_servico>` para forcar ele nunca iniciar. 

lista de serviços:

```
    accounts-daemon.service is a potential security risk. It is part of AccountsService, which allows programs to get and manipulate user account information. I can't think of a good reason to allow this kind of behind-my-back operations, so I mask it.

    avahi-daemon.service is supposed to provide zero-configuration network discovery, and make it super-easy to find printers and other hosts on your network. I always disable it and don't miss it.

    brltty.service provides Braille device support, for example, Braille displays.

    debug-shell.service opens a giant security hole and should never be enabled except when you are using it. This provides a password-less root shell to help with debugging systemd problems.

    ModemManager.service is a DBus-activated daemon that controls mobile broadband (2G/3G/4G) interfaces. If you don't have a mobile broadband interface -- built-in, paired with a mobile phone via Bluetooth, or USB dongle -- you don't need this.

    pppd-dns.service is a relic of the dim past. If you use dial-up Internet, keep it. Otherwise, you don't need it.

    rtkit-daemon.service sounds scary, like rootkit, but you need it because it is the real-time kernel scheduler.

    whoopsie.service is the Ubuntu error reporting service. It collects crash reports and sends them to https://daisy.ubuntu.com. You may safely disable it, or you can remove it permanently by uninstalling apport.

    wpa_supplicant.service is necessary only if you use a Wi-Fi network interface.

```

Otimizando initramfs: No arquivo `/etc/initramfs-tools/initramfs.conf` mude MODULES= para MODULES=dep e COMPRESS= para lzop (caso tenha ssd coloque cat), por fim `sudo update-initramfs -u -k all`

### Dicas de segurança:

Anonimizar mac adress: Para evitar que seja rastreado na rede que você se conecta vamos colocar para que seu endereço fisico mude toda vez que conecta novamente, crie o arquivo `/etc/NetworkManager/conf.d/30-mac-randomization.conf` contendo: [fonte](https://blogs.gnome.org/thaller/2016/08/26/mac-address-spoofing-in-networkmanager-1-4-0/)

```
[device-mac-randomization]
# "yes" is already the default for scanning
wifi.scan-rand-mac-address=yes

[connection-mac-randomization]
ethernet.cloned-mac-address=random
wifi.cloned-mac-address=random
```

ssh hardening: Vai habilitar um servidor ssh na sua maquina? Habile o ufw: `ufw enable` e libere o ssh `ufw limit ssh`.
gere novas chaves:
```
sudo -s
cd /etc/ssh
rm ssh_host_*
ssh-keygen -t rsa -b 4096 -f ssh_host_rsa_key
ssh-keygen -t ed25519 -f ssh_host_ed25519_key
```

opções do ssh: mude o arquivo `/etc/ssh/sshd_config` e mude as seguintes opções:

```
# (se quiser mude para uma porta aleatoria entre 49152–65535)
#Port 22

# (comente as opcoes dsa e ecdsa)
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_ed25519_key


HostKeyAlgorithms ssh-ed25519-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,ssh-ed25519,ssh-rsa

KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256
 
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
 
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com 

LoginGraceTime 1m
PermitRootLogin no

# (desative passwordauth e coloque apenas pubkey: 
# gere uma chave com ssh-keygen -t ed25519 -o -a 300 -f ~/.ssh/chave
# copie e chave com ssh-copy-id -i ~/.ssh/chave user@server
#PubkeyAuthentication yes
#PasswordAuthentication yes
PermitEmptyPasswords no

UsePrivilegeSeparation sandbox

ClientAliveInterval 20
```

habilite 2FA no ssh: [Hardening SSH with OTP for 2 factor authentication](https://jonarcher.info/2015/07/hardening-ssh-with-otp-for-2-factor-authentication/)

spectre e meltdown: são duas vunerabilidades graves: verique se você está vuneravel: [Spectre & Meltdown Checker](https://github.com/speed47/spectre-meltdown-checker), para mitigar essas vunerabilidades instale o pacote `intel-microcode` (habilite os repositorios non-free)

ecryptfs: Quer criptografar seu /home de maneira transparante? seu usuario NAO PODE ESTAR LOGADO, reinicie sua maquine e rode pelo tty, como root os comandos abaixo:

```
sudo apt install ecryptfs-utils cryptsetup
sudo modprobe ecryptfs
ecryptfs-migrate-home -u <username>
sudo ecryptfs-setup-swap
```

criptografar /boot : instalou com disco criptografado ? criptografe o /boot para tornar a criptografia de disco mais segura: [Encrypting More: /boot Joins The Party](https://dustymabe.com/2015/07/06/encrypting-more-boot-joins-the-party/)

```
[root@localhost ~]# mount --bind / /mnt/
[root@localhost ~]# cp -a /boot/* /mnt/boot/
[root@localhost ~]# cp -a /boot/.vmlinuz-* /mnt/boot/
[root@localhost ~]# diff -ur /boot/ /mnt/boot/
[root@localhost ~]# umount /mnt

[root@localhost ~]# umount /boot
[root@localhost ~]# sed -i -e '/\/boot/d' /etc/fstab


[root@localhost ~]# cp /boot/grub2/grub.cfg /boot/grub2/grub.cfg.backup
[root@localhost ~]# grub2-mkconfig > /boot/grub2/grub.cfg
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.0.4-301.fc22.x86_64
Found initrd image: /boot/initramfs-4.0.4-301.fc22.x86_64.img
Found linux image: /boot/vmlinuz-0-rescue-3f9d22f02d854d9a857066570127584a
Found initrd image: /boot/initramfs-0-rescue-3f9d22f02d854d9a857066570127584a.img
done
[root@localhost ~]# cat /boot/grub2/grub.cfg | grep cryptodisk
        insmod cryptodisk
        insmod cryptodisk
        
        
[root@localhost ~]# echo GRUB_ENABLE_CRYPTODISK=y >> /etc/default/grub
[root@localhost ~]# cat /etc/default/grub
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="rd.lvm.lv=fedora/swap rd.lvm.lv=fedora/root rd.luks.uuid=luks-cb85c654-7561-48a3-9806-f8bbceaf3973 rhgb quiet"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_CRYPTODISK=y
[root@localhost ~]# grub2-install /dev/sda
Installing for i386-pc platform.
Installation finished. No error reported.

```

* [The Practical Linux Hardening Guide](https://github.com/trimstray/the-practical-linux-hardening-guide/blob/master/README.md)

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

