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
        if self.key in self.a:
            return self.a[self.key]
        else:
            return 'not found'
        pass
    def get_key(self):
        return list(self.a.keys())
        pass
    def update_dict(self):
        result = []
        for key1 in self.a:
            result.append(self.a[key1])
        for key2 in self.b:
            result.append(self.b[key2])
        return result
        pass

dicta={'a':'1213','b':'sdfsdf','c':'jhfg'}
dictb={'key_one':'zk','key_two':'noe','key_three':'testing'}

cd = dictclass(a=dicta,key='a',b=dictb)


print(cd.get_key())
