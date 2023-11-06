# app/config.py
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://ossute5_master2:ISJ_datascience+2023@192.145.239.38/ossute5_pointsinterest"
    SQLALCHEMY_POOL_RECYCLE = 3  # Durée de vie de la connexion en secondes
    SQLALCHEMY_POOL_TIMEOUT = 3600
