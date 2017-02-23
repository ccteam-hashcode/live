class System:
    def __init__(self):
        self.cache_servers = []
        self.endpoints = []
        self.requests = []


class Video:
    def __init__(self, size):
        self.size = size


class CacheServer:
    def __init__(self, capacity):
        self.videos = []
        self.capacity = capacity

    def add_video(self, size):
        v = Video(size)
        self.videos.append(v)

    def get_video(self, n):
        return self.videos[n]


class Endpoint:
    def __init__(self, latency_center):
        self.latency_cache = []
        self.latency_center = 0


class Request:
    def __init__(self):
        self.video = None
        self.endpoint = 1
        self.count = 0
