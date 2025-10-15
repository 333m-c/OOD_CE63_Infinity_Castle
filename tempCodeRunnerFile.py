
            tmp = hotel.dequeue()
            hotel.enqueue(tmp)
            arr.append(pow(2,tmp[0]-1)*pow(3,tmp[1]-1)*pow(5,tmp[2]-1)*pow(7,i))
        end = max(arr)
        if end < roomNumber:
            print(f"Not found room : {targetRoom}")
            continue
        status = search(roomNumber)
        if not status:
            print(f"Not found room : {targetRoom}")