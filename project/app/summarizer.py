import nltk
from newspaper import Article

from app.models.tortoise import TextSummary


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    summary = article.summary

    # the summary is generated after the response is sent back to the client.
    await TextSummary.filter(id=summary_id).update(summary=summary)
