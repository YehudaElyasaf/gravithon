from gravithon.Space import Space
from gravithon.Body import Body
from gravithon.Sphere import Sphere
from tkinter import *
from multipledispatch import dispatch


class Screen:
    def __init__(self, space: Space,
                 start_x: float = None, end_x: float = None, start_y: float = None, end_y: float = None):
        if space.dimensions != 2:
            raise Exception('only 2d spaces are renderable!')

        self.space = space
        self.master = Tk()
        self.master.title = 'TITLE'  # TODO

        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

        self.canvas = Canvas(self.master, bg=self.space.background_color, bd=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.enable_pan_and_zoom(self.canvas)

    def draw_body(self, canvas: Canvas, body: Body):
        x = body.position[0]
        y = body.position[1]

        if isinstance(body, Sphere):
            # draw sphere
            coords = [(x - body.radius, y - body.radius), (x + body.radius, y + body.radius)]
            canvas.create_oval(self.space_to_px(coords, canvas), fill=body.color, width=0)

    @staticmethod
    def enable_pan_and_zoom(canvas):
        zoom_factor = 1.1

        def zoom_in(event):
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            factor = zoom_factor
            canvas.scale(ALL, x, y, factor, factor)

        def zoom_out(event):
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            factor = 1 / zoom_factor
            canvas.scale(ALL, x, y, factor, factor)

        def scan_mark(event):
            canvas.scan_mark(event.x, event.y)

        def scan_dragto(event):
            canvas.scan_dragto(event.x, event.y, gain=1)

        canvas.bind_all('<Button-4>', zoom_in)
        canvas.bind_all('<Button-5>', zoom_out)
        canvas.bind('<ButtonPress-1>', scan_mark)
        canvas.bind("<B1-Motion>", scan_dragto)

    def render(self):
        self.canvas.delete(ALL)

        for body in self.space.bodies:
            self.draw_body(self.canvas, body)

    @dispatch(tuple, Canvas)
    def space_to_px(self, point: tuple, canvas: Canvas):
        """
        convert in meters to pixels according to space's size
        :param canvas: canvas
        :param point: x, y
        :return: value in pixels
        """
        x = point[0]
        y = point[1]
        a = 100
        x *= a
        y *= a
        y = canvas.winfo_screenheight() - y

        return x, y

    @dispatch(list, Canvas)
    def space_to_px(self, points: list, canvas: Canvas):
        """
        convert meters to pixels according to space's size
        :param canvas: canvas
        :param points: list of points in meters
        :return: list of points in pixels
        """
        ret = []
        for value in points:
            ret.append(self.space_to_px(value, canvas))

        return ret

    def close(self):
        pass

    def show(self):
        self.render()
        self.master.mainloop()

    def step(self):
        self.render()
        self.space.step()
        step_duration_ms = int(self.space.step_duration * 1000)  # convert seconds to ms
        self.master.after(step_duration_ms, self.step)

    def play(self):
        # TODO: stop condition
        self.step()
        self.master.mainloop()
