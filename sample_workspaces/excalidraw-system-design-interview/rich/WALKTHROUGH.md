# System Design Interview Walkthrough · 30-min Walkthrough

> **Wave A · High Quality** — marketing / demo asset. Suitable for a live demo
> recording.

## 1. Two whiteboards
- `url-shortener` · `news-feed` — both drawn step-by-step in five stages
- Capacity / trade-off panels are included inside each diagram

## 2. Region cite signature
- Capture one box in the diagram (e.g. the Redis cache in url-shortener)
- AI interviewer mode: "What happens if this cache goes down?" / "How do you
  invalidate it?"
- The AI poses simulated follow-up questions → the candidate extends the
  whiteboard on the spot

## 3. 35-min mock interview flow
- Follow the 5-step templating in INTERVIEW_GUIDE.md
- url-shortener: explain the write path (INCR → base62 → insert) and the read
  path (cache → 301) separately
- news-feed: at the push-vs-pull decision point, follow up with the celebrity case
- When done, export to SVG and share it with the feedback
