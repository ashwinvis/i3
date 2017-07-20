# ashwinvis/i3 

## Courtesy

 - [bookercodes/dotfiles](https://github.com/bookercodes/dotfiles)

 - [electro7/dotfiles](https://github.com/electro7/dotfiles)

 - [marguerite/linux-bing-wallpaper](https://github.com/marguerite/linux-bing-wallpaper)

## i3

![lemonbar full](https://av.mooo.info/nextcloud/index.php/s/8T6v2dwpFa61AW3/download)

Lemonbar config files and help [here](https://github.com/ashwinvis/i3/tree/master/.i3/lemonbar)

### Installation

#### Arch Linux

* Install Arch Linux (without X desktop).

* Install required packages:

    ```sh
    # pacman -S i3 rxvt-unicode sddm xorg-apps
    # pacman -S git
    # pacman -S conky curl alsa-utils
    # pacman -S mpd mpc
    # pacman -S notification-daemon xinput
    # pacman -S perl-anyevent-i3 awesome-terminal-fonts
    ```

* Delete all files in $HOME/.i3 and clone git:

    ```sh
    $ git clone https://github.com/ashwinvis/i3.git ~/.i3
    ```

* Install pacaur / use makepkg

* Install lemonbar:

    ```sh
    $ pacaur -S lemonbar-xft-git
    ```


#### Debian jessie 8.5:
*Installation instructions by @electro7: May be incomplete*

* Install debian base (without X desktop).

* Install required packages:

    ```sh
    $ apt-get install i3 rxvt-unicode-256color lightdm x11-xserver-utils
    $ apt-get install git vim
    $ apt-get install conky curl alsa-utils
    $ apt-get install mpd mpc ncmpcpp
    $ apt-get install notification-daemon xinput

    ```

* Delete all files in $HOME and clone git:

    ```sh
    $ git clone https://github.com/electro7/dotfiles.git .
    ```

* Install vim plugins:

    ```sh
    $ git clone https://github.com/gmarik/Vundle.git ~/.vim/bundle/Vundle.vim
    $ vim +PluginInstall +qall
    ```

* Install lemonbar:

    ```sh
    $ mkdir tmp; cd tmp
    $ git clone  https://github.com/LemonBoy/bar.git
    $ apt-get install build-essential checkinstall
    $ apt-get install libxcb1-dev libxcb-xinerama0-dev libxcb-randr0-dev
    $ make
    $ checkinstall -D make install
    ```

* Restart lightdm.    

