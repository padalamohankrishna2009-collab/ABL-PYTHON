# Flowchart — Basic Arithmetic Calculator

Beginner-level flowchart using sequence, decisions, and loops from the Python syllabus.

```mermaid
flowchart TD
 A([Start]) --> B[/Input a and b/] --> C[Display sum, difference, product] --> D{b is not zero?}
 D -- Yes --> E[Display quotient and remainder] --> F([End])
 D -- No --> G[Display division warning] --> F
```
