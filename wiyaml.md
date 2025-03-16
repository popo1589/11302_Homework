# install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# check docker installed
docker --version

# install and check minikube
brew install minikube
minikube version

# install and check Kubernetes CLI
brew install kubectl
kubectl version --client

# start minikebu
minikube start
kubectl cluster-info

# run

# pull imagine
docker pull vulfocus/libssh-cve_2018_10933

# run docker in 2 SSH container
docker run -d --name ssh-internet -p 2222:22 vulfocus/libssh-cve_2018_10933
docker run -d --name ssh-intranet -p 2223:22 vulfocus/libssh-cve_2018_10933

# check docker status
docker ps

