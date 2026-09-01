
class Stack :              #Creating Stack 
    def __init__(self):
        self.top=-1
        self.ST=[0]*100      #Stack size is fixed to 100 , not more than 100 elements are possible
    

    def push(self,x):
        if self.top==99:     #Size of queue 5 , therefore index 4
            print("Stack is overflow....")
            return
        self.top=self.top+1   #Increment your stack index

        self.ST[self.top]=x   #We need to add element 'x' in Rear side and it must be stored inside qt only.


    def pop(self):    #Deletion is performed at front end
        if self.top==-1:
            print("Nothing to  print..")   #Empty
            return
        else:
            x=self.ST[self.top]
            self.top=self.top-1  #Dequeue operation will be donr from front side , so after deleting element at index 0 , next element will we get deleted from index 1 and so on. That's why +1 is there.
        return x

    def peek(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            print("Top Element =", self.ST[self.top])


    def display(self):
        if self.top==-1:
            print("Nothing to print")
            return
        for i in range(self.top,-1,-1):  #Id queue is not empty then we have to retrive all the elements and for that we are using for loop
            print(self.ST[i],end=" ")
        print()

q=Stack()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch=int(input("Enter the choice :"))

    if ch==1:
        x=int(input("Enter Element :"))
        q.push(x)
    elif ch==2 :
        x=q.pop()
        if x is not None:
            print("Deleted Element =",x)
    elif ch==3:
        q.peek()
    elif ch==4:
        q.display()
    elif ch==5:
        break
    else:
        print("Invalid Choice")