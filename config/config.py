import os

# Channel IDs are not secrets
LEADERBOARD_CHANNEL_ID = 1082390207057379379
KNOWLEDGE_BASE_FORUM_CHANNEL_ID = 1080547370669981737

# Secrets
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
POSTGRES_PASSWORD = os.environ.get("PG_PASSWORD")

# Database
DB_PASSWORD = POSTGRES_PASSWORD
DB_HOST = "206.189.250.92"
DB_USER = "bot"
DB_NAME = "bot"
DB_PORT = 5432


# Task Settings
HOURS_BETWEEN_LEADERBOARD_REFRESH = 1
