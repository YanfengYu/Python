'''
飞机大战游戏的全局配置文件config
'''

import tkinter as tk
import os
import random as rd



game_flag = ''

#游戏窗口的标题和边界
window_title = "Plant Warface Game"
window_boundary_row = 600
window_boundary_col = 480

#角色的生命状态
life_status_alive = 0 #活动
life_status_dead = 1  #死亡
life_status_reset = 2 #重置

#角色生命值
lives_num_enemy = 1
lives_num_hero = 3

#游戏中各部位图像的路径和文件名
images_path = os.getcwd() + os.path.join("/Images/")
filename_suffix = ".gif"
filename_sky = "background"
filename_pause = "pause"
filename_start = "start"
filename_start_label = "start_label"
filename_gameover = "gameover"
filename_smallplane = "smallplane"
filename_bee = "bee"
filename_bigplane = "bigplane"
filename_bullet = "bullet"
filename_hero = "hero"
filename_default = filename_hero


#游戏中各部件的宽和高
image_sky_width = 480
image_sky_height = 600
image_pause_width = 400
image_pause_height = 654
image_start_width = 400
image_start_height = 654
image_gameover_width = 400
image_gameover_height = 654
image_smallplane_width = 49
image_smallplane_height = 36
image_bigplane_width = 69
image_bigplane_height = 99
image_bullet_width = 8
image_bullet_height = 14
image_hero_width = 97
image_hero_height = 124
image_bee_width = 60
image_bee_height = 50



#游戏中各图片的初始锚点及对应初始显示位置坐标
#天空
initial_anchor_sky_1 = tk.SE
initial_anchor_sky_x_1 = window_boundary_col
initial_anchor_sky_y_1 = window_boundary_row
#暂停
initial_anchor_pause = tk.CENTER
initial_anchor_pause_x = window_boundary_col/2
initial_anchor_pause_y = window_boundary_row/2
#开始
initial_anchor_start = tk.CENTER
initial_anchor_start_x = window_boundary_col/2
initial_anchor_start_y = window_boundary_row/2
#结束
initial_anchor_gameover = tk.CENTER
initial_anchor_gameover_x = window_boundary_col/2
initial_anchor_gameover_y = window_boundary_row/2
#小飞机
initial_anchor_smallplane = tk.SW
initial_anchor_smallplane_x = rd.randint(0,window_boundary_col-image_smallplane_width)
initial_anchor_smallplane_y = 0
#大飞机
initial_anchor_bigplane = tk.SW
initial_anchor_bigplane_x = rd.randint(0,window_boundary_col-image_bigplane_width)
initial_anchor_bigplane_y = 0
#蜜蜂
initial_anchor_bee = tk.NW
initial_anchor_bee_x = rd.randint(0,window_boundary_col-image_bee_width)
initial_anchor_bee_y = 0
#英雄
initial_anchor_hero = tk.CENTER
initial_anchor_hero_x = window_boundary_col/2
initial_anchor_hero_y = window_boundary_row/3*2
#英雄的子弹
initial_anchor_bullet = tk.CENTER
initial_anchor_bullet_x = window_boundary_col/2
initial_anchor_bullet_y = window_boundary_row/3*2


#各部件的移动步长
step_length_default = 1
step_length_sky_x = 0
step_length_sky_y = 10
step_length_smallplane_x = 0
step_length_smallplane_y = 5
step_length_bigplane_x = 0
step_length_bigplane_y = 3
step_length_bee_x = 5
step_length_bee_y = 3
step_length_bullet_x = 0
step_length_bullet_y = 12
step_length_hero_x = 5
step_length_hero_y = 5


#记录生成各部件的计数
total_number_hero = 0
total_number_bullet = 0
total_number_smallplane = 0
total_number_bigplane = 0
total_number_bee = 0


#记录当前各部件的数目
current_bullet_num = 1
current_number_hero = 0
current_number_smallplane = 0
current_number_bigplane = 0
current_number_bee = 0


#击落敌军的奖励分数
score_enemy_small = 2
score_enemy_big = 5
score_enemy_bee = 1
score_highest = 10


#标识
bullet_create_flag = 1
hero_move_flag = True
break_record_flag = False
hero_aircraft_death = False


#击落战机数量
defeat_big_nums = 0
defeat_small_nums = 0
defeat_bee_nums = 0