#from pynput.keyboard import Key, Listener
import os
from pynput import keyboard
import time
import json
from mutagen.mp3 import MP3
from pygame import mixer
#create a linked list to store the song
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    # check for repetation in linked list    
    def not_repeat(self,value):
        new_node=self.head
        while(new_node):
            if new_node.data==value:
                return False
            new_node=new_node.next
        return True
    
    #its like last get first and first get last like stack
    def push(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node

    #gives the position of the index
    def get_postion(self,index):
        first=self.head
        count=0
        while(first):
            count+=1
            if count==index:
                return first.data
            first=first.next

    # gives the length of linked list
    def length(self):
        first=self.head
        count=0
        while(first):
            count=count+1
            first=first.next
        return count
   # output the song in linked list
    def printlist(self):
        first=self.head
        while(first):
            print(first.data)
            first=first.next

#up 
up='''
^
|
|'''
#down
down='''
|
|
v'''
#right
right='''
----->'''
#left
left='''
<-----'''
#path of song directory
with open('path.json', 'r') as f:
  data = json.load(f)
path=data["path"]

#get name of all file in list.
files=os.listdir(path)
#get all songs file name that endswith .wav
songs=[songs for songs in files if songs.endswith('.mp3') or songs.endswith('.wav')]

#check is data.josn file exist and is it empty 
# then fill with the song name
def empty_json(songs):
   dic={}
   for song in songs:
      dic[song]=0
   json_object = json.dumps(dic, indent=4)
   with open("data.json", "w") as outfile:
      outfile.write(json_object)

#check is there any song from directory is missing in json file
# then include that song name in the json file
def missing_json(songs):
   jsonfile=open("data.json", "r")
   data=json.load(jsonfile)   
   jsonfile.close()  
   if len(data.keys())!=len(songs):
      with open("data.json", "w") as outfile:
         for song in songs:
            if song not in data:
               data[song]=0
         json.dump(data, outfile)

#check the size of file        
check_file = os.stat("data.json").st_size
# if empty 
if check_file==0:
   empty_json(songs)
# if songs missing
else:
   missing_json(songs) 
         

#read a file to check which song gets more hit 
filename=open('data.json','r')
data = json.load(filename)
filename.close()
all_played_count=[]
for i,song in enumerate(data.keys()):
    # load the json data in list 
   all_played_count.append([song,data[song],i])

#now sort the all_played_count 2-d list on behalf of hits it gets...
new_played_count=sorted(all_played_count,key=lambda x:x[1], reverse=True)
#print(new_played_count)  
#intialize the song_list to empty  
song_list=[] 
for i in range(len(new_played_count)):
  #print the song 
  print("["+str(i)+"]"+new_played_count[i][0])
  #append the song name and song.index to the list for future uses ..
  song_list.append([new_played_count[i][0],new_played_count[i][2]])

print('\n')

#genrate  the song run time..
def convert(seconds):
    seconds=seconds%(24*3600)
    hour=seconds//3600
    seconds%=3600
    minutes=seconds//60
    seconds%=60
    return f"{round(hour)}:{round(minutes)}:{round(seconds)}"

#call a linked list that we created intially
llist=Linked_list()


#intialize a variable. using this variable we can go up and down in song list
count_pointer_postion=0
#intialize a variable . using this variable we can move in already played songs 
count_back_front=0
flag=True

intial_song=""
final_song=""
#print(songs_hit)
def on_press(key):
    mixer.init()
    global count_pointer_postion
    global count_back_front
    global flag
    global intial_song
    global final_song
    print('{0} release'.format(key))
    # it is for horizontal movement in played song list 
    # <-- move left in the linked list
    if key== keyboard.Key.left:
        if count_back_front>0:
            count_back_front-=1
            print("[<]Pointer of left on postion:{0}{1}".format(count_back_front,left))
            print('\n')
    # move right in the linked list -->
    if key==keyboard.Key.right:
        if count_back_front<llist.length():
            count_back_front+=1
            print("[>]Pointer of right on postion:{0}{1}".format(count_back_front,right))
            print("[+]{0}".format(song_list[count_pointer_postion][0]))
            print('\n')
    
   
    #it is for vertical movement in list of song
    # for move up in song list /\
    if key==keyboard.Key.up:
        if count_pointer_postion>0:
            count_pointer_postion-=1
            count_back_front=0
            print("[^]Pointer of up on postion:{0}{1}".format(count_pointer_postion,up))
            print("[+]{0}".format(song_list[count_pointer_postion][0]))
            print('\n')
           
    #move down in the song list \/
    if key==keyboard.Key.down:
        if count_pointer_postion<(len(song_list)-1):
            count_pointer_postion+=1
            count_back_front=0
            print("[v]Pointer of down on postion:{0}{1}".format(count_pointer_postion,down))
            print("[+]{0}".format(song_list[count_pointer_postion][0]))
            print('\n')
    # to pause a song
    if key==keyboard.KeyCode(char='q'):
        print("[*]Your song is paused..")
        mixer.music.pause()
    # to unpause a song
    if key==keyboard.KeyCode(char='r'):
        print('[*]Your song is unpaused..')
        mixer.music.unpause()
   
    # to play the current pointer song from the song list
    if key==keyboard.Key.enter:
        # if we are not pointing in linked list then
        if count_back_front==0:
            #check the counter value and choose the song 
            song=song_list[count_pointer_postion][0]
            #print(songs_hit)
            #open the json file in read mode
            openfile= open('data.json', 'r')
            # Reading from json file
            json_object = json.load(openfile)
            #closing the json file
            openfile.close()
            #iterate throught json file 
            for value in json_object.keys():
               #if match is true 
               if value.strip()==song:
                   #increment the song hit by 1
                  json_object[value]+=1
                  #then write all dictionary again in json file 
                  with open('data.json','w') as file_update:
                     json_updated = json.dump(json_object, file_update,indent=4)
                  #print(json_object)
            # we do this becaue we dont want to save the current_song in linked list which is playing
            # we want to store intial song 
            intial_song=song
            #interchange the values
            intial_song,final_song=final_song,intial_song
            if intial_song!="" and final_song!="":
                # it checks intial song is not repeated in the linked list
                if llist.not_repeat(intial_song)==True:
                    #push the played song to linked list
                    llist.push(intial_song)
            #llist.push(song)
            #get the path of song and get the lenght of song.
            if song.endswith('.wav')==False:
                audio=MP3(path+song)
                song_len=audio.info.length
                duration=convert(song_len)
            #then covnvert lenght into time format using convert() function and print it to screen
                print("[(*)] Now playing:{0}.[{1}]".format(song,duration))
            else:
                print("[(*)] Now playing:{0}".format(song))
            #then play the song repatedly until new song is not chossen by user..
            mixer.music.load(path+song)
            mixer.music.play(-1)
            #llist.push(song)
            #llist.printlist()
            
        # if we are pointing in linked list then play from history
        else:
            #this is for playing song alreday played stored in linked list as history ..
            song=llist.get_postion(count_back_front)

            try:
                    print("[(#)]Now playing:{0}".format(song))
                    mixer.music.load(path+song)
                    mixer.music.play() 
            except Exception as e:
                    print("[-]Soory sir there is not any song recently played")
                
    # to exit the program    
    if key== keyboard.Key.esc:
        time.sleep(1)
        return False
#def on_release(key):

#using pynput we take user input 
def listen():
    with keyboard.Listener(on_press=on_press,) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

listen()
#press esc



