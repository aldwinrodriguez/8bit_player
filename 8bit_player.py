from tkinter import *
from midi2audio import FluidSynth
import pygame
import os

class eight_bit_player:

  def __init__(self,root):
    self.root = root
    self.root.title("8-bit Player")
    self.root.geometry("600x445+200+200")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    trackframe = LabelFrame(self.root,text="Now Playing",font=("terminal",15,"bold"),bg="skyblue",fg="gold",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=300,height=300)
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("terminal",12,"bold"),bg="skyblue",fg="gold").grid(row=0,column=0,padx=10,pady=5)
    trackstatus = Label(trackframe,textvariable=self.status,font=("terminal",12,"bold"),bg="skyblue",fg="gold").grid(row=0,column=1,padx=10,pady=5)

    buttonframe = LabelFrame(self.root,text="Controls",font=("terminal",15,"bold"),bg="skyblue",fg="gold",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=300,width=600,height=145)
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=24,height=2,font=("terminal",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=24,height=2,font=("terminal",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=24,height=2,font=("terminal",16,"bold"),fg="navyblue",bg="gold").grid(row=1,column=0,padx=10,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=24,height=2,font=("terminal",16,"bold"),fg="navyblue",bg="gold").grid(row=1,column=1,padx=10,pady=5)

    songsframe = LabelFrame(self.root,text="Playlist",font=("terminal",15,"bold"),bg="skyblue",fg="gold",bd=5,relief=GROOVE)
    songsframe.place(x=300,y=0,width=300,height=300)
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("terminal",22),bg="orange",fg="darkslategray",bd=5,relief=GROOVE)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    os.chdir("songs")
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END,track)

  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("-Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  def stopsong(self):
    self.status.set("-Stopped")
    pygame.mixer.music.stop()

  def pausesong(self):
    self.status.set("-Paused")
    pygame.mixer.music.pause()

  def unpausesong(self):
    self.status.set("-Playing")
    pygame.mixer.music.unpause()

root = Tk()


eight_bit_player(root)
root.mainloop()