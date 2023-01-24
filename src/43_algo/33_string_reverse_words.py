def reverseWords(self, S):
    if S is None:
        return

    result = []
    split_words = S.split(".")

    for idx in range(len(split_words) - 1, -1, -1):
        result.append(split_words[idx])

    return ".".join(result)