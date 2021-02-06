V, T, S, D = map(int, input().split())

print(["Yes", "No"][V*T <= D <= V*S])