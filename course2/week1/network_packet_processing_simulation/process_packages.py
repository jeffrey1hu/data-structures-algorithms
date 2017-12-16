# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here

        # if buffer is empty, and wait for the pocket
        if not self.finish_time_:
            begin_time = request.arrival_time

            finish_time = begin_time + request.process_time
            self.finish_time_.append(finish_time)

            return Response(False, begin_time)
        # if buffer has queued packet
        else:
            begin_time = max(self.finish_time_[-1], request.arrival_time)
            finish_time = begin_time + request.process_time
            if len(self.finish_time_) == size:
                if self.finish_time_[0] > request.arrival_time:
                     return Response(True, -1)
                else:
                    self.finish_time_.append(finish_time)
                    self.finish_time_ = self.finish_time_[1:]
            else:
                self.finish_time_.append(finish_time)
            return Response(False, begin_time)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
