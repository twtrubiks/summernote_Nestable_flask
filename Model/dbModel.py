from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Document(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(32))
    Content = db.Column(db.String(128))
    Parent = db.Column(db.Integer)
    Sequence = db.Column(db.Integer)

    def __init__(self,
                 Title,
                 Content,
                 Parent,
                 Sequence,
                 ):
        self.Title = Title
        self.Content = Content
        self.Parent = Parent
        self.Sequence = Sequence


if __name__ == '__main__':
    manager.run()
