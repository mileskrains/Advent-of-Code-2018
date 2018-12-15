with open('input08-0.txt') as f:
    tree_data = [int(n) for n in f.readline().split()]

# tree_data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

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


def sum_children():
    child_ct = next(tree_iter)
    meta_ct = next(tree_iter)
    child_values = [sum_children() for _ in range(child_ct)]
    meta_values = [next(tree_iter) for _ in range(meta_ct)]
    if child_values:
        chm_sum = 0
        for m in meta_values:
            if 0 < m <= len(child_values):
                chm_sum += child_values[m - 1]
        return chm_sum
    else:
        return sum(meta_values)


tree_iter = iter(tree_data)
print(sum_children())