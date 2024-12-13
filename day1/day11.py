team1 = []
team2 = []
total_distance = 0

with open('input11.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        team1.append(num1)
        team2.append(num2)

team1.sort()
team2.sort()


for i in range(len(team1)):
    total_distance += abs(team1[i]-team2[i])

print(total_distance)

