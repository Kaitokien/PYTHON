n = int(input())
a = ["name", "Accepted", "Submitted"]
arr = []
for _ in range(n):
    mark = []
    name = input()
    x = list(map(int, input().split()))
    mark.append(name)
    mark.append(x[0])
    mark.append(x[1])
    c = dict(zip(a, mark))
    arr.append(c)
arr.sort(key = lambda x : (-x.get("Accepted"), x.get("Submitted"), x.get("name")))
for i in range(n):
    print(arr[i].get("name"), arr[i].get("Accepted"), arr[i].get("Submitted"))