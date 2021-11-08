import pygame
import pygame_menu
import pymysql

class Rank():
    def __init__(self):
        self.score_db = pymysql.connect(
            user = 'admin',
            passwd = 'the-journey',
            host = 'the-journey-db.cvfqry6l19ls.ap-northeast-2.rds.amazonaws.com',
            db = 'sys',
            charset = 'utf8'
        )

    def load_data(self,mode):                                             #데이터 베이스에서 데이터 불러오기
            curs = self.score_db.cursor(pymysql.cursors.DictCursor)
            if mode == "easy":
                sql = "select * from easy_score order by score desc"
            elif mode == "hard":
                sql = "select * from hard_score order by score desc"
            curs.execute(sql)
            data = curs.fetchall()
            curs.close()
            return data

    def add_data(self, ID, score):                                   #데이터 베이스에서 데이터 추가하기
        curs = self.score_db.cursor()
        sql = "INSERT INTO test_score (ID, score) VALUES (%s, %s)"
        curs.execute(sql, (ID, score))
        self.score_db.commit()
        curs.close()  