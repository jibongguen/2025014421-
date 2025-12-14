from tkinter import *
import pygame
import random
import random
import time

gameover = 1
realgameover = 0
question = 0
showing = 0

class wolf:
    def __init__(self,canvas,image,id):
        self.id='w'+str(id) 
        self.canvas=canvas 
        self.image=image
        self.wolf = self.canvas.create_image(960,random.randint(10,470), image = self.image,tags=self.id)
        self.wolfmove=0

    def update(self):
        self.canvas.move(self.wolf,-4,0) 

    def wolfPos(self):
        return self.canvas.coords(self.wolf) 

    def wolfId(self):
        return self.wolf 

class eagle:
    def __init__(self,canvas,image,id):
        self.id='e'+str(id) 
        self.canvas=canvas 
        self.image=image
        self.eagle = self.canvas.create_image(960,random.randint(10,470), image = self.image,tags=self.id)
        self.stonefire=time.time()
        self.stonewhen=time.time()
        
        
    def update(self):
        self.canvas.move(self.eagle,-2,0) 

    def eaglePos(self):
        return self.canvas.coords(self.eagle)

    def eagleId(self):
        return self.eagle 

class stone:
    def __init__(self,canvas,image,id,spawn):
        self.id='s'+str(id)  
        self.canvas=canvas 
        self.image=image
        self.spawn_x=spawn[0]
        self.spawn_y=spawn[1]
        self.stone = self.canvas.create_image(self.spawn_x,self.spawn_y, image = self.image,tags=self.id)
        
    def update(self):
        self.canvas.move(self.stone,-10,0)
        
    def stonePos(self):
        return self.canvas.coords(self.stone)

    def stoneId(self):
        return self.stone 


class pig:
    def __init__(self,canvas,image,id):
        self.id='p'+str(id) 
        self.canvas=canvas 
        self.image=image
        self.pig = self.canvas.create_image(960,random.randint(10,470), image = self.image,tags=self.id) 
        self.pigrush = 0
        self.pig_rush_time=time.time()
        self.pig_now_time=time.time()
        self.pigmove=0

    def update(self):
        self.canvas.move(self.pig,self.pigrush,0) 
        self.pig_now_time=time.time()
        if((self.pig_now_time-self.pig_rush_time) >= 1):
            self.pigrush-=1
            self.pig_rush_time=self.pig_now_time

    def pigPos(self):
        return self.canvas.coords(self.pig) 

    def pigId(self):
        return self.pig 
        
class elephant:
    def __init__(self,canvas,image,id):
        self.id='el'+str(id) 
        self.canvas=canvas 
        self.image=image
        self.elephant = self.canvas.create_image(960,random.randint(10,470), image = self.image,tags=self.id) 
        self.el_life=5

    def update(self):
        self.canvas.move(self.elephant,-2,0) 

    def elephantPos(self):
        return self.canvas.coords(self.elephant) 

    def elephantId(self):
        return self.elepahnt 

class GamePlay:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("960x480")
        self.window.title("게임")
        self.keys = set()

        global gameover
        global realgameover
        global question
        global showing

        pygame.init()
        pygame.mixer.music.load("image/bgm2.mp3")
        pygame.mixer.music.play(-1) 

        
        self.sounds = pygame.mixer
        self.sounds.init()
        self.gun_sound = self.sounds.Sound("image/gun_sound.mp3")
        self.shoot_sound = self.sounds.Sound("image/shoot.mp3")
        self.wolf_sound = self.sounds.Sound("image/wolf_sound.mp3")
        self.pig_sound = self.sounds.Sound("image/pig_sound.mp3")
        self.elephant_sound = self.sounds.Sound("image/elephant_sound.mp3")
        self.eagle_sound = self.sounds.Sound("image/eagle_sound.mp3")
        self.stone_sound = self.sounds.Sound("image/stone_sound.mp3")
        self.dash_sound = self.sounds.Sound("image/dash_sound.mp3")
        self.gameover_sound = self.sounds.Sound("image/gameover.mp3")
        
        
        
        self.canvas=Canvas(self.window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)
        self.window.bind("<KeyPress>",self.keyPressHandler)
        self.window.bind("<KeyRelease>",self.keyReleaseHandler)        
        self.window.protocol("WM_DELETE_WINDOW", self.onClose)

        
        
        self.firelist=[]
        self.fireimg = PhotoImage(file="image/gun_shot_go.png").subsample(4)
        self.firewhen=time.time()

        self.shottingtime=time.time()
        self.shottingwhen=time.time()
        
        self.wolflist=[]
        self.wolfsummon=time.time()
        self.wolfimg= [PhotoImage(file="image/wolf_run1.png").subsample(8),PhotoImage(file="image/wolf_run2.png").subsample(8),PhotoImage(file="image/wolf_run3.png").subsample(8)]
        self.wolf_id=0
        self.lasttime_w=time.time()
        self.wolf_rand=random.randint(1,2)

        self.eaglelist=[]
        self.eaglesummon=time.time()
        self.eagleimg = PhotoImage(file="image/eagle.png").subsample(6)
        self.eagle_id=0
        self.lasttime_e=time.time()
        self.eagle_rand=random.randint(2,4)

        self.stonelist=[]
        self.stoneimg = PhotoImage(file="image/stone_img.png").subsample(14)
        self.stone_id=0

        self.stop_hunter = 0
        self.stop_time=0
        self.hunter_time=0

        self.piglist=[]
        self.pigsummon=time.time()
        self.pigimg= [PhotoImage(file="image/pigimg1.png").subsample(8),PhotoImage(file="image/pigimg2.png").subsample(8),PhotoImage(file="image/pigimg3.png").subsample(8)]
        self.pig_id=0
        self.lasttime_p=time.time()
        self.pig_rand=random.randint(1,3)

        self.elephantlist=[]
        self.elephantsummon=time.time()
        self.elephantimg= PhotoImage(file="image/elephant_img1.png").subsample(4)
        self.elephant_id=0
        self.lasttime_el=time.time()
        self.elephant_rand=random.randint(4,6)
        
        self.backimg = PhotoImage(file="image/background_img.png")
        self.background = self.canvas.create_image(320,240, image = self.backimg)
        self.backimg1 = PhotoImage(file="image/background_img1.png")
        self.background = self.canvas.create_image(1120,240, image = self.backimg1)


        self.score=0;
       
        self.huntimg = PhotoImage(file="image/hunter_img.png").subsample(8)
        self.hunter = self.canvas.create_image(30,240, image = self.huntimg,tags="hunter")

        self.language1 = self.canvas.create_text(480,240,font="Time 20 bold",text="The Hunter", fill="blue")
        self.language2 = self.canvas.create_text(480,360,font="Time 13 bold",text="press s to start")
        self.language3 = self.canvas.create_text(480,380,font="Time 13 bold",text="press q how to play")

        self.showing = self.canvas.create_text(600,200,font="Time 13 bold",text="위, 아래 화살표로 이동 \n 스페이스바로 총을 발사해서 \n 동물들이 지나가는것 막아내라! \nf키로 3초마다 강한 샷건을 쏘자!\nz로 도움닫고 화살표로 원하는 방향으로 빠르게 옆으로 피해보도록! \n\n\n늑대 - 가장 기본적인 사냥감\n멧되지 - 서서히 빨라지니 주의\n거대 독수리 - 가끔 돌을 던져서 사냥꾼을 경직시킨다\n코끼리 - 그 크기만큼이나 맷집이 세다\n\n\n press e to quit")
        self.canvas.itemconfigure(self.showing, state="hidden")

        self.score=0
        self.score_text=self.canvas.create_text(50,10,font="Times 13 bold",text=f"score:{self.score}",fill='black')

        self.over_text=self.canvas.create_text(480,240,font="Times 20 bold",text="GAME OVER!",fill='red')
        self.canvas.itemconfigure(self.over_text, state="hidden")
        
        self.final_score=self.canvas.create_text(480,300,font="Times 13 bold",text=f"score:{self.score}",fill='black')
        self.canvas.itemconfigure(self.final_score, state="hidden")
               
        self.restart=self.canvas.create_text(480,320,font="Times 13 bold",text="press s to restart",fill='black')
        self.canvas.itemconfigure(self.restart, state="hidden")

        self.shoot_count=0;

        self.dash_ready = 0;
        self.dashtime = time.time();
        self.dashwhen = time.time();
        self.dash_count = 0;

        while True:
            
            try:
                
                if gameover == 1 and realgameover == 0 and question == 0:
                    for key in self.keys: 
                        if key == 83:                 
                            gameover = 0
                            
                            self.canvas.itemconfigure(self.language1, state="hidden")
                            self.canvas.itemconfigure(self.language2, state="hidden")
                            self.canvas.itemconfigure(self.language3, state="hidden")
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("image/bgm.mp3")
                            pygame.mixer.music.play(-1)
                        if key == 81 :
                            self.canvas.itemconfigure(self.language1, state="hidden")
                            self.canvas.itemconfigure(self.language2, state="hidden")
                            self.canvas.itemconfigure(self.language3, state="hidden")
                            self.canvas.itemconfigure(self.showing, state="normal")
                            question = 1

                if question == 1 and gameover ==1 and realgameover==0:
                    self.canvas.itemconfigure(self.showing, state="normal")
                    for key in self.keys: 
                        if key == 69:
                            self.canvas.itemconfigure(self.showing, state="hidden")
                            self.canvas.itemconfigure(self.language1, state="normal")
                            self.canvas.itemconfigure(self.language2, state="normal")
                            self.canvas.itemconfigure(self.language3, state="normal")
                            question = 0;
                            



                if gameover == 1 and realgameover == 1:
                    for key in self.keys: 
                        if key == 83:                 
                            gameover = 0
                            self.canvas.itemconfigure(self.over_text, state="hidden")
                            self.canvas.itemconfigure(self.final_score, state="hidden")
                            self.canvas.itemconfigure(self.restart, state="hidden")
                            self.score_text=self.canvas.create_text(50,10,font="Times 13 bold",text=f"score:{self.score}",fill='black')
                            pygame.mixer.music.load("image/bgm.mp3")
                            pygame.mixer.music.play(-1)
                            

                if gameover == 0 and question == 0:

                    for fire in self.firelist:
                        self.canvas.move(fire,8,0)

                    for fire in self.firelist:
                        if self.canvas.coords(fire)[0] >= 960:
                            self.canvas.delete(fire)

                    self.shottingtime = time.time()
                    if (self.shottingtime - self.shottingwhen) > 0.1:
                        self.canvas.delete(self.shoot_count)
                        if self.shottingtime - self.shottingwhen > 3:
                            self.shoot_count = self.canvas.create_text(100,50,font="Times 13 bold",text="shoot_count[f]: fire!",fill='black')
                        else:
                            self.shoot_count = self.canvas.create_text(100,50,font="Times 13 bold",text=f"shoot_count[f]:{3-self.shottingtime + self.shottingwhen:.1f}",fill='black')
                        
                    self.dashtime=time.time();
                    if (self.dashtime - self.dashwhen) > 0.1:
                        self.canvas.delete(self.dash_count)
                        if self.dash_ready ==1:
                            self.dash_count = self.canvas.create_text(100,30,font="Times 13 bold",text=f"dash_count[z]: ready!",fill='black')
                        elif self.dashtime - self.dashwhen > 1.5:
                            self.dash_count = self.canvas.create_text(100,30,font="Times 13 bold",text="dash_count[z]: full!",fill='black')
                        else:
                            self.dash_count = self.canvas.create_text(100,30,font="Times 13 bold",text=f"dash_count[z]:{1.5-self.dashtime + self.dashwhen:.1f}",fill='black')
                    

                    position = self.canvas.coords("hunter")
                    if position[1]<0:
                        self.canvas.move(self.hunter, 0, -position[1])

                    elif position[1]>470:
                        self.canvas.move(self.hunter, 0, -(position[1]-470))

                    
                    if self.stop_hunter == 0:
                        for key in self.keys: 
                            if key == 38:                 
                                self.canvas.move(self.hunter, 0, -10)
                                if self.dash_ready == 1 and self.dashtime-self.dashwhen > 1.5:
                                    self.canvas.move(self.hunter, 0, -90)
                                    self.dash_ready=0;
                                    self.dashwhen=time.time()
                                    self.dash_sound.play()
                            if key == 90 and self.dashtime-self.dashwhen > 1.5:
                                self.dash_ready = 1;
                                self.canvas.delete(self.dash_count)
                                self.dash_count = self.canvas.create_text(100,30,font="Times 13 bold",text=f"dash_count[z]: ready!",fill='black')
                        
                            if key == 40:                 
                                self.canvas.move(self.hunter, 0, 10)
                                if self.dash_ready == 1 and self.dashtime-self.dashwhen > 1.5:
                                    self.canvas.move(self.hunter, 0, 90)
                                    self.dash_ready=0;
                                    self.dashwhen=time.time()
                                    self.dash_sound.play()
                        
                            if key == 32:
                                firetime = time.time()
                        
                                if (firetime-self.firewhen) > 0.3:
                                    firepos = self.canvas.coords("hunter")
                                    self.gun_sound.play()
                                    fire = self.canvas.create_image(firepos[0], firepos[1], image = self.fireimg,tags="fire")
                                    
                                    self.firelist.append(fire)
                                    self.firewhen=time.time()

                            if key == 70:
                        
                                if (self.shottingtime-self.shottingwhen) > 3:
                                    firepos = self.canvas.coords("hunter")
                                    self.shoot_sound.play()
                                    for s in range(-1,2):
                                        fire = self.canvas.create_image(firepos[0], firepos[1]+s*20, image = self.fireimg,tags="fire")
                                    
                                        self.firelist.append(fire)
                                    self.shottingwhen=time.time()
                        

                    else:
                        if self.hunter_time - self.stop_time > 1:
                            self.stop_hunter =0
                
                    self.hunter_time=time.time()
                            
                    self.wolfmanage()
                    if self.score >=1000:
                        self.pigmanage()
                    if self.score >= 4000:
                        self.eaglemanage()
                        self.stonemanage()
                    if self.score >=10000:
                        self.elephantmanage()
                    if self.score >=30000:
                        self.wolfmanage()
                        self.pigmanage()
                        

            except TclError:
                return

            self.window.after(33)
            self.window.update() 

    def wolfmanage(self): 
        
        self.wolfsummon=time.time()
        if self.wolfsummon-self.lasttime_w >= self.wolf_rand:
            self.wolflist.append(wolf(self.canvas,self.wolfimg[0],self.wolf_id))
            self.wolf_id +=1
            if self.score >= 30000:
                self.wolflist.append(wolf(self.canvas,self.wolfimg[0],self.wolf_id))
                self.wolf_id +=1
            self.lasttime_w=self.wolfsummon
            self.wolf_rand=random.randint(1,2)

            
        for w in self.wolflist:
            w.update()
            w.wolfmove+=1
            self.canvas.itemconfig(w.wolf, image = self.wolfimg[(w.wolfmove%6)//2])
            if w.wolfPos()[0] < 0:
                self.canvas.delete(w.wolf)
                self.wolflist.pop(self.wolflist.index(w))
                self.gameover()
        self.wolfsummon=time.time()
        
        hitbox = 30
        for f in self.firelist[:]:  
            f_pos = self.canvas.coords(f)
            if not f_pos:  
                self.firelist.remove(f)
                continue

            for w in self.wolflist[:]:  
                w_pos = w.wolfPos()
                if not w_pos:  
                    self.wolflist.remove(w)
                    continue

        
                if (w_pos[0]-hitbox < f_pos[0] < w_pos[0]+hitbox) and (w_pos[1]-hitbox < f_pos[1] < w_pos[1]+hitbox):
                    self.canvas.delete(w.wolf)  
                    self.wolflist.remove(w)
                    self.canvas.delete(f)       
                    self.firelist.remove(f)
                    self.score+=100
                    self.canvas.delete(self.score_text)
                    self.wolf_sound.play()
                    self.score_text=self.canvas.create_text(50,10,font="Times 13 bold",text=f"score:{self.score}",fill='black')
                    break

    def eaglemanage(self): 
        self.eaglesummon=time.time()
        if self.eaglesummon-self.lasttime_e > self.eagle_rand:
            self.eaglelist.append(eagle(self.canvas,self.eagleimg,self.eagle_id))
            self.eagle_id +=1
            if self.score >= 50000:
                self.eaglelist.append(eagle(self.canvas,self.eagleimg,self.eagle_id))
                self.eagle_id +=1
            self.lasttime_e=self.eaglesummon
            self.eagle_rand=random.randint(3,5)
           
            
        for e in self.eaglelist:
            e.update()
            if e.eaglePos()[0] < 0:
                self.canvas.delete(e.eagle)
                self.eaglelist.pop(self.eaglelist.index(e))
                self.gameover()
        self.wolfsummon=time.time()
        
        hitbox = 30
        for f in self.firelist[:]:  
            f_pos = self.canvas.coords(f)
            if not f_pos:  
                self.firelist.remove(f)
                continue

            for e in self.eaglelist[:]:  
                e_pos = e.eaglePos()
                if not e_pos:  
                    self.eaglelist.remove(e)
                    continue

        
                if (e_pos[0]-hitbox < f_pos[0] < e_pos[0]+hitbox) and (e_pos[1]-hitbox < f_pos[1] < e_pos[1]+hitbox):
                    self.canvas.delete(e.eagle)  
                    self.eaglelist.remove(e)
                    self.canvas.delete(f)        
                    self.firelist.remove(f)
                    self.score+=200
                    self.eagle_sound.play()
                    self.canvas.delete(self.score_text)
                    self.score_text=self.canvas.create_text(50,10,font="Times 13 bold",text=f"score:{self.score}",fill='black')
                    
                    break
                
        for e in self.eaglelist[:]: 
            e_pos = e.eaglePos()
            if not e_pos:  
                self.eaglelist.remove(e)
                continue

            if e.stonefire-e.stonewhen >2.5:
                self.stonelist.append(stone(self.canvas,self.stoneimg,self.stone_id,e_pos))
                self.stone_id +=1
                e.stonewhen=e.stonefire

            e.stonefire=time.time()

    def stonemanage(self): 
        
        for s in self.stonelist:
            s.update()
            print(len(self.stonelist))
            if s.stonePos()[0] < 0:
                self.canvas.delete(s.stone)
                self.stonelist.pop(self.stonelist.index(s))
        
        hitbox = 50

        h_pos = self.canvas.coords(self.hunter)
        hitbox=50
            
        for s in self.stonelist[:]:  
            s_pos = s.stonePos()
            
            if not s_pos:  
                self.stonelist.remove(s)
                continue

            if (h_pos[0]-hitbox < s_pos[0] < h_pos[0]+hitbox) and (h_pos[1]-hitbox < s_pos[1] < h_pos[1]+hitbox):
                self.canvas.delete(s.stone)   
                self.stonelist.remove(s)
                self.stop_hunter=1
                self.stop_time=time.time()
                self.stone_sound.play()


    def pigmanage(self): 
        self.pigsummon = time.time()
        if self.pigsummon-self.lasttime_p > self.pig_rand:
            self.piglist.append(pig(self.canvas,self.pigimg[0],self.pig_id))
            self.pig_id +=1
            if self.score >= 30000:
                self.piglist.append(pig(self.canvas,self.pigimg[0],self.pig_id))
                self.pig_id +=1
            self.lasttime_p=time.time()
            self.pig_rand = random.randint(2,3)
           
            
        for p in self.piglist:
            p.update()
            self.canvas.itemconfig(p.pig, image = self.pigimg[(p.pigmove%6)//2])
            p.pigmove +=1
            if p.pigPos()[0] < 0:
                self.canvas.delete(p.pig)
                self.piglist.pop(self.piglist.index(p))
                self.gameover()
        self.pigsummon=time.time()
        
        hitbox = 30
        for f in self.firelist[:]:  
            f_pos = self.canvas.coords(f)
            if not f_pos:  
                self.firelist.remove(f)
                continue

            for p in self.piglist[:]: 
                p_pos = p.pigPos()
                if not p_pos:  
                    self.piglist.remove(p)
                    continue

        
                if (p_pos[0]-hitbox < f_pos[0] < p_pos[0]+hitbox) and (p_pos[1]-hitbox < f_pos[1] < p_pos[1]+hitbox):
                    self.canvas.delete(p.pig)   
                    self.piglist.remove(p)
                    self.canvas.delete(f)        
                    self.firelist.remove(f)
                    self.score+=150
                    self.canvas.delete(self.score_text)
                    self.pig_sound.play()
                    self.score_text=self.canvas.create_text(50,10,font="Times 13 bold",text=f"score:{self.score}",fill='black')
                    
                    break
    
                
    def elephantmanage(self):
        self.elephantsummon = time.time()
        if self.elephantsummon-self.lasttime_el > self.elephant_rand:    
            self.elephantlist.append(elephant(self.canvas,self.elephantimg,self.elephant_id))
            self.elephant_id +=1
            if self.score >=100000:
                self.elephantlist.append(elephant(self.canvas,self.elephantimg,self.elephant_id))
                self.elephant_id +=1
            self.lasttime_w=time.time()
            self.lasttime_el=self.elephantsummon
            self.elephant_rand=random.randint(5,7)
           
            
        for el in self.elephantlist:
            el.update()
            if el.elephantPos()[0] < 0:
                self.canvas.delete(el.elephant)
                self.elephantlist.pop(self.elephantlist.index(el))
                self.gameover()
        self.wolfsummon=time.time()
        
        hitbox = 60
        for f in self.firelist[:]:  
            f_pos = self.canvas.coords(f)
            if not f_pos: 
                self.firelist.remove(f)
                continue

            for el in self.elephantlist[:]:  
                el_pos = el.elephantPos()
                if not el_pos:  
                    self.elephantlist.remove(el)
                    continue

        
                if (el_pos[0]-hitbox < f_pos[0] < el_pos[0]+hitbox) and (el_pos[1]-hitbox < f_pos[1] < el_pos[1]+hitbox):
                    self.canvas.delete(f)        
                    self.firelist.remove(f)
                    el.el_life-=1
                    if el.el_life <=0:
                        self.canvas.delete(el.elephant)   
                        self.elephantlist.remove(el)
                        self.elephant_sound.play()
                        self.score+=300
                        self.canvas.delete(self.score_text)
                        self.score_text=self.canvas.create_text(50,10,font="Times 13 bold",text=f"score:{self.score}",fill='black')
                    break

    def gameover (self):
        
        pygame.mixer.music.stop()
        self.gameover_sound.play()
        for w in self.wolflist[:]:
            self.canvas.delete(w.wolf)   
            self.wolflist.remove(w)
            print("wolf")

        for e in self.eaglelist[:]:
            self.canvas.delete(e.eagle)   
            self.eaglelist.remove(e)
            print("eagle")

        for p in self.piglist[:]:
            self.canvas.delete(p.pig)   
            self.piglist.remove(p)
            print("pig")

        for el in self.elephantlist[:]:
            self.canvas.delete(el.elephant)   
            self.elephantlist.remove(el)
            print("elephant")

        for st in self.stonelist[:]:
            self.canvas.delete(st.stone)   
            self.stonelist.remove(st)
            print("stone")

        for f in self.firelist[:]:
            self.canvas.delete(f)   
            self.firelist.remove(f)
            print("fire")



        self.canvas.itemconfigure(self.over_text, state="normal")
        self.final_score=self.canvas.create_text(320,300,font="Times 13 bold",text=f"score:{self.score}",fill='black')
        self.canvas.itemconfigure(self.restart, state="normal")
        self.canvas.delete(self.score_text)
        global gameover
        global realgameover

        gameover = 1
        realgameover = 1
        self.score=0
        


    


    def keyReleaseHandler(self, event):
        if event.keycode in self.keys:
            self.keys.remove(event.keycode)

    def keyPressHandler(self,event):
        if event.keycode == 27:			
            self.onClose()
        else:
            self.keys.add(event.keycode)



    def onClose(self):
        pygame.mixer.music.stop()
        pygame.quit()
        self.window.destroy()
        

GamePlay()
