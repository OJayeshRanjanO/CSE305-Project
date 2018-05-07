import pymysql.cursors


def connect_db():
    return pymysql.connect(host='cse305.ctn44dwr3swf.us-east-2.rds.amazonaws.com',
                    user='cse305Team1',
                    passwd='cse305Team1',
                    db='tempcse305',
                    cursorclass=pymysql.cursors.DictCursor)

def purge_db():
    return pymysql.connect(host='cse305.ctn44dwr3swf.us-east-2.rds.amazonaws.com',
                    user='cse305Team1',
                    passwd='cse305Team1',
                    cursorclass=pymysql.cursors.DictCursor)
