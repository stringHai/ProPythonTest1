

class Student():
    name = ""
    age = 0
    # 类的初始化函数
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name)
        print(age)



    def homework(self,hard):
        hard = hard
        return hard


student_1 = Student("小名",11)
student_2 = Student("小芳",14)

wo = 1
work1 = student_1.homework(wo)
name1 = student_1.name
print(name1+"在做第"+str(work1)+"次作业")



'''
def sum_my(list):
    sum = 0
    for sum in list:
        print("sum",sum)
        sum += sum
    return sum




list1 = [1,2,3,4,5]
mysum = sum_my(list1)
print(mysum)
'''
