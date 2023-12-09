#!/bin/sh

sudo apt -y update
sudo apt install wget -y
sudo apt install python3 -y
sudo apt install python3-pip -y

sudo wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
sudo tar -C /usr/local/ -xzf go1.21.5.linux-amd64.tar.gz
rm go1.21.5.linux-amd64.tar.gz
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
source ~/.bashrc

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/hahwul/dalfox/v2@latest

sudo cp ~/go/bin/subfinder /bin/
sudo cp ~/go/bin/httpx /bin/
sudo cp ~/go/bin/katana /bin/
sudo cp ~/go/bin/dalfox /bin/

pip install requests