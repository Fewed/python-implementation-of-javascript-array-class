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

    def filter(self, cb):
        argcount = cb.__code__.co_argcount
        new_arr = self.__duplicate([])

        for idx, item in enumerate(self.value):
            arg_list = (item, idx, self.value)[:argcount]
            if cb(*arg_list):
                new_arr.value += [item]

        return new_arr

    def reduce(self, cb, initial):
        argcount = cb.__code__.co_argcount
        temp = initial

        for idx, item in enumerate(self.value):
            arg_list = (temp, item, idx, self.value)[:argcount]
            temp = cb(*arg_list)

        return temp

    def join(self, separator=','):
        print(separator, len(separator))
        temp = ''
        for item in self.value:
            temp += str(item) + separator
        if len(separator):
            return temp[:-len(separator)]
        return temp

    def push(self, *args):
        self.value += args
        return len(self.value)

    def pop(self):
        temp = self.value[-1]
        self.value = self.value[:-1]
        return temp

    def slice(self, start=0, end=-1):
        return self.__duplicate(self.value[start:end])

    def splice(self, start, delete_count, *items):
        deleted = self.value[start:start + delete_count]
        self.value = self.value[:start] + list(items) + self.value[start + delete_count:]
        return deleted
