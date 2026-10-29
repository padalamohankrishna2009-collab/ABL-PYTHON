# Flowchart — List Statistics

Beginner-level flowchart using sequence, decisions, and loops from the Python syllabus.

```mermaid
flowchart TD
 A([Start]) --> B[Create empty list] --> C[Set i = 1] --> D{i <= 5?}
 D -- Yes --> E[/Input number/] --> F[Append number to list] --> H[Increase i by 1] --> D
 D -- No --> I[Display list, sum, maximum, minimum, sorted list] --> J([End])
```
