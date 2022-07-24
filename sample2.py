def nClick_seconds_up():
    global main_timer
    main_timer += 1
    lbl_timer.config(text=main_timer)

btn_seconds_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_seconds_up, relief='flat', borderwidth=0)


def start_main_timer(main_timer):
    while main_timer:
        m, s = divmod(main_timer, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        main_timer -= 1
        lbl_timer.config(text=main_timer)


btn_start_main_timer = Button(window, text="START/PAUSE", font=("square sans serif 7", 20), command=start_main_timer,
                              relief='flat', bg='black', fg='#fe0000', borderwidth=0)

lbl_timer = Label(window, text=main_timer, bg="black", fg="#fe0000", font=("digital numbers", 60))