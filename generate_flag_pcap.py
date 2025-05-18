import os
import subprocess
import time
import threading
import signal  # 用於發送信號給子程序
from flask import Flask, request

# === Step 1: 建立 Flask 伺服器 ===
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    content = f.read()
    print("[*] 接收到檔案內容：", content)  # 詳細顯示收到的檔案內容
    return "File received!"

def run_flask():
    # 變更為監聽所有介面，支援 Docker port 映射
    app.run(host='0.0.0.0', port=8000)

# === Step 1.1: 產生 flag 檔案 ===
flag = "picoCTF{auto_generated_flag_123}"
with open("flag.txt", "w") as f:
    f.write(flag)
print("[*] 已建立 flag.txt")

# === Step 2: 啟動 Flask 伺服器於背景執行 ===
print("[*] 啟動 Flask HTTP 伺服器...")
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

time.sleep(1)  # 等待伺服器啟動完成

# === Step 3: 開始封包擷取 ===
pcap_file = "generated_flag.pcap"
print(f"[*] 開始封包擷取到 {pcap_file} ...")
tcpdump_proc = subprocess.Popen(
    ["tcpdump", "-i", "lo", "port", "8000", "-w", pcap_file],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(1)  # 等待 tcpdump 完全啟動

# === Step 4: 使用 curl 上傳含 flag 的檔案 ===
print("[*] 使用 curl 上傳 flag 檔案中...")
subprocess.run([
    "curl", "-F", "file=@flag.txt", "http://127.0.0.1:8000/upload"
])

# === Step 5: 停止封包擷取並優雅關閉 ===
time.sleep(1)  # 等待最後一筆封包輸出
print("[*] 停止 tcpdump，結束封包擷取...")
tcpdump_proc.send_signal(signal.SIGINT)
tcpdump_proc.wait()  # 等待 tcpdump 完全結束，確保 pcap 檔案完整

print("[*] 封包擷取已完成 ✅")
print(f"[*] 已輸出封包檔：{pcap_file}")
