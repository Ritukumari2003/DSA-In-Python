
def simple_hash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    return total

keys = ['bat', 'ball', 'tab']
for key in keys:
    hash_value = simple_hash(key)
    print(f'{key}: {hash_value % 5}')