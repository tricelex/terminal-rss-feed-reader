import feedparser
import argparse


def get_url():
    parser = argparse.ArgumentParser(description="enter the rss url")

    # Add the arguments
    parser.add_argument('Url',
                        metavar='url',
                        type=str,
                        help='the path to the rss')

    args = parser.parse_args()
    return args.Url


def check_valid_rss():
    is_valid = True
    url = get_url()
    d = feedparser.parse(url)
    if len(d.entries) == 0:
        is_valid = False
    return is_valid


def run():
    if check_valid_rss():
        feed = feedparser.parse(get_url())
        for f in feed.entries:
            print(f.title)
            print(f.description)
            print(f.link)
            print('')


if __name__ == "__main__":
    run()
