'''
hero
'''

import tkinter
import mover
import config


class HeroPlane(mover.BaseMover):
    def __init__(self, root, canvas, position, x, y, tags, lives):
        super().__init__(root, canvas, position, x, y, tags, config.image_bigplane_width,
                         config.image_bigplane_height, True)
        # 移动步长
        self.steps = [config.step_length_hero_x, config.step_length_hero_y]
        # 移动方向
        self.move_direction = [0, -1]
        # 图片加载
        self.bg_image_fullname = config.images_path + config.filename_hero + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        #         self.bg_image_tags = tags
        super().set_lives_num(lives)
        root.bind('<KeyPress-Left>', self.key_press)
        root.bind('<KeyPress-Up>', self.key_press)
        root.bind('<KeyPress-Down>', self.key_press)
        root.bind('<KeyPress-Right>', self.key_press)

    def exec_move(self):
        if 0 < self.nw[0] and 0 < self.nw[1] and self.se[0] < config.window_boundary_col and \
                self.se[1] < config.window_boundary_row:
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)
        else:
            if self.nw[0] <= 0:
                self.base_move(self.bg_image_tags, 1, 0)
            if self.nw[1] <= 0:
                self.base_move(self.bg_image_tags, 0, 1)
            if self.se[0] >= config.window_boundary_col:
                self.base_move(self.bg_image_tags, -1, 0)
            if self.se[1] >= config.window_boundary_row:
                self.base_move(self.bg_image_tags, 0, -1)

    # 获取死亡图片
    def get_dead_images(self):
        img = []
        if self.do_dead_play:
            for i in self.dead_image_index:
                image_fullname = config.images_path + config.filename_hero + str(i) + config.filename_suffix
                image = tkinter.PhotoImage(file=self.bg_image_fullname)
                img.append(image)
            return img

    # 英雄跟随按键移动
    def key_press(self, event):
        code = event.keycode

        if code == 38:  # 向上
            self.move_direction = [0, -1]
        elif code == 40:  # 向下
            self.move_direction = [0, 1]
        elif code == 37:  # 向左
            self.move_direction = [-1, 0]
        elif code == 39:  # 向右
            self.move_direction = [1, 0]

    # 英雄跟随鼠标移动
    def follow_mouse(self, event):
        mouse = [event.x, event.y]
        item = self
        # y轴方向移动
        if mouse[1] > item.center[1]:
            item.move_direction[1] = 1
        elif mouse[1] < item.center[1]:
            item.move_direction[1] = -1
        else:
            item.move_direction[1] = 0

        # x轴方向移动
        if mouse[0] > item.center[0]:
            item.move_direction[0] = 1
        elif mouse[0] < item.center[1]:
            item.move_direction[0] = -1
        else:
            item.move_direction[0] = 0

    def Release_mouse(self, event):
        print("into Release_mouse: ", event)