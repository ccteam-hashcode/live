class Output():
    file_name = 'ouput.out'
    file = None
    system = None

    def __init__(self, system):
        self.file = open(self.file_name, 'w+')
        self.system = system

    def generate_output(self):
        self.file.write(len(self.system.get_cache_servers))
