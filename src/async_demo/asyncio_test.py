import asyncio
import time


class ThrottleTestApp:

    def __init__(self):
        self._req_id_seq = 0
        self._futures = {}
        self._results = {}
        self.sem = asyncio.Semaphore()

    async def allow_requests(self, sem):
        """Permit 100 requests per second; call
           loop.create_task(allow_requests())
        at the beginning of the program to start this routine.  That call returns
        a task handle that can be canceled to end this routine.

        asyncio.Semaphore doesn't give us a great way to get at the value other
        than accessing sem._value.  We do that here, but creating a wrapper that
        adds a current_value method would make this cleaner"""

        while True:
            while sem._value < 100: sem.release()
            await asyncio.sleep(1)  # Or spread more evenly
                                    # with a shorter sleep and
                                    # increasing the value less

    async def do_request(self, req_id, obj):
        await self.sem.acquire()

        # this is the work for the request
        self.req_data(req_id, obj)

    def run(self, *awaitables):

        loop = asyncio.get_event_loop()

        if not awaitables:
            loop.run_forever()
        elif len(awaitables) == 1:
            return loop.run_until_complete(*awaitables)
        else:
            future = asyncio.gather(*awaitables)
            return loop.run_until_complete(future)

    def sleep(self, secs: [float]=0.02) -> True:

        self.run(asyncio.sleep(secs))
        return True

    def get_req_id(self) -> int:

        new_id = self._req_id_seq
        self._req_id_seq += 1
        return new_id

    def start_req(self, key):

        loop = asyncio.get_event_loop()
        future = loop.create_future()
        self._futures[key] = future
        return future

    def end_req(self, key, result=None):

        future = self._futures.pop(key, None)
        if future:
            if result is None:
                result = self._results.pop(key, [])
            if not future.done():
                future.set_result(result)

    def req_data(self, req_id, obj):
        # This is the method that "does" something
        self.req_data_end(req_id)
        pass

    def req_data_end(self, req_id):

        print(req_id, " has ended")
        self.end_req(req_id)

    async def req_data_batch_async(self, objs):

        futures = []
        FLAG = False

        for obj in objs:
            req_id = self.get_req_id()
            future = self.start_req(req_id)
            futures.append(future)

            if FLAG is False:
                FLAG = True
                start = time.time()

            self.do_request(req_id, obj)

        await asyncio.gather(*futures)
        elapsed = time.time() - start
        print("Roughly %s per second" % (len(objs)/elapsed))

        return futures


if __name__ == '__main__':

    asyncio.get_event_loop().set_debug(True)
    app = ThrottleTestApp()

    objs = [obj for obj in range(10000)]

    app.run(app.req_data_batch_async(objs))