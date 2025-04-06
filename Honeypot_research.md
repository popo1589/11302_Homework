# 資安實務軟體Honeypot之研究

## [Abstract] 緣起摘要

* Honeypot（蜜罐）是一種主動資安防禦技術，刻意暴露虛假的系統或服務，引誘攻擊者進行攻擊，以達到誘捕及分析的目的。
* 當駭客對此類系統攻擊時，Honeypot 能即時記錄攻擊手法、工具及行為模式，協助防守方有效地防範與偵測攻擊。
* 本文件以開源蜜罐工具 Cowrie 為例，透過 Docker 容器技術快速佈署並展示其基本功能及使用方式。

## [Relational] 相關資訊

1. Honeypot 主要功能目的包括：
- 誘捕並誤導攻擊者，避免真實系統受攻擊。
- 收集攻擊行為與模式資訊，提升資安防禦能力。
- 透過分析攻擊資料，提前識別並防範新興的資安威脅。

2. Honeypot 常見工具：
- Cowrie：SSH/Telnet 蜜罐，記錄詳細指令。
- Dionaea：多協定蜜罐，支援 SMB、FTP 等。
- Glastopf：網頁應用程式蜜罐，針對 SQL Injection 等攻擊。
- T-Pot：整合多種蜜罐功能的綜合型平台。

3. Honeypot Cowrie工具的特點包括：
- **開源且普及**：為開源軟體，具良好文件、活躍社群及豐富資源。
- **仿真性佳**：具高仿真能力，能模擬 SSH 與 Telnet 等常見服務，誘捕駭客展開攻擊。
- **部署簡便性**：透過 Docker 等容器化技術，可快速完成部署。
- **資源消耗低**：Cowrie 以 Python 開發，運行所需資源較少。

## [Procedure] 步驟紀錄

### 1. Docker 實際運行

本次採用 Cowrie 作為 Honeypot 示範工具，透過 Docker 容器部署：

```bash
docker pull cowrie/cowrie
docker run -d --name honeypot -p 2222:2222 cowrie/cowrie
```

以上指令將啟動 Cowrie 蜜罐容器，並監聽於主機 2222 埠。

### 2. 操作方式

- 啟動完成後，可透過 SSH 工具連線到 Docker 主機的 2222 埠，即可模擬駭客攻擊行為。
- 容器內 Cowrie 會自動記錄所有連線嘗試、使用指令、攻擊行為，並存放於日誌檔案中，供後續分析。

示範連線指令：
```bash
ssh root@<Docker主機IP> -p 2222
```

### 3. 攻擊行為記錄與查看

- 登入容器查看攻擊日誌：
```bash
docker exec -it honeypot /bin/sh
cat var/log/cowrie/cowrie.log
```

- 可從日誌中了解攻擊者試圖使用的指令與攻擊路徑，協助進一步分析與防範。

## [Suggestion] 結論建議

* 教育訓練與實務教學，增進資安知識與能力。
* 實際環境部署，主動監測攻擊並提前發現安全漏洞。
* 配合其他資安工具（如 ELK）進行深入資料分析，強化組織資安防禦。

