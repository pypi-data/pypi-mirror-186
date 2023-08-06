from dagline.utils import cli

def main():
    """Main executable function"""
    parser = cli.get_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()