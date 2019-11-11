import matplotlib.pyplot as plt
import tkinter
import PIL
from PIL import ImageTk

window = tkinter.Tk()
window.title('Background Eraser')
window.geometry("800x450")

images = tkinter.Label(window)

picture = ''
picture_jpg = ''


def all_children(wind):
    _list = wind.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


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

        image_tk = ImageTk.PhotoImage(picture)

        for item in all_children(window):
            item.pack_forget()
            
        title = tkinter.Label(window, text='Background Eraser, by Sanjit and Wyatt', width=69).pack()
        select_file_button = tkinter.Button(window, text='Select File', width=25, command=select_file).pack()
        save_file_button = tkinter.Button(window, text='Save', width=25, command=save_file).pack()
        images = tkinter.Label(window, image=image_tk, width=picture.size[0])
        images.pack()
        window.mainloop()

        fig_new, axes_new = plotter.subplots(1, 1)
        axes_new.imshow(picture, interpolation='none')
        plotter.show()
        fig_new.canvas.mpl_connect('button_press_event', on_click)
        return coords

    fig.canvas.mpl_connect('button_press_event', on_click)


title = tkinter.Label(window, text='Background Eraser, by Sanjit and Wyatt', width=69).pack()
select_file_button = tkinter.Button(window, text='Select File', width=25, command=select_file).pack()
save_file_button = tkinter.Button(window, text='Save', width=25, command=save_file).pack()

window.mainloop()
