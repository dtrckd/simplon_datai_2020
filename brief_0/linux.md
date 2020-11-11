
Explore the following ressources:

https://doc.ubuntu-fr.org/

https://www.archlinux.org/


Choose a distribution

* ubuntu: https://ubuntu.com/download/desktop
* debian desktop ("live images"): https://get.debian.org/images/
* debian netinst (testing): https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/
* debian netinst (testing with firmware): https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/
                                          https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/bullseye_di_alpha1/amd64/iso-cd/firmware-bullseye-DI-alpha1-amd64-netinst.iso


**On windows**
 To burn the iso download

    rufus.ie

(fat32, image DD)

Reduce the disk an eventually fragment it.

Change the boot bios setting
* to set secure boot mode off.
* (to boot windows, change boot mode to LEGACY)

**Issues**

In case of "invalide partition table" at boot. You may stilll be able to boot pressing some F* button.
Then check the partition table with fdisk. The / partition should be bootable or set as "hybrid MBR" with fdisk or gdisk (r, ...)

Voici les étapes à réaliser pour corriger cette erreur :

0. tapez `lsblk` et notez le numéro de la partition dont le point de montage (mountpoint) est `/`.
1. ouvrer un terminal et tapez les commandes suivantes
2. `sudo apt install os-prober -y`
3. `sudo os-prober`
4. `sudo update-grub`
5. `sudo gdisk /dev/sda`
6. ensuite, tapez `r`
7. puis `h`
8. ensuite rentrez le numéro de la partition que vous avez noté à l'étape 0.
9. ensuite répondez Oui (Y) aux questions qu'il vous pose (sauf si si il  pose la question `Unused partition space found. Use one to protect....`, là répondez Non (N)
10. enfin, à l'étape suivante  tapez `w` pour sauver et quitter.
11. ensuite redémarez, pour vérifier que l'erreur a bien disparu.

**Post instalation**

update source.list, update, upgrade, install base software (make, git, htop)

add user to sudoers

    su -
    usermod -aG sudo YOUR_USERNAME
    exit

setup bashrc and complete $PATH


