
## wkhtmltopdf install
### Reference

- https://computingforgeeks.com/install-wkhtmltopdf-on-ubuntu-debian-linux/
- https://python-bloggers.com/2022/06/convert-html-to-pdf-using-python/



Install wkhtmltopdf on Ubuntu / Debian Linux
Download the latest precompiled binary from the releases page. The latest release as of this article update is 0.12.6.

Install wget utility package

sudo apt update
sudo apt install wget


Install wkhtmltopdf on Ubuntu 20.04/18.04
Ubuntu 22.04/20.04:

```

wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
sudo apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb

```

Ubuntu 18.04:

```

wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo apt install ./wkhtmltox_0.12.6-1.bionic_amd64.deb

```

Ubuntu 16.04:

```

wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.xenial_amd64.deb
sudo apt install ./wkhtmltox_0.12.6-1.xenial_amd64.deb

```


```
https://pypi.org/project/pdfkit/

pip install pdfkit
```
