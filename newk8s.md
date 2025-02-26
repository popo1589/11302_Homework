# 場景標題：存取控制措施-限制提升root權限
1. 場景概述：限制容器權限，防止惡意程式獲取root權限。
2. 細部規格：使用Kubernetes來部署一個安全的Nginx伺服器，並確保它不能以root權限運行，以防止攻擊者利用漏洞獲得系統控制權。
3. 具體作法：部署Nginx安全性規則。
4. 測試作法：測試容器安全性。

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

## First Step
### start the Docker
open the docker, and keep it running.

## start the Kubernetes
`kubectl version --client`

## create YAML file
`nano nginx-secure.yaml`

# write content
```yaml
apiVersion: v1  # 指定 Kubernetes API 版本
kind: Pod  # 創建一個 Pod
metadata:
  name: nginx-secure  # Pod 的名稱
spec:
  securityContext:
    runAsNonRoot: true  # 強制使用非 root 身份執行
    runAsUser: 101  # 指定以 UID 101 執行（Nginx 非 root 用戶）
  containers:
  - name: nginx
    image: nginx
    securityContext:
      allowPrivilegeEscalation: false  # 禁止權限提升
      capabilities:
        drop:
          - ALL  # 移除所有權限
      readOnlyRootFilesystem: true  # 設定唯讀檔案系統
    ports:
      - containerPort: 80  # 開放 80 端口
    volumeMounts:  # 提供可寫入的快取空間
      - mountPath: /var/cache/nginx
        name: cache-volume
      - mountPath: /var/run
        name: run-volume
  volumes:
    - name: cache-volume
      emptyDir: {}
    - name: run-volume
      emptyDir: {}
```

# Deployment Nginx
#kubectl delete pod nginx-secure

### Create Nginx Container with safety rules
`kubectl apply -f nginx-secure.yaml`

### Test pods
`kubectl get pods`

# Test the Container's safty
### access to container
`kubectl exec -it nginx-secure -- /bin/sh`

### check current user
`id`

### check whether can create new file
`touch /root/test`

### try to get root
`sudo su`

### exit to container
`exit`






