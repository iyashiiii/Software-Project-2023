  def shortcut(s, event):
        if event.keysym == 'Return' and event.state == 8:
            s.new_window
        elif event.keysym == 'Return' and event.state == 0:
            s.new_window