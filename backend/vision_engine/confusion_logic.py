class ConfusionDetector:
    """
    Human-inspired confusion scoring system
    """

    def compute_score(self, signals):
        score = (
            signals["brow_furrow"] * 40 +
            (1 - signals["smile"]) * 20 +
            signals["head_tilt"] * 10 +
            signals["lip_press"] * 15 +
            signals["eye_squint"] * 15
        )
        return round(score, 2)

    def classify(self, score):
        if score >= 60:
            return "CONFUSED"
        return "FOCUSED"
