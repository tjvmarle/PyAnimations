import time

# TODO: Move to some central library


class FpsTimer:

    def __init__(self, fps):
        self.prev_time = time.time()
        self.framerate = fps
        self.framecounter = 0
        self.waitcounter = 0

    def endFrame(self):  # Wait untill the current frame ends for the given framerate
        curr_time = time.time()
        spf = 1 / self.framerate
        wait_time = self.prev_time + spf - curr_time
        self.prev_time += spf  # This prevents fps slowdown due to overhead

        # Monitor fps usage per second
        self.framecounter += 1
        self.waitcounter += wait_time if wait_time > 0 else 0
        if self.framecounter == self.framerate:
            self.framecounter = 0
            print("Frame usage: ", (1 - self.waitcounter) * 100, "%")
            self.waitcounter = 0

        if wait_time > 0:
            time.sleep(wait_time)
