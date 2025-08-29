````markdown
# 🎬 IMDb Telegram Bot

> **Note:** This project was created as a **Python & Selenium assignment**, which is why Selenium is used for web scraping IMDb.

A Telegram bot that fetches the **top 10 most popular movies and TV shows** from IMDb in real time.
Browse trending lists and all-time top-rated content, and view detailed descriptions, ratings, and runtimes — all within Telegram.

---

## ✨ Features

- **Interactive inline menu** for easy navigation
- **Movies**
    - 🔥 Most Popular Now (current top 10)
    - 🏆 Most Popular All Time
- **TV Shows**
    - 🔥 Most Popular Now
    - 🏆 Most Popular All Time
- **Details for each title**
    - Title
    - IMDb rating
    - Runtime
    - Description

---

## 🛠 Requirements

- Python 3.8+
- Telegram Bot Token (create via [@BotFather](https://t.me/botfather))
- Google Chrome installed
- ChromeDriver matching your Chrome version

Install dependencies with:

```bash
pip install -r requirements.txt
````

-----

## 📦 Installation

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/v4han/imdb_telegram_bot.git](https://github.com/v4han/imdb_telegram_bot.git)
    cd imdb_telegram_bot
    ```

2.  **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    # Linux/macOS
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Add your bot token**
    Create a `.env` file in the project root:

    ```bash
    TOKEN=your_telegram_bot_token_here
    ```

-----

## 🚀 Usage

Run the bot:

```bash
python bot.py
```

  * Start the bot in Telegram with `/start`
  * Navigate the menu to explore movies or TV shows
  * Click on a title to view detailed information

-----

## 📂 Project Structure

```
imdb_telegram_bot/
├── bot.py           # Telegram bot logic (menus, commands, callbacks)
├── parser.py        # Selenium scraping functions for IMDb
├── .env             # Environment variables (your bot token)
└── requirements.txt # Python dependencies
```

-----

## ⚠️ Notes

  * IMDb site layout may change; CSS selectors in `parser.py` may need updates.
  * Avoid spamming commands to prevent IMDb from blocking requests.

```
```
