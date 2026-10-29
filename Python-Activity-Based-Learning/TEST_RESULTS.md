# Test Execution Report — Python Activity-Based Learning

## Status

The repository's existing [TEST_CASES.md](./TEST_CASES.md) contains 31 planned checks. The test plan has been retained. The full 31-case suite has **not yet been verified by a completed automated run**, so this document deliberately does not claim that all tests passed.

The files under `screenshots/` are SVG terminal-style sample-run captures showing representative inputs and expected output for each program. They are generated sample transcripts, not unedited screenshots taken from a browser session. Use them as presentation examples, not as proof that all 31 cases were executed.

## Test coverage

- Calculator: normal arithmetic and division by zero
- Marks and grade: A, B, C, D, and Fail bands
- Number classification: positive, negative, zero, even, and odd
- Multiplication table: positive, zero, and negative inputs
- Star triangle: positive row counts, zero, and negative row counts
- String analyzer: mixed-case Python match, no match, and empty input
- Palindrome checker: palindrome, mixed case, non-palindrome, one-character, and empty input
- List statistics: ascending, mixed, and repeated values
- Tuple record: typical record, zero roll number, and multi-word name
- Set operations: overlap, duplicates, empty set, and membership check

## Artifact index

- [Test cases](./TEST_CASES.md)
- [Sample-run captures](./screenshots/)
- [Flowcharts](./flowcharts/)

## How to execute the test plan

From each program folder, run `python main.py` and enter the matching inputs from TEST_CASES.md. Compare the output with the expected behavior listed there. Set output ordering may vary between Python runs, so compare set membership rather than printed order.
