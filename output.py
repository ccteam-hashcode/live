from objects import System


class Output():

    def generate_output(self, ouput_file):
        file = open(ouput_file, 'w+')

        cache_servers = System.get_cache_servers()
        file.write(str(len(cache_servers)) + '\n')
        for server in cache_servers:
            videos = server.get_videos()
            file.write(str(server.id))
            for video in videos:
                    file.write(' ' + str(video.id))
            file.write('\n')

