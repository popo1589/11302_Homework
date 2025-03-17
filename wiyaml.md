## Install homebrew
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

## Check docker installed and check status
`docker --version`

`docker ps`

## Install and check minikube
`brew install minikube`

`minikube version`

## Install and check Kubernetes CLI
`brew install kubectl`

`kubectl version --client`

## Start minikebu
`minikube start`

`kubectl cluster-info`

## Deployment YAML file
`kubectl apply -f <your_yaml_file.yaml>`

## pull imagine
`docker pull vulfocus/libssh-cve_2018_10933`

## run docker in 2 SSH container
`docker run -d --name ssh-internet -p 2222:22 vulfocus/libssh-cve_2018_10933`

`docker run -d --name ssh-intranet -p 2223:22 vulfocus/libssh-cve_2018_10933`

## Check kubernetes objects and SSH service
`kubectl get all -n namespace-double-ssh`

kubectl port-forward service/service-internet 10022:22 -n namespace-double-ssh --address 0.0.0.0

`minikube service service-internet -n namespace-double-ssh --url`



```yaml
# Debug
## Enable ssh-rsa
nano ~/.ssh/config


Host localhost
    HostKeyAlgorithms +ssh-rsa
    PubkeyAcceptedKeyTypes +ssh-rsa
```



## Debug
✅ 2️⃣ 確保 Kali 可以連線到 macOS
由於 Kali 是 VM（虛擬機），它的網路模式可能影響到連線能力。

🔹 方法 1：如果使用「橋接模式」（Bridged Adapter，推薦）
在 VirtualBox 或 VMware 選擇 Kali VM
進入「設定」>「網路」
將「介面 1」的「連線方式」改為 橋接介面（Bridged Adapter）
啟動 Kali，查看 IP 地址：
ip a
你應該會看到一個與 macOS 相同區網的 IP（例如 192.168.1.x）。
從 Kali 連線到 macOS：
ssh -p 10022 root@<macOS的IP>
ifconfig | grep "inet "
找到 macOS 在區網內的 IP，例如 192.168.1.100，然後在 Kali 上連線：
ssh -p 10022 root@192.168.1.100

確保 Kubernetes 內的 SSH 服務正常運行






