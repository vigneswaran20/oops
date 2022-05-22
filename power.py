class pow:
   def power(self, x, y):
        if x==0 or x==1 or y==1:
            return x
        val = self.power(x,y//2)
        if y%2 ==0:
            return val*val
        return val*val*x

x=int(input("Enter x value :"))
y=int(input("Enter y value :"))
print("pow(x,y) value is :",pow().power(x,y));
