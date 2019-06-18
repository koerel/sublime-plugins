import sublime, sublime_plugin, re
CONFIG_FILE = "LaravelGoTo.sublime-settings"

def go_to(view, location):
    view.sel().clear()
    view.sel().add(location)
    view.show_at_center(location)

class LaravelGoToCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        config = sublime.load_settings(CONFIG_FILE)
        locale = config.get("default_locale")
        fallback = config.get("fallback_command")
        folder = self.view.window().extract_variables()['folder']
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                content = self.view.substr(line)
                view = re.search('view\(\'([a-zA-Z.-_]*)\'\)', content)
                config = re.search('config\(\'([a-zA-Z.-_]*)\'\)', content)
                env = re.search('env\(\'([a-zA-Z.-_]*)\',*\s*\'?([a-zA-Z.-_]*)\'*\)', content)
                trans = re.search('[trans|__]\(\'([a-zA-Z.-_]*)\'\)', content)
                if view:
                    parts = view.group(1).split('.')
                    file = parts.pop()
                    path = '/'.join(parts)
                    total = folder + '/resources/views/' + path + '/' + file + '.blade.php'
                    self.view.window().open_file(total)
                elif trans:
                    parts = trans.group(1).split('.')
                    file = parts[0]
                    total = folder + '/resources/lang/' + locale + "/" + file + '.php'
                    self.view.window().open_file(total)
                elif env:
                    key = env.group(1)
                    print(key)
                    total = folder + '/.env'
                    new_view = self.view.window().open_file(total)
                    region = new_view.find(key, 0)
                    go_to(new_view, region.begin())
                elif config:
                    parts = config.group(1).split('.')
                    levels = len(parts)
                    print(levels)
                    search = parts[levels - 1]
                    file = parts[0]
                    total = folder + '/config/' + file + '.php'
                    new_view = self.view.window().open_file(total)
                    tab_size = new_view.settings().get('tab_size')
                    offset = tab_size * (levels - 1)
                    region = new_view.find("\s{" + str(offset) + "}[\'\"]" + search, 0)
                    go_to(new_view, region.begin() + offset)
                else:
                    self.view.window().run_command(fallback)