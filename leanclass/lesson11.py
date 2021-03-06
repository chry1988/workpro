"""
题目一： 写一个网页数据操作类。完成下面的功能：
提示：需要用到urllib模块
get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int
get_htmlcontent() 获取网页的内容。返回类型:str
get_linknum()计算网页的链接数目。
"""
from urllib import  request
class urlmode(object):
    def __init__(self):
        self.urls='http://10.78.107.190/'
    def get_httpcode(self):
        with request.urlopen(self.urls) as f:
            return int(f.status)
            #print('status',f.status,f.reason)
            #for k, v in f.getheaders():
            #    print('%s: %s' % (k, v))
            #print('Data:', f.read().decode('utf-8'))
        pass
    def get_htmlcontent(self):
        with request.urlopen(self.urls) as f:
            print(f.read().decode('utf-8'))
        pass
    def get_linknum(self):
        n=0
        for line in request.urlopen(self.urls).read().decode('utf-8'):
            print( line)

        print(n)

        pass
act = urlmode().get_linknum()
"""
题目二：
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()

体会下这段代码，把结果的执行流程用自己的话写下。
"""