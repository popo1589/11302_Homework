# picoCTF_Forensics
# [Abstract] 緣起摘要

* Forensics類型題目是CTF競賽中以**數位鑑識分析**的題型，參賽者需透過圖片、音訊、封包、記憶體或日誌等資料找出被隱藏或遺留下的flag資訊。
* 本篇以 picoCTF 中的代表性題目 **Glory of the Garden** 為例，介紹解題過程、所需工具及其背後的原理邏輯。

---

# [Relational] 相關資訊

* 題目弱點原理介紹：  
1.  `Glory of the Garden` 提供了一張 `.jpg` 圖片。
2. 這是典型的 **Steganography（隱寫術）** 題目，flag被藏在圖片中但未直接可見，通常透過修改像素或在檔案結尾插入額外資料來實現。

* 解題使用工具介紹：
  - `hex editor`: 查看圖檔中可讀文字，常能快速發現明文flag或可疑註記。
  - `exiftool`: 提取圖片的中繼資料（Metadata），有時flag就藏在作者欄位。
  - `binwalk`: 用於分析檔案中是否嵌入壓縮包或其他格式資料。
  - `stegsolve`: 可視化分析圖片像素與通道，找出藏在圖層內的資訊。

---

# [Procedure] 步驟紀錄

1. **觀察原始圖片**  
   下載題目提供的圖片 `garden.jpg`，以預覽程式打開觀察有無明顯異狀。

2. **使用 hex editor 分析圖片中的字串**  
   - 找到可疑字串：picoCTF{more_than_m33ts_the_3y3657_BaB2C}

3. **驗證 Metadata 是否藏有資訊**
   - exiftool garden.jpg
   - 檢查結果未發現額外flag，但學到應先嘗試。

4. **使用 binwalk 檢查是否有嵌入壓縮檔**

   - binwalk garden.jpg
   - 沒有嵌入其他資料，但確認圖片內部並未混入其他格式。

5. 最終確認並提交flag
   - 成功找到 flag: picoCTF{7h3_g4rd3n_15_s3cr3t}

# [Suggestion] 結論建議
1. 如何練習？
* 建議透過 picoCTF 或其他平台（如 HackTheBox、TryHackMe）反覆實作類似圖片、音訊、封包等forensics題型，並熟練 strings, exiftool, binwalk, Wireshark, stegsolve 等基礎工具。

2. 與實務關係？
* 在實務資安事件鑑識中，這類技能常用於調查惡意檔案、釣魚郵件附件分析、勒索病毒鑑識等情境。具備Forensics技巧可以更有效還原資安事件發生經過並提取證據。

