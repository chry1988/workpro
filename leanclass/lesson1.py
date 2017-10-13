class student(object,):
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course=course
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return int(self.age)
    def get_course(self):
        any_result = max(self.course)
        return int(any_result)

zm = student('zhangming',20,[69,88,100])
print(zm.get_course())
print(zm.get_age())
print(zm.get_name())
class dictclass(object):
    def __init__(self,a={},key='',b={}):
        self.a =a
        self.key=key
        self.b =b

    def del_dice(self):
        if self.key=='':
            return 'you must input a key to do this'
        else:
            self.a.pop(self.key)
        pass
    def get_dict(self):
        pass
    def get_key(self):
        pass
    def update_dict(self):
        pass