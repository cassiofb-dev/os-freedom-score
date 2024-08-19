<h1 align="center">
  OS Freedom Score
</h1>

<h4 align="center">A python script to classify installed packages licenses</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#usage">Usage</a> •
  <a href="#todo">Todo</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## About

A python script to classify installed packages licenses in the terminal using:

- [SPDX License List](https://spdx.org/licenses/)

## Usage

```sh
git clone https://github.com/cassiofb-dev/os-freedom-score

cd os-freedom-score

python -m src.main
```

## Todo

- [ ] Add suport for [Pacman](https://wiki.archlinux.org/title/Pacman)
  - [ ] Arch Linux
  - [x] CachyOS
- [ ] Linux Support
  - [ ] Add suport for [APK](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper)
    - [ ] Alpine Linux
    - [x] Chimera Linux
  - [ ] Add suport for [APT](https://wiki.debian.org/PackageManagement)
    - [ ] Debian
    - [ ] Ubuntu
    - [ ] Pop!_OS
    - [ ] Mint
  - [ ] Add suport for [DNF](https://docs.fedoraproject.org/en-US/fedora/latest/system-administrators-guide/package-management/DNF/)
    - [ ] Fedora
    - [ ] RHEL
- [ ] Add suport for [Flatpak](https://flathub.org/)
- [ ] Use GNU license list data
- [x] Improve the license classification method
  - [x] Handle non spdx compliant licenses
  - [x] Handle non spdx compliant softwares

## Screenshots

### APK - Chimera Linux

![APK - Chimera Linux](./data/chimera.png)

---

### Pacman - CachyOS

![Pacman - CachyOS](./data/cachyos.png)

## Credits

- [SPDX License List](https://spdx.org/licenses/)
- [GNU License List](https://www.gnu.org/licenses/license-list.html)

## License

MIT
