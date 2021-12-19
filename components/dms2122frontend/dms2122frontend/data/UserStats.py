class UserStats:
    def __init__(self, id: str, n_ans: float, n_correct: float, score: float) -> None:
        self.id = id
        self.n_ans = n_ans
        self.n_correct = n_correct
        self.score = score
        self.ok_percent = n_correct / n_ans * 100

    def __repr__(self) -> str:
        return f"{self.id}: n_ans: {self.n_ans} n_correct: {self.n_correct} score: {self.score} percent: {self.ok_percent}"
