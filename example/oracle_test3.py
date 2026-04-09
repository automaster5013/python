import oracledb
import sys

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
        print(f"DB 연결 실패: {e}")
        sys.exit(1)

def show_menu():
    print("\n" + "="*30)
    print("   임직원 관리 시스템 (Oracle)")
    print("="*30)
    print(" 1. 직원 추가")
    print(" 2. 직원 삭제")
    print(" 3. 직원 조회")
    print(" 4. 프로그램 종료")
    print("="*30)
    return input("메뉴를 선택해 주세요: ")

def insert_emp(cursor, conn):
    print("\n[직원 추가]")
    try:
        empno = input("사번 입력: ").strip()
        ename = input("이름 입력: ").strip()
        
        if not empno or not ename:
            print("오류: 사번과 이름은 필수 입력 사항입니다.")
            return

        sql = "INSERT INTO EMP(EMPNO, ENAME) VALUES (:1, :2)"
        cursor.execute(sql, [empno, ename.upper()])
        conn.commit()
        print(f"성공: {ename.upper()}({empno}) 직원이 등록되었습니다.")
        
    except oracledb.IntegrityError:
        print("오류: 이미 존재하는 사번입니다.")
    except oracledb.DatabaseError as e:
        print(f"DB 오류 발생: {e}")

def delete_emp(cursor, conn):
    print("\n[직원 삭제]")
    empno = input("삭제할 직원의 사번을 입력하세요: ").strip()
    
    try:
        sql = "DELETE FROM EMP WHERE EMPNO = :1"
        cursor.execute(sql, [empno])
        
        if cursor.rowcount == 0:
            print(f"알림: 사번 {empno}번 직원을 찾을 수 없습니다.")
        else:
            conn.commit()
            print(f"성공: 사번 {empno}번 직원이 삭제되었습니다.")
            
    except oracledb.DatabaseError as e:
        print(f"DB 오류 발생: {e}")

def search_emp(cursor):
    print("\n[직원 목록 조회]")
    try:
        cursor.execute("SELECT EMPNO, ENAME, JOB, HIREDATE, SAL FROM EMP ORDER BY EMPNO")
        rows = cursor.fetchall()
        
        if not rows:
            print("데이터가 존재하지 않습니다.")
            return

        print("-" * 50)
        print(f"{'사번':<10}{'이름':<15}{'직업':<15}{'급여':<10}")
        print("-" * 50)
        for row in rows:
            # None 값 처리를 위해 str() 변환 및 슬라이싱 활용
            print(f"{str(row[0]):<10}{str(row[1]):<15}{str(row[2] or 'N/A'):<15}{str(row[4] or 0):<10}")
        print("-" * 50)
        
    except oracledb.DatabaseError as e:
        print(f"DB 오류 발생: {e}")

def main():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        while True:
            select = show_menu()
            
            if select == '1':
                insert_emp(cursor, conn)
            elif select == '2':
                delete_emp(cursor, conn)
            elif select == '3':
                search_emp(cursor)
            elif select == '4':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 1~4 사이의 숫자를 입력해주세요.")
                
    finally:
        # 오류 발생시 종료료
        cursor.close()
        conn.close()
        print("DB 연결이 해제되었습니다.")

if __name__ == "__main__":
    main()