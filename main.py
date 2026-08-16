import os
import requests

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def fetch_tech_news():
    """Fetch top tech headlines from HackerNews API."""
    try:
        top_ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        top_ids = requests.get(top_ids_url, timeout=10).json()[:5]
        
        news_items = []
        for index, item_id in enumerate(top_ids, 1):
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
            item = requests.get(item_url, timeout=10).json()
            title = item.get("title", "No Title")
            url = item.get("url", f"https://news.ycombinator.com/item?id={item_id}")
            news_items.append(f"{index}. [{title}]({url})")
            
        return "\n".join(news_items)
    except Exception as e:
        print(f"Error fetching news: {e}")
        return "• Could not retrieve news today."

def send_telegram_message(text):
    """Send formatted markdown message to Telegram."""
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing BOT_TOKEN or CHAT_ID environment variables.")
        return False
        
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    
    response = requests.post(url, json=payload, timeout=10)
    if response.status_code == 200:
        print("✅ Daily broadcast sent successfully!")
        return True
    else:
        print(f"❌ Failed to send message: {response.text}")
        return False

def main():
    print("🚀 Starting automated daily cloud task...")
    
    news_summary = fetch_tech_news()
    
    message = (
        "☀️ *Good Morning! Here is your Daily Automated Briefing*\n\n"
        "🔥 *Top Trending Tech Headlines:*\n"
        f"{news_summary}\n\n"
        "🤖 _Executed automatically_ [via GitHub](https://github.com/MrBoss002) _Actions Cloud Workflow_.\n\n"
        "*◈ Powered By: @MrBossTG ♥️*\n"
        "*◈ Developed By: @MrBossRobot ♥️*" 
    )
    
    send_telegram_message(message)

if __name__ == "__main__":
    main()
