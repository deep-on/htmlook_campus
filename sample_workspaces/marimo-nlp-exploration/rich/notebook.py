import marimo as mo

__generated_with = "0.10.0"
app = mo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import re
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from collections import Counter
    return Counter, mo, np, pd, plt, re


@app.cell
def __(mo):
    mo.md(
        """
        # NLP Text Exploration · Customer Feedback

        A self-contained text-analysis notebook over a small inline corpus of
        product reviews. We cover tokenization, a word-frequency distribution,
        and a tiny lexicon-based sentiment score — no model downloads, no NLTK
        corpora. Swap the `reviews` list for your own text to reuse it.
        """
    )
    return


@app.cell
def __():
    # Inline corpus: 12 short product reviews. Self-contained so the notebook
    # runs anywhere — replace with your own list of strings to analyze.
    reviews = [
        "The battery life is excellent and the screen is bright and clear.",
        "Setup was simple and the app feels fast and responsive.",
        "Terrible support, my order arrived broken and nobody replied.",
        "Love the design, but the price is a little high for what you get.",
        "Works great, charges quickly, and the sound quality is amazing.",
        "Disappointed with the build quality, it feels cheap and flimsy.",
        "The interface is clean and intuitive, a delight to use every day.",
        "Slow shipping and the packaging was damaged, very frustrating.",
        "Reliable performance and a comfortable, lightweight feel overall.",
        "The camera is mediocre and the photos look grainy in low light.",
        "Fantastic value, I would happily recommend it to a friend.",
        "Buggy software, it crashes often and drains the battery fast.",
    ]
    return (reviews,)


@app.cell
def __(mo, reviews):
    total_chars = sum(len(r) for r in reviews)
    mo.md(
        f"""
        **{len(reviews)} reviews** ·
        **{total_chars}** characters ·
        avg **{total_chars / len(reviews):.0f}** chars/review.
        """
    )
    return (total_chars,)


@app.cell
def __(re, reviews):
    # Lowercase, strip punctuation, split on whitespace, drop common stopwords.
    STOPWORDS = {
        "the", "is", "and", "a", "an", "to", "of", "it", "in", "for", "on",
        "with", "my", "but", "i", "you", "was", "are", "be", "this", "that",
        "very", "so", "what", "would", "get", "feels", "feel", "look", "looks",
        "every", "day", "little", "overall",
    }

    def tokenize(text):
        words = re.findall(r"[a-z']+", text.lower())
        return [w for w in words if w not in STOPWORDS and len(w) > 1]

    tokens_per_review = [tokenize(r) for r in reviews]
    all_tokens = [t for toks in tokens_per_review for t in toks]
    return STOPWORDS, all_tokens, tokenize, tokens_per_review


@app.cell
def __(all_tokens, mo, tokens_per_review):
    vocab = set(all_tokens)
    avg_len = sum(len(t) for t in tokens_per_review) / len(tokens_per_review)
    mo.md(
        f"""
        After tokenizing and removing stopwords:
        **{len(all_tokens)}** tokens ·
        **{len(vocab)}** unique words ·
        avg **{avg_len:.1f}** content words/review.
        """
    )
    return avg_len, vocab


@app.cell
def __(Counter, all_tokens, pd):
    freq = Counter(all_tokens)
    top = pd.DataFrame(freq.most_common(12), columns=["word", "count"])
    top
    return freq, top


@app.cell
def __(plt, top):
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.barh(top["word"][::-1], top["count"][::-1], color="#3b7dd8")
    ax.set_title("Most frequent content words")
    ax.set_xlabel("count")
    fig
    return ax, fig


@app.cell
def __():
    # A tiny opinion lexicon: +1 for positive cues, -1 for negative cues.
    POSITIVE = {
        "excellent", "bright", "clear", "simple", "fast", "responsive",
        "love", "great", "quickly", "amazing", "clean", "intuitive",
        "delight", "reliable", "comfortable", "lightweight", "fantastic",
        "value", "recommend", "happily",
    }
    NEGATIVE = {
        "terrible", "broken", "high", "disappointed", "cheap", "flimsy",
        "slow", "damaged", "frustrating", "mediocre", "grainy", "buggy",
        "crashes", "drains", "broke",
    }
    return NEGATIVE, POSITIVE


@app.cell
def __(NEGATIVE, POSITIVE, pd, tokens_per_review):
    def sentiment(tokens):
        pos = sum(t in POSITIVE for t in tokens)
        neg = sum(t in NEGATIVE for t in tokens)
        return pos - neg

    scores = [sentiment(toks) for toks in tokens_per_review]
    sent = pd.DataFrame({"score": scores})
    sent["label"] = sent["score"].apply(
        lambda s: "positive" if s > 0 else ("negative" if s < 0 else "neutral")
    )
    sent
    return scores, sent, sentiment


@app.cell
def __(plt, sent):
    counts = sent["label"].value_counts().reindex(
        ["positive", "neutral", "negative"], fill_value=0
    )
    fig2, ax2 = plt.subplots(figsize=(6, 3))
    ax2.bar(counts.index, counts.values,
            color=["#2e9e6b", "#9aa0a6", "#d9534f"])
    ax2.set_title("Sentiment distribution across reviews")
    ax2.set_ylabel("# reviews")
    fig2
    return ax2, counts, fig2


@app.cell
def __(counts, freq, mo, sent):
    top_word, top_count = freq.most_common(1)[0]
    net = int(sent["score"].sum())
    mo.md(
        f"""
        ## Takeaway

        The most common content word is **{top_word}** ({top_count} mentions).
        Sentiment skews **{"positive" if net > 0 else "negative" if net < 0 else "neutral"}**:
        **{int(counts['positive'])} positive**, **{int(counts['neutral'])} neutral**,
        **{int(counts['negative'])} negative** (net score **{net:+d}**).

        Next steps: expand the lexicon, weight by frequency, or feed the tokens
        into TF-IDF before clustering reviews into themes.
        """
    )
    return net, top_count, top_word


if __name__ == "__main__":
    app.run()
