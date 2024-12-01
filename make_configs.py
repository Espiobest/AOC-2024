import os

for i in range(2, 26):
    os.makedirs(f"day-{i}", exist_ok=True)
    template = '''with open('data.txt', 'r') as r:
    lines = r.read().splitlines()'''
    with open(os.path.join(f'day-{i}', f'day-{i}.py'), 'w') as f:
            f.write(template)        
    open(os.path.join(f'day-{i}', f'data.txt'), 'w').close()

print("Created folders!")
