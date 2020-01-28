from tkinter.ttk import *
from tkinter import *
import matplotlib.pyplot as plt
import random
import time
import mysql.connector
counter=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
first=''
last=''
age=0
region=''
gender=''
try:
    def close():
        master.destroy()
    def show():
        global first
        global last
        global age
        global region
        global gender
        if v==1:
            gender='Male'
        elif v==2:
            gender='Female'
        elif v==3:
            gender='Other'
        first,last,age,region=e1.get(),e2.get(),spin.get(),combo.get()
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='')
        cur=sql.cursor()
        try:
            cur.execute('create database game')
        except:
            pass    
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        try:
            cur.execute('create table score (Name char(100),Score int(2),Age int(2),Region char(100),Gender char(100))')
        except:
            pass
        com='insert into score (Name,Score,Age,Region,Gender) values(%s,%s,%s,%s,%s)'
        val=(str(first+' '+last),str(counter),str(age),str(region),str(gender))
        cur.execute(com,val)
        sql.commit()
    def game():
        tk=Toplevel(master)
        tk.wm_iconbitmap('BRICK-BREAKER_LOGO.ico')
        tk.title('Brick Breacker')
        tk.resizable(0,0)
        tk.wm_attributes('-topmost',1)
        canvas=Canvas(tk,width=535,height=400,bd=0,highlightthickness=0)
        canvas.pack()
        canvas.update()
        class Ball:
            def __init__(self,canvas,paddle,block,color):
                self.canvas=canvas
                self.paddle=paddle
                self.block=block
                self.id=canvas.create_oval(5,5,25,25,fill=color)
                self.canvas.move(self.id,245,100)
                starts=[-3,-2,-1,1,2,3]
                random.shuffle(starts)
                self.x=starts[0]
                self.y=-10
                self.canvas_height=self.canvas.winfo_height()
                self.canvas_width=self.canvas.winfo_width()
                self.hit_bottom=False
            def score(self):
                global counter
                counter+=1
                tk.title('Score: '+str(counter))
            def hit_block(self,pos):
                block_pos=self.canvas.coords(self.block.id)
                List=[block_pos]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global a
                            a+=1
                            return True
                return False
            def hit_block1(self,pos):
                block_pos1=self.canvas.coords(self.block.id1)
                List=[block_pos1]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global b
                            b+=1
                            return True           
                return False
            def hit_block2(self,pos):
                block_pos2=self.canvas.coords(self.block.id2)
                List=[block_pos2]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global c
                            c+=1
                            return True
                return False
            def hit_block3(self,pos):
                block_pos3=self.canvas.coords(self.block.id3)
                List=[block_pos3]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global d
                            d+=1
                            return True
                return False
            def hit_block4(self,pos):
                block_pos4=self.canvas.coords(self.block.id4)
                List=[block_pos4]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global e
                            e+=1
                            return True
                return False
            def hit_block5(self,pos):
                block_pos5=self.canvas.coords(self.block.id5)
                List=[block_pos5]
                for i in List:
                    if (pos[0] >=i[0] and pos[2]<=i[2]): 
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global f
                            f+=1
                            return True
                    if pos[2]>=i[0] and pos[0]<=i[2]:
                        if pos[3]>=i[1] and pos[3]<=i[3]:
                            f+=1
                            return False
            def hit_block6(self,pos):
                block_pos6=self.canvas.coords(self.block.id6)
                List=[block_pos6]
                for i in List:
                    if pos[0]>=i[0] and pos[2]<=i[2]:
                        if pos[1]>=i[1] and pos[1]<=i[3]:
                            self.score()
                            global g
                            g+=1
                            return True
                    if pos[2]>=i[0] and pos[0]<=i[2]:
                        if pos[3]>=i[1] and pos[3]<=i[3]:
                            g+=1
                            return False
            def hit_paddle(self,pos):
                paddle_pos=self.canvas.coords(self.paddle.id)
                if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                    if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                        self.x+=self.paddle.x
                        self.y+=1
                        return True
                return False
            def draw(self):
                self.canvas.move(self.id,self.x,self.y)
                pos=self.canvas.coords(self.id)
                if pos[1]<=0:
                    self.y=3
                if self.hit_block(pos)==True:
                    self.y=3
                    self.block.id=canvas.create_rectangle(10,10,110,20,fill='yellow')
                if self.hit_block1(pos)==True:
                    self.y=3
                    self.block.id1=canvas.create_rectangle(115,10,215,20,fill='yellow')
                if self.hit_block2(pos)==True:
                    self.y=3
                    self.block.id2=canvas.create_rectangle(220,10,320,20,fill='yellow')
                if self.hit_block3(pos)==True:
                    self.y=3
                    self.block.id3=canvas.create_rectangle(325,10,425,20,fill='yellow')
                if self.hit_block4(pos)==True:
                    self.y=3
                    self.block.id4=canvas.create_rectangle(430,10,530,20,fill='yellow')
                if self.hit_block5(pos)==True:
                     self.y=3
                     self.block.id5=canvas.create_rectangle(100,150,200,160,fill='yellow')
                if self.hit_block5(pos)==False:
                     self.y=-3
                     self.block.id5=canvas.create_rectangle(100,150,200,160,fill='yellow') 
                if self.hit_block6(pos)==False:
                     self.y=-3
                     self.block.id6=canvas.create_rectangle(350,150,450,160,fill='yellow')
                if self.hit_block6(pos)==True:
                    self.y=3
                    self.block.id6=canvas.create_rectangle(350,150,450,160,fill='yellow')
                if pos[3]>=self.canvas_height:
                    self.hit_bottom=True
                if pos[3]>=self.canvas_height:
                    self.y=3
                if self.hit_paddle(pos)==True:
                    self.y=-3
                    canvas.delete(block)
                if pos[0]<=0:
                    self.x=3
                if pos[2]>=self.canvas_width:
                    self.x=-3
        class Block:
            def __init__(self,canvas,color):
                self.canvas=canvas
                self.id=canvas.create_rectangle(10,10,110,20,fill=color )
                self.id1=canvas.create_rectangle(115,10,215,20,fill=color)
                self.id2=canvas.create_rectangle(220,10,320,20,fill=color)
                self.id3=canvas.create_rectangle(325,10,425,20,fill=color)
                self.id4=canvas.create_rectangle(430,10,530,20,fill=color)
                self.id5=canvas.create_rectangle(100,150,200,160,fill=color)
                self.id6=canvas.create_rectangle(350,150,450,160,fill=color)
                self.x=0
        class Paddle:
            def __init__(self,canvas,color):
                self.canvas=canvas
                self.id=canvas.create_rectangle(0,0,100,10,fill=color)
                self.canvas.move(self.id,230,300)
                self.x=0
                self.canvas_width=self.canvas.winfo_width()
                self.started=False
                self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
                self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
                self.canvas.bind_all('<Button-1>',self.start_game)
            def draw(self):
                self.canvas.move(self.id,self.x,0)
                pos=self.canvas.coords(self.id)
                if pos[0]<=0:
                    self.x=0
                elif pos[2]>=self.canvas_width:
                    self.x=0
            def turn_left(self,evt):
                pos=self.canvas.coords(self.id)
                if pos[0]>=0:
                    self.x=-5
            def turn_right(self,evt):
                pos=self.canvas.coords(self.id)
                if pos[2]<=self.canvas_width:
                    self.x=5
            def start_game(self,evt):
                self.started=True
        paddle=Paddle(canvas,'blue')
        block=Block(canvas,'green')
        ball=Ball(canvas,paddle,block,'red')
        while 1:
            if ball.hit_bottom==False and paddle.started==True:
                ball.draw()
                paddle.draw()
            if ball.hit_bottom==True:
                canvas.create_text(270,200,text='GAME OVER',font=28)
                canvas.create_text(270,250,text='Score='+str(counter),font=28)
            if a and b and c and d and e and f and g>=1:
                ball.y=0
                ball.x=0
                paddle.x=0
                canvas.create_text(270,200,text='YOU WIN!',font=28)
                canvas.create_text(270,250,text=' Score='+str(counter),font=28)
                break
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        tk.mainloop()
    def search():
        global first
        global last
        first,last=e1.get(),e2.get()
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        n=str(first+' '+last)
        sco='select Name,Score from score where Name="%s"'%n
        cur.execute(sco,n)
        for x in cur:
            print(x[1],'has scored',x[0])
    def graph():
        try:
            sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
        except:
            sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
        cur=sql.cursor()
        cur.execute('select  * from score')
        names=[]
        scores=[]
        for x in cur:
            names.append(x[0])
            scores.append(x[1])
        plt.bar(names,scores)
        plt.xlabel('User')
        plt.ylabel('Score')
        scale_y=1
        '''plt.savefig('graph.png')
        image=PhotoImage(file='graph.png')
        Label(master,image=image).grid(row=20)'''
        plt.show()
    master=Tk()
    master.geometry('600x300')
    master.wm_iconbitmap('BRICK-BREAKER_LOGO.ico')
    master.title('Brick Breacker')
    master.configure(background="#A9FF9E")
    
    style=ttk.Style()
    style.configure("TButton", foreground="#84E2E8", background="#E8D884", font=("Jokerman", 10), anchor="center")
    style.configure("TLabel", foreground="#84E2E8", background="#E8D884", font=("Jokerman", 10), anchor="center")                 
    ttk.Label(master,text='First Name:').grid(row=0)
    ttk.Label(master,text='Last Name:').grid(row=1)
    e1=Entry(master,width=50)
    e1.grid(row=0,column=100,pady=5,padx=5)
    e2=Entry(master,width=50)
    e2.grid(row=1,column=100,pady=5,padx=5)
    ttk.Label(master,text='Age:').grid(row=2)
    spin=Spinbox(master,from_=1,to=90,width=48)
    spin.grid(row=2,column=100,pady=5)
    ttk.Label(master,text='Region:').grid(row=3)
    combo=Combobox(master,width=47)
    combo['values']=tuple(['Select','Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Costa Rica', 'Côte d’Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon','The Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'North Korea', 'South Korea', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Federated States of Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'])
    combo.current(0)
    combo.grid(column=100,row=3,pady=5)
    ttk.Label(master,text='Gender:').grid(row=4,pady=2)
    v=IntVar()
    Radiobutton(master,text='Male',variable=v,value=1).grid(row=4,column=100)
    Radiobutton(master,text='Female',variable=v,value=2).grid(row=5,column=100)
    Radiobutton(master,text='Other',variable=v,value=3).grid(row=6,column=100)
    ttk.Button(master,text='Search',command=search).grid(row=15,column=3,padx=5)
    ttk.Button(master,text='Enter',command=lambda:[show(),game()]).grid(row=15,column=2,padx=5)
    ttk.Button(master,text='Exit',command=master.destroy).grid(row=15,column=4,padx=5)
    ttk.Button(master,text='Graph',command=graph).grid(row=15,column=5,padx=5)
    master.mainloop()
except:
    print()
try:
    sql=mysql.connector.connect(host='localhost',user='root',password='root')
except:
    sql=mysql.connector.connect(host='localhost',user='root',password='')
cur=sql.cursor()
try:
    cur.execute('create database game')
except:
    pass
try:
    sql=mysql.connector.connect(host='localhost',user='root',password='root',database='game')
except:
    sql=mysql.connector.connect(host='localhost',user='root',password='',database='game')
cur=sql.cursor()
try:
    cur.execute('create table score (Name char(100),Score int(2),Age int(2),Region char(100),Gender char(100))')
except:
    pass
com='insert into score (Name,Score,Age,Region,Gender) values(%s,%s,%s,%s,%s)'
val=(str(first+' '+last),str(counter),str(age),str(region),str(gender))
cur.execute(com,val)
sql.commit()
cur=sql.cursor()
cur.execute('select  * from score')
