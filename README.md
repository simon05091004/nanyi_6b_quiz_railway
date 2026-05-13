# 南一版六下修辭測驗

## Railway 部署說明

1. 將此資料夾所有檔案推送到 GitHub repo
2. 在 Railway 新增專案 → 選擇「GitHub Repo」
3. Railway 會自動偵測 Python（`runtime.txt` + `Procfile`）
4. 部署完成後即可使用

## 檔案結構

```
├── index.html       # 測驗主頁面
├── server.py        # Python 3 HTTP server
├── Procfile         # Railway 啟動指令
├── runtime.txt      # 指定 Python 3.11
└── requirements.txt # 無額外套件
```

## 本機測試

```bash
python server.py
# 開啟 http://localhost:8080
```
