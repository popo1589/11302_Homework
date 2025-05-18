### 1. 清除舊檔與舊容器
```
rm -f generated_flag.pcap
docker ps -a | grep forensics_ctf | awk '{print $1}' | xargs -r docker rm -f
```

### 建置 Docker 映像
```
docker build -t forensics_image .
```

### 2. 再次執行容器（加上必要權限）
```
docker run --rm \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  -v "$(pwd)":/app:rw \
  forensics_image
```

### 確認輸出
```
ls -l flag.txt generated_flag.pcap
```
=== Orgin ===
## Dockerfile
```Dockerfile
# 使用官方 Python 3.9 slim 映像
FROM python:3.9-slim

# 2. 安裝 tcpdump、curl 與 bash，並用 pip 安裝 flask
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      tcpdump \
      curl \
      bash && \
    pip install flask && \
    rm -rf /var/lib/apt/lists/*

# 3. 設定工作目錄
WORKDIR /app

# 4. 複製自動化腳本到container
COPY generate_flag_pcap.py .

# 5. 開放 8000 埠（Flask 伺服器監聽）
EXPOSE 8000

# 6. 容器啟動時直接執行腳本
CMD ["python", "generate_flag_pcap.py"]
```

## generate_flag_pcap.py
```python
import os
import subprocess
import time
import threading
from flask import Flask, request

# === Step 1: 建立 Flask 伺服器 ===
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    content = f.read()
    print("[*] 接收到檔案內容：", content)
    return "File received!"

def run_flask():
    app.run(host='0.0.0.0', port=8000)
    #app.run(host='0.0.0.0', port=8000)


# === Step 2: 產生 flag 檔案 ===
flag = "picoCTF{auto_generated_flag_123}"
with open("flag.txt", "w") as f:
    f.write(flag)
print("[*] 已建立 flag.txt")

# === Step 3: 啟動 Flask 伺服器於背景 ===
print("[*] 啟動 Flask HTTP 伺服器")
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

time.sleep(1)  # 等待伺服器啟動

# === Step 4: 開始擷取封包 ===
pcap_file = "generated_flag.pcap"
print(f"[*] 開始封包擷取到 {pcap_file} ")
tcpdump_proc = subprocess.Popen(
    ["tcpdump", "-i", "any", "port", "8000", "-w", pcap_file],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(1)  # 等待 tcpdump 啟動

# === Step 5: 使用 curl 上傳含 flag 的檔案 ===
print("[*] 使用 curl 上傳 flag 檔案中")
subprocess.run([
    "curl", "-F", "file=@flag.txt", "http://127.0.0.1:8000/upload"
])

# === Step 6: 結束擷取 ===
time.sleep(1)
tcpdump_proc.terminate()
print("[*] 封包擷取已完成 ✅")
print(f"[*] 已輸出封包檔：{pcap_file}")
```












