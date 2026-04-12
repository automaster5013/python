import oracledb
from person import Person  # Person 객체 모델 사용
from datetime import datetime

# 1. DB 접속 설정
dsn = oracledb.makedsn("localhost", 1521, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)
cursor = conn.cursor()

person_list = []  # 메모리 상의 객체 리스트

def show_menu():
    print("\n" + "="*45)
    print("   [임직원 관리 시스템 - Advanced]")
    print("="*45)
    print(" 1. 직원 추가 (Insert)")
    print(" 2. 직원 삭제 (Delete)")
    print(" 3. 정보 수정 (Update - JOB/SAL)")
    print(" 4. 전체 조회 (Select All)")
    print(" 5. 상세 조회 (Select One)")
    print(" 6. 프로그램 종료")
    print("-" * 45)
    return input("메뉴를 선택해 주세요: ")

# DB와 리스트 동기화 함수 (필요할 때만 호출)
def sync_data():
    person_list.clear()
    try:
        cursor.execute("SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO FROM EMP ORDER BY EMPNO")
        for row in cursor:
            person_list.append(Person(*row))
    except oracledb.DatabaseError as e:
        print(f"동기화 오류: {e}")

def insert_emp():
    print("\n[새 직원 등록]")
    try:
        empno = input("사번(숫자): ").strip()
        if not empno.isdigit():
            print("오류: 사번은 숫자만 입력 가능합니다.")
            return
            
        ename = input("이름: ").strip().upper()
        job = input("직무(JOB): ").strip().upper()
        sal = input("급여(SAL): ").strip()
        
        # 입사일은 오늘 날짜를 기본값으로 하되 형식에 맞춰 입력 가능
        hiredate_str = input("입사일(YYYY-MM-DD, 미입력시 오늘): ").strip()
        if not hiredate_str:
            hiredate = datetime.now()
        else:
            hiredate = datetime.strptime(hiredate_str, "%Y-%m-%d")

        sql = "INSERT INTO EMP(EMPNO, ENAME, JOB, SAL, HIREDATE) VALUES (:1, :2, :3, :4, :5)"
        cursor.execute(sql, [empno, ename, job, sal, hiredate])
        conn.commit()
        
        print(f"성공: {ename} 직원이 등록되었습니다.")
        person_list.clear() # 리스트 초기화 (새로고침 유도)
        
    except ValueError:
        print("오류: 날짜 형식이 잘못되었습니다 (YYYY-MM-DD).")
    except oracledb.DatabaseError as e:
        print(f"DB 등록 오류: {e}")

def update_emp():
    print("\n[직원 정보 수정]")
    empno = input("수정할 직원의 사번을 입력하세요: ").strip()
    
    # 수정 전 데이터 존재 확인
    cursor.execute("SELECT ENAME, JOB, SAL FROM EMP WHERE EMPNO = :1", [empno])
    row = cursor.fetchone()
    
    if row:
        print(f"현재 정보 -> 이름: {row[0]}, 직무: {row[1]}, 급여: {row[2]}")
        new_job = input("새로운 직무(변경 없으면 엔터): ").strip().upper() or row[1]
        new_sal = input("새로운 급여(변경 없으면 엔터): ").strip() or row[2]
        
        try:
            sql = "UPDATE EMP SET JOB = :1, SAL = :2 WHERE EMPNO = :3"
            cursor.execute(sql, [new_job, new_sal, empno])
            conn.commit()
            print(f"사번 {empno}번 직원의 정보가 수정되었습니다.")
            person_list.clear()
        except oracledb.DatabaseError as e:
            print(f"수정 오류: {e}")
    else:
        print("해당 사번의 직원이 존재하지 않습니다.")

def delete_emp():
    print("\n[직원 삭제]")
    empno = input("삭제할 직원의 사번: ").strip()
    
    try:
        cursor.execute("DELETE FROM EMP WHERE EMPNO = :1", [empno])
        if cursor.rowcount == 0:
            print(f"삭제 실패: 사번 {empno}번 직원이 없습니다.")
        else:
            conn.commit()
            print(f"성공: 사번 {empno}번 직원이 삭제되었습니다.")
            person_list.clear()
    except oracledb.DatabaseError as e:
        print(f"삭제 오류: {e}")

def print_table_header():
    print("-" * 75)
    print(f"{'사번':<8} | {'이름':<12} | {'직무':<10} | {'입사일':<12} | {'급여':<10}")
    print("-" * 75)

def search_all():
    if not person_list:
        sync_data()
    
    if not person_list:
        print("조회할 데이터가 없습니다.")
        return

    print(f"\n[전체 직원 목록 - 총 {len(person_list)}명]")
    print_table_header()
    for p in person_list:
        # Person 객체 내부에 포맷팅된 출력 메서드가 있다면 p.print_person() 사용
        # 여기서는 가독성을 위해 직접 정렬 출력
        print(f"{str(p.empno):<8} | {p.ename:<12} | {str(p.job or ''):<10} | {str(p.hiredate)[:10]:<12} | {str(p.sal or 0):<10}")
    print("-" * 75)

def search_one():
    empno = input("조회할 사번을 입력하세요: ").strip()
    cursor.execute("SELECT * FROM EMP WHERE EMPNO = :1", [empno])
    row = cursor.fetchone()
    
    if row:
        p = Person(*row)
        print("\n[상세 정보 조회 결과]")
        print_table_header()
        print(f"{str(p.empno):<8} | {p.ename:<12} | {str(p.job or ''):<10} | {str(p.hiredate)[:10]:<12} | {str(p.sal or 0):<10}")
        print("-" * 75)
    else:
        print("해당 직원을 찾을 수 없습니다.")

# 메인 루프
try:
    while True:
        menu = show_menu()
        if menu == '1':
            insert_emp()
        elif menu == '2':
            delete_emp()
        elif menu == '3':
            update_emp()
        elif menu == '4':
            search_all()
        elif menu == '5':
            search_one()
        elif menu == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴 선택입니다.")
finally:
    cursor.close()
    conn.close()
    print("DB 연결이 안전하게 해제되었습니다.")



###################################################################################################################################
# 주요 수정 및 추가 사항
# Update(수정) 기능 추가: 사번을 입력받아 해당 직원의 JOB(직업)과 SAL(급여)을 수정

# Insert(추가) 확장: 이름뿐만 아니라 JOB, SAL, HIREDATE를 입력받는다. (HIREDATE는 기본값으로 오늘 날짜를 쓰거나 직접 입력 가능)

# 상세 조회 추가: 사번을 통해 특정 직원 한 명의 정보만 확인하는 기능을 추가

# 동기화 로직 최적화: DB에 변경(추가/삭제/수정)이 생기면 person_list를 초기화하여 다음 조회 시 최신 데이터를 가져오도록 설계

# 가독성 개선: 테이블 형태의 레이아웃 적용
###################################################################################################################################


###################################################################################################################################
# 데이터 무결성 및 확장: insert_emp에서 JOB, SAL, HIREDATE를 추가로 받으며, HIREDATE 입력 시 형식이 틀리면 ValueError 예외 처리를 수행

# Update 시 기존 데이터를 먼저 보여주고, 엔터를 치면 기존 값을 유지하는 편의 기능을 추가

# 효율적인 리스트 관리: person_list.clear()를 적절히 활용하여 DB 값이 바뀌면 리스트를 비우고, 
#                   다음에 조회(search_all)할 때 자동으로 최신 데이터를 DB에서 읽어와 Person 객체로 변환

# 가독성 높은 출력: f-string 정렬(:<8, :<12 등)을 사용하여 사번, 이름, 직무 등이 수직으로 정렬된 표 형태로 출력

# 전체 목록과 상세 조회의 출력 폼을 통일하여 일관성 추구구

# 안전성: try...finally 문을 사용하여 프로그램이 도중에 오류로 꺼지더라도 DB 연결은 반드시 해제되도록 보완
###################################################################################################################################
