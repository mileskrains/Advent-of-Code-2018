with open('input08-0.txt') as f:
    tree_data = [int(n) for n in f.readline().split()]

kind_stack = ['header']
metadata_sum = 0
for n in tree_data:
    kind = kind_stack.pop()
    if kind == 'header':
        child_ct = n
        kind_stack.append('meta_ct')
    if kind == 'meta_ct':
        for _ in range(n):
            kind_stack.append('meta')
        for _ in range(child_ct):
            kind_stack.append('header')
    if kind == 'meta':
        metadata_sum += n

print(metadata_sum)