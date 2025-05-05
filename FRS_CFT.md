## Forensics - [藍隊監控] 從封包找檔案

## 1. [Abstract] 緣起摘要
1. Forensics 類型題目在 CTF 中，主要需具備針對網路封包、圖片、記憶體等數位資料，進行還原、分析與證據提取的能力。  
2. 本文以模擬藍隊在分析網路流量時，從 HTTP 封包中還原並分析已被提取與傳輸的檔案（flag.txt）。

## 2. [Relational] 相關資訊
### 2.1 題目弱點原理介紹
- 模擬一般企業網路流量中，駭客可能透過 HTTP 上傳、傳送檔案。  
- 藍隊需擷取封包流量，並分析其檔案內容。
  
### 2.2 解題使用工具介紹
- **tcpdump**：擷取 `lo` 介面上 8000 埠的 HTTP 封包並寫入 `.pcap`。  
- **curl**：發送 HTTP POST 請求，夾帶 `flag.txt`。  
- **Wireshark**：載入 `.pcap`，過濾 `http`，並 **Follow HTTP Stream** 取得隱藏的 flag。

## 3. [Procedure] 步驟紀錄
### 3.1 題目設計步驟
1. **撰寫自動化腳本**  
   - 產生 `flag.txt`，內容為 `picoCTF{auto_generated_flag_123}`  
   - 啟動 Flask 伺服器，監聽本機 8000 埠  
   - 背景執行 `tcpdump -i lo port 8000 -w generated_flag.pcap`  
   - 用 `curl -F "file=@flag.txt" http://127.0.0.1:8000/upload` 上傳檔案  
   - 停止 `tcpdump`，完成 `generated_flag.pcap` 檔案製作  
2. **腳本內容**
   - 模擬封包提取過程與輸出pcap檔。
```python
import os
import subprocess
import time
import threading
from flask import Flask, request

# === Step 1: 建立 Flask 伺服器 ===
# 建立 Flask 應用，用來模擬 HTTP 上傳
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # 從請求中取得上傳的檔案
    f = request.files['file']
    content = f.read()  # 讀取檔案內容
    print("[*] 接收到檔案內容：", content)  # 顯示在主控台（可驗證內容是否含有 flag）
    return "File received!"  # 回傳簡單訊息表示成功

# 定義一個函式來啟動 Flask（用執行緒背景執行）
def run_flask():
    app.run(host='127.0.0.1', port=8000)

# === Step 2: 產生 flag 檔案 ===
# 設定 flag 內容
flag = "picoCTF{auto_generated_flag_123}"

# 將 flag 寫入文字檔 flag.txt
with open("flag.txt", "w") as f:
    f.write(flag)

print("[*] 已建立 flag.txt")  # 顯示成功訊息

# === Step 3: 啟動 Flask 伺服器於背景 ===
print("[*] 啟動 Flask HTTP 伺服器...")

# 建立並啟動背景執行的 Flask 伺服器執行緒
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True  # 設定為背景執行
flask_thread.start()

time.sleep(1)  # 稍等伺服器啟動完成

# === Step 4: 開始擷取封包 ===
pcap_file = "generated_flag.pcap"  # 封包檔案名稱
print(f"[*] 開始封包擷取到 {pcap_file} ...")

# 使用 subprocess 執行 tcpdump，擷取指定介面與 port 的封包
tcpdump_proc = subprocess.Popen(
    ["sudo", "tcpdump", "-i", "lo", "port", "8000", "-w", pcap_file],  # 擷取本機介面 lo 上 8000 埠的封包
    stdout=subprocess.DEVNULL,   # 不顯示輸出
    stderr=subprocess.DEVNULL
)

time.sleep(1)  # 等待 tcpdump 確實啟動

# === Step 5: 使用 curl 上傳含 flag 的檔案 ===
print("[*] 使用 curl 上傳 flag 檔案中...")

# 呼叫 curl 發送 HTTP POST 請求，上傳剛剛的 flag.txt
subprocess.run([
    "curl", "-F", "file=@flag.txt", "http://127.0.0.1:8000/upload"
])

# === Step 6: 結束擷取 ===
time.sleep(1)  # 等待封包傳輸完成
tcpdump_proc.terminate()  # 停止封包擷取程式

# 顯示結果訊息
print("[*] 封包擷取已完成 ✅")
print(f"[*] 已輸出封包檔：{pcap_file}")
```

```bash
sudo python3 generate_flag_pcap.py

```

2. **檢查與驗證**  
   - 確認 `generated_flag.pcap` 存在  
   - 用 Wireshark 開啟 `.pcap`，過濾器輸入 `http`，Follow HTTP Stream，觀察 `picoCTF{…}`  

### 3.2 題目部署步驟
1. 確認環境已安裝：`python3`、`pip install flask`、`tcpdump`、`curl`。  
2. 執行  
   ```bash
   sudo python3 generate_flag_pcap.py
   ```  
   自動完成封包產出。

### 3.3 解題步驟
1. 在 Wireshark 中開啟 `generated_flag.pcap`。  
2. 過濾器輸入：  
   ```plaintext
   http
   ```  
   找出含有 `picoCTF{…}` 的 HTTP payload。  
3. 右鍵 → **Follow** → **HTTP Stream**，閱讀整段 POST 內容。  
4. 從 stream 中複製完整 flag，例如：  
   ```plaintext
   picoCTF{auto_generated_flag_123}
   ```

## 4. [Suggestion] 結論建議
1. 以藍隊角度，訓練快速從大量封包中，篩選出可疑 HTTP 流量，並提取其中傳輸的檔案。  
2. 實際競賽時注意事項：  
   - 當有大量封包時，善用「協定」或「IP」快速過濾。  
   - 使用 Wireshark **Follow Stream** 能快速定位 flag。  
   - 熟悉基礎命令：`tcpdump`、`curl`、Wireshark 過濾規則。  
