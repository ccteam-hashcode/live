from objects import System


class Output():

    def generate_output(self, ouput_file):
        print('generating file' + ouput_file)
        file = open(ouput_file, 'w+')

        cache_servers = System.get_cache_servers()
        file.write(str(len(cache_servers)) + '\n')
        latency_left = []
        for server in cache_servers:
            videos = server.get_videos()
            file.write(str(server.id))
            for video in videos:
                    file.write(' ' + str(video.id))
            file.write('\n')
            latency_left.append(server.left_capacity)
        print(max(latency_left))
        file.close()

