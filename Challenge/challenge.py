'''
############################## From AliFGT ##############################
'''
from tkinter import *
import pygame
pygame.mixer.init()

root = Tk()
root.title('AliFGT Quiz Generator')
root.iconbitmap('assets/spaceship_red.ico')
root.geometry('500x500')
ft = 'poppins'

def correct():
    swal.pack_forget()
    jwab1.pack_forget()
    jwab.pack_forget()
    pygame.mixer.music.load('Challenge/correct.mp3')
    pygame.mixer.music.play(loops=0)
    q = Label(root, text='Correct Awnser!', font=(ft, 20)).pack(pady=20)
    s = Label(root, text='كان ودي اسوي بعد اسئله لكن\nالوقت لايسمح', font=(ft, 20))
    s.pack(pady=30)


def uncorrect():
    swal.pack_forget()
    jwab1.pack_forget()
    jwab.pack_forget()
    pygame.mixer.music.load('Challenge/incorrect.mp3')
    pygame.mixer.music.play(loops=0)
    q = Label(root, text='UnCorrect Awnser', font=(ft, 20)).pack(pady=20)
    s = Label(root, text='كان ودي اسوي بعد اسئله لكن\nالوقت لايسمح', font=(ft, 20))
    s.pack(pady=30)



def strat():
    global swal
    global jwab
    global jwab1
    wel.pack_forget()
    start.pack_forget()
    ctrdits.pack_forget()
    quiz = open('Challenge/Quiz.txt', 'r', encoding='utf-8')
    swal = Label(root, text=quiz.readline(), font=(ft, 25))
    swal.pack(pady=50)
    awnsers = open('Challenge/Awnsers.txt', 'r', encoding='utf-8')
    jwab = Button(root, text=awnsers.readline(), command=correct)
    jwab.pack()
    jwab1 = Button(root, text=awnsers.readline(), command=uncorrect)
    jwab1.pack(pady=20, ipadx=10, ipady=10)
    

    awnsers.close()
    quiz.close()



def backk():
    back.pack_forget()
    credits1.pack_forget()
    wel.pack(pady=20)
    start.pack(pady=50)
    ctrdits.pack()



def my_credits():
    global back
    global credits1
    wel.pack_forget()
    start.pack_forget()
    ctrdits.pack_forget()
    back = Button(root, text='Back', command=backk, font=(ft, 10))
    back.pack(pady=40)
    credits1 = Label(root, text='تم انشاء السكربت بواسطة علي\nAliFGT\nجميع الحقوق محفوظه', font=(ft, 30))
    credits1.pack()



wel = Label(root, text='Welcome to codezilla Quiz App!', font=(ft, 20))
wel.pack(pady=20)

start = Button(root, text='Click to Start', font=(ft, 20), command=strat)
start.pack(pady=50)

ctrdits = Button(root, text='Credits', font=(ft, 20), command=my_credits)
ctrdits.pack()


root.mainloop()