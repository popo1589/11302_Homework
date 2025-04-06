# SSH + FTP attack
## Debug can,t pull image
```yaml
containers:
  - name: libssh1
    image: cyberacademylabs/metasploitable2
    imagePullPolicy: Never  # 不從網路拉取映像檔
```

## Check all namespaces ip
kubectl get namespaces

kubectl get pods --all-namespaces -o wide


## Test k8s SSH service
kubectl get svc -n namespace-double-nodes


## Metaspoilt 2
### access into Metaspoilt 2 container
docker exec -it metasploitable2 bash
ip a
ifconfig

## create file
```
echo '#!/bin/bash
logger -t system_status "$(date '+%Y-%m-%d %H:%M:%S') System Check OK" &&
echo "Log written successfully." || echo "Log write failed."' > /syslogger.sh
```

## Kali
ssh msfadmin@172.xx.x.x

## Scan host live
telnet 192.0.0.1 80
nc -vz 192.0.0.1 80
nmap -Pn -p 80 192.0.0.1





