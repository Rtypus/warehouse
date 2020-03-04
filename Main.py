from Company import Company
import string
company=Company()


x=string.ascii_uppercase
for i in x[:len(x)-1]:
    for j in range(1,6):
        for k in range(9,-1,-1):
            for l in range(10):
                print(str(i)+str(j)+str(k)+str(l))
                company.inputCommand('1'+str(i)+str(j)+str(k)+str(l))

company.inputCommand("1I100")
company.inputCommand("40000")

