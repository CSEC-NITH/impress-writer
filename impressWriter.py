#!/usr/bin/env python3
'''
  Copyright (c) 2017 Kartikeya Sharma
  Copyright (c) 2017 Navanshu Agarwal
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Pango,Gdk

from thesScript import *
from dictScript import *
from stringProcessing import *
from localData import *
from dataManager import *
from spellCheck import *

class SearchDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Search", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_FIND, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()

        label = Gtk.Label("Insert text you want to search for:")
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()

        
class ProgramWindow(Gtk.Window):
    def __init__(self):

#########Setting_Basic_Window_Size&Border########################################
        
        Gtk.Window.__init__(self,title="Impress Writer")
        self.set_border_width(1)
        self.set_default_size(1366,768)

###################Header_Bar###################################################

        hb=Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title="Impress Writer"
        self.set_titlebar(hb)

#############################Adding_Overall_Grid################################

        self.grid=Gtk.Grid()
        self.add(self.grid)

###################Adding_Toolbar############################################

        self.create_toolbar_top()

###########Adding_TextView#################################################

        self.text_grid = Gtk.Grid()        
        self.create_main_view()
        self.create_textview()
        self.create_toolbar()
        self.create_buttons()

#############Adding synonyms flowbox######################################

        self.create_synonyms_flowbox()
        
    def create_toolbar_top(self):
        toolbar=Gtk.Toolbar()
        self.grid.attach(toolbar,0,0,4,1)

##############New_Button#################################################

        button_new=Gtk.ToolButton()
        button_new.set_icon_name("document-new")
        toolbar.insert(button_new,0)
        toolbar.insert(Gtk.SeparatorToolItem(),1)

##############Open_Button############################################

        button_open=Gtk.ToolButton()
        button_open.set_icon_name("document-open")
        toolbar.insert(button_open,2)
        toolbar.insert(Gtk.SeparatorToolItem(),3)

#############Save_Buton#################################################

        button_save=Gtk.ToolButton()
        button_save.set_icon_name("document-save")
        toolbar.insert(button_save,4)
        toolbar.insert(Gtk.SeparatorToolItem(),5)

#########Help_Button#####################################################

        button_help=Gtk.ToolButton()
        button_help.set_icon_name("help-about")
        toolbar.insert(button_help,6)

    def create_main_view(self):

        #Layout
        
        vbox_main=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)

        hbox_top=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox_top.set_homogeneous(False)

        self.vbox_left1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox_left1.set_homogeneous(False)
        self.vbox_right1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox_right1.set_homogeneous(False)

        hbox_bottom=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox_bottom.set_homogeneous(False)

        self.vbox_left2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox_left2.set_homogeneous(False)

        vbox_right2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right2.set_homogeneous(False)

        vbox_main.pack_start(hbox_top,False,True,0)
        vbox_main.pack_start(hbox_bottom,False,True,0)
        
        hbox_top.pack_start(self.vbox_left1,True,True,0)
        hbox_top.pack_start(self.vbox_right1,False,True,0)

        hbox_bottom.pack_start(self.vbox_left2,True,True,0)
        hbox_bottom.pack_start(vbox_right2,False,True,0)
        
        #Creating Scrolled Window For Dict_Text_View

        scrolledwindow1=Gtk.ScrolledWindow()
        scrolledwindow1.set_hexpand(True)
        scrolledwindow1.set_vexpand(True)

        label=Gtk.Label()
        label.set_markup("<u><b>Dictionary</b></u>")

        self.vbox_right1.pack_start(label,False,True,6)
        self.vbox_right1.pack_start(scrolledwindow1,True,True,0)

        #Defining Dic_Text_View

        self.textview_dict=Gtk.TextView()
        self.textview_dict.set_editable(False)
        self.textbuffer_sample=self.textview_dict.get_buffer()
        self.textbuffer_sample.set_text("Dictionary: Meaning of Selected Word Shall Be Displayed Here")
        scrolledwindow1.add(self.textview_dict)
        self.textview_dict.set_wrap_mode(Gtk.WrapMode.WORD)
        #Right Tool Box

        self.button_replace=Gtk.Button(label="Replace")
        self.button_undo=Gtk.Button(label="Undo")
        self.button_reset=Gtk.Button(label="Reset")
        self.button_original_text=Gtk.Button(label="Original Text")

        self.button_replace.connect('clicked',self.replace_button_clicked)
        
        vbox_right2.pack_start(self.button_replace,True,True,0)
        vbox_right2.pack_start(self.button_undo,True,True,0)
        vbox_right2.pack_start(self.button_reset,True,True,0)
        vbox_right2.pack_start(self.button_original_text,True,True,0)

        self.grid.attach(vbox_main,0,2,10,12)

    #main text window
    def create_toolbar(self):
        toolbar = Gtk.Toolbar()
        self.text_grid.attach(toolbar, 0, 0, 3, 1)
        
        button_bold = Gtk.ToolButton()
        button_bold.set_icon_name("format-text-bold-symbolic")
        toolbar.insert(button_bold, 0)
        
        button_italic = Gtk.ToolButton()
        button_italic.set_icon_name("format-text-italic-symbolic")
        toolbar.insert(button_italic, 1)
        
        button_underline = Gtk.ToolButton()
        button_underline.set_icon_name("format-text-underline-symbolic")
        toolbar.insert(button_underline, 2)
        
        button_bold.connect("clicked", self.on_button_clicked, self.tag_bold)
        button_italic.connect("clicked", self.on_button_clicked,
                              self.tag_italic)
        button_underline.connect("clicked", self.on_button_clicked,
                                 self.tag_underline)
        
        toolbar.insert(Gtk.SeparatorToolItem(), 3)
        
        radio_justifyleft = Gtk.RadioToolButton()
        radio_justifyleft.set_icon_name("format-justify-left-symbolic")
        toolbar.insert(radio_justifyleft, 4)
        
        radio_justifycenter = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifycenter.set_icon_name("format-justify-center-symbolic")
        toolbar.insert(radio_justifycenter, 5)
        
        radio_justifyright = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifyright.set_icon_name("format-justify-right-symbolic")
        toolbar.insert(radio_justifyright, 6)
        
        radio_justifyfill = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifyfill.set_icon_name("format-justify-fill-symbolic")
        toolbar.insert(radio_justifyfill, 7)
        
        radio_justifyleft.connect("toggled", self.on_justify_toggled,
                                  Gtk.Justification.LEFT)
        radio_justifycenter.connect("toggled", self.on_justify_toggled,
                                    Gtk.Justification.CENTER)
        radio_justifyright.connect("toggled", self.on_justify_toggled,
                                   Gtk.Justification.RIGHT)
        radio_justifyfill.connect("toggled", self.on_justify_toggled,
                                  Gtk.Justification.FILL)
        
        toolbar.insert(Gtk.SeparatorToolItem(), 8)
        
        button_clear = Gtk.ToolButton()
        button_clear.set_icon_name("edit-clear-symbolic")
        button_clear.connect("clicked", self.on_clear_clicked)
        toolbar.insert(button_clear, 9)
        
        toolbar.insert(Gtk.SeparatorToolItem(), 10)
        
        button_search = Gtk.ToolButton()
        button_search.set_icon_name("system-search-symbolic")
        button_search.connect("clicked", self.on_search_clicked)
        toolbar.insert(button_search, 11)
        
    def create_textview(self):
        self.vbox_left1.add(self.text_grid)
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.text_grid.attach(scrolledwindow, 0, 1, 3, 1)
        
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("TextViewer: Insert Text Here")
        scrolledwindow.add(self.textview)
        
        self.tag_bold = self.textbuffer.create_tag("bold",
                                                   weight=Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic",
                                                     style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline",
                                                        underline=Pango.Underline.SINGLE)
        self.tag_found = self.textbuffer.create_tag("found",
                                                    background="yellow")
        self.textview.connect("key_release_event",self.on_key_release)
        
    def create_buttons(self):
        check_editable = Gtk.CheckButton("Editable")
        check_editable.set_active(True)
        check_editable.connect("toggled", self.on_editable_toggled)
        self.text_grid.attach(check_editable, 0, 2, 1, 1)
        
        check_cursor = Gtk.CheckButton("Cursor Visible")
        check_cursor.set_active(True)
        check_editable.connect("toggled", self.on_cursor_toggled)
        self.text_grid.attach_next_to(check_cursor, check_editable,
                                 Gtk.PositionType.RIGHT, 1, 1)
        
        radio_wrapnone = Gtk.RadioButton.new_with_label_from_widget(None,
                                                                    "No Wrapping")
        self.text_grid.attach(radio_wrapnone, 0, 3, 1, 1)
        
        radio_wrapchar = Gtk.RadioButton.new_with_label_from_widget(
            radio_wrapnone, "Character Wrapping")
        self.text_grid.attach_next_to(radio_wrapchar, radio_wrapnone,
                                 Gtk.PositionType.RIGHT, 1, 1)
        
        radio_wrapword = Gtk.RadioButton.new_with_label_from_widget(
            radio_wrapnone, "Word Wrapping")
        self.text_grid.attach_next_to(radio_wrapword, radio_wrapchar,
                                 Gtk.PositionType.RIGHT, 1, 1)
        
        radio_wrapnone.connect("toggled", self.on_wrap_toggled,
                               Gtk.WrapMode.NONE)
        radio_wrapchar.connect("toggled", self.on_wrap_toggled,
                               Gtk.WrapMode.CHAR)
        radio_wrapword.connect("toggled", self.on_wrap_toggled,
                               Gtk.WrapMode.WORD)
        
    def on_button_clicked(self, widget, tag):
        bounds = self.textbuffer.get_selection_bounds()
        if len(bounds) != 0:
            start, end = bounds
            self.textbuffer.apply_tag(tag, start, end)
            
    def on_clear_clicked(self, widget):
        start = self.textbuffer.get_start_iter()
        end = self.textbuffer.get_end_iter()
        self.textbuffer.remove_all_tags(start, end)
        
    def on_editable_toggled(self, widget):
        self.textview.set_editable(widget.get_active())
        
    def on_cursor_toggled(self, widget):
        self.textview.set_cursor_visible(widget.get_active())
        
    def on_wrap_toggled(self, widget, mode):
        self.textview.set_wrap_mode(mode)
        
    def on_justify_toggled(self, widget, justification):
        self.textview.set_justification(justification)
        
    def on_search_clicked(self, widget):
        dialog = SearchDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cursor_mark = self.textbuffer.get_insert()
            start = self.textbuffer.get_iter_at_mark(cursor_mark)
            if start.get_offset() == self.textbuffer.get_char_count():
                start = self.textbuffer.get_start_iter()
                
                self.search_and_mark(dialog.entry.get_text(), start)
                
                dialog.destroy()
                
    def search_and_mark(self, text, start):
        end = self.textbuffer.get_end_iter()
        match = start.forward_search(text, 0, end)
        
        if match != None:
            match_start, match_end = match
            self.textbuffer.apply_tag(self.tag_found, match_start, match_end)
            self.search_and_mark(text, match_end)

    #flowbox for synonyms
    
    def create_synonyms_flowbox(self):

        label_Synonyms=Gtk.Label()
        label_Synonyms.set_markup("<u><b>Synonyms</b></u>")
        self.vbox_left2.pack_start(label_Synonyms,False,True,0)
        self.scrolled=Gtk.ScrolledWindow()
        self.scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.flowbox=Gtk.FlowBox()
        self.flowbox.set_valign(Gtk.Align.START)
        self.flowbox.set_max_children_per_line(7)
        self.flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        self.toggle_button_list=[]
        for i in range(100):
            x=Gtk.ToggleButton(label=str(i))
            self.toggle_button_list.append(x)

        for i in range(100):
            self.toggle_button_list[i].connect('clicked',self.toggle_button_clicked)
        
        for i in self.toggle_button_list:
            self.flowbox.add(i)

        self.scrolled.add(self.flowbox)
        self.add(self.scrolled)
        self.vbox_left2.pack_start(self.scrolled,True,True,0)
                                
        ########Implementing Spell Check#############
        self.hbox_inner=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=1)
        self.hbox_inner.set_homogeneous(False)
        label_display=Gtk.Label()
        label_display.set_markup("<b>Spell Check:  </b>")
        
        self.label_spellcheck=Gtk.Label()
        self.label_spellcheck.set_justify(Gtk.Justification.RIGHT)
        
        self.button_substitute=Gtk.Button(label="Substitute")
        self.vbox_right1.pack_start(self.hbox_inner,False,True,2)
        

        self.hbox_inner.pack_end(self.button_substitute,False,True,8) 
        self.hbox_inner.pack_start(label_display,False,True,0)
        self.hbox_inner.pack_start(self.label_spellcheck,True,False,0)
       
        
        
        

#########signal callback functions######################
    def on_key_release(self,widget,ev,data=None):
        if ev.keyval == Gdk.KEY_space:
            for i in range(0,100):
                self.toggle_button_list[i].hide()
            
            start=self.textbuffer.get_start_iter()
            end=self.textbuffer.get_end_iter()
            word_to_fetch=get_last_word(self.textbuffer.get_text(start,end,False))
            #print(word_to_fetch)
            #word_to_fetch="dog"
            self.label_spellcheck.set_label(correction(word_to_fetch.lower()))
            self.synonyms=data_manager_get_synonyms(word_to_fetch)
            #print(synonyms)
            if self.synonyms != None:
                for i in range(0,len(self.synonyms)):
                    self.toggle_button_list[i].set_label(self.synonyms[i])
                    self.toggle_button_list[i].show()

    def toggle_button_clicked(self,widget):
        word=widget.get_label()
        self.string_to_be_replaced=word
        for i in range(0,len(self.synonyms)):
            if not self.toggle_button_list[i].get_label()==widget.get_label():
                self.toggle_button_list[i].set_active(False)
        
        self.textbuffer_sample.set_text(dict_script_get_meaning(word))

    def replace_button_clicked(self,widget):
        start=self.textbuffer.get_start_iter()
        end=self.textbuffer.get_end_iter()
        
        text=self.textbuffer.get_text(start,end,False)
        self.textbuffer.set_text(replace_last_word(self.string_to_be_replaced,text))

    def about_click_event():
        pass

local_data_init()
window= ProgramWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
for i in range(0,100):
    Gtk.Widget.hide(window.toggle_button_list[i])
Gtk.main()
        
    
        
                  
