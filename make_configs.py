import os

for i in range(1, 26):
    i = str(i)
    os.makedirs(f"day-{i.zfill(2)}", exist_ok=True)
    template = '''with open('data.txt', 'r') as r:
    lines = r.read().splitlines()'''
    with open(os.path.join(f'day-{i.zfill(2)}', f'day-{i.zfill(2)}.py'), 'w') as f:
            f.write(template)        
    open(os.path.join(f'day-{i.zfill(2)}', f'data.txt'), 'w').close()

print("Created folders!")
