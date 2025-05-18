# 使用官方 Python 3.9 slim 映像
FROM python:3.9-slim

# 安裝系統套件：tcpdump（擷取封包）、curl、及其他必要套件
RUN apt-get update && \
    apt-get install -y --no-install-recommends tcpdump curl && \
    rm -rf /var/lib/apt/lists/*

# 安裝 Python 套件：Flask
RUN pip install --no-cache-dir flask

# 建立工作目錄
WORKDIR /app

# 複製自動化腳本到容器中
COPY generate_flag_pcap.py .

# 暴露 8000 埠供 Flask 使用
EXPOSE 8000

# 預設執行指令：運行自動化封包產生腳本
CMD ["python", "generate_flag_pcap.py"]
