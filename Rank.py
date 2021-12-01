import pygame
import pygame_menu
import pymysql
from datetime import datetime

class Rank():
    def __init__(self):
        self.score_db = pymysql.connect(
            user = 'admin',
            passwd = 'the-journey',
            host = 'the-journey-db.cvfqry6l19ls.ap-northeast-2.rds.amazonaws.com',
            db = 'sys',
            charset = 'utf8'
        )

    def load_data(self, term, mode):                                           #데이터 베이스에서 데이터 불러오기
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        if term == 'current':
            if mode == 'easy':
                sql = 'select * from current_easy_score order by score desc'
            elif mode == 'hard':
                sql = 'select * from current_hard_score order by score desc'

        if term == 'past':
            if mode == 'easy':
                sql = 'select * from past_easy_score order by score desc'
            elif mode == 'hard':
                sql = 'select * from past_hard_score order by score desc'

        curs.execute(sql)
        data = curs.fetchall()
        curs.close()
        return data

    def load_current_latest_data(self, mode):
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        if mode == 'easy':
            sql = 'select * from current_easy_score order by date desc'
        elif mode == 'hard':
            sql = 'select * from current_hard_score order by date desc'
        curs.execute(sql)
        data = curs.fetchall()
        if(len(data) > 0): return str(data[0]['date'])
        else:
            if mode == 'easy':
                sql = 'select * from past_easy_score order by date desc'
            elif mode == 'hard':
                sql = 'select * from past_hard_score order by date desc'
            curs.execute(sql)
            data = curs.fetchall()
            curs.close()
            return str(data[0]['date'])
         
        # return datetime.now().strftime('%Y-%m-%d')
        # latest_data_date = str(data[0]['date'])
        # return latest_data_date

    def search_data(self, term, mode, ID):                                  
        if term == 'current':
            if mode == 'easy':
                data = self.load_data('current', 'easy')
            elif mode == 'hard':
                data = self.load_data('current', 'hard')

        if term == 'past':
            if mode == 'easy':
                data = self.load_data('past', 'easy')
            elif mode == 'hard':
                data = self.load_data('past', 'hard')

        for i in range(len(data)):
            if data[i]['ID'] == ID:
                return i+1
        return 0

    def add_data(self, term, mode, ID, score):                                   #데이터 베이스에서 데이터 추가하기
        curs = self.score_db.cursor()
        now = datetime.now()
        if term == 'current':
            if mode == 'easy':
                sql = 'INSERT INTO current_easy_score (ID, score, date) VALUES (%s, %s, %s)'

            if mode == 'hard':
                sql = 'INSERT INTO current_hard_score (ID, score, date) VALUES (%s, %s, %s)'

        if term == 'past':
            if mode == 'easy':
                sql = 'INSERT INTO past_easy_score (ID, score, date) VALUES (%s, %s, %s)'

            if mode == 'hard':
                sql = 'INSERT INTO past_hard_score (ID, score, date) VALUES (%s, %s, %s)'
        curs.execute(sql, (ID, score, now.strftime('%Y-%m-%d')))
        self.score_db.commit()
        curs.close()

    def paste_to_past_data(self, mode, ID, score, date):                                   #데이터 베이스에서 데이터 추가하기
        curs = self.score_db.cursor()
        if mode == 'easy':
            sql = 'INSERT INTO past_easy_score (ID, score, date) VALUES (%s, %s, %s)'

        if mode == 'hard':
            sql = 'INSERT INTO past_hard_score (ID, score, date) VALUES (%s, %s, %s)'

        curs.execute(sql, (ID, score, date))
        self.score_db.commit()
        curs.close()

    def check_ID(self, mode, ID):       # ID 중복 체크 (나중에 NULL 체크도 필요)
        curs = self.score_db.cursor()
        if mode == 'easy':
            sql = 'select * from current_easy_score where ID = binary(%s)'
        if mode == 'hard':
            sql = 'select * from current_hard_score where ID = binary(%s)'
        curs.execute(sql, (ID))
        data = curs.fetchall()
        curs.close()
        if(len(data)>0): return 0   # 중복임
        else: return 1              # 중복아님

    
    def clear_data(self, term, mode):   
        curs = self.score_db.cursor(pymysql.cursors.DictCursor)
        if term == 'current':
            if mode == 'easy':
                sql = 'delete from current_easy_score'
            elif mode == 'hard':
                sql = 'delete from current_hard_score'

        if term == 'past':
            if mode == 'easy':
                sql = 'delete from past_easy_score'
            elif mode == 'hard':
                sql = 'delete from past_hard_score'

        curs.execute(sql)
        self.score_db.commit()
        curs.close()

    def move_data(self, mode):
        data = self.load_data('current', mode)
        for i in range(len(data)):
            name = str(data[i]['ID'])
            score = str(data[i]['score'])
            date = str(data[i]['date'])
            self.paste_to_past_data(mode, name, score, date)

    def update_data(self):      # 랭킹 등록 시 date의 월 값이 달라질 때 update_data 호출 하면 될 듯
        self.clear_data('past', 'easy')
        self.move_data('easy')
        self.clear_data('past', 'hard')
        self.move_data('hard')
        self.clear_data('current', 'easy')
        self.clear_data('current', 'hard')

    def check_update(self):
        # 가장 최근에 기록된 랭킹의 날짜 데이터 받아오기
        current_latest_data_date = self.load_current_latest_data('easy')
        # 예외처리 ?
        # if(current_latest_data_date < self.load_current_latest_data('hard')): current_latest_data_date = self.load_current_latest_data('hard')

        if(current_latest_data_date[0:4] < datetime.now().strftime('%Y')): # Year 비교
            self.update_data()
        elif(current_latest_data_date[5:7] < datetime.now().strftime('%m')): # month 비교
            self.update_data()



