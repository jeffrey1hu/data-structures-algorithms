# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, s, bkt):
        # print('yes' if was_found else 'no')
        is_found = False
        if not self.elems[bkt]:
            return is_found
        else:
            for cur in self.elems[bkt]:
                if cur == s:
                    is_found = True
                    return is_found
        return is_found

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if self.elems[query.ind]:
                self.write_chain([cur for cur in reversed(self.elems[query.ind])])
            else:
                print("")
        else:
            # try:
            #     ind = self.elems.index(query.s)
            # except ValueError:
            #     ind = -1
            bkt = self._hash_func(query.s)
            is_found = self.write_search_result(query.s, bkt)
            if query.type == 'find':
                if is_found:
                    print("yes")
                else:
                    print("no")
            elif query.type == 'add':
                if not is_found:
                    self.elems[bkt].append(query.s)
            else:
                if is_found:
                    self.elems[bkt].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
