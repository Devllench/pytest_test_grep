import os,pytest

def grep_start(grep_commands='', grep_parameters=''):
    grep_command_start = grep_commands + grep_parameters
    #print("CODE STATUS:")
    print(os.system(grep_command_start))
    return os.system(grep_command_start)

@pytest.mark.parametrize("grep_commands_tests", ['/bin/grep ', 'grep '])
def test_grep_without_parameters(grep_commands_tests):
    assert grep_start(grep_commands_tests) == 512

@pytest.mark.parametrize("grep_parameters_tests", [' --help'])
@pytest.mark.parametrize("grep_commands_tests", ['/bin/grep ', 'grep '])
def test_grep_help_positive(grep_commands_tests,grep_parameters_tests):
    #print("\nStart grep test")
    #print("\nCMD: " + grep_commands_positive_tests,grep_parameters_positive_tests)
    assert grep_start(grep_commands_tests,grep_parameters_tests) == 0

@pytest.mark.parametrize("grep_parameters_tests", [' --help'])
@pytest.mark.parametrize("grep_commands_tests", ['/bin/grep ', 'grep '])
def test_grep_help_positive(grep_commands_tests,grep_parameters_tests):
    #print("\nStart grep test")
    #print("\nCMD: " + grep_commands_positive_tests,grep_parameters_positive_tests)
    assert grep_start(grep_commands_tests,grep_parameters_tests) == 0
