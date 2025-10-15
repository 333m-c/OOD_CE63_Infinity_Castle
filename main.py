import tracemalloc
import time
import os

tracemalloc.start()


def insertPeople(hotel,roomNumber,countManual):
    if roomNumber in hotel:
        return hotel , countManual , False
    hotel[roomNumber] = f"Insert Manual {countManual}"
    return hotel,countManual+1 , True

def findRoom(hotel:dict,roomNumber):
    if roomNumber in hotel:
        return f"Room {roomNumber} : {hotel[roomNumber]}"
    return f"Not Found room : {roomNumber}"

def exportFile(hotel:dict,countAdd):
    filePath = "./Hotel's room.txt"
    lastRound = countAdd-1
    sorted_hotel = dict(sorted(hotel.items()))
    if os.path.exists(filePath):
        os.remove(filePath)
    with open(filePath, "a", encoding="utf-8") as f:
        for roomNumber , info in sorted_hotel.items():
            channel , people , round = info.split()
            if channel[0] == "I":
                    f.write(f"Room : {roomNumber} : {channel} {people} {round}\n")
            else:
                if lastRound == int(round):
                    f.write(f"New!!! Room : {roomNumber} : Come from channel {channel} and person {people}\n")
                else:
                    f.write(f"Room : {roomNumber} : Come from channel {channel} and person {people}\n")
    fileSize = os.path.getsize(filePath)
    file_size_mb = fileSize / 1024 /1024
    return f"File size in MB: {file_size_mb:.2f} MB"

def removePeople(hotel:dict,roomNumber):
    if roomNumber in hotel:
        del hotel[roomNumber]
        return hotel , True
    return hotel , False
    


def seeMemory():
    current, peak = tracemalloc.get_traced_memory()
    return f"Current memory usage: {current / 1024 / 1024:.2f} MB"



def HashRoom(sequence_of_way : int, sequence_of_people : int):
    return int(int((sequence_of_way+sequence_of_people-1)*(sequence_of_way+sequence_of_people)/2-(sequence_of_way-1)))


def addRoom(hotel,channels,countCollision,channel,peoples,countAdd):
    
    start_time = time.perf_counter()
    if channel == 0 or peoples == 0:
        print("Peoples and channel cannot be '0'")
        return hotel,channel
    channel+=1
    if channel in channels:
        start = channels[channel]+1
        end = start+peoples
    else:
        start = 1
        end = peoples+1
    channels[channel] = end-1
    for people in range(start,end):
        key_room_number = HashRoom(channel,people)
        if key_room_number in hotel:
            info = hotel[key_room_number]
            key_room_collision = HashRoom(1,countCollision)
            hotel[key_room_collision] = info
            countCollision+=1
        hotel[key_room_number] = f"{channel-1} {people} {countAdd}"
    countAdd+=1
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time (Prepare phase): {elapsed_time:.10f} seconds")
    return hotel , channels ,countCollision,countAdd
    
    


hotel = {}
channels = {}
countManual = 1
countCollision = 1
countAdd = 1





print("==========================================================")
print("**************** Welcome to our H O T E L ****************")
print("==========================================================")
print()
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
        channel = int(input("Enter channel : "))
        peoples = int(input("Enter peoples in channel : "))
        hotel , channels,countCollision ,countAdd= addRoom(hotel,channels,countCollision,channel,peoples,countAdd)
        
        
    elif cmd == "d":
        targetRoom = input("Enter room number : ")
        start_time = time.perf_counter()
        print("Delete room . . .")
        targetRoom = int(targetRoom)
        hotel ,status = removePeople(hotel,targetRoom)
        if status:
            print(f"Delete room : {targetRoom} ")
        else:
            print("This room is Empty")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (Prepare phase): {elapsed_time:.10f} seconds")

    elif cmd == "f":
        targetRoom = input("Enter room number : ")
        start_time = time.perf_counter()
        targetRoom = int(targetRoom)
        print("Find room . . .")
        print(findRoom(hotel,targetRoom))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (Prepare phase): {elapsed_time:.10f} seconds")

    elif cmd == "i":
        targetRoom = input("Enter room number : ")
        print("Insert room . . .")
        start_time = time.perf_counter()
        targetRoom = int(targetRoom)
        hotel , countManual , status = insertPeople(hotel,targetRoom,countManual)
        if status:
            print("insert success")
        else:
            print(f"Room : {targetRoom} already have people")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (Prepare phase): {elapsed_time:.10f} seconds")
            


    elif cmd == "m":

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")

    elif cmd == "e":
        start_time = time.perf_counter()
        print(exportFile(hotel,countAdd))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time (Prepare phase): {elapsed_time:.10f} seconds")

            

    elif cmd == "q":

        print("Thank you!!")
        break

    else:

        print("Plese enter a,d,f,i,m,q,e !!")

    print()
