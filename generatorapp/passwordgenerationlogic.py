import random
import string

class generator():

    def __init__(self,isSpcl,isCap,isNum,passLength):
        self.isSpcl = isSpcl
        self.isCap = isCap
        self.isNum = isNum
        self.passLength = int(passLength)

    def generatePassword(self):
        print('This is spcl',self.isSpcl)

        if(self.isNum != True):
            if(self.isCap):
                if(self.isSpcl):
                    letters = string.ascii_letters + string.punctuation
                else:
                    letters = string.ascii_letters    
            else:
                if(self.isSpcl):
                    letters = string.ascii_lowercase + string.punctuation
                else:
                    letters = string.ascii_lowercase 
        else:
            if(self.isCap):
                if(self.isSpcl):
                    letters = string.ascii_letters  + string.digits + string.punctuation
                else:
                    letters = string.ascii_letters  + string.digits 
                
            else:
                if(self.isSpcl):
                    letters = string.ascii_lowercase + string.digits + string.punctuation
                else:
                    letters = string.ascii_letters  + string.digits
                
        



        result_str = ''.join(random.choice(letters) for i in range(self.passLength))
        print(f'Random string of length is {result_str}')
        return result_str








randPass = generator(True,False,True,16)
randPass.generatePassword()

