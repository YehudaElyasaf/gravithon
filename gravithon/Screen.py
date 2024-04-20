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
        # TODO: colors
        self.render()

        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

    def draw_body(self, canvas: Canvas, body: Body):
        x = body.position[0]
        y = body.position[1]

        if isinstance(body, Sphere):
            # draw sphere
            coords = x - body.radius, y - body.radius, x + body.radius, y + body.radius
            canvas.create_oval(self.mtopx(coords), fill=body.color)

    def enable_pan_and_zoom(self, canvas):
        ZOOM_FACTOR = 1.1

        def zoom_in(event):
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            factor = ZOOM_FACTOR
            canvas.scale(ALL, x, y, factor, factor)

        def zoom_out(event):
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            factor = 1 / ZOOM_FACTOR
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
        canvas = Canvas(self.master, bg=self.space.background_color, bd=0)
        self.enable_pan_and_zoom(canvas)

        for body in self.space.bodies:
            self.draw_body(canvas, body)

        canvas.pack(fill=BOTH, expand=True)
        self.master.mainloop()

    @dispatch(float)
    def mtopx(self, m: float):
        """
        convert in meters to pixels according to space's size
        :param m:value in meters
        :return:value in pixels
        """
        return m / 100000000

    @dispatch(tuple)
    def mtopx(self, m: tuple):
        """
        convert meters to pixels according to space's size
        :param m:tuple of values in meters
        :return:tuple of values in pixels
        """
        ret = ()
        for value in m:
            ret += (self.mtopx(value),)

        return ret


def close(self):
    pass
