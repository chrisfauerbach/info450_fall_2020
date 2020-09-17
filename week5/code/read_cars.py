import json
cars = []
with open("data.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        parts = line.split(",")
        cars.append({ "id": parts[0],
                      "color": parts[1],
                      "make": parts[2],
                      "model": parts[3]
                      })
# print(cars)
# print(json.dumps(cars))
print(json.dumps(cars, sort_keys=True, indent=4))
