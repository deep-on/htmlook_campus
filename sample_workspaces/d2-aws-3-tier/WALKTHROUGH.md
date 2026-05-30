# AWS 3-tier Architecture Walkthrough

A short tour of the Northwind Retail 3-tier production architecture.

## 1. Render the diagram
```bash
brew install d2
d2 --watch architecture.d2 architecture.svg
```

## 2. Pane pair
- Left: edit architecture.d2
- Right: the HTMLook viewer auto-reloads architecture.svg

## 3. Region cite
1. Capture the Web tier region.
2. Ask the AI: "Estimate the cost of this region and suggest alternatives."
3. The AI returns a cost-estimate section plus an alternative pattern.

## 4. Multi-target
- Adapting to an internal app: swap ALB -> NLB and update the domain in one pass.
