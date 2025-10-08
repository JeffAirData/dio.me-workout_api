from workoutapi.configs.settings import settings

print(f"DB_URL original: {settings.DB_URL}")

# Convert async URL to sync URL
sync_db_url = settings.DB_URL.replace("postgresql+asyncpg://", "postgresql+psycopg2://")
print(f"DB_URL convertida: {sync_db_url}")