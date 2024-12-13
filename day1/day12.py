team1 = []
team2 = []
sim = 0

with open('input11.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        team1.append(num1)
        team2.append(num2)

for i in range(len(team1)):
    number = team1[i]
    total = team2.count(number)
    sim +=  number*total
print(sim)