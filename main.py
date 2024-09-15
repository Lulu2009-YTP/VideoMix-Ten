from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from pydub import AudioSegment
import random
import os

# Function to apply random effects to video
def random_video_effects(clip):
    effects = [vfx.speedx, vfx.time_mirror, vfx.invert_colors, vfx.mirror_x]
    effect = random.choice(effects)
    return effect(clip)

# Function to apply sentence mixing (chop sentences randomly)
def sentence_mixing(clip, word_duration=0.3):
    words = []
    duration = clip.duration
    t = 0
    while t < duration:
        word_clip = clip.subclip(t, min(t + word_duration, duration))
        words.append(word_clip)
        t += random.uniform(0.2, 0.5)  # random intervals for chaotic effect
    random.shuffle(words)
    return concatenate_videoclips(words)

# Function for chaotic video remixing
def chaos_remixing(video_path, output_path="output_chaos.mp4"):
    clip = VideoFileClip(video_path)

    # Apply sentence mixing
    remixed_clip = sentence_mixing(clip)

    # Apply random video effects
    remixed_clip = random_video_effects(remixed_clip)

    # Save the remixed video
    remixed_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Function to apply audio remixing (using pydub)
def random_audio_effects(audio_path, output_path="output_audio_remix.mp3"):
    audio = AudioSegment.from_file(audio_path)

    # Random pitch shifting and speed changes
    speed_change = random.uniform(0.7, 1.5)  # random speed change
    new_audio = audio.speedup(playback_speed=speed_change)
    
    # Randomly apply fade in/out
    if random.choice([True, False]):
        new_audio = new_audio.fade_in(2000).fade_out(2000)

    # Save the remixed audio
    new_audio.export(output_path, format="mp3")

# Example usage
if __name__ == "__main__":
    video_input_path = "input_video.mp4"
    audio_input_path = "input_audio.mp3"
    
    # Perform video remixing
    chaos_remixing(video_input_path, "output_video.mp4")
    
    # Perform audio remixing
    random_audio_effects(audio_input_path, "output_audio.mp3")
