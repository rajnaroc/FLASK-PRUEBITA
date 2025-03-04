import os

class Config:
    SECRET_KEY= os.getenv('SECRET_KEY')

class developmentConfig(Config):
    DEBUF=True
    MYSQL_HOST= os.getenv('MYSQL_HOST')
    MYSQL_USER= os.getenv('MYSQL_USER')
    MYSQL_PASSWORD= os.getenv('MYSQL_PASSWORD')
    MYSQL_DB= os.getenv('MYSQL_DB')

class ProductionConfig(Config):
    DEBUF=False
    MYSQL_HOST= os.getenv('MYSQL_HOST')
    MYSQL_USER= os.getenv('MYSQL_USER')
    MYSQL_PASSWORD= os.getenv('MYSQL_PASSWORD')
    MYSQL_DB= os.getenv('MYSQL_DB')

config = {
    'dev' : developmentConfig,
    'product' : ProductionConfig
}