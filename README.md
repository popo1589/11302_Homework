# 11302 Homework
## This is for professor's assignments' workspace.

## start Docker
`minikube start --driver=docker`

## Depolyment nginx
```kubectl create deployment nginx --image=nginx
kubectl get deployments  #check

kubectl expose deployment nginx --type=LoadBalancer --port=80  #將 Nginx 部署暴露為一個 LoadBalancer 類型的服務
kubectl get services  #check

minikube service nginx --url



