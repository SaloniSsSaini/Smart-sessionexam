class MicroExpressionAnalyzer:
    """
    Extracts micro-expression signals
    Values are normalized between 0 and 1
    """

    def analyze(self, face_box):
        """
        face_box = (x, y, w, h)
        Using geometric heuristics for stress / effort
        """

        _, _, w, h = face_box
        aspect_ratio = w / h if h != 0 else 1

        brow_furrow = min(1.0, abs(1 - aspect_ratio))
        smile = 0.2                     # neutral default
        head_tilt = min(1.0, abs(aspect_ratio - 1))
        lip_press = 0.6
        eye_squint = 0.5

        return {
            "brow_furrow": brow_furrow,
            "smile": smile,
            "head_tilt": head_tilt,
            "lip_press": lip_press,
            "eye_squint": eye_squint
        }
