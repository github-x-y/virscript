# from random import randint,choice
# def exam():
#     a = [randint(1,100) for i in range(2)]
#     a.sort(reverse=True)
#     c = choice('+-')
#     if c == '+':
#         result = a[0] + a[1]
#     else:
#         result = a[0] - a[1]
#     promat = '%s %s %s =' % (a[0],c,a[1])
#     counter = 0
#     while counter < 3:
#       e = int(input(promat))
#       if e == result:
#         print('you is good')
#         break
#     else:
#       counter+=1
#     print('%s %s' % (promat,result))
# def fun1():
#     while 1:
#       exam()
#       e = input('play/ny:')
#       if e == 'n':
#             break
# i
#
#
#
#
#
#
#
#
#
#
#
#
#
#  __name__ == '__main__':
#     fun1()
# a = input('please enter you username:')
# print('welcome to',a)
from random import randint

def qsort(seq):
    middle = seq[0]
    smaller = []
    larger = []

    for data in seq[1:]:
        if data < middle:
            smaller.append(data)
        else:
            larger.append(data)

    return smaller + [middle] + larger

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
