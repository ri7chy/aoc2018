a=open('13.in').read().split('\n')
a.pop(len(a)-1)
a=[[x for x in y] for y in a]
#for x in a: print(x)

class cart:
    def __init__(self,col,row,direction):
        self.c,self.r=col,row
        if direction=='<': self.d=3
        elif direction=='^': self.d=0
        elif direction=='>': self.d=1
        elif direction=='v': self.d=2
        self.i=0
        print('cart found',self.c,self.r)
    def right(self):
        return (self.d+1)%4
    def left(self):
        return (self.d-1)%4
    def walk(self):
        DR=[-1,0,1,0]
        DC=[0,1,0,-1]
        if a[self.r][self.c]=='+': self.intersection()
        elif a[self.r][self.c]=='/' and self.d in[0,2]: self.d=self.right()
        elif a[self.r][self.c]=='\\' and self.d in [1,3]: self.d=self.right()
        elif a[self.r][self.c]=='/' and self.d in[1,3]: self.d=self.left()
        elif a[self.r][self.c]=='\\' and self.d in [0,2]: self.d=self.left()
        self.c,self.r=self.c+DC[self.d],self.r+DR[self.d]
    def intersection(self):
        self.i=(self.i+1)%3
        if self.i==1: self.d=self.left()
        elif self.i==0: self.d=self.right()

def findcarts():
    carts=[]
    for r in range(len(a)):
        for c in range(len(a[r])):
            if a[r][c]in ['<','>','v','^']:
                carts.append(cart(c,r,a[r][c]))
                if a[r][c] in ['<','>']: a[r][c]='-'
                elif a[r][c] in ['v','^']: a[r][c]='|'
    return carts
def isCart(r,c,carts):
    cart=-1
    for x in carts:
        if x.c==c and x.r==r: cart=x.d
    return cart
def output(carts,k):
    out=''
    D=['^','>','v','<']
    for r in range(len(a)):
        for c in range(len(a[r])):
            if isCart(r,c,carts)==-1:out+=a[r][c]
            else: out+=D[isCart(r,c,carts)]
        out+='\n'
    print(out)
def checkCollision(carts):
    for x in carts:
        for y in carts:
            if y.c==x.c and y.r==x.r and x.d!=y.d: return [True,x.c,x.r]
def main():
    carts=findcarts()
    while 1:
        for x in carts:
            x.walk()
            k=checkCollision(carts)
        #output(carts,k)
        if k!=None:
            print('part1', k[1],k[2])
            break
if __name__ == '__main__':
    main()
