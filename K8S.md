# 場景標題：存取控制措施-隔離訪問權限
1. 場景概述：開發時，限制團隊間Pod訪問特定空間。
2. 細部規格：隔離開發和生產環境，避免不同環境互相干擾，隔離資源、控制存取權限，提升安全。
3. 具體內容：示範於Kubernetes中使用命名空間(Namespace)將應用程式隔離，避免不同應用程式互相干擾。例如，一個命名空間用於生產環境，另一個用於開發環境，避免開發程式碼意外地影響生產環境。
4. 測試作法：驗證命名空間隔離。

## install Homebrew
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew --version`

## install Kubernetes CLI
`brew install kubectl
kubectl version --client`

## install Docker -- to Docker website

## install minikube
`brew install minikube
minikube version`

### First Step
#### start the minikube
`minikube start --driver=docker
minikube status
kubectl get nodes`

### namespace 
#### kubectl create namespace
`kubectl create namespace dev-team
kubectl create namespace prod-team`

### create Nginx Pod
`kubectl run nginx-dev-app --image=nginx:latest -n dev-team
kubectl run nginx-prod-app --image=nginx:stable -n prod-team`

### switch to dev-Pod
`kubectl config set-context --current --namespace=dev-team`

### check Pod
`kubectl get pods -n dev-team
kubectl get pods -n prod-team`

### execu namespace
###kubectl exec -it nginx-prod-app -n dev-team -- bash # 失敗
###kubectl exec -it nginx-dev-app -n dev-team -- bash # 成功

`kubectl exec -it nginx-dev-app -n dev-team -- bash # 成功
kubectl exec -it nginx-prod-app -n dev-team -- bash # 失敗 (或輸出不符預期)`

#Ctrl + D → 結束 Bash 會話，回到本機終端
#Ctrl + C → 中斷當前命令，然後再輸入 exit
#Ctrl + Z → 將會話掛起，回到本機終端（不會關閉 Bash)

## other
### create YMAL
```nano resource-quota.yaml

#------------------------
apiVersion: v1
kind: ResourceQuota
metadata:
  name: cpu-memory-limit
  namespace: dev-team
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi ```

# apply
kubectl apply -f resource-quota.yaml
kubectl get resourcequota -n dev-team
kubectl create deployment nginx --image=nginx --namespace=dev-team







