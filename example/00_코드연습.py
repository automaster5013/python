# 데이터를 담아둘 캐시와 수정 여부 확인용 변수
cached_person_list = []
is_dirty = True  # 처음에는 무조건 한 번 가져와야 하므로 True

def search_emp():
    global is_dirty, cached_person_list
    
    # 1. 수정된 적이 있다면 DB에서 새로 가져오기 (for 루프 활용)
    if is_dirty:
        print("[System] DB에서 최신 데이터를 동기화합니다...")
        try:
            cursor.execute("SELECT * FROM EMP ORDER BY EMPNO")
            cached_person_list = [Person(*row) for row in cursor]
            is_dirty = False # 동기화 완료
        except oracledb.DatabaseError as e:
            print(f"Fetch Error: {e}")
    else:
        print("[System] 캐시된 데이터를 사용합니다.")

    # 2. 결과 출력
    for p in cached_person_list:
        p.print_person()

# insert_emp와 delete_emp 마지막에 'is_dirty = True' 코드를 추가해야 합니다!








needs_sync = True
emp_cache = []

def search_emp_sync():
    global needs_sync, emp_cache
    
    # 데이터가 최신이 아닐 동안만(while) DB 접속 시도
    while needs_sync:
        try:
            cursor.execute("SELECT * FROM EMP")
            emp_cache = [Person(*row) for row in cursor]
            needs_sync = False # 성공적으로 가져오면 루프 탈출
        except oracledb.DatabaseError:
            print("DB 연결 불안정. 재시도 중...")
            break # 혹은 재시도 로직

    for p in emp_cache:
        p.print_person()








emp_data = []

def get_employees():
    while True:
        # 일단(Do) 메모리에 데이터가 있는지 확인
        if emp_data:
            return emp_data
        
        # 없으면(While) DB에서 채워 넣기
        print("[System] 메모리가 비어있어 DB에 접근합니다.")
        cursor.execute("SELECT * FROM EMP")
        emp_data.extend([Person(*row) for row in cursor])
        # 한 바퀴 돌고 나면 emp_data가 채워져 있으므로 다음 순서에 리턴됨

def search_emp_do_while():
    records = get_employees()
    for p in records:
        p.print_person()

# 추가/삭제 시에는 'emp_data.clear()'를 호출하여 메모리를 비워주면 됩니다.








class EmployeeRepository:
    def __init__(self, db_cursor):
        self.cursor = db_cursor
        self._cache = []
        self._valid = False # 캐시 유효 여부

    def invalidate(self):
        """데이터 변동 시 호출하여 캐시를 무효화함"""
        self._valid = False

    def get_all(self):
        # 유효하지 않을 때만 DB 접근
        if not self._valid:
            print("[Repo] DB에서 데이터를 새로 로드합니다.")
            self.cursor.execute("SELECT * FROM EMP ORDER BY EMPNO")
            self._cache = [Person(*row) for row in self.cursor]
            self._valid = True
        return self._cache

# 사용 예시
repo = EmployeeRepository(cursor)

def search_emp_oop():
    for p in repo.get_all():
        p.print_person()

# insert_emp나 delete_emp 성공 시 repo.invalidate()만 호출해주면 끝!



