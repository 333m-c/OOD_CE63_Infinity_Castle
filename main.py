import tracemalloc
import time
import os

tracemalloc.start()

class Queue:
    def __init__(self, datas = None):
        self.items = []
        if datas:
            for data in datas:
                self.enqueue(data)
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)
        
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def reverse(self):
        self.items = self.items[::-1]
    
    
    def clear(self):
        self.items=[]

    def __str__(self):
        return str(self.items)


def findRoom(n: int, limits=None):
    primes = [2, 3, 5, 7]
    exponents = []

    for p in primes:
        count = 0
        while n % p == 0:
            n //= p
            count += 1

        if limits and p in limits and count > limits[p]:
            return False

        exponents.append(count)

    if n != 1:
        return False

    return exponents


            
def search(roomNumber):
    isFound = False
    if roomNumber in delRoom:
        return False
    else:
        for index in range(hotel.size()):
            arr = hotel.dequeue()
            hotel.enqueue(arr)
            dic = {
                2:arr[0]-1,
                3:arr[1]-1,
                5:arr[2]-1,
                7:index
            }
            result = findRoom(roomNumber,dic)
            if result:
                result = [i+1 for i in result]
                return (f"Room : {roomNumber} stayed by : people {result[0]} , bus {result[1]} , boat {result[2]} , round {hotel.size()-(result[3]-1)}")
        if not isFound:
            return f"Room : {roomNumber} is Empty"

inp = []

print()
print("Welcome to our H O T E L ")
print()
print("==========================================================")
print()
print("การเดินทาง เรือ > รถบัส > คน")
inp1 = int(input("จำนวนเรือ   : "))
inp2 = int(input("จำนวนรถบัส  : "))
inp3 = int(input("จำนวนคน    : "))
start_time = time.perf_counter()
print()
print("==========================================================")
print()
print("Prepare phase")
print()
print("Prepare . . .")
print()
inp.extend([inp1, inp2, inp3])
hotel= Queue()
hotel.enqueue(inp)


delRoom = []
addRoom= []

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time (Prepare phase): {elapsed_time:.10f} seconds")

print()


while True:
    print("==========================================================")
    cmd = input("""
Command :
    a : Add tourists
    d : Delete room
    f : Find room
    i : Insert room
    m : See memory
    e : Export file
    q : Quit

Enter command : """)
    print()
    print("==========================================================")
    print()
    if cmd == "a":
        print("Add tourists")
        inp1 = int(input("จำนวนเรือ   : "))
        inp2 = int(input("จำนวนรถบัส  : "))
        inp3 = int(input("จำนวนคน    : "))
        print()
        print("==========================================================")
        print()
        start_time = time.perf_counter()
        print("Add room . . .")
        arr = []
        arr.extend([inp1, inp2, inp3])
        hotel.reverse()
        hotel.enqueue(arr)
        print(f"Already add {arr}")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (add): {elapsed_time:.10f} seconds")
        start_time = time.perf_counter()
        print("Sort room . . .")
        hotel.reverse()
        print(f"Already sort {hotel}")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (sort): {elapsed_time:.10f} seconds")
        
    elif cmd == "d":
        targetRoom = input("Enter room number : ")
        print("Delete room . . .")
        start_time = time.perf_counter()
        targetRoom = int(targetRoom)
        if targetRoom in addRoom:
            addRoom.remove(targetRoom)
        if not targetRoom in delRoom:
            delRoom.append(targetRoom)
            print(f"Room : {targetRoom} is deleted")
        else:
            print(f"Room : {targetRoom} already delete")
        
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (del): {elapsed_time:.10f} seconds")

    elif cmd == "f":
        targetRoom = input("Enter room number : ")
        print("Find room . . .")
        start_time = time.perf_counter()
        roomNumber = int(targetRoom)
        status = search(roomNumber)
        if not status:
            print(f"Not found room : {targetRoom}")
        else:print(status)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (find): {elapsed_time:.10f} seconds")

    elif cmd == "i":
        targetRoom = input("Enter room number : ")
        print("Insert room . . .")
        start_time = time.perf_counter()
        targetRoom = int(targetRoom)
        arr = []
        for room in addRoom:
            arr.append(room)
        for i in range(hotel.size()):
            tmp = hotel.dequeue()
            hotel.enqueue(tmp)
            arr.append(pow(2,tmp[0]-1)*pow(3,tmp[1]-1)*pow(5,tmp[2]-1)*pow(7,i))
        end = max(arr)
        if end >= targetRoom:
            print(f"Room : {targetRoom} already have")
            continue
        if targetRoom in delRoom:
            delRoom.remove(targetRoom)
        if not targetRoom in addRoom:
            print(f"Insert room : {targetRoom}")
            addRoom.append(targetRoom)
        else:
            print(f"insert Room : {targetRoom}")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (insert): {elapsed_time:.10f} seconds")

    elif cmd == "m":

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")

    elif cmd == "e":
        print("Export File . . .")
        start_time = time.perf_counter()
        arr = []
        for room in addRoom:
            arr.append(room)
        for i in range(hotel.size()):
            tmp = hotel.dequeue()
            hotel.enqueue(tmp)
            arr.append(pow(2,tmp[0]-1)*pow(3,tmp[1]-1)*pow(5,tmp[2]-1)*pow(7,i))
        end = max(arr)
        if os.path.exists("./Hotel's room.txt"):
            os.remove("./Hotel's room.txt")
        with open("Hotel's room.txt", "a", encoding="utf-8") as f:
            for i in range(1,end+1):
                status = search(i)
                if status:
                    f.write(f"{status}\n")
        filePath = "./Hotel's room.txt"
        fileSize = os.path.getsize(filePath)
        file_size_mb = fileSize / 1024 /1024
        print()
        print("Done!!")
        print(f"File size in MB: {file_size_mb:.2f} MB")
        print()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (export file): {elapsed_time:.10f} seconds")

            

    elif cmd == "q":

        print("Thank you!!")
        break

    else:

        print("Plese enter a,d,f,i,m,q,e !!")

    print()
