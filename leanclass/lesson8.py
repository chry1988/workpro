class Listinfo(object):
    def __init__(self,keyname,lista=[],listb=[],num=1):
        self.lista = lista
        self.listb = listb
        self.keyname = keyname
        self.num =num
        pass
    def add_key(self):
        return self.lista.append(self.keyname)
        pass
    def get_key(self):
        if not isinstance(self.num,int):
            return 'you must input num as num'
        return self.lista[self.num]
        pass
    def update_list(self):
        return self.lista.extend(self.listb)
        pass
    def del_key(self):
        return self.lista.pop()
        pass
    def __del__(self):
        del self.listb
        del self.lista
lista = ['a','b','c','d']
listb = ['11','22','33']

l =Listinfo(lista=lista,listb=listb,num=0,keyname=4)
print(l.del_key())
print(lista)
'''定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)'''
class Setinfo(object):
    def __init__(self):
        pass
    def add_setinfo(self):
        pass
    def get_intersection(self):
        pass
    def get_union(self):
        pass
    def del_difference(self):
        pass