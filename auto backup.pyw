#   Minecraft bedrock dedicated server auto backuper v1.0
#      by LightningWB
#################################################################################################
#                   Change These bellow            
##############################################################################################

backupinterval = 60   #       Minutes
worldname = 'My World'  # as in server.prorerties
#     ! ! ! ! ! Edit within quotes ! ! ! !

###################################################################################
#                      Don't change bellow
#######################################################################
from pynput.keyboard import Key, Controller
import pygame
import os
import shutil
import time
from datetime import datetime
from pygame.locals import (
    K_F1,
    K_F2,
    K_F3,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
##################################################            Setup

os.startfile('.\\bedrock_server.exe')
pygame.init
screen=pygame.display.set_mode([300, 300])
pygame.display.set_caption('Auto backup for minecraft bedrock dedicated server')
screen.fill((0, 0, 0))

keyboard = Controller()
try:
        os.mkdir('.\\Backup')
except:
    pass
paused=False
running=True
clock= pygame.time.Clock()
##############################         Functions

def pause():
    global paused
    pygame.draw.circle(screen, (255, 0, 0), (150, 150), 100)
    paused = True

def unpause():
    global paused
    pygame.draw.circle(screen, (0, 255, 0), (150, 150), 100)
    paused = False

def tellchat(message):
    m = 'say ' + message
    keyboard.type(m)
    keyboard.press(Key.enter)

def backup(wrld):
    keyboard.type('stop')
    keyboard.press(Key.enter)
    now = datetime.now()
    new = now.strftime('Day_%d;Month_%m;Year_%Y___Hour_%H;Minute_%M;Second_%S')
    src = '.\\worlds\\' + wrld
    dst = '.\\Backup\\' + new 
    time.sleep(1)
    destination = shutil.copytree(src, dst, copy_function = shutil.copy)
    os.startfile('.\\bedrock_server.exe')

backups = 0
minutes=0
seconds=0
tick=0
unpause()
#################################           Loop  ##################################
while running:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
            elif event.key == K_F1:
                pause()
            elif event.key == K_F2:
                unpause()
            elif event.key == K_F3:
                time.sleep(5)
                keyboard.type('stop')
                keyboard.press(Key.enter)
                running=False
        elif event.type==QUIT:
            running=False
    if not paused:
        tick += 1
        if tick == 30:
            seconds += 1
            tick = 0
            print(seconds)
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes== backupinterval:
            backup(worldname)
            backups += 1
            minutes = 0
            print('Total backups:')
            print(backups)
    ##  Warnings
        # 10 minute warning
        if minutes == backupinterval - 10 and seconds == 0 and tick == 0:
            m = '10 Minutes till save'
            tellchat(m)

        # 5 minute warning
        if minutes == backupinterval - 5 and seconds == 0 and tick == 0:
            m = '5 Minutes till save'
            tellchat(m)

        # 1 minute warning
        if minutes == backupinterval - 1 and seconds == 0 and tick == 0:
            m = '1 Minutes till save'
            tellchat(m)

    pygame.display.flip()
    clock.tick(30)
