from moviepy.audio.fx.MultiplyVolume import MultiplyVolume
from moviepy.decorators import audio_video_effect

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from dataclasses import dataclass

@dataclass
class AudioNormalize(Effect) :
    """Return a clip whose volume is normalized to 0db.

    Return an audio (or video) clip whose audio volume is normalized
    so that the maximum volume is at 0db, the maximum achievable volume.

    Examples
    --------

    >>> from moviepy import *
    >>> videoclip = VideoFileClip('myvideo.mp4').with_effect(afx.AudioNormalize())

    """
    
    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        max_volume = clip.max_volume()
        if max_volume == 0:
            return clip
        else:
            return clip.with_effect(MultiplyVolume(1 / max_volume))
