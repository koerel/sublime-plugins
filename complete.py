import sublime, sublime_plugin, re

class CompleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        tabsize = 2
        syntax = self.view.settings().get('syntax').split('/')[-1]
        if syntax == 'PHP.sublime-syntax':
            tabsize = 4;
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                content = self.view.substr(line)
                case = re.search('case', content)
                match = re.search('(if|for|foreach|while|switch)\s?\(.*\)', content)
                end = line.end();
                print(content)
                if case:
                    offset =  case.span()[0]
                    self.view.insert(edit, end, ":\n")
                    end += 2
                    for x in range(0, offset + tabsize):
                        self.view.insert(edit, end, " ")
                        end += 1
                    cursor = end
                    self.view.insert(edit, end, "\n")
                    end += 1
                    for x in range(0, offset + tabsize):
                        self.view.insert(edit, end, " ")
                        end += 1
                    self.view.insert(edit, end, "break;")
                    self.view.sel().clear()
                    self.view.sel().add(cursor)
                elif match:
                    offset =  match.span()[0]
                    self.view.insert(edit, end, " {\n")
                    end += 3
                    for x in range(0, offset + tabsize):
                        self.view.insert(edit, end, " ")
                        end += 1
                    cursor = end
                    self.view.insert(edit, end, "\n")
                    end += 1
                    for x in range(0, offset):
                        self.view.insert(edit, end, " ")
                        end += 1
                    self.view.insert(edit, end, "}")
                    self.view.sel().clear()
                    self.view.sel().add(cursor)
                else:
                    cursor = end + 1
                    self.view.insert(edit, end, ";")
                    self.view.sel().clear()
                    self.view.sel().add(cursor)











