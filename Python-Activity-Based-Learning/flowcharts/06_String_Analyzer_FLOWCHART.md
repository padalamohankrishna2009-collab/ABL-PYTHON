# Flowchart — String Analyzer

Beginner-level flowchart using sequence, decisions, and loops from the Python syllabus.

```mermaid
flowchart TD
 A([Start]) --> B[/Input sentence/] --> C[Display length, uppercase, lowercase] --> D{Does lowercase sentence contain python?}
 D -- Yes --> E[Display word present] --> F([End])
 D -- No --> G[Display word absent] --> F
```
