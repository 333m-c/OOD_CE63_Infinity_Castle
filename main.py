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



def hash(a,b):
    return pow(2,a) * pow(3,b) 



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



def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_at_index(index: int):
    count = 0
    num = 1
    while True:
        num += 1
        if is_prime(num):
            count += 1
            if count == index:
                return num
            
def serch(roomNumber):
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
            # print(result,dic)
            if result:
                result = [i+1 for i in result]
                return (f"Room : {roomNumber} stayed by : people {result[0]} , channel {result[1]} , way {result[2]} , round {hotel.size()-(result[3]-1)}")
        if not isFound:
            return f"Room : {roomNumber} is Emthy"


inp = input("Welcome to our H O T E L (format : x/x/x): ").split("/")
start_time = time.perf_counter()
print()
print("==========================================================")
print()
print("Prepare phase")
print()
print("Prepare . . .")
print()
inp = [int(i) for i in inp]
while len(inp) < 3:
    inp.append(1)
hotel= Queue()
# result = 1
# for index in range(len(inp)):
#     result*= pow(prime_at_index(index+1),inp[index])
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
Add tourists (a) Delete room (d) Find room (f)
Insert room (i)  See memory (m)  Export file (e)
                    Quit (q)

Enter command : """)
    print()
    print("==========================================================")
    print()
    if cmd == "a":
        arr = input("Welcome to our H O T E L (format : x/x/x): ")
        start_time = time.perf_counter()
        print("Add room . . .")
        text =arr
        arr = arr.split("/")
        arr = [int(i) for i in arr]
        while len(arr) < 3:
            arr.append(1)
        # result = 1
        # for index in range(len(arr)):
        #     result*= pow(prime_at_index(index+1),inp[index])
        hotel.reverse()
        hotel.enqueue(arr)
        #print(hotel)
        print(f"Already add {text}")
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
        
    # elif cmd[0] == "s":
    #     start_time = time.perf_counter()
    #     print("sort")
    #     end_time = time.perf_counter()
    #     elapsed_time = end_time - start_time
    #     print(f"Execution time: {elapsed_time:.4f} seconds")

    elif cmd == "f":

        targetRoom = input("Enter room number : ")
        print("Find room . . .")
        start_time = time.perf_counter()
        roomNumber = int(targetRoom)
        status = serch(roomNumber)
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
        if targetRoom in delRoom:
            delRoom.remove(targetRoom)
        if not targetRoom in addRoom:
            print(f"Insert room : {targetRoom}")
            addRoom.append(targetRoom)
        else:
            print(f"Room : {targetRoom} already insert")
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
                status = serch(i)
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
    print("==========================================================")
    print()
    print()
