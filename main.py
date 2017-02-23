from objects import System
from output import Output


def main():
    system = System()
    output = Output(system)
    output.generate_output()
    pass

if __name__ == '__main__':
    main()
