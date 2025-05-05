# Forensics 題目：從封包中找出 Flag

## 題目說明

你已經拿到一個名為 `find_the_flag.pcap` 的網路封包擷取檔，這份封包中包含一次 HTTP POST 上傳動作：上傳的檔案中藏有一個 picoCTF 格式的 flag。

**flag 格式**  
```
picoCTF{xxxxxxxxxxxxxxxx}
```

---

## 任務目標

1. 使用 **Wireshark** 開啟 `find_the_flag.pcap`。  
2. 在顯示過濾器 (Display Filter) 中輸入：
   ```
   http
   ```
   過濾出 HTTP 流量。  
3. 在篩選後的封包中，尋找包含 `picoCTF` 字樣的封包。  
4. 右鍵點選該封包 → **Follow** → **HTTP Stream**，查看完整的 POST 資料。  
5. 從 HTTP Stream 的內容中複製出完整的 flag，並將它作為答案回報。

---

## 工具提示

- **Wireshark**：開啟並分析 `.pcap` 檔。  
- 可選：使用 CLI 工具 `strings` 或 `tshark -r find_the_flag.pcap -Y http` 來輔助排查（非必須）。

---

## 交付格式

請以純文字回報你找到的 flag，例如：

```
picoCTF{your_found_flag_here}
```

---

## 建議流程

1. 打開 Wireshark，選擇 `find_the_flag.pcap`。  
2. 在過濾器輸入欄鍵入 `http`，按下 Enter。  
3. 找到出現 `POST /upload` (或類似) 的封包。  
4. 右鍵 → **Follow** → **HTTP Stream**。  
5. 在彈出的視窗中，找到 `picoCTF{...}`，複製並回報。

祝你順利完成任務！  
