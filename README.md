# Analog LLM Wiki — OTA 與 Transistor Sizing

本專案是一份**以人工擷取的 7 篇公開資料摘要為基礎**的可離線瀏覽 Wiki + 教學 HTML 簡報。

## 開啟網站
直接用瀏覽器開啟 `index.html`，或 GitHub Pages 部署後進入網站首頁。
- `index.html`：可搜尋 Wiki，顯示 7 筆來源摘要與出處
- `slides.html`：13 張教學投影片；鍵盤左右鍵、全螢幕、Wiki 對應、課後測驗
- `workflow.html`：圖/循環/檢查說明

## 生成與驗證
```bash
python3 scripts/build.py
python3 scripts/validate.py
```

## 資料結構
- `data/sources.json`：7 篇公開資料的**人工摘錄知識點**、URL、資料 ID
- `data/wiki.json`：7 個 Wiki 知識節點與來源對應
- `data/slides.json`：13 頁簡報與 Wiki ID 對應
- `docs/workflow.md`：loop / graph、反思與頁面映射
- `docs/validation-report.txt`：實際結構檢查結果

## 範圍聲明
沒有使用 LLM Wiki 專用 SaaS、全文 ingest 或向量嵌入；目前為**可檢索的結構化 Wiki prototype**，再由該 Wiki 產生 HTML。網站不需要外部 JS/CDN。規則式檢查只保證資料結構/引用的一致性，非自動語義正確性證明。

