class System:
    max_cache_size = 0
    cache_servers = []
    endpoints = []
    requests = []
    videos = []

    @staticmethod
    def get_cache_servers():
        return System.cache_servers


class Video:
    def __init__(self, size, id):
        self.size = size
        self.id = id


class CacheServer:
    def __init__(self, left_capacity, id):
        self.videos = []
        self.left_capacity = left_capacity
        self.id = id

    def add_video(self, size, id):
        v = Video(size, id)
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
    def __init__(self, video_id, endpoint_id, count):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.count = count
