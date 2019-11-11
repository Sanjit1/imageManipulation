import matplotlib.pyplot as plt
import tkinter
import PIL

window = tkinter.Tk()
window.title('Background Eraser')

picture = ''
picture_jpg = ''


def save_file():
    picture.save((picture_jpg[:-5] + ".png"), 'PNG')
    print("Saved Location: " + picture_jpg[:-5] + ".png")


def select_file():
    print('hi')
    plotter = plt
    picture_jpg = tkinter.filedialog.askopenfilename(
        filetypes=(("Pictures", "*.png;*.jpg;*.jpeg;*.PNG;*.JPG;*.JPEG;*.gif;*.GIF;*.BMP,*.bmp"),
                   ("AlL FiLes StUPid", "*.*")))
    picture = PIL.Image.open(picture_jpg).convert('RGBA')
    plotter.ion()
    picture_load = picture.load()
    fig, axes = plotter.subplots(1, 1)
    plotter.imshow(picture)

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

        for x in range(picture.size[0]):
            for y in range(picture.size[1]):
                r = picture_load[x, y][0]
                b = picture_load[x, y][1]
                g = picture_load[x, y][2]
                if color[0] + 20 > r > color[0] - 20 and color[1] + 20 > b > color[1] - 20 and color[2] + 20 > g > \
                        color[
                            2] - 20:
                    picture_load[x, y] = (255, 255, 255, 0)

        picture.save((picture_jpg[:-5] + ".png"), 'PNG')

        fig_new, axes_new = plotter.subplots(1, 1)
        axes_new.imshow(picture, interpolation='none')
        plotter.show()
        ci = fig_new.canvas.mpl_connect('button_press_event', on_click)
        return coords

    cid = fig.canvas.mpl_connect('button_press_event', on_click)


select_file_button = tkinter.Button(window, text='Select File', width=25, command=select_file)
save_file_button = tkinter.Button(window, text='Save', width=25)
select_file_button.pack()
save_file_button.pack()

window.mainloop()
