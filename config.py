import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'domislove'
    FLASK_CONFIG = os.environ.get('FLASK_CONFIG') or 'default'

    @staticmethod
    def init_app(app):
        app.logger.handlers = []
        # log to syslog
        import logging
        import sys
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        app.logger.addHandler(ch)
        pass


class DevelopmentConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        import logging
        from slack_log_handler import SlackLogHandler
        slackHandler = SlackLogHandler(Config.SLACK_LOG_URL)
        slackHandler.setLevel(logging.WARNING)
        app.logger.addHandler(slackHandler)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
