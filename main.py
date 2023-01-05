import datetime
import sys

import pymysql
import shutil

# MySQL Connection 연결
conn = pymysql.connect(host='llocalhost:3000',
                       user='user',
                       password='1234',
                       db='db',
                       charset='utf8')
# Cursor 객체 반환
curs = conn.cursor()

# 기본 경로
directory = '/data/hunters/client/'

# 기존 파일 경로
old_path = '{}candidate_resume'.format(directory)
# 삭제 예정 폴더 경로
new_path = '{}delete_candidate_resume'.format(directory)

# arguments 통한 날짜 계산
date = sys.argv[1] if sys.argv.__len__() > 1 else datetime.date.today() - datetime.timedelta(weeks=2)

# Cursor 로 테이블 조회를 위한 SQL 문 실행
sql = "select url from resume".format(date)
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)  # 전체 rows

# 파일 이동 처리
for val in rows:
    try:
        shutil.move('{}/{}'.format(old_path, val[0]), '{}/{}'.format(new_path, val[0]))
    except FileNotFoundError as e:
        print('not found : {}/{}'.format(old_path, val[0]))

# Connection 닫기
conn.close()
