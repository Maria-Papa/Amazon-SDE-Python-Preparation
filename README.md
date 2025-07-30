# Amazon-SDE-Python-Preparation
A repository to help me prepare for an Amazon SDE role interview


# Python Style Guide
| Item              | Naming Convention               | Example                    | Notes/Why                                                          |
| ----------------- | ------------------------------- | -------------------------- | ------------------------------------------------------------------ |
| **Folder**        | lowercase, underscores optional | `array/`, `bit_magic/`     | Should be valid Python package names; no spaces, no leading digits |
| **File (module)** | lowercase\_with\_underscores    | `max_subarray_sum.py`      | Descriptive, concise, PEP 8 recommended                            |
| **Function**      | lowercase\_with\_underscores    | `max_subarray_sum()`       | Readable, consistent, PEP 8                                        |
| **Variable**      | lowercase\_with\_underscores    | `current_sum`, `max_value` | Easy to read, snake\_case                                          |
| **Class**         | CapWords (PascalCase)           | `TrieNode`, `LinkedList`   | Distinguishes classes visually                                     |
| **Constants**     | UPPERCASE\_WITH\_UNDERSCORES    | `MAX_SIZE = 100`           | Immutable values, PEP 8 standard                                   |
| **Package**       | lowercase, no underscores       | `array`, `string`          | Usually avoid underscores in package names for simpler imports     |


# Sources
[Amazon SDE Sheet: Interview Questions and Answers 2024](https://www.geeksforgeeks.org/dsa/amazon-sde-sheet-interview-questions-and-answers/)
