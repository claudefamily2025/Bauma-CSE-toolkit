bauma-cse-toolkit/
├── 📖 README.md                          # 專案說明（首頁）
├── 🔧 requirements.txt                   # Python套件清單
├── 🚫 .gitignore                        # 排除敏感文件
├── 🔐 .env.example                      # API金鑰模板
│
├── 📊 data/
│   ├── input/                           # Sunny的原始檔案
│   │   └── sample_exhibitors.xlsx      # 小樣本（不含敏感資料）
│   └── cache/                           # 暫存區（不進版控）
│
├── 📈 outputs/
│   ├── runs/                            # 每次執行的結果
│   └── samples/                         # 範例輸出展示
│
├── 📝 logs/
│   └── processing.log                   # 執行記錄（不進版控）
│
├── 💻 src/
│   └── bauma_cse/                       # 核心程式碼
│       ├── __init__.py                  # Python模組標記
│       ├── config.py                    # 設定管理
│       ├── cse_search.py                # Google搜尋核心
│       ├── gemini_ai.py                 # AI摘要生成
│       ├── data_processor.py            # 資料處理
│       └── main_runner.py               # 主執行流程
│
├── 🖥️ cli/
│   └── bauma_cli.py                     # 命令列介面
│
├── 🧪 tests/
│   ├── test_cse_search.py              # 搜尋功能測試
│   ├── test_data_processor.py          # 資料處理測試
│   └── sample_data/                    # 測試用小數據
│
├── 📚 docs/
│   ├── user_guide.md                   # 使用手冊（給Sunny/寶拉）
│   ├── api_setup.md                    # API設定教學
│   ├── troubleshooting.md              # 問題排解
│   └── changelog.md                    # 版本更新記錄
│
└── 🤝 collaboration/
    ├── chat_to_claude_handoff.md       # Chat老師→Claude家族交接
    ├── quality_standards.md            # 品質標準
    └── cost_monitoring.md              # 成本控制指南
