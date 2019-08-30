class Array:
    def __init__(self, *args):
        self.value = list(args)

    def __duplicate(self, init_val=None):
        new_arr = self.__class__(*self.value)
        if init_val is not None:
            new_arr.value = init_val
        return new_arr

    def reverse(self):
        return self.__duplicate(self.value[::-1])

    def map(self, cb):
        argcount = cb.__code__.co_argcount
        new_arr = self.__duplicate([])
        for idx, item in enumerate(self.value):
            arg_list = (item, idx, self.value)[:argcount]
            res = cb(*arg_list)
            new_arr.value += [res]
        return new_arr

    def join(self, separator=''):
        temp = ''
        for item in self.value:
            temp += str(item) + separator
        return temp[:-len(separator)]
