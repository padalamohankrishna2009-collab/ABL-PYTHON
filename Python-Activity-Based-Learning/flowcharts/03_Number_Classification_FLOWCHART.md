# Flowchart — Number Classification

Beginner-level flowchart using sequence, decisions, and loops from the Python syllabus.

```mermaid
flowchart TD
 A([Start]) --> B[/Input integer/] --> C{Number > 0?}
 C -- Yes --> D[Print positive] --> H{Number divisible by 2?}
 C -- No --> E{Number < 0?}
 E -- Yes --> F[Print negative] --> H
 E -- No --> G[Print zero] --> H
 H -- Yes --> I[Print even] --> J([End])
 H -- No --> K[Print odd] --> J
```
