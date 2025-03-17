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




