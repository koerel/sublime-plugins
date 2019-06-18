import sublime
import sublime_plugin
import re
from subprocess import check_output
import json
import os

class LaravelTransCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        folder = self.view.window().extract_variables()['folder']
        path = folder + "/resources/lang/en/"
        filelist = os.listdir(path)
        transfiles = list(map(lambda l: l.split('.')[0], filelist))
        print(transfiles)
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                content = self.view.substr(line)
                trans = re.search('trans\(\'([a-zA-Z.-]*)\'\)', content)
                end = line.end()
                if trans:
                    parts = trans.group(1).split('.')
                    print(parts)
                    file = parts[0]
                    total = path + file + '.php'
                    print(total)
                    config = check_output(['php', '-r', 'echo json_encode(include "' + total + '");'])
                    config = json.loads(config.decode("utf-8"))
                    print(config.keys())
                    # self.view.window().open_file(total)