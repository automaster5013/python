class Person:
    def __init__(self, empno, ename, job, mgr, hiredate, sal, comm, deptno):
        self.empno = empno
        self.ename = ename 
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal = sal
        self.comm = comm
        self.deptno = deptno

    def print_person(self):
        # print(f"{self.empno} : {self.ename} => {self.job} : ({self.mgr}) : [{self.hiredate}] : {self.sal} : {self.comm} / {self.deptno}")
        if self.sal is not None:
            print(f"{self.empno} : {self.ename:>10} : {self.sal}")
        else:
            print(f"{self.empno} : {self.ename:>10} : 0")
 

