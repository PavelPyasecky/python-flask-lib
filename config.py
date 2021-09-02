import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # SQLalchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DEBUG
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")

    # SECRET KEYS
    SECRET_KEY = os.getenv("SECRET_KEY")
    CSRF_ENABLED = os.getenv("CSRF_ENABLED")

    # Mail settings
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["pyasecky2012pavel@mail.ru"]

    # Telegram bot TOKEN
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
