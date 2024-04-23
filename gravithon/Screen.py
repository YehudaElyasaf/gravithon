from gravithon.Space import Space
from gravithon.Body import Body
from gravithon.Circle import Circle
from gravithon.Line import Line
from gravithon.errors import *
from tkinter import *
from multipledispatch import dispatch
import pkgutil


class Screen:
    def __init__(self, space: Space,
                 start_x: float = None, end_x: float = None, start_y: float = None, end_y: float = None):
        if space.dimensions != 2:
            raise Exception('only 2d spaces are renderable!')

        self.space = space

        self.master = Tk()
        self.master.title = 'Gravithon'

        icon_path = pkgutil.get_data('gravithon', 'img/icon.png')
        icon = PhotoImage(data=icon_path)
        self.master.iconphoto(False, icon)

        # title frame
        self.title_frame = Frame(self.master)
        self.title_frame.pack(fill=X)

        self.play_pause_btn = Button(self.title_frame, command=self.__toggle_play)
        self.play_pause_btn.pack(side=LEFT)

        self.step_btn = Button(self.title_frame, command=self.step)
        self.step_btn.pack(side=LEFT)

        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

        # canvas
        self.canvas = Canvas(self.master, bg=self.space.background_color, bd=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.render()
        self.playing = False

        self.master.bind("<space>", self.__toggle_play)

    def draw_body(self, canvas: Canvas, body: Body):

        if isinstance(body, Circle):
            # draw circle
            x = body.position[0]
            y = body.position[1]

            coords = [(x - body.radius, y - body.radius), (x + body.radius, y + body.radius)]
            coords = self.space_to_px(coords)
            canvas.create_oval(coords, fill=body.color, width=0)
        elif isinstance(body, Line):
            # draw line
            self.master.update()
            # TODO: fill screen allways
            coords = [(0, body.y_intercept()), (canvas.winfo_width(), body.solve(0))]
            coords = self.space_to_px(coords)
            canvas.create_line(coords, fill=body.color, width=3)
        else:
            raise BodyNotSupportedError(body)

    def render(self):
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
        a = 1 / 100000000
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

    def close(self):
        self.master.destroy()

    def step(self):
        self.space.step()
        self.render()

    def animate(self):
        if not self.playing:
            return

        self.step()
        step_duration_ms = int(self.space.step_duration * 1000)  # convert seconds to ms
        self.master.after(step_duration_ms, self.animate)

    def __toggle_play(self, event=None):
        self.playing = not self.playing
        self.animate()

    def show(self):
        self.master.mainloop()

    def play(self):
        self.playing = True
        self.animate()
        self.show()
