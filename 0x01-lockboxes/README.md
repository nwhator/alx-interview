# Lockboxes

Welcome to the Lockboxes directory! Here, you'll find a Python solution for determining if all boxes can be opened.

## Task Overview

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and may contain keys to other boxes. You need to implement a method that determines if all the boxes can be opened.

### Prototype
```
def canUnlockAll(boxes):
    pass
```

## Requirements

- `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.
- Return `True` if all boxes can be opened, else return `False`.

### Example

```
boxes = [[1], [2], [3], [4], []]
canUnlockAll(boxes) # Output: True
```

## Contents

- `0-lockboxes.py`: Python script containing the implementation of the `canUnlockAll` function.
- `README.md`: This readme file provides an overview of the directory and its contents.
- `tests:` Directory containing unit tests to verify the correctness of the implemented function.

## How to Use

1. Clone the repository to your local machine.
2. Navigate to the `0x01-lockboxes` directory.
3. Explore the `0-lockboxes.py` script to understand the implementation of the `canUnlockAll` function.
4. Execute the provided tests in the `tests` directory to verify the correctness of the function.

## Contribution

Contributions are welcome! If you have any improvements, optimizations, or additional features to suggest, feel free to submit a pull request. Let's collaborate to enhance the Lockboxes solution and make it even more efficient and versatile!

## Get Started

Start exploring the Lockboxes problem and dive into developing an efficient solution. Happy coding! 🌟
