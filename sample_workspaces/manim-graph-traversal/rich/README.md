# manim · Graph Traversal (rich)

Three scenes over a small 7-node graph (root `A` with two subtrees):

1. **BfsTraversal** — breadth-first search driven by a `deque` queue,
   coloring nodes green in visit order and printing the path.
2. **DfsTraversal** — depth-first search driven by recursion (a stack),
   diving deep before backtracking, in orange.
3. **QueueVsStack** — the one-line difference (`queue.popleft()` vs
   `stack.pop()`) that turns BFS into DFS.

```bash
pip install -r requirements.txt
manim -pql scene.py BfsTraversal   # or DfsTraversal / QueueVsStack
```

Educational sample — no fictional company. Edit `POSITIONS` and `EDGES`
to traverse your own graph.
