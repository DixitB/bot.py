# Replace updater.start_polling() with:
PORT = int(os.environ.get('PORT', 10000))
updater.start_webhook(
    listen="0.0.0.0",
    port=PORT,
    url_path=os.getenv("TELEGRAM_TOKEN"),
    webhook_url=f"{os.getenv('WEBHOOK_URL')}/{os.getenv('TELEGRAM_TOKEN')}"
)
