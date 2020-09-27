class Frame():
    def __init__(self, id=None, path=None, frame=None, width=None, height=None, video=False):
        self.id = id
        self.path = path
        self.frame = frame
        self.width = width
        self.height = height
        self.video = video
    
    def get_frame_by_id(self, frames, id):
        for frame in frames:
            if frame.id == id:
                return frame
        return None