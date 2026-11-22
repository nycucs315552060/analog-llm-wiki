# 作業繳交內容（將網址及個人資料填入後繳交）

**繳交標題：** [學校] [學號] [系級] [姓名] Analog Circuit Design — OTA 與 Transistor Sizing

## 1. LLM Wiki 主題與簡短介紹
我的主題是 **Analog Circuit Design：從 OTA 到 Transistor Sizing**。這份 Wiki 針對沒有類比電路背景的讀者，整理了 OTA 的原理、MOSFET 小訊號 gm/ro、Two-stage OTA、Gain/GBW/Phase Margin，以及 Netlist、PDK、SPICE 和 sizing 設計流程。我先討論教學範圍和章節順序，再擷取 7 篇公開技術文件的重點，組成 7 個具有來源追溯關係的 Wiki 節點。

## 2. LLM Wiki 連結或成果
- Wiki 網址：[部署後填入 GitHub Pages 首頁網址]
- Wiki 成果：`index.html`，可搜尋知識節點、查看詳細解釋、注意事項和原始來源網址。
- 來源資料：`data/sources.json`，7 篇公開技術資料摘要。

## 3. 教學 HTML 簡報連結
- HTML 簡報網址：[部署後填入 GitHub Pages 網址]/slides.html
- 簡報共 13 頁，支援上/下一頁、方向鍵、全螢幕、Wiki 引用查詢和觀念測驗。

## 4. Loop / Graph 設計
流程：**蒐集資料 → Ingest 來源摘要 → 建立 Wiki 節點 → 驗證來源與內容 → 檢索 Wiki → 規劃教學順序 → 產生 HTML 簡報 → 檢查及修正**。

- **Loop A（Source）**：來源 ID、URL、標題和摘要不完整時回到整理資料。
- **Loop B（Wiki）**：Wiki 未引用合法來源，或概念有不明確的地方，回到 Wiki 節點修正。
- **Loop C（Slides）**：簡報頁沒有對應 Wiki ID 或內容過度簡化時，退回 Wiki/簡報重新產生。

這樣設計可以確保所有簡報內容都能追溯到知識節點及公開來源，也避免錯誤在輸出端重複出現。

## 5. 一次實際執行結果與檢查紀錄
以 `python3 scripts/build.py` 將 Wiki 節點及投影片資料產生成三份 HTML，接著執行 `python3 scripts/validate.py`。

測試結果：**14 / 14 項結構檢查通過**，包括：7 篇資料（超過最低 5 篇要求）、7 個 Wiki 節點、13 頁簡報、來源 ID 完整性、Wiki/簡報引用完整性及 HTML 檔案存在。檢查詳情見 `docs/validation-report.txt`。另外已透過 `node --check` 確認 Wiki 與投影片的 JavaScript 語法通過。

## 6. 反思與 Workflow 調整
**最容易出錯的節點是 Wiki → Slides 的內容映射**：在濃縮技術概念時，可能漏掉引用或忽略公式的適用條件，例如將簡化的 `gm × Rout` 直接當作整個 OTA 的精確增益。

**我將檢查往前移到「Wiki 整理完成、簡報生成之前」**：每個 Wiki 節點都加上來源 ID 和「易混淆處」，再用程式檢查所有 Wiki 來源與投影片連結是否合法。

**Workflow 因此改為具有回退分支的 graph**：若來源不齊全則重整來源；Wiki 有問題則先修 Wiki；投影片有問題則回到對應節點修改，而不是等到整份 HTML 完成才檢查。這能減少反覆修改的範圍。

---

**實作範圍說明：** 這份作業採用人工擷取公開來源摘要的結構化 Wiki 原型與規則式 HTML 產生/檢查，未連接 LLM API 或第三方 LLM Wiki 服務，也沒有將原始全文放入向量資料庫。此點應在老師要求特定 LLM Wiki 工具時據實說明。
