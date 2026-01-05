class GazeTracker:
    """
    Gaze estimation based on head position proxy
    (advanced systems use eye landmarks – here logic is explainable)
    """

    def estimate_gaze(self, face_box, frame_shape):
        """
        face_box = (x, y, w, h)
        frame_shape = (height, width, _)
        """
        x, y, w, h = face_box
        frame_h, frame_w = frame_shape[:2]

        face_center_x = x + w / 2
        face_center_y = y + h / 2

        horiz_ratio = face_center_x / frame_w
        vert_ratio = face_center_y / frame_h

        if horiz_ratio < 0.35:
            return "LEFT"
        if horiz_ratio > 0.65:
            return "RIGHT"
        if vert_ratio < 0.35:
            return "UP"
        if vert_ratio > 0.65:
            return "DOWN"

        return "CENTER"
