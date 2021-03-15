import os, pytest

# функция для выполнение команды grep
def grep_start(grep_commands='grep', grep_parameters='',grep_option='', grep_templates=''):
    grep_command_start = grep_commands+' '+ grep_parameters + ' ' + grep_option + ' ' + grep_templates
    # запсь выходных данных команд
    # hosts_process = subprocess.Popen([grep_command_start], stdout=True)
    # hosts_out, hosts_err = hosts_process.communicate()
    return os.system(grep_command_start)

# тесты grep

@pytest.mark.parametrize("grep_options_tests", ['--help','--v','--version'])
@pytest.mark.parametrize("grep_commands_tests", ['grep '])
def test_grep_other_parameters(grep_commands_tests,grep_options_tests):
    assert grep_start(grep_commands_tests,grep_options_tests) == 0

@pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
@pytest.mark.parametrize("grep_options_tests", {'"JOSEPH"'})
@pytest.mark.parametrize("grep_commands_tests", ['grep'])
def test_grep_find_positive(grep_commands_tests,grep_options_tests,grep_find_templates_tests):
    assert grep_start(grep_commands_tests,grep_options_tests,grep_find_templates_tests) == 0

@pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
@pytest.mark.parametrize("grep_options_tests", {'"JOSEPH123"'})
@pytest.mark.parametrize("grep_commands_tests", ['grep'])
def test_grep_find_negative(grep_commands_tests,grep_options_tests,grep_find_templates_tests):
    assert grep_start(grep_commands_tests,grep_options_tests,grep_find_templates_tests) == 256

@pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt','grep*'])
@pytest.mark.parametrize("grep_options_tests", {'"JOSEPH"','"#"','.txt','"JOH*"'})
@pytest.mark.parametrize("grep_parameters_tests", {'-H','-v','-i','-i -v','-A 4','-B 2','-C 2','-c','-n','-w', '-E'})
@pytest.mark.parametrize("grep_commands_tests", ['grep'])
def test_grep_parameters_find_positive(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests):
    assert grep_start(grep_commands_tests,grep_options_tests,grep_find_templates_tests) == 0

@pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
@pytest.mark.parametrize("grep_options_tests", {'"JOSEPH123"','"@"','".jgep"','"*all*"'})
@pytest.mark.parametrize("grep_parameters_tests", {'-i -v','-n','-w'})
@pytest.mark.parametrize("grep_commands_tests", ['grep'])
def test_grep_parameters_find_negative(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests):
    assert grep_start(grep_commands_tests,grep_options_tests,grep_find_templates_tests) == 256

@pytest.mark.parametrize("grep_find_templates_tests", ['greb*','loggg.txt'])
@pytest.mark.parametrize("grep_options_tests", {'"JOSEPH'})
@pytest.mark.parametrize("grep_parameters_tests", {'-c','-w'})
@pytest.mark.parametrize("grep_commands_tests", ['grep'])
def test_grep_parameters_file_not_found(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests):
    assert grep_start(grep_commands_tests,grep_options_tests,grep_find_templates_tests) == 512

@pytest.mark.parametrize("grep_commands_tests", ['/bin/grep', 'grep','egrep','fgrep'])
def test_grep_without_parameters(grep_commands_tests):
    assert grep_start(grep_commands_tests) == 512