class System:
    max_cache_size = 0
    cache_servers = []
    """ :type: list[CacheServer]"""
    endpoints = []
    """ :type: list[Endpoint]"""
    requests = []
    """ :type: list[Request]"""
    videos = []
    """ :type: list[Video]"""

    valid_endpoints = []
    valid_videos = []

    @staticmethod
    def get_cache_servers():
        return System.cache_servers

    @staticmethod
    def _clear():
        System.max_cache_size = 0
        System.cache_servers = []
        System.endpoints = []
        System.requests = []
        System.videos = []
        System.valid_endpoints = []
        System.valid_videos = []

    @staticmethod
    def filter_endpoints():
        for endpoint in System.endpoints:
            if len(endpoint.latency_cache) != 0:
                System.valid_endpoints.append(endpoint)

    @staticmethod
    def filter_big_videos():
        for video in System.videos:
            if video.size <= System.max_cache_size:
                System.valid_videos.append(video)
    @staticmethod
    def run():
        System.filter_endpoints()
        System.filter_big_videos()
        index = 0
        cache_server = System.cache_servers[index]
        for video in System.valid_videos:
            if video.size > cache_server.left_capacity:
                index += 1
                if index < len(System.cache_servers):
                    cache_server = System.cache_servers[index]
                else:
                    break
            cache_server.add_video(video)


class Video:
    def __init__(self, size, id):
        self.size = size
        self.id = id


class CacheServer:
    def __init__(self, left_capacity, id):
        self.videos = []
        self.left_capacity = left_capacity
        self.id = id

    def add_video(self, video):
        self.left_capacity -= video.size
        self.videos.append(video)

    def get_video(self, n):
        return self.videos[n]

    def get_videos(self):
        return self.videos


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
