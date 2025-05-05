## Forensics - [藍隊監控] 從封包找檔案

## 1. [Abstract] 緣起摘要
* Forensics 類型題目在 CTF 中，主要需具備針對網路封包、圖片、記憶體等數位資料，進行還原、分析與證據提取的能力。
* 本文以模擬藍隊在分析網路流量時，從 HTTP 封包中提取一個被傳輸的檔案（flag.txt）。

## 2. [Relational] 相關資訊
### 題目弱點原理介紹：
* 模擬一般企業網路流量中，駭客可能透過 HTTP 上傳、傳送檔案。
* 藍隊需擷取封包流量，並分析其檔案內容。
  
### 解題使用工具介紹：
- **Wireshark**：流量分析工具，可從 HTTP 流量重組檔案。
- **tcpdump**：封包擷取工具，用於收集網路流量。
- **strings**：快速查看檔案中的可讀字串。

## 3. [Procedure] 步驟紀錄
### 題目設計步驟
#### 模擬封包傳送行為：
* 使用 curl 上傳一個小型文字檔 `flag.txt`。

##### AI提示詞
> 請模擬一段 HTTP 流量，其中夾帶一個檔案 flag.txt，內容為 picoCTF{forensics_flag_found}，並擷取成 pcap 檔案。

* 擷取流量存成封包檔（`capture_flag.pcap`）
  ```bash
  sudo tcpdump -i lo port 8000 -w capture_flag.pcap
  # 使用 tcpdump 擷取本機 lo 介面的 8000 埠流量，並儲存成封包檔（capture_flag.pcap）

  
#### 題目部署步驟
* 建立 Dockerfile 模擬小型 HTTP Server
```Dockerfile
FROM python:3                              # 使用官方 Python 3 映像作為基底
RUN pip install flask                      # 安裝 Flask 套件（用於建立 HTTP 伺服器）
COPY app.py /app/app.py                    # 將本地端的 app.py 複製到容器內部路徑
WORKDIR /app                               # 設定工作目錄為 /app
CMD ["python", "app.py"]                   # 啟動容器時執行 app.py（啟動 Flask 伺服器）

```

* 撰寫簡單 Flask 伺服器 (app.py)
```python
from flask import Flask, request           # 匯入 Flask 模組與 request 物件
app = Flask(__name__)                      # 建立一個 Flask 應用實例

@app.route('/upload', methods=['POST'])    # 定義 /upload 路由，接受 POST 方法（上傳用）
def upload_file():
    file = request.files['file']           # 從上傳的資料中取得檔案
    content = file.read()                  # 讀取檔案內容
    print(content)                         # 將內容印出（模擬處理）
    return "File received!"                # 回傳簡單確認訊息

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)     # 以 0.0.0.0 啟動伺服器，開啟 8000 埠

```

* Docker build and run
```bash
docker build -t http-upload-server .       # 建立映像檔，名稱為 http-upload-server
docker run -d -p 8000:8000 http-upload-server  # 在背景執行容器，並將主機的 8000 埠對應到容器的 8000 埠

```

* 測試上傳 flag.txt
```bash
echo "picoCTF{forensics_flag_found}" > flag.txt             # 建立測試檔案 flag.txt，內容為 picoCTF 的 flag
curl -F "file=@flag.txt" http://127.0.0.1:8000/upload        # 使用 curl 透過 POST 上傳檔案至本機 HTTP 伺服器

```

## 擷取流量
  ```bash
sudo tcpdump -i lo port 8000 -w capture_flag.pcap  # 擷取 8000 埠的網路封包，並輸出成 pcap 格式

```
> (打開另個 terminal 上傳後，停止 tcpdump，即可得到封包檔。)

### 解題步驟
#### 1. 用 Wireshark 開啟 capture_flag.pcap
#### 2. 依協定過濾器輸入：
 ```
http    # 在 Wireshark 中過濾所有 HTTP 封包
 ```
找到包含檔案上傳的封包。

#### 3. 使用 Wireshark 重組 HTTP 封包
   - 點選該封包 → 右鍵 -> Follow -> HTTP Stream
   - 儲存該 Stream 為 raw 資料。
#### 4. 從檔案中找出 flag
   - 開啟儲存檔案，用文字編輯器或 strings 查看。
   - 應該可以找到：
```
picoCTF{forensics_flag_found}   # 預期要從 raw 資料中看到的 flag 字串
```

## 4. [Suggestion] 結論建議
* 以藍隊角度，訓練快速從大量封包中，篩選出可疑 HTTP 流量，並提取其中傳輸的檔案。
* 實際競賽時注意事項：
- 當有大量封包時，善用「協定」或「IP」快速過濾。
- 分析 HTTP payload 時，留意 Content-Type 與傳輸內容異常。
- 盡量備熟 strings、Wireshark、tcpdump等基本指令。
