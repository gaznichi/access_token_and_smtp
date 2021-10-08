import peewee as pw

db = pw.SqliteDatabase('db.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class User(BaseModel):
	id = pw.AutoField()
	username = pw.CharField()
	password = pw.CharField()

if __name__ == '__main__':
    User.create_table()