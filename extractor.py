from newspaper import Article, Config

config = Config()
config.keep_article_html = True


def extract(url):
    article = Article(url=url, config=config)
    article.download()
    article.parse()
    return dict(
        title=article.title,
        text=article.text,
        html=article.article_html,
        image=article.top_image,
        authors=article.authors,
    )
