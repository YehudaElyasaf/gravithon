import copy

from gravithon.Space import Space
from gravithon.Body import Body
from gravithon.Circle import Circle
from gravithon.Line import Line
from gravithon.errors import *
from gravithon.units import time
from tkinter import *
from multipledispatch import dispatch
import pkgutil


class Screen:
    def __init__(self, space: Space,
                 start_x: float = None, end_x: float = None, start_y: float = None, end_y: float = None,
                 outline_width: int = 0):
        if space.dimensions != 2:
            raise Exception('only 2d spaces are renderable!')

        self.speed = 1.0
        self.frame = 0
        self.frames = [space]

        self.master = Tk()
        self.master.title('Gravithon')

        # title frame
        self.title_frame = Frame(self.master)
        self.title_frame.pack(fill=X)

        # previous frame button
        self.step_btn = Button(self.title_frame, command=self.previous_frame)
        self.step_btn.pack(side=LEFT)

        # play pause button
        self.play_pause_btn = Button(self.title_frame, command=self.__toggle_play)
        self.play_pause_btn.pack(side=LEFT)

        # next frame button
        self.step_btn = Button(self.title_frame, command=self.next_frame)
        self.step_btn.pack(side=LEFT)

        # time label
        self.time_lbl = Label(self.title_frame)
        self.time_lbl.pack(side=LEFT)

        # frame label
        self.frame_lbl = Label(self.title_frame, text='Frame: ')
        self.frame_lbl.pack(side=LEFT)

        def frame_entry_callback(event):
            frame_entry_text = self.frame_entry.get()
            try:
                frame_number = int(frame_entry_text)
                if frame_number >= 0:
                    self.to_frame(frame_number)
            except ValueError:
                pass

            self.render()
            # unfocus entry
            self.master.focus()

            # write frame number
            self.frame_entry.delete(0, END)
            self.frame_entry.insert(0, str(self.frame))

        self.frame_entry = Entry(self.title_frame, width=5)
        self.frame_entry.pack(side=LEFT)
        self.frame_entry.bind('<Return>', frame_entry_callback)

        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

        # canvas
        self.canvas = Canvas(self.master, bg=self.space.background_color, bd=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.outline_width = outline_width
        self.render()
        self.playing = False

        # key binds
        self.master.bind('<space>', self.__toggle_play)

        # avoid errors on close
        self.master.protocol("WM_DELETE_WINDOW", self.canvas.destroy)
        self.master.protocol("WM_DELETE_WINDOW", self.master.destroy)

    @property
    def space(self):
        return self.frames[self.frame]

    def draw_body(self, canvas: Canvas, body: Body):
        # draw circle
        if isinstance(body, Circle):
            coords = [(body.x - body.radius, body.y - body.radius), (body.x + body.radius, body.y + body.radius)]
            coords = self.space_to_px(coords)
            canvas.create_oval(coords, fill=body.color, width=self.outline_width, outline=body.color)
        # draw line
        elif isinstance(body, Line):
            self.master.update()
            # TODO: fill screen allways
            coords = [(0, body.y_intercept()), (canvas.winfo_width(), body.solve(canvas.winfo_width()))]
            coords = self.space_to_px(coords)
            canvas.create_line(coords, fill=body.color, width=3)
        else:
            raise BodyNotSupportedError(body)

    @staticmethod
    def __time_to_str(seconds):
        if seconds == 0:
            return '%05.2f' % seconds

        # nanoseconds
        if seconds < time.microsecond:
            ns = seconds / time.nanosecond
            return '%05.2f ns' % ns

        # microseconds
        elif seconds < time.millisecond:
            μs = seconds / time.microsecond
            return '%05.2f μs' % μs

        # milliseconds
        elif seconds < time.second:
            ms = seconds / time.millisecond
            return '%05.1f ms' % ms  # different format because milliseconds has 3 digits

        # seconds
        elif seconds < time.minute:
            s = seconds
            return '%05.2f s' % s

        # minutes
        elif seconds < time.hour:
            m = seconds / time.minute
            return '%05.2f h' % m

        # hours
        elif seconds < time.day:
            h = seconds / time.hour
            return '%05.2f h' % h

        # days
        else:
            d = seconds / time.day
            return '%05.2f d' % d

    def render(self):
        # title frame
        time_text = 'Time: ' + self.__time_to_str(self.space.time)
        self.time_lbl.config(text=time_text)

        # write frame number
        self.frame_entry.delete(0, END)
        self.frame_entry.insert(0, str(self.frame))

        # canvas
        self.canvas.delete(ALL)
        for body in self.space.bodies:
            self.draw_body(self.canvas, body)

    @dispatch(tuple)
    def space_to_px(self, point: tuple):
        """
        convert in meters to pixels according to space's size
        :param point: x, y
        :return: value in pixels
        """
        x = point[0]
        y = point[1]
        # TODO: decide ratio
        a = 1 / 150000000
        a = 100
        x *= a
        y *= a
        self.master.update()
        y = self.canvas.winfo_height() - y

        return x, y

    @dispatch(list)
    def space_to_px(self, points: list):
        """
        convert meters to pixels according to space's size
        :param points: list of points in meters
        :return: list of points in pixels
        """
        ret = []
        for value in points:
            ret.append(self.space_to_px(value))

        return ret

    def to_frame(self, frame: int):
        if frame < 0:
            # frame doesn't exist
            raise Exception(f'frame {frame} doesn\'t exist')

        if frame == self.frame:
            # no need to move
            return

        if frame < len(self.frames):
            # frame already exists in frame list
            self.frame = frame
        else:
            # step to frame
            self.frame = len(self.frames) - 1  # move to last frame exists
            while self.frame < frame:
                # move to next frame
                self.frames.append(copy.deepcopy(self.space))
                self.frame += 1
                self.space.step(self.speed)

        self.render()

    def next_frame(self):
        self.to_frame(self.frame + 1)

    def previous_frame(self):
        self.to_frame(self.frame - 1)

    def animate(self):
        # stop if not playing
        if not self.playing:
            return

        try:
            self.next_frame()
        except TclError:
            # master has been destroyed
            return

        step_duration_ms = int(self.space.step_duration * 1000)  # convert seconds to ms
        self.master.after(step_duration_ms, self.animate)

    def __toggle_play(self, event=None):
        self.playing = not self.playing
        self.animate()

    def show(self, speed: float = None):
        if speed is not None:
            self.speed = speed

        self.master.mainloop()

    def play(self, speed: float = None):
        self.playing = True
        self.animate()
        self.show(speed)
