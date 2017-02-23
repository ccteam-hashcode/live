import operator


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
    avg_size = 0

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

        results = {}
        for cache in System.cache_servers:
            for endpoint in cache.endpoints:
                for video_id, count in System.endpoints[endpoint].videos.items():
                    score = count * (System.endpoints[endpoint].latency_center - System.endpoints[endpoint].latency_cache[cache.id])
                    key = (str(video_id) + "_" + str(cache.id))
                    if key in results:
                        results[key] = results[key] + score
                    else:
                        results[key] = score
        sorted_x = sorted(results.items(), key=operator.itemgetter(1), reverse=True)

        for item in sorted_x:
            pair = item[0].split('_')
            cache = System.cache_servers[int(pair[1])]
            video = System.valid_videos[int(pair[0])]
            if cache.left_capacity >= video.size:
                cache.add_video(video)
        pass


class Video:
    def __init__(self, size, id):
        self.size = size
        self.id = id


class CacheServer:
    def __init__(self, left_capacity, id):
        self.videos = []
        self.left_capacity = left_capacity
        self.id = id
        self.endpoints = []

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

    def __init__(self, latency_center, id):
        self.latency_center = latency_center
        self.id = id
        self.videos = {}
        self.latency_cache = {}

    def add_cache(self, cache_server: CacheServer, latency: int):
        self.latency_cache[cache_server.id] = latency


class Request:
    def __init__(self, video_id, endpoint_id, count):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.count = count
