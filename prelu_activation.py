def prelu(x: float, alpha:float) -> float:
    return max(alpha * x, x)


