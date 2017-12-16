# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda s: s.start)
    points = []
    #write your code here
    while segments:
        signed_point = 0
        temp_start = segments[0].start
        temp_end = segments[0].end
        for i, s in enumerate(segments):
            if s.start <= temp_end:
                temp_start = s.start
                temp_end = min(s.end, temp_end)
                signed_point = i
            else:
                break
        points.append(temp_start)
        segments = segments[signed_point+1:]

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
