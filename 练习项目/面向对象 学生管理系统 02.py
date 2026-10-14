#该文件增添了保存文件功能，以csv形式
import csv
import os
class Student:
    def __init__(self, student_id, student_name, student_age, student_score):
        self.id = student_id
        self.name =student_name
        self.age = student_age
        self.score = student_score
    def __repr__(self):
        return f"{self.id},{self.name},{self.age},{self.score}"

class Students_M:
    def __init__(self,data_file="students.csv"):
        self.students=[]
        self.data_file=data_file
        self.load_from_csv()
    def gen_id(self):
        if not self.students:
            return "S001"
        max_num = max(int(stu.id[1:]) for stu in self.students)
        return f"S{max_num + 1:03d}"
#
    def load_from_csv(self):
        """程序启动时，从 CSV 读取数据"""
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                stu = Student(
                    row["学号"],
                    row["姓名"],
                    int(row["年龄"]),
                    float(row["成绩"]),
                )
                self.students.append(stu)

    def save_to_csv(self):
        """把内存里的学生数据写回 CSV"""
        fieldnames = ["学号", "姓名", "年龄", "成绩"]
        with open(self.data_file, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for stu in self.students:
                writer.writerow({
                    "学号": stu.id,
                    "姓名": stu.name,
                    "年龄": stu.age,
                    "成绩": stu.score,
                })
#
    def add(self):
        print("请按照学生姓名 年龄 分数 输入")
        name=input()
        age=int(input())
        score=float(input())
        id=self.gen_id()
        stu=Student(id,name,age,score)
        self.students.append(stu)
        self.save_to_csv()
        print("该学生添加成功")
    def all_students(self):
        for stu in self.students:
            print(stu)
    def search_student(self):
        print("请输入学生名字或学号：")
        keyword=input()
        for student in self.students:
            if student.name == keyword or student.id == keyword:
                print(student)
            else:
                print("未找到该学生")
    def rewrite(self):
        self.all_students()
        number=input("请输入学号：")
        for s in self.students:
            if s.id==number:
                 rage=int(input("输入想改为的年龄："))
                 rscore=float(input("输入想改为的成绩："))
                 s.score=rscore
                 s.age=rage
                 self.save_to_csv()
                 print("修改成功")
        else:
            print("输入错误")

    def delete(self):
        delete_number=input("请输入你要删除的学生学号")
        for s in self.students:
            if delete_number==s.id:
                cnt=input("是否要删除（y/n）：")
                if cnt=="y":
                    self.students.remove(s)
                    self.save_to_csv()
                    print("删除成功")
                    break
                else:
                    break
            else:
                print("未找到该学生")
table="""###########################################
# 1.添加学生  输入姓名，年龄，成绩             #
# 2.查看全部  以表格形式打印所有学生           #
# 3.查询学生  按照学号精准查询 按照名字模糊查询  #
# 4.修改学生  先查再改 可改年龄成绩 不可改学号  #
# 5.删除学生  删除前要二次确认                #      
# 6.退出系统                               #
###########################################
"""
if __name__ == "__main__":
    manager = Students_M()
    while True:
        print(table)
        choice=int(input("请选择你要进行的操作（1~5）："))
        match choice:
            case 1:
                manager.add()
            case 2:
               manager.all_students()
            case 3:
                manager.search_student()
            case 4:
                manager.rewrite()
            case 5:
                manager.delete()
            case 6:
                break
            case _:
                print("数字错误")
