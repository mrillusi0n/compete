# steps: 00, 15, 30, 45

def get_floored(time):
    minutes = int(time.split(':')[1])
    return time[:3] + str(minutes - minutes % 15).zfill(2)

tests = ['15:30', '18:43', '08:48', '19:03']

for test in tests:
    print(get_floored(test))

