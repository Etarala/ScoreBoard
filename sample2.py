def pause():
    global paused_main_timer
    paused_main_timer = not paused_main_timer
    if not paused_main_timer:
        update_main_timer()

def update_main_timer():
    global period_time
    global paused_main_timer
    if paused_main_timer:
        btn_pause_main_timer.config(bg='yellow')
        return
    btn_pause_main_timer.config(bg='black')
    period_time = period_time - 1
    if period_time >= 0:
        m, s = divmod(period_time, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        lbl_timer.config(text=min_sec_format)
        window.after(1000, update_main_timer)

def start_main_timer(timer):
    global period_time
    global game_started
    if game_started:
        return
    else:
        game_started = True
        m, s = divmod(period_time+1, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        period_time = timer
        lbl_timer.config(text=min_sec_format)
        window.after(1000, update_main_timer)


command=lambda: start_main_timer(period_time),