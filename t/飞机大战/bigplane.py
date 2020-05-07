'''
bigplane
'''

import tkinter
import mover
import config


class BigPlane(mover.BaseMover):
    def __init__(self, root, canvas, position, x, y, tags):
        super().__init__(root, canvas, position, x, y, tags, config.image_bigplane_width,
                         config.image_bigplane_height, True)
        # 移动步长
        self.steps = [config.step_length_bigplane_x, config.step_length_bigplane_y]
        # 移动方向
        self.move_direction = [0, 1]
        # 图片加载
        self.bg_image_fullname = config.images_path + config.filename_bigplane + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        self.bg_image_tags = tags

    def exec_move(self):
        if self.nw[1] < config.window_boundary_row:
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)
        else:
            self.base_move(self.bg_image_tags, 0, -config.window_boundary_row)

    # 获取死亡图片
    def get_dead_images(self):
        img = []
        if self.do_dead_play:
            for i in self.dead_image_index:
                image_fullname = config.images_path + config.filename_bigplane + str(i) + config.filename_suffix
                image = tkinter.PhotoImage(file=self.bg_image_fullname)
                img.append(image)
            return img