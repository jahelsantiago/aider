from pathlib import Path

from .dump import dump  # noqa: F401


def safe_abs_path(res):
    "Gives an abs path, which safely returns a full (not 8.3) windows path"
    res = Path(res).resolve()
    return str(res)


def show_messages(messages, title=None, functions=None):
    if title:
        print(title.upper(), "*" * 50)

    for msg in messages:
        role = msg["role"].upper()
        content = msg.get("content")
        if content:
            for line in content.splitlines():
                print(role, line)
        content = msg.get("function_call")
        if content:
            print(role, content)

    if functions:
        dump(functions)


def word_distance(word1, word2):
    """
    Calculates the minimum number of operations (insertion, deletion, or replacement) required to transform word1 into word2.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        int: The minimum number of operations required to transform word1 into word2.
    """
    def helper(i, j):
        if i == 0:
            return j  # Insert all characters from word2
        if j == 0:
            return i  # Delete all characters from word1

        if word1[i - 1] == word2[j - 1]:
            return helper(i - 1, j - 1)
        else:
            insert = 1 + helper(i, j - 1)      # Insert a character
            delete = 1 + helper(i - 1, j)      # Delete a character
            replace = 1 + helper(i - 1, j - 1)  # Replace a character
            return min(insert, delete, replace)

    return helper(len(word1), len(word2))


def word_distance_optimized(word1, word2):
    """
    Calculates the minimum number of operations (insertion, deletion, or replacement) required to transform word1 into word2.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        int: The minimum number of operations required to transform word1 into word2.
    """
    # Create a memoization table to store results of subproblems
    memo = {}

    def calculate_edit_distance(i, j):
        # Check if the result is already memoized
        if (i, j) in memo:
            return memo[(i, j)]

        # Base cases: If one of the words is empty, we need to perform insertions or deletions
        if i == 0:
            memo[(i, j)] = j  # Insert all characters from word2
        elif j == 0:
            memo[(i, j)] = i  # Delete all characters from word1
        else:
            # If the current characters match, no additional operation is needed
            if word1[i - 1] == word2[j - 1]:
                memo[(i, j)] = calculate_edit_distance(i - 1, j - 1)
            else:
                # Calculate the minimum cost among insertion, deletion, and replacement
                insert = 1 + calculate_edit_distance(i, j - 1)      # Insert a character
                delete = 1 + calculate_edit_distance(i - 1, j)      # Delete a character
                replace = 1 + calculate_edit_distance(i - 1, j - 1)  # Replace a character
                memo[(i, j)] = min(insert, delete, replace)

        return memo[(i, j)]

    # Start the recursive calculation with the lengths of both words
    return calculate_edit_distance(len(word1), len(word2))

