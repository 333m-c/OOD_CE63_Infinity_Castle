for room in addRoom:
            arr.append(room)
        for i in range(hotel.size()):
            tmp = hotel.dequeue()
            hotel.enqueue(tmp)
            arr.append(pow(2,tmp[0]-1)*pow(3,tmp[1]-1)*pow(5,tmp[2]-1)*pow(7,i))
        end = max(arr)
        if end >= targetRoom:
            print(f"Room : {targetRoom} already have")