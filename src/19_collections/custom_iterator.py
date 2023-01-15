class myiterator:

    def setValue(self, myStrlist):
        if type(myStrlist) != str:
            raise Exception("myStrlist must be of type String")

        self.mylist = myStrlist.split(",")

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.mylist):
            result = self.mylist[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration


o = myiterator()
o.setValue("1,2,3")
itr = iter(o)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))  # This will raise StopIteration Exception
