# Given a time frame and two lists of tuples representing time
# slots that are occupied for two people, output a list of time slots that
# are free for both.

from functools import total_ordering
from itertools import product, starmap

@total_ordering
class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def to_minutes(self):
        return self.hours * 60 + self.minutes

    @classmethod
    def from_str(cls, strf):
        return cls(*map(int, strf.split(':')))

    def __sub__(self, other):
        return self.__class__(*divmod(self.to_minutes() - other.to_minutes(), 60))

    def __lt__(self, other):
        return self.hours == other.hours and self.minutes < other.minutes or self.hours < other.hours

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __repr__(self):
        return '{:02}:{:02}'.format(self.hours, self.minutes)


@total_ordering
class TimeInterval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def union(self, other):
        # assume they overlap
        start = min(self.start, other.start)
        end = max(self.end, other.end)

        return self.__class__(start, end)

    def intersect(self, other):
        start = max(self.start, other.start)
        end = min(self.end, other.end)

        return self.__class__(start, end)

    def overlaps(self, other):
        return not (self.start >= other.end or self.end <= other.start)

    def __bool__(self):
        return self.end > self.start

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        return self.end < other.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return '{} -> {}'.format(self.start, self.end)


def get_free_slots(window, intervals):
    slots = [TimeInterval(window.start, intervals[0].start)]

    for a, b in zip(intervals[:-1], intervals[1:]):
        slots.append(TimeInterval(a.end, b.start))

    slots.append(TimeInterval(intervals[-1].end, window.end))

    return filter(None, slots)

def solve(schedule_a, schedule_b):
    mix = []

    for a, b in zip(schedule_a, schedule_b):
        smaller = a if a < b else b
        larger = a if a >= b else b

        mix.append(smaller)
        mix.append(larger)

    res = []
    for a, b in zip(mix[:-1], mix[1:]):
        if a.overlaps(b):
            continue
        res.append(TimeInterval(a.end, b.start))

    return res


def main():
    ind_a = [
        ("08:00", "09:30"),
        ("12:00", "13:00"),
        ("14:45", "16:00"),
    ]

    ind_b = [
        ("09:00", "10:00"),
        ("11:00", "12:15"),
        ("12:15", "13:00"),
    ]

    res = [
        ("10:00", "11:00"),
        ("13:00", "14:45"),
        ("16:00", "17:00"),
    ]

    one = [TimeInterval(*[Time.from_str(x) for x in inter]) for inter in ind_a]
    two = [TimeInterval(*[Time.from_str(x) for x in inter]) for inter in ind_b]
    res = [TimeInterval(*[Time.from_str(x) for x in inter]) for inter in res]

    one_free = get_free_slots(TimeInterval(Time.from_str('8:00'), Time.from_str('17:00')), one)
    two_free = get_free_slots(TimeInterval(Time.from_str('8:00'), Time.from_str('17:00')), two)
    
    # print(*[a.intersect(b) for a, b in product(one_free, two_free) if a.overlaps(b)], sep='\n')
    # print(*filter(None, starmap(TimeInterval.intersect, product(one_free, two_free))))

    print(solve(one, two))


if __name__ == '__main__':
    main()
