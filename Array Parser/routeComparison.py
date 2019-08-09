inputRoutes = open("./routeInput.txt")

myRoute = inputRoutes.readline()
myRoute = myRoute.replace("\n", "")

onlineRoute = inputRoutes.readline()
onlineRoute = onlineRoute.replace("â‡’", ",")
onlineRoute = onlineRoute.replace("\n", "")

myrouteCounter = 0
onlineRouteCounter = 0

for char in myRoute:
    if char == ",":
        myrouteCounter += 1

myrouteCounter += 1

for char in onlineRoute:
    if char == ",":
        onlineRouteCounter += 1

onlineRouteCounter += 1

print(myrouteCounter)
print(myRoute)
print("\n")
print(onlineRouteCounter)
print(onlineRoute)
print("\n")
print("Same: " + str((myRoute == onlineRoute)))


