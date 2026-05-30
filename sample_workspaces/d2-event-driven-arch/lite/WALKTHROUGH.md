# Event-Driven Architecture Walkthrough

A short tour of the Tidewell Commerce event-driven order platform.

## 1. Render the diagram
```bash
d2 --watch architecture.d2 diagram.svg --layout=elk
```

## 2. Trace the SAGA flow
- Capture the SAGA orchestrator region of the diagram.
- Ask the AI: "Explain this SAGA's compensation flow step by step."
- The AI narrates the dispatch -> fail -> compensate sequence.
