import os, sys
import subprocess

class shell_agent:
    """ Template model of Gaia """
    id = "";

    def __init__(self, id):
        self.id = id;
        print ("_gaia object [%s] is born\n" % self.id)

    def execute_commands(self, statement_command=None):
        if (statement_command == None):
            statement_command = r"line_index=2; ps -ef | head -n $line_index | tail -1 | awk -v column_index=8 '{print $column_index}'"

        # p = subprocess.Popen(statement_command, stdout=subprocess.PIPE)
        # status = p.communicate()
        status = os.system(statement_command)
        output = os.popen(statement_command).read()

        return output, status

    def who_am_i(self): #
        """ Introspection """
        self.line_storage = [];

        print ("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print ("_gaia object [%s] removed\n" % self.id);

####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <shell_agent>"
    print ("=====[" + id + " Start]===== \n")
    shell_agent_object = shell_agent(id)
    shell_agent_object.who_am_i()

    # output, status = shell_agent_object.execute_commands()

    #shell_agent_object.display_variable_name_and_value(status)
    #shell_agent_object.display_variable_name_and_value(output)

    command_statement = 'echo 0: 63616e746765747468697332776f726b | xxd -r \
        | openssl enc -aes-128-ecb -nopad -K 00000000000000000000000000000000 | xxd -p'

    command_statement = 'echo 0: 63616e746765747468697332776f726b'

    output, status = shell_agent_object.execute_commands(command_statement)

    # shell_agent_object.display_variable_name_and_value(status)
    # shell_agent_object.display_variable_name_and_value(output)

    # command_statement = 'run me'

    # output, status = shell_agent_object.execute_commands(command_statement)

    # shell_agent_object.display_variable_name_and_value(status)
    # shell_agent_object.display_variable_name_and_value(output)