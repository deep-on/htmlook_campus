import marimo as mo
__generated_with = "0.10.0"
app = mo.App(width="medium")

@app.cell
def __():
    import marimo as mo
    return mo,

@app.cell
def __(mo):
    mo.md("# NLP Text Exploration · LDA Topics on customer feedback")
    return

@app.cell
def __(mo):
    n_topics = mo.ui.slider(start=2, stop=20, value=5, label="# topics")
    n_topics
    return n_topics,

@app.cell
def __(mo, n_topics):
    mo.md(f"Running LDA with **{n_topics.value} topics** on 5,000 customer reviews.")
    return

if __name__ == "__main__":
    app.run()
