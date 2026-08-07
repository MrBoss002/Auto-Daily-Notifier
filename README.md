<div align="center">

  <h1>⚡ Auto-Daily-Notifier</h1>
  <p>An automated cloud workflow powered by Python and GitHub Actions. Runs scheduled daily tasks without external server hosting.</p>

  <p>
    <a href="https://github.com/MrBoss002/Auto-Daily-Notifier/actions"><img src="https://img.shields.io/github/actions/workflow/status/MrBoss002/Auto-Daily-Notifier/daily-run.yml?branch=main&style=for-the-badge&logo=github&label=Workflow" alt="Workflow Status"/></a>
    <a href="https://github.com/MrBoss002/Auto-Daily-Notifier/stargazers"><img src="https://img.shields.io/github/stars/MrBoss002/Auto-Daily-Notifier?style=for-the-badge&color=0088CC" alt="Stars"/></a>
  </p>

</div>

---

## ✨ Overview

`Auto-Daily-Notifier` is an automated serverless script that executes on a schedule using **GitHub Actions**. It fetches real-time trending tech news and broadcasts formatted daily reports straight to Telegram.

- ⚙️ **Zero Hosting Cost:** Runs completely on GitHub's cloud runners.
- ⏰ **Scheduled CRON:** Triggered automatically every day at 06:00 UTC.
- 🕹️ **Manual Trigger:** Supports one-click execution from the GitHub Actions tab.

---

## ⚙️ Setup Instructions

### 1. Configure GitHub Secrets
Go to your repository settings on GitHub:
1. Navigate to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Add the following secrets:
   - `BOT_TOKEN`: Your Telegram Bot API token.
   - `CHAT_ID`: Your Telegram channel or user ID.

### 2. Manual Testing
You can manually run the workflow at any time:
1. Click the **Actions** tab on top of your GitHub repository.
2. Select **Daily Cloud Workflow**.
3. Click **Run workflow** > **Run workflow**.

---

<div align="center">

  <p>Developed with ❤️ by <b>Muhammad Riswan C</b> (<a href="https://github.com/MrBoss002">@MrBoss002</a>)</p>

</div>
