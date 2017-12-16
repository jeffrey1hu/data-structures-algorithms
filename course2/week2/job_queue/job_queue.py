# python3
from collections import defaultdict

class MinHeap:
    def __init__(self, arr, size, max_size):
        self._data = arr
        self.size = size
        self.max_size = max_size
        for i in range(self.size // 2, 0, -1):
            # print("sift down {}".format(i))
            self.sift_down(i)


    def sift_up(self, i):
        while i > 1 and self._data[self.parent(i) - 1] > self._data[i - 1]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        # i is 1 based idx
        max_idx = i
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        # print("i {}, left {}, right {}".format(max_idx, left_child, right_child))

        if left_child <= self.size and self._data[left_child-1] < self._data[max_idx-1]:
            max_idx = left_child

        if right_child <= self.size and self._data[right_child-1] < self._data[max_idx-1]:
            max_idx = right_child

        if i != max_idx:
            self.swap(i, max_idx)
            self.sift_down(max_idx)

    def swap(self, i, j):
        # print("add swap {}".format((i, j)))
        # self.swaps.append((i-1, j-1))
        self._data[i-1], self._data[j-1] = self._data[j-1], self._data[i-1]

    def extract_min(self):
        assert self.size > 0, "the heap is empty"
        result = self._data[0]
        self.size -= 1
        self._data[0] = self._data[self.size]
        self._data[self.size] = result
        self.sift_down(1)
        return result

    def get_min(self):
        return self._data[0]

    def insert(self, ele):
        assert self.size < self.max_size, "exceed the maximum size"
        self.size += 1
        self._data[self.size - 1] = ele
        self.sift_up(self.size)

    @staticmethod
    def left_child(i):
        return 2 * i

    @staticmethod
    def right_child(i):
        return 2*i + 1

    @staticmethod
    def parent(i):
        return i // 2


class PriorityQueue(MinHeap):
    def __init__(self, n, max_size):
        init_queue = [None] * max_size
        init_queue[:n] = list(range(n))
        size = n
        MinHeap.__init__(self, init_queue, size, max_size)


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.

        current_ts = 0
        end_ts = 0
        thread_queue = PriorityQueue(self.num_workers, self.num_workers)
        # print("threads {}".format(thread_queue._data))
        process_queue = PriorityQueue(0, self.num_workers)
        finished_jobs = defaultdict(list)
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        for i, job_cost in enumerate(self.jobs):
            if thread_queue.size == 0:
                # print("there is no more free thread left")
                coming_finish_ts = process_queue.get_min()
                # print("check after extract min , process_queue size {}".format(process_queue.size))
                for _thread in finished_jobs.pop(coming_finish_ts, []):
                    process_queue.extract_min()
                    thread_queue.insert(_thread)
                finished_jobs[coming_finish_ts] = []
                current_ts = coming_finish_ts

            thread_id = thread_queue.extract_min()

            # print("thread_id {}, thread left {}, size {}, end_ts {}".format(thread_id, thread_queue._data, thread_queue.size, end_ts))
            self.assigned_workers[i] = thread_id
            self.start_times[i] = current_ts

            end_ts = current_ts + job_cost
            process_queue.insert(end_ts)
            finished_jobs[end_ts].append(thread_id)
            # print("process_queue size {}".format(process_queue.size))


        # self.assigned_workers = [None] * len(self.jobs)
        # self.start_times = [None] * len(self.jobs)
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

