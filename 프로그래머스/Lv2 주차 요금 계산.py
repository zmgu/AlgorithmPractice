def solution(fees, records):
    btime, bfee, utime, ufee = fees
    precords = {}
    
    for record in records:
        time, car_no, act = record.split()
        time = int(time[:2]) * 60 + int(time[3:])
        
        if car_no not in precords:
            precords[car_no] = [0, time, 'IN']
        else:
            if act == "IN":
                precords[car_no][1] = time
                precords[car_no][2] = 'IN'
            elif act == "OUT":
                precords[car_no][0] += (time - precords[car_no][1])
                precords[car_no][1] = 0
                precords[car_no][2] = 'OUT'
                
    result = []
    for car_no, (ttime, ctime, act) in sorted(precords.items()):
        if ctime > 0:
            ttime += (23 * 60 + 59 - ctime)
        elif ctime == 0 and act == 'IN':
            ttime += 23 * 60 + 59
            
        if ttime <= btime:
            fee = bfee
        else:
            etime = ttime - btime
            fee = bfee + ((etime + utime - 1) // utime) * ufee
        
        result.append(fee)
    
    return result
