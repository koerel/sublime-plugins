import sublime
import sublime_plugin

isToggled = False

class ToggleBetweenTheLastTwoFilesCommand( sublime_plugin.TextCommand ):
    """
        toggle_between_the_last_two_files
    """

    def run( self, edit ):
        global isToggled
        window = self.view.window()

        if isToggled:
            isToggled = False
            window.run_command( "prev_view_in_stack" )

        else:
            isToggled = True
            window.run_command( "next_view_in_stack" )