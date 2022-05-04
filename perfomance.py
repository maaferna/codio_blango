directory_list = listdir("/")
i = 0
while True:
        print(f"Item at {i} is {directory_list[i]}")
        i = i + 1
        if i == len(directory_list):
                break


#Not optimizate 

i = 0
while True:
        directory_list = listdir("/")
        print(f"Item at {i} is {directory_list[i]}")
        i = i + 1
        if i == len(directory_list):
        break

for i, item in enumerate(listdir("/")):
        print(f"Item at {i} is {directory_list[i]}")

