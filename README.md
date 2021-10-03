# Ludum Dare 49 Submission
This time we're using pygame!


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
