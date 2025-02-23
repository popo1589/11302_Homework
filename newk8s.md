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
```apiVersion: v1
kind: Pod
metadata:
  name: nginx-secure
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 101  # 指定以 UID 101 執行（Nginx 非 root 用戶）
  containers:
  - name: nginx
    image: nginx
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
          - ALL
      readOnlyRootFilesystem: true
    ports:
      - containerPort: 80
    volumeMounts:
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
`kubectl apply -f nginx-secure.yaml`
`kubectl get pods`

# Test
`kubectl exec -it nginx-secure -- /bin/sh`
`id`
`touch /root/test`
`sudo su`
`exit`






