piersTravelEvents = str(input()).split(" ")

piers = int(piersTravelEvents[0])
travel = int(piersTravelEvents[1])
events = int(piersTravelEvents[2])
ids = []

class customers():
    def __init__(self, customerID: int, taps: list):
        self.customerID = customerID
        self.taps = taps

    def add_tap(self, tap):
        self.taps.append(tap)

    def get_ID(self):
        return self.customerID
    
    def get_taps(self):
        return self.taps
    
    def remove_taps(self):
        try:
            self.taps.reverse()
            self.taps.pop()
            self.taps.pop()
            self.taps.reverse()
            return 0
        except:
            return 1

    def calc_trip(self):
        sum = 0

        while len(self.taps) != 0:
            try:
                total = int(self.taps[0]) - int(self.taps[1])
            except:
                total = 100

            if total < 0:
                total = total * -1

            if total == 0:
                sum = sum + 100

            self.remove_taps()

            sum = sum + total

        return sum

customer = []

for event in range(events):
    tapEvents = str(input()).split(" ")
    customerID = tapEvents[1]
    Pier = tapEvents[0]
    shouldAdd = True

    for cust in customer:
        if cust.get_ID() == customerID:
            cust.add_tap(Pier)
            shouldAdd = False
            break
        else:
            shouldAdd = True
    
    if shouldAdd:
        shouldAdd = False
        customer.append(customers(customerID, [Pier]))
        ids.append(customerID)
    

not_found = True

for id in ids:
    for cust in customer:
        if id == cust.get_ID():
            not_found = False
            break
        else:
            not_found = True
    if not_found:
        customer.append(customers(id,[]))

customer.sort(key=customers.get_ID())

sum = ""

for custom in customer:
    trip = custom.calc_trip()
    sum = sum + str(trip) + " "

sum = sum[:-1]
print(sum)