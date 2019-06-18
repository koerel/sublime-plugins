import sublime, sublime_plugin, re
import json

class NamespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if '/app/' in filename:
            base_path = self.view.file_name().split('app/')[0]
            file_path = self.view.file_name().split('app/')[1]
            parts = file_path.split('/')
            parts.pop()
            location = 'app'
            with open(base_path + 'composer.json') as data_file:    
                data = json.load(data_file)
            namespace_root = list(data['autoload']['psr-4'])[0]
            namespace = 'namespace ' + namespace_root + '\\'.join(parts) + ';'
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                self.view.erase(edit, line)
                self.view.insert(edit, line.a, namespace)













