# Flowchart — Palindrome Word Checker

Beginner-level flowchart using sequence, decisions, and loops from the Python syllabus.

```mermaid
flowchart TD
 A([Start]) --> B[/Input word/] --> C[Convert word to lowercase] --> D[Reverse word using slicing] --> E{Word equals reverse?}
 E -- Yes --> F[Display palindrome] --> G([End])
 E -- No --> H[Display not palindrome] --> G
```
