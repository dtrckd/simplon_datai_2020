# Installer et configurer Linux sur votre machine

compétences: c17, c11

tags: linux, windows, hardware

## Description

Vous devez installer un système d'exploitation Linux sur votre machine, depuis Windows et avec un clé USB, afin de vous approprier et de configurer votre environnement de travail.

## Contexte

1. Veille distribution -- 30min + prez 5min:
    * Ubuntu Unity
    * Debian Kde
    * Debian fce
    * Debian Gnome
    * (opt) Arch Linux
2. Télecharger l'iso de votre choix -- 10min
3. (opt) vérifier l'intégriter de l'iso -- 15min
4. graver l'iso sur une clé bootable (rufus.ie) () -- 10 min
5. installer linux en dual boot -- 1h
6. Configurer son systeme (apt, bashrc, man) (installer vlc, un éditeur atom/..., gimp, snap, discord, thunderbird) + veille -- 30 min
7. restorer la clé USB: fdisk+mkfs or gparted
8. Bash scripting:  1h
	* Télécharger toutes les ressources pdf présente dans l'url donnée à l'aide du logiciel `wget` et stocké dans un répertoire personnel. Executer plusieurs fois le script. Qu'observez vous ?
	* faire le même script python qui réalise la même tache, en se basant sur le script suivant: 
```
import urllib.request
with urllib.request.urlopen('http://www.perdu.com/') as f:
    html = f.read().decode('utf-8')

with open("my-file.html", "w") as f:
    f.write(html)
```
	 Lequel est le plus rapide ?

## Ressources

**Linux**
* doc ubuntu: https://doc.ubuntu-fr.org/
* doc arch: https://www.archlinux.org/
* tutoriel fr: https://lecrabeinfo.net/installer-linux-debian-le-guide-complet.html
* debian netinst (testing with firmware): https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/

**Ligne de commande et script bash**
* https://linux.developpez.com/ligne--de-commande/
* https://linux.goffinet.org/administration/scripts-shell/
* https://fr.wikibooks.org/wiki/Programmation_Bash

## livrable

Un système Linux opérationnel en dual boot.

## modalité pédagogique

Veille 20min par ilot. Élection d'un représentant pour restitution <5min.  
Travail individuel/collectif.
