agaro-campus-bot/
├── .env                    # Environment variables (BOT_TOKEN)
├── .gitignore              # Ignore .env, __pycache__, etc.
├── README.md               # Project description, setup instructions
├── requirements.txt        # Dependencies (python-telegram-bot)
├── run.py                  # Entry point to start the bot
├── bot/
│   ├── __init__.py
│   ├── main.py             # Application builder and main loop
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── start.py        # /start command handler
│   │   ├── language.py     # Language selection handler
│   │   ├── amharic.py      # All Amharic menu logic
│   │   └── oromiffa.py     # All Oromiffa menu logic
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── menu.py         # ReplyKeyboardMarkup definitions
│   │   └── language.py     # Language selection keyboard
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py       # Logging configuration
│   └── config.py           # Load token from .env
└── tests/                  # (Optional) unit tests
    └── ...
