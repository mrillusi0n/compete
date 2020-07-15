
# don't move the trees

def sort_heights(a):
    tree_pos = [i for i, j in enumerate(a) if j == -1]
    people = []

    for i, j in zip(tree_pos[:-1], tree_pos[1:]):
        people.extend(a[i + 1:j])
    people.extend(a[tree_pos[-1] + 1:])

    print(tree_pos)
    return sorted(people)


t = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sort_heights(t))
