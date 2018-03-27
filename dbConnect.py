import pymysql.cursors


def connect_db():
    return pymysql.connect(host='cse305.ctn44dwr3swf.us-east-2.rds.amazonaws.com',
                    user='cse305Team1',
                    passwd='cse305Team1',
                    db='cse305',
                    cursorclass=pymysql.cursors.DictCursor)
