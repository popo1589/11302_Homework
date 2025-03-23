# SSH + FTP attack
## Debug can,t pull image
```yaml
containers:
  - name: libssh1
    image: cyberacademylabs/metasploitable2
    imagePullPolicy: Never  # 不從網路拉取映像檔
```


## Metaspoilt 2
docker exec -it metasploitable2 bash
ip a
ifconfig
