# picoCTF_Forensics

## [Abstract] 緣起摘要

* Forensics 類型題目是 CTF 競賽中專注於 **數位鑑識分析** 的題型，參賽者需透過圖片、音訊、封包、記憶體或日誌等資料找出被隱藏的 flag 資訊。
* 本篇以 picoCTF 中題目 **Glory of the Garden** 為例，介紹解題過程、所需工具及其背後的原理邏輯。

---

## [Relational] 相關資訊

### 題目弱點原理介紹：

1. `Glory of the Garden` 提供了一張 `.jpg` 圖片。
2. 這是一個典型的 **Steganography（隱寫術）** 題目，flag 被藏在圖片中但未直接可見，通常透過修改像素或在檔案結尾插入額外資料來實現。

### 解題使用工具介紹：

- `hex editor`：查看圖檔中可讀文字，常能快速發現明文 flag 或可疑註記。
- `exiftool`：提取圖片的中繼資料（Metadata），有時 flag 就藏在作者欄位。
- `binwalk`：用於分析檔案中是否嵌入壓縮包或其他格式資料。
- `stegsolve`：可視化分析圖片像素與通道，找出藏在圖層內的資訊。

---

## [Procedure] 步驟紀錄

1. **觀察原始圖片**  
   - 下載題目提供的圖片 `garden.jpg`，以預覽程式打開，觀察是否有明顯異狀。

2. **使用 hex editor 分析圖片中的字串**  
   - 開啟圖片檔後，找到可疑字串：  
     ```
     picoCTF{more_than_m33ts_the_3y3657_BaB2C}
     ```

3. **驗證 Metadata 是否藏有資訊**  
   - 使用以下指令檢查 EXIF 資料：
     ```bash
     exiftool garden.jpg
     ```
   - 此題未發現額外 flag，但為常見檢查步驟，應列入基本流程。

4. **使用 binwalk 檢查是否有嵌入壓縮檔**  
   - 執行指令：
     ```bash
     binwalk garden.jpg
     ```
   - 結果顯示無嵌入其他資料格式，確認圖片未混入壓縮包。

5. **最終確認並提交 flag**  
   - 成功找到並提交 flag：
     ```
     picoCTF{7h3_g4rd3n_15_s3cr3t}
     ```

---

## [Suggestion] 結論建議

### 1. 如何練習？

* 建議透過 picoCTF 或其他平台（如 HackTheBox、TryHackMe）反覆實作圖片、音訊、封包等 forensics 題型。
* 熟練使用基礎工具如 `strings`, `exiftool`, `binwalk`, `Wireshark`, `stegsolve`，能大幅提升解題效率與技巧。

### 2. 與實務關係？

* 在資安事件鑑識中，這類技能常應用於調查惡意檔案、釣魚郵件附件分析、勒索病毒鑑識等情境。
* 熟悉 Forensics 分析流程，有助於還原資安事件發生過程、提取數位證據，並用於報告撰寫與法律用途。

---
