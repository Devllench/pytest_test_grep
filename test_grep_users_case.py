import pytest
from fixture.grep_app import GrepAppClass

class TestsUserCase:
    # наиболее частые использования grep
    # тест считается пройденым, если мы получаем ожидаемый код завершения
    @pytest.mark.parametrize("grep_options_tests", ['--help','--v','--version'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep '])
    def test_grep_other_parameters(self,grep_commands_tests,grep_options_tests):
        grep_command = GrepAppClass(grep_commands_tests,grep_options_tests)
        assert grep_command.get_exit_status() == 0

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH"'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_grep_find_positive(self,grep_commands_tests,grep_options_tests,grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests, grep_find_templates_tests)
        assert grep_command.get_exit_status() == 0

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH123"'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_grep_find_negative(self,grep_commands_tests,grep_options_tests,grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests,grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == 256


    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt','grep*'])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH"','"#"','.txt','"JOH*"','[aBbCcDd]'})
    @pytest.mark.parametrize("grep_parameters_tests", {'-H','-v','-i','-i -v','-A 4','-B 2','-C 2','-c','-n', '-E'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_grep_parameters_find_positive(self,grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == 0

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH123"','"@"','".jgep"','"*all*"'})
    @pytest.mark.parametrize("grep_parameters_tests", {'-i','-n','-w'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_grep_parameters_find_negative(self,grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == 256

    @pytest.mark.parametrize("grep_find_templates_tests", ['greb*','loggg.txt'])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH'})
    @pytest.mark.parametrize("grep_parameters_tests", {'-c','-w'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_grep_parameters_file_not_found(self,grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == 512

    @pytest.mark.parametrize("grep_commands_tests", ['/bin/grep', 'grep','egrep','fgrep'])
    def test_grep_without_parameters(self,grep_commands_tests):
        grep_command = GrepAppClass(grep_commands_tests)
        assert grep_command.get_exit_status() == 512
