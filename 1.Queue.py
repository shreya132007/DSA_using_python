# It implements a simple (linear) Queue using a Python list.
# Queue follows FIFO

class Queue :              #Creating Queue  
    def __init__(self):
        self.F=-1
        self.R=-1
        self.QT=[0]*5      #Queue size is fixed to 5 , not more than 5 elements are possible
    

    def insert(self,x):
        if self.R==4:     #Size of queue 5 , therefore index 4
            print("Queue is overflow....")
            return
        self.R=self.R+1   #Updating rear

        self.QT[self.R]=x   #We need to add element 'x' in Rear side and it must be stored inside qt only.

        if self.F==-1:   #Updating front
            self.F=0

    def delete(self):    #Deletion is performed at front end
        if self.F==-1:
            print("Nothing to  print..")
            return
        else:
            y=self.QT[self.F]

        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1  #Dequeue operation will be donr from front side , so after deleting element at index 0 , next element will we get deleted from index 1 and so on. That's why +1 is there.
        return y
    
    def display(self):
        if self.F==-1:
            print("Nothing to print")
            return
        for i in range(self.F,self.R+1):  #Id queue is not empty then we have to retrive all the elements and for that we are using for loop
            print(self.QT[i])

q=Queue()

while True:
    ch=int(input("Enter the choice : \n1. For insert \n2.For delete \n3. For display\n"))
    if ch==1:
        data = input("Enter data to insert in queue :")
        q.insert(data)
    elif ch==2:
        print(f"The deleted node is {q.delete()}")
    elif ch==3:
        q.display()
    else :
        break