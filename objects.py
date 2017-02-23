class System:
    def __init__(self):
        self.max_cache_size = 0
        self.cache_servers = []
        self.endpoints = []
        self.requests = []


class Video:
    def __init__(self, size, id):
        self.size = size
        self.id = id


class CacheServer:
    def __init__(self, left_capacity, id):
        self.videos = []
        self.left_capacity = left_capacity
        self.id = id

    def add_video(self, size):
        v = Video(size)
        self.videos.append(v)

    def get_video(self, n):
        return self.videos[n]


class CacheLatency:
    def __init__(self, latency, cache):
        self.latency = latency
        self.cache = cache


class Endpoint:
    def __init__(self, latency_center):
        self.latency_cache = []
        self.latency_center = latency_center

    def add_cache(self, cache_server: CacheServer, latency: int):
        self.latency_cache.append(CacheLatency(latency, cache_server))


class Request:
    def __init__(self):
        self.video = None
        self.endpoint = 1
        self.count = 0
