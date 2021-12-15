class UserStats:
    def __init__(self, id: str, n_ans: float, n_correct: float, score: float) -> None:
        self.id = id
        self.n_ans = n_ans
        self.n_correct = n_correct
        self.score = score
