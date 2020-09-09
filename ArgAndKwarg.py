# *arg for list
# def test_var_args(f_arg, *argv):
#     print("first normal arg:", f_arg)
#     for arg in argv:
#         print("another arg through *argv:", arg)

# test_var_args('one','two','three','four')

# **kwargs for dictionary
# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} == {1}".format(key, value))

# greet_me(name="Myname")

def get_values(arg1, arg2, arg3):
    print('arg1'+ arg1)
    print('arg2'+ arg2)
    print('arg3'+ arg3)

args=("abc","3","5")
#get_values(*args)

kwarg = {'arg1':'abc','arg3':'5','arg2':'3'}
get_values(**kwarg)

