import os,subprocess
# Класс выполняющий команду grep
class GrepAppClass:

    def __init__(self,grep_commands='grep', grep_parameters='',grep_option='', grep_templates=''):
        self.grep_command_start = grep_commands+' '+ grep_parameters + ' ' + grep_option + ' ' + grep_templates

    def get_exit_status(self):
            exit_status = os.system(self.grep_command_start)
            return exit_status

    def get_len_exit_data(self):
        #запсь выходных данных команды
        cmd = subprocess.getstatusoutput(self.grep_command_start)
        #print(cmd[-1])
        return len(cmd[-1])

