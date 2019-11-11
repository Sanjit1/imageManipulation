import matplotlib.pyplot as plotter
import tkinter
import os.path
import PIL

window = tkinter.Tk()
window.title('Background Eraser')


def select_file():
    print('hi')
    picture_jpg = tkinter.filedialog.askopenfilename(
        filetypes=(("Pictures", "*.png;*.jpg;*.jpeg;*.PNG;*.JPG;*.JPEG;*.gif;*.GIF;*.BMP,*.bmp"),
                   ("AlL FiLes StUPid", "*.*")))
    cwd = os.path.dirname(os.path.abspath(__file__))
    picture_cat = PIL.Image.open(picture_jpg).convert('RGBA')
    picture_load = picture_cat.load()
    fig, axes = plotter.subplots(1, 1)
    axes.imshow(picture_cat, interpolation='none')
    plotter.show()

    def on_click(event):
        global ix, iy
        ix, iy = event.xdata, event.ydata
        print('x = %d, y = %d' % (ix, iy))
        coords = [(ix, iy)]
        color = picture_load[ix, iy]
        if len(coords) == 2:
            fig.canvas.mpl_disconnect(cid)
        print(color)

        for x in range(picture_cat.size[0]):
            for y in range(picture_cat.size[1]):
                r = picture_load[x, y][0]
                b = picture_load[x, y][1]
                g = picture_load[x, y][2]
                if color[0] + 20 > r > color[0] - 20 and color[1] + 20 > b > color[1] - 20 and color[2] + 20 > g > \
                        color[
                            2] - 20:
                    picture_load[x, y] = (255, 255, 255, 0)
        picture_cat.save((picture_jpg[:-5]+".png"), 'PNG')
        return coords

    cid = fig.canvas.mpl_connect('button_press_event', on_click)


select_file_button = tkinter.Button(window, text='Select File', width=25, command=select_file)
select_file_button.pack()

window.mainloop()

