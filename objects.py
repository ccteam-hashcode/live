class Video:
    def __init__(self, size):
        self.size = size


class CacheServer:
    def __init__(self):
        self.videos = []
        self.capacity = 0


class Endpoint:
    def __init__(self):
        self.latency_cache = []
        self.latency_center = 0


class Request:
    def __init__(self):
        self.video = None
        self.endpoint = 1
        self.count = 0
