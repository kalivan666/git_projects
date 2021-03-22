# def main():
#     s = 'Intel Core i3 560 @ 3.3 GHz or AMD Phenom II X4 945 @ 3.0 GHz'
#     f = s.split(' ')
#     a = s.find('Intel')
#     l = len(f)
#     z = ''
#     x = 0
#     for i in range(l - 1):
#         if f[x] == 'Intel®':
#             f.pop(x)
#             l -= 1
#         elif f[x] == 'Intel':
#             f.pop(x)
#             l -= 1
#         elif f[x] == 'AMD':
#             f.pop(x)
#             l -= 1
#         else:
#             x +=1
#     if check(f):
#         a = f.index('or')
#         treatment(a, f)
#     if check_new(f):
#         a = f.index('/')
#         treatment(a, f)
# def treatment(a, f):
#     z = ('_'.join(f[0:a]))
#     print(z)
# def check(f):
#     try:
#         a = f.index('or')
#         return True
#     except ValueError:
#         return False
# def check_new(f):
#     try:
#         a = f.index('/')
#         return True
#     except ValueError:
#         return False
#
# if __name__ == '__main__':
#     main()

a = 1 * 90 %
print(a)