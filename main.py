from args import parser_arguments
from services.onepagebuilder import OnePageBuilder

def main():
    args = parser_arguments()
    onepagebuilder = OnePageBuilder('openai')
    onepagebuilder.build(args)

if __name__ == "__main__":
    main()
