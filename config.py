from pathlib import Path

basedir = Path(__file__).parent.absolute()

class Config:
    SECRET_KEY = 'lkjsdfon'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir.joinpath("app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    