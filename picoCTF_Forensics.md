# picoCTF_Forensics

## [Abstract] 緣起摘要

* Forensics 類型題目是 CTF 競賽中專注於 **數位鑑識分析** 的題型，參賽者需透過圖片、音訊、封包、記憶體或日誌等資料找出被隱藏的 flag 資訊。
* 本篇以 picoCTF 中題目 **Glory of the Garden** 為例，介紹解題過程、所需工具及背後原理邏輯。

---

## [Relational] 相關資訊

### 題目弱點原理介紹：

1. `Glory of the Garden` 提供了一張 `.jpg` 圖片。
2. 這是典型的 **Steganography（隱寫術）** 題目，flag 被藏在圖片中但未直接可見，通常透過修改像素或在檔案結尾插入額外資料來實現。
3. 題目提供Hints：What is a hex editor?

### 解題使用工具介紹：

- `hex editor`：查看圖檔中可讀文字，常能快速發現明文 flag 或可疑註記。

---

## [Procedure] 步驟紀錄

1. **觀察原始圖片**  
   - 下載題目提供的圖片 `garden.jpg`，以預覽程式打開，觀察是否有明顯異狀。
   - <img src="https://github.com/popo1589/11302_Homework/blob/main/garden.jpg" width="50%">

2. **使用 hex editor 分析圖片中的字串**  
   - 開啟圖片檔後，找到可疑字串：  
     ```
     picoCTF{more_than_m33ts_the_3y3657_BaB2C}
     ```

3. **確認並提交 flag**  
   - 成功找到並提交 flag：
     ```
     picoCTF{more_than_m33ts_the_3y3657_BaB2C}
     ```
---

## [Suggestion] 結論建議

### 1. 如何練習？

* 可透過 picoCTF 或其他平台（如 HackTheBox、TryHackMe）反覆實作 forensics 題型。
* 熟練使用鑑識基礎工具，如 `strings`, `exiftool`, `binwalk`, `Wireshark`, `stegsolve`，能提升解題效率與技巧。

### 2. 與實務關係？

* 在資安事件鑑識中，這類技能常應用於調查惡意檔案、釣魚郵件附件分析、勒索病毒鑑識等情境。
* 熟悉 Forensics 分析流程，有助於還原資安事件發生過程、提取數位證據。

---
