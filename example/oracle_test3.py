import oracledb
import sys
from datetime import datetime

# 1. 데이터베이스 접속 설정
db_config = {
    "user": "c##mbc",
    "password": "qwer1234",
    "dsn": oracledb.makedsn("localhost", 1521, service_name="XE")
}

def get_connection():
    try:
        conn = oracledb.connect(**db_config)
        return conn
    except oracledb.Error as e:
        print(f"❌ DB 연결 실패: {e}")
        sys.exit(1)

def show_menu():
    print("\n" + "="*40)
    print("      임직원 관리 시스템 (Oracle)")
    print("="*40)
    print(" 1. 직원 추가 (Insert)")
    print(" 2. 직원 정보 수정 (Update)")
    print(" 3. 직원 삭제 (Delete)")
    print(" 4. 전체 직원 목록 조회 (Select)")
    print(" 5. 특정 직원 검색 (Search)")
    print(" 6. 프로그램 종료")
    print("="*40)
    return input("메뉴를 선택해 주세요: ")

def insert_emp(cursor, conn):
    print("\n[직원 추가]")
    try:
        empno = input("사번(숫자) 입력: ").strip()
        ename = input("이름 입력: ").strip()
        job = input("담당 업무 입력: ").strip().upper()
        sal = input("급여 입력: ").strip() or "0"
        
        if not empno or not ename:
            print("⚠️ 오류: 사번과 이름은 필수 입력 사항입니다.")
            return

        # 오늘 날짜를 입사일로 자동 설정
        hiredate = datetime.now().strftime('%Y-%m-%d')

        sql = "INSERT INTO EMP(EMPNO, ENAME, JOB, SAL, HIREDATE) VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))"
        cursor.execute(sql, [empno, ename.upper(), job, sal, hiredate])
        conn.commit()
        print(f"✅ 성공: {ename.upper()} 직원이 등록되었습니다.")
        
    except oracledb.IntegrityError:
        print("❌ 오류: 이미 존재하는 사번입니다.")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

def update_emp(cursor, conn):
    print("\n[직원 정보 수정]")
    empno = input("수정할 직원의 사번을 입력하세요: ").strip()
    
    # 존재 여부 먼저 확인
    cursor.execute("SELECT ENAME, JOB, SAL FROM EMP WHERE EMPNO = :1", [empno])
    row = cursor.fetchone()
    
    if not row:
        print("⚠️ 해당 사번의 직원을 찾을 수 없습니다.")
        return

    print(f"현재 정보 -> 이름: {row[0]}, 업무: {row[1]}, 급여: {row[2]}")
    new_job = input("변경할 업무 (입력 없이 엔터 시 유지): ").strip().upper() or row[1]
    new_sal = input("변경할 급여 (입력 없이 엔터 시 유지): ").strip() or row[2]

    try:
        sql = "UPDATE EMP SET JOB = :1, SAL = :2 WHERE EMPNO = :3"
        cursor.execute(sql, [new_job, new_sal, empno])
        conn.commit()
        print(f"✅ 사번 {empno}번 직원의 정보가 수정되었습니다.")
    except oracledb.DatabaseError as e:
        print(f"❌ DB 오류 발생: {e}")

def delete_emp(cursor, conn):
    print("\n[직원 삭제]")
    empno = input("삭제할 직원의 사번을 입력하세요: ").strip()
    
    try:
        sql = "DELETE FROM EMP WHERE EMPNO = :1"
        cursor.execute(sql, [empno])
        
        if cursor.rowcount == 0:
            print(f"⚠️ 알림: 사번 {empno}번 직원을 찾을 수 없습니다.")
        else:
            conn.commit()
            print(f"✅ 성공: 사번 {empno}번 직원이 삭제되었습니다.")
            
    except oracledb.DatabaseError as e:
        print(f"❌ DB 오류 발생: {e}")

def list_all_emp(cursor):
    print("\n[전체 직원 목록 조회]")
    try:
        cursor.execute("SELECT EMPNO, ENAME, JOB, TO_CHAR(HIREDATE, 'YYYY-MM-DD'), SAL FROM EMP ORDER BY EMPNO")
        rows = cursor.fetchall()
        
        if not rows:
            print("데이터가 존재하지 않습니다.")
            return

        print("-" * 70)
        print(f"{'사번':<8} {'이름':<12} {'직업':<12} {'입사일':<15} {'급여':<10}")
        print("-" * 70)
        for row in rows:
            print(f"{str(row[0]):<8} {str(row[1]):<12} {str(row[2] or 'N/A'):<12} {str(row[3]):<15} {format(int(row[4] or 0), ','):>8}")
        print("-" * 70)
        
    except oracledb.DatabaseError as e:
        print(f"❌ DB 오류 발생: {e}")

def search_emp_detail(cursor):
    print("\n[특정 직원 상세 조회]")
    name = input("조회할 직원의 이름(일부 가능): ").strip().upper()
    
    try:
        sql = "SELECT EMPNO, ENAME, JOB, TO_CHAR(HIREDATE, 'YYYY-MM-DD'), SAL FROM EMP WHERE ENAME LIKE :1"
        cursor.execute(sql, [f"%{name}%"])
        rows = cursor.fetchall()
        
        if not rows:
            print(f"'{name}' 검색 결과가 없습니다.")
            return

        for row in rows:
            print(f"\n[ {row[1]} 직원의 상세 정보 ]")
            print(f"- 사번: {row[0]}")
            print(f"- 업무: {row[2]}")
            print(f"- 입사일: {row[3]}")
            print(f"- 급여: {format(int(row[4] or 0), ',')}원")
            
    except oracledb.DatabaseError as e:
        print(f"❌ DB 오류 발생: {e}")

def main():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        while True:
            select = show_menu()
            
            if select == '1':
                insert_emp(cursor, conn)
            elif select == '2':
                update_emp(cursor, conn)
            elif select == '3':
                delete_emp(cursor, conn)
            elif select == '4':
                list_all_emp(cursor)
            elif select == '5':
                search_emp_detail(cursor)
            elif select == '6':
                print("프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
                break
            else:
                print("⚠️ 잘못된 선택입니다. 1~6 사이의 숫자를 입력해주세요.")
                
    finally:
        cursor.close()
        conn.close()
        print("📡 DB 연결이 안전하게 해제되었습니다.")

if __name__ == "__main__":
    main()

####### (수정 및 보완 사항)

# 직원 정보 수정(Update) 추가: 급여나 직업을 변경할 수 있는 기능 추가

# 데이터 입력 확장: 이름뿐만 아니라 JOB, SAL, HIREDATE를 입력받도록 개선

# 검색 기능 세분화: 전체 목록뿐만 아니라 특정 사번으로 상세 조회가 가능

# 출력 가독성: 데이터가 정렬되어 보이도록 포맷팅을 개선

###############################################################################################


####### (앞으로 더 발전시킨다면?)

# 앞으로 보완할 사항은?

# 클래스화(OOP): 지금은 함수형이지만, EmployeeManager 클래스를 만들어 관리하면 코드가 더 깔끔

# 환경 변수 사용: db_config에 비밀번호를 직접 적는 것보다 .env 파일 등을 사용하는 것이 보안상 안전

# 입력 유효성 검사: 급여 입력란에 문자를 넣으면 에러가 날 수 있으니, try-except로 숫자인지 체크하는 로직을 보강

###############################################################################################


