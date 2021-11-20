masss = []
class My_List:
    mass = []
    def __init__(self, m):
            self.mass = m

    def add(self,elem):
       self.mass.append(elem)
       return self.mass

    def add2(self,elem):
       self.mass.insert(0,elem)
       return self.mass

    def delete(self, n):
        del(self.mass[n])
        return self.mass

    def vivod_revers(self):
      a=self.mass
      a= list(reversed(a))
      return (self.mass,a)

    def sum(self):
        total = 0
        for i in range(len(self.mass)):
            total += int(self.mass[i])
        return total

    def sort(self):
       a = sorted(self.mass)
       return a


menu = 1
while menu == 1:
    n = int(input("Виберіть дію \n"
          "1-додати об'єкт \n"
          "2-додати елемент у список в кінець\n"
          "3-додати елемент у список на початок\n"
          "4-вилучити елемент за індексом\n"
          "5-сортування списку\n"
          "6-виведення елементів списку від початку і від кінця\n"
          "7-обчислення суми елементів\n"
          "8-відсортувати по умові завдання\n"
          "0-вийти з програми\n"))

    if (n==1):
        t=1
        element = []
        while t==1:
            while t==1:
                qqq = input("Введіть елемент списку\n")
                element.append(int(qqq))
                t = int(input("Бажаєте додати ще елемент списку? так - 1, ні - інше число\n"))
            a = My_List(element)
            masss.append(a)
            element=[]
            t = int(input("Бажаєте додати ще екземпляр класу? так - 1, ні - інше число\n"))

    elif(n==2):
        i=int(input("Виберіть до якого екземпляру додати елемент\n"))
        add = int(input("Введіть елемент\n"))
        print (str(masss[i-1].add(add)))

    elif (n == 3):
        i = int(input("Виберіть до якого екземпляру додати елемент\n"))
        add = int(input("Введіть елемент\n"))
        print(str(masss[i - 1].add2(add)))


    elif(n==4):
        i = int(input("Виберіть від якого екземпляру відняти елемент\n"))
        d = int(input("Введіть номер елементу\n"))
        print(str(masss[i - 1].delete(d - 1)))

    elif (n == 5):
        for i in range(len(masss)):
            print(str(masss[i].sort()))

    elif(n==6):
        for i in range(len(masss)):
            print(str(masss[i].vivod_revers()))

    elif(n==7):
        for i in range(len(masss)):
            print(str((str(masss[i].mass) + " Сума = " + str(masss[i].sum()))))

    elif(n==8):
        N = len(masss)
        for i in range(N-1):
            m = masss[i].sum()
            p = i
            for j in range(i+1, N):
                if m < masss[j].sum():
                    m = masss[j]
                    p = j
                    
            if p != i:
                t = masss[i]
                masss[i] = masss[p]
                masss[p] = t
        
        for i in range(len(masss)):
            print (str((str(masss[i].mass) +" Сума = "+str(masss[i].sum()))))


    elif (n==0):
        menu=0
    else: print("Некоректне введення\n")