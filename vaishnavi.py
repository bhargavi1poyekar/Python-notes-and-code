from numpy import poly


class Polynomial:
    def __init__(self, poly):
        self.poly=poly

    def eval_poly(self, val):
        sum=0
        for i in range(len(self.poly)):
            term=self.poly[i][0]
            for j in range(len(self.poly[i][1])):
                term*=val[self.poly[i][1][j]]**self.poly[i][2][j]
            sum+=term
        return sum
    
    def print_poly(self):
        eqn=''
        for i in range(len(self.poly)):
            if self.poly[i][0]!=1:
                term=str(self.poly[i][0])
            else: #If coefficient is 1
                term=''
            for j in range(len(self.poly[i][1])):
                if self.poly[i][2][j]!=1: 
                    term+=self.poly[i][1][j]+'^'+str(self.poly[i][2][j])
                else: # if power is 1
                    term+=self.poly[i][1][j]
            if eqn=='' or term[0]=='-':# If first term or the term is negative
                eqn+=term # Just append the term
            else:
                eqn+='+'+ term #append '+ term'
        return eqn
        
p1=Polynomial([[2,('x'),(2,)], [-4,('x','y'),(1,2)],[33,('x','y','z'),(2,2,1)]])
# print(p1.eval_poly({'x': 2,'y':-3,'z':4}))
print(p1.print_poly())

