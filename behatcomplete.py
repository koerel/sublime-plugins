import sublime
import sublime_plugin
import subprocess

def plugin_loaded():
    global results
    folder = sublime.active_window().extract_variables()
    print(folder)
    test = subprocess.check_output(["/Users/karel/Code/degroeneboog-api/vendor/bin/behat", "-c", "/Users/karel/Code/degroeneboog-api/behat.yaml", "-dl"])
    lines = test.decode('utf-8').split("\n")
    results = []
    for line in lines:
        line = line.replace("default | ", "")
        line = line.replace("/^", "")
        line = line.replace("(?:|I )", "I ")
        line = line.replace('(?P<field>(?:[^"]|\")*)', "")
        line = line.replace('$/', "")
        line = line.replace('([^"]*)', "$1")
        results.append([line, line])

class BehatComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        syntax = view.settings().get('syntax')
        if "Cucumber" not in syntax:
            return [];
        return results