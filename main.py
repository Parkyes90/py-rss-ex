import feedparser

urls = ("https://rss.blog.naver.com/parkyes90.xml",)


def rss(url):
    blog = feedparser.parse(url)
    for entry in blog.entries:
        print(entry)


def main():
    for url in urls:
        rss(url)


if __name__ == "__main__":
    main()
