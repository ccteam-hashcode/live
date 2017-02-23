class Parser(object):

    @staticmethod
    def parse(filename):
        with open(filename) as infile:
            init_line = infile.readline()
            c_video, c_endpoint, c_request, c_cache,  cache_size = init_line.split(' ')

            for video_size in infile.readline().split(' '):
                pass

