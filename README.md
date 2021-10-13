[![pygame](https://img.shields.io/badge/pygame-yellow?style=for-the-badge&logo=Python&logoWidth=30&link=https://www.pygame.org/)](https://www.pygame.org/)

# Dot Blaster
#### Game for [Ludum Dare 49]



Shoot the dots with the appropriate blaster before they get too close!

![gameplay gif]

## To Play:
```
pip install dot-blaster
play_dot_blaster
```

## Dependencies


### MacOS
```
brew install portaudio
```

### Debian/Ubuntu/Rasberry Pi OS

```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y portaudio19-dev
```

### Fedora

```
sudo dnf upgrade --refresh
sudo dnf install -y portaudio-devel redhat-rpm-config
```

### Centos
```

# CentOS 8
sudo dnf upgrade --refresh
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

# CentOS 7
yum -y update
rpm -Uvh https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm

# CentOS 6
yum -y update
rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

sudo yum install -y portaudio portaudio-devel

```


[gameplay gif]: socials/gameplay.gif
[Ludum Dare 49]: https://ldjam.com/events/ludum-dare/49
