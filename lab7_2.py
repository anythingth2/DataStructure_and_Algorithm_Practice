k = 20
b = [20,10,5,5,3,2,20,10]
def matching(price,pack,currentIndex,orderList):
    if len(orderList) != 0:
        currentIndex += 1
        price += orderList[currentIndex]
        pack.append(orderList[currentIndex])
            
        if price < k:
            if matching(price,pack,currentIndex,orderList) != 'over':
                
            else:

                return
        elif price > k:
            return 'over'
        else:
            print(pack)
            return 'full'
    else:
