# class Student:
#     school_name = 'MIT'
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         print('Not Del')
#     # name = property()
#
#
# stu1_obj = Student('Sherry')
# print(stu1_obj.name)


class Student:
    school_name = 'MIT'

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def del_name(self):
        print('Not Del')

    name = property(get_name, set_name, del_name)


stu1_obj = Student('Sherry')
print(stu1_obj.name)
stu1_obj.name = 'Jack'
print(stu1_obj.name)
del stu1_obj.name
