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