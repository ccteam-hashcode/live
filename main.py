from objects import System, Video, Endpoint, CacheServer, Request
from output import Output


class Parser(object):
    @staticmethod
    def parse(filename):
        with open(filename) as infile:
            init_line = infile.readline()
            c_video, c_endpoint, c_request, c_cache, cache_size = init_line.split(' ')

            System.max_cache_size = int(cache_size)

            i = 0
            for video_size in infile.readline().split(' '):
                System.videos.append(Video(int(video_size), i))
                i += 1

            for a in range(int(c_cache)):
                System.cache_servers.append(CacheServer(int(cache_size), a))

            for e_idx in range(int(c_endpoint)):
                latency_to_center, endpoint_caches_count = infile.readline().split(' ')
                e = Endpoint(int(latency_to_center), e_idx)

                for a in range(int(endpoint_caches_count)):
                    cache_id, latency = infile.readline().split(' ')
                    e.add_cache(System.cache_servers[int(cache_id)], int(latency))
                    System.cache_servers[int(cache_id)].endpoints.append(e_idx)
                System.endpoints.append(e)

            for b in range(int(c_request)):
                video_id, endpoint, requests = infile.readline().split(' ')
                System.requests.append(Request(int(video_id), int(endpoint), int(requests)))
                System.endpoints[int(endpoint)].videos[int(video_id)] = int(requests)

        pass


def main():
    Parser.parse('me_at_the_zoo.in')
    System.run()
    output = Output()
    output.generate_output('me_at_the_zoo.out')
    System._clear()

    # Parser.parse('kittens.in')
    # System.run()
    # output = Output()
    # output.generate_output('kittens.out')
    # System._clear()
    #
    # Parser.parse('trending_today.in')
    # System.run()
    # output = Output()
    # output.generate_output('trending_today.out')
    # System._clear()
    #
    # Parser.parse('videos_worth_spreading.in')
    # System.run()
    # output = Output()
    # output.generate_output('videos_worth_spreading.out')
    # System._clear()


if __name__ == '__main__':
    main()
