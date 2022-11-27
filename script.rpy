label start:
  
  #if you want to disable afm while a video is playing
  #go to screen.rpy
  show screen noclick
  $ renpy.movie_cutscene("yourvideo.webm", stop_music=False)
  hide screen noclick
  $ persistent.vid_1 = True
  
  #if you want to change the time the dialogue is shown
  c "go to options.rpy"

return

