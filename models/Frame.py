class Frame():
    def __init__(self, id=None, path=None, frame=None, width=None, height=None, video=False, background_ignore=False):
        self.id = id
        self.path = path
        self.frame = frame
        self.width = width
        self.height = height
        self.video = video
        self.background_ignore = background_ignore
    
    def get_frame_by_id(self, frames, id):
        for frame in frames:
            if frame.id == id:
                return frame
        return None

    def video_validator(self, count):
        if count < len(self.frame):
            return count
        else:
            return 0