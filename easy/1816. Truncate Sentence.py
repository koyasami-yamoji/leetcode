

def truncateSentence(s: str, k: int) -> str:
    return ' '.join(s.split()[:k])


print(truncateSentence("Hello how are you Contestant", 4))