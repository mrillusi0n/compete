'''
Check if the chaos in the queue is too much.
'''

def minimumBribes(q):
    total = 0
    for i, n in enumerate(q):
        diff = i + 1 - n
            if diff < -2:
                print('Too chaotic')
                    return

            if diff > 0:
                total += diff
            else if diff < 0:
                total += diff + 1
    print(total)

minimumBribes((1, 2, 5, 3, 7, 8, 6, 4))
