import gi

from gi.repository import Gtk

class AddGoalWidget(Gtk.Frame):
    def __init__(self):
        Gtk.Frame.__init__(self, label="Add Goal")
        self.add_stuff()

    def add_stuff(self):

        self.content = Gtk.VBox()

        self.name_row = NameRow()
        self.date_row = DateRow()

        self.content.add(self.name_row)
        self.content.add(self.date_row)
        self.add(self.content)

class DateRow(Gtk.HBox):
    def __init__(self):
        Gtk.HBox.__init__(self)
        self.calendar = Gtk.Calendar()
        self.add(self.calendar)

class NameRow(Gtk.HBox):
    def __init__(self):
        Gtk.HBox.__init__(self)
        self.add(Gtk.Label("Goal Name:"))
        self.name_input = Gtk.Entry()
        self.add(self.name_input)

