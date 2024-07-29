import tkinter
import tkinter.messagebox




def main():
    flag = True

    # button command, change the text on the label
    def change_label_text():
        """
        按钮在红蓝之间转换，取决于flag的值
        flag==True, red
        flag==False, blue

        """
        nonlocal flag       # nonlocal 用来在此函数中使用外部变量
        flag = not flag
        color, msg = ('red', '牵牵你好') \
            if flag else ('blue', '牵牵再见')
        label.config(text=msg, fg=color)

    # button command, confirm to quit
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('Warning:', '你真的不想看到牵牵嘛？'):
            color, msg = ('red', '牵牵生气了！')
            label.config(text=msg, fg=color)
            top.quit()

    # top window
    top = tkinter.Tk()          # generate top window
    top.geometry('800x600')     # set size
    top.title('little game')    # set title

    # label
    label = tkinter.Label(top, text='牵牵你好', font='Arial -32', fg='red')
    label.pack(expand=1)

    # panel generate
    panel = tkinter.Frame(top)

    # button
    button1 = tkinter.Button(panel, text='change', command=change_label_text)
    button1.pack(side='left')

    button2 = tkinter.Button(panel, text='exit', command=confirm_to_quit)
    button2.pack(side='right')

    # panel pack
    panel.pack(side='top')

    # open main loop
    tkinter.mainloop()


if __name__ == '__main__':
    main()
