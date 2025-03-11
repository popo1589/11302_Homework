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
  * [Metaspoilt with Docker](https://github.com/popo1589/11302_Homework/blob/main/Metaspoilt%20with%20Docker.md)

# [Suggestion]結論建議
  * 透過Docker快速部署Metasploit環境，並利用Samba漏洞取得遠端控制權限。滲透測試的基本流程，包括：偵查、漏洞分析與攻擊。
  * 安全防護：避免使用舊版的服務，並定期更新系統。
  * 防禦措施：設定防火牆規則，阻擋來自外部的445連線，並監控異常行為。
  * 進一步學習：嘗試使用Metasploit測試其他漏洞，提升滲透測試技能。

