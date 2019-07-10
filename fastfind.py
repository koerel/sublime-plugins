import os
import sublime
import sublime_plugin

class IndentStyleSelectionInputHandler(sublime_plugin.ListInputHandler):

    def name(self):
        return 'name'

    def placeholder(self):
        return 'Allman'

    def list_items(self):
        items = [
            ('Allman', 'allman'),
            ('GNU', 'gnu'),
            ('Horstmann', 'horstmann'),
            ('K & R', 'k_and_r'),
            ('Lisp', 'lisp'),
            ('Pico', 'pico'),
            ('Ratliff', 'ratliff'),
            ('Whitesmiths', 'whitesmiths')
        ]
        return items

    def preview(desc, value):
        
        return ''

class FastFind( sublime_plugin.TextCommand ):
    def run( self, edit ):
        folder = self.view.window().extract_variables()['folder']
        output = os.popen('/usr/local/bin/rg --no-ignore --vimgrep broadcastWith ' + folder).read()
        lines  = output.split('\n')
        print(lines)
        return IndentStyleSelectionInputHandler()