from objects import System


class Output():
    file_name = 'ouput.out'

    def __init__(self):
        self.file = open(self.file_name, 'w+')

    def generate_output(self):
        cache_servers = System.get_cache_servers()
        self.file.write(len(cache_servers) + '\n')
        for server in cache_servers:
            videos = server.get_videos()
            self.file.write(server.id)
            for video in videos:
                    self.file.write(' ' + video.id)
            self.file.write('\n')

