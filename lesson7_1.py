class Matrix():
    def __init__(self, mylist):
        self.mylist = mylist

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.mylist]))

    def __add__(self, other):

        for i in range(len(self.mylist)):

            for j in range(len(other.mylist[i])):
                self.mylist[i][j] = self.mylist[i][j] + other.mylist[i][j]

       # for i in range(len(self.mylist)):
       #     for i_2 in range(len(other.mylist[i])):
       #         self.mylist[i][i_2] = self.mylist[i][i_2] + other.mylist[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))
