import sublime
import sublime_plugin
import subprocess
import os
from subprocess import check_output
import re
import json

global files

def plugin_loaded():
    global files
    global path
    folder = sublime.active_window().extract_variables()['folder']
    path = folder + "/resources/lang/en/"
    filelist = os.listdir(path)
    transfiles = list(map(lambda l: l.split('.')[0], filelist))
    files = list(map(lambda t: [t + "\t" + "trans", t] ,transfiles))
    print(files)

class LaravelTransComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        for region in view.sel():
            if region.empty():
                line = view.line(region)
                content = view.substr(line)
                trans = re.search('trans\(\'([a-zA-Z.-]*)\'\)', content)
                end = line.end()
                if trans:
                    default_completions = view.extract_completions(prefix)
                    parts = trans.group(1).split('.')
                    print(parts)
                    if len(parts) == 1:
                        for comp in default_completions:
                            files.append(comp)
                        return files
                    if len(parts) == 2:
                        file = parts[0]
                        total = path + file + '.php'
                        print(total)
                        config = check_output(['php', '-r', 'echo json_encode(include "' + total + '");'])
                        config = json.loads(config.decode("utf-8"))
                        completions = list(map(lambda k: [k + "\ttrans", k], config.keys()))
                        for comp in default_completions:
                            completions.append(comp)
                        return completions
