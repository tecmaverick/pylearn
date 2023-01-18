class A:
    # gets called “last”(the lowest priority), if Python cannot find the attribute.
    def __getattr__(self, name):
        return ("getattr:"+name)

    # gets called “first”(the highest priority), whether or not there’s the attribute.
    # def __getattribute__(self,name):
    #     return ("getattribute:" + name)

    def test(self):
        return "test"

a = A()
a.aaa = "abc"

print(a.aaa)
print(a.aaa1)
print(a.__dict__)