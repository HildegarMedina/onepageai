from args import parser_arguments

def main():
    parser = parser_arguments()
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()
