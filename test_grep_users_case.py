import pytest
from fixture.grep_app import GrepAppClass
from model.grep_tests_parametrize import GrepPar

class TestsUserCase:

    case_file_name = GrepPar.get_case_file_name(case_id=0)
    # наиболее частые использования grep
    # тест считается пройденым, если мы получаем ожидаемый код завершения
    @pytest.mark.parametrize("grep_options_tests", ['--help','--v','--version'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep '])
    @pytest.mark.parametrize("valid_exit_assert", [0])
    def test_grep_other_parameters(self, grep_commands_tests, grep_options_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests,grep_options_tests)
        assert grep_command.get_exit_status() == valid_exit_assert

    @pytest.mark.parametrize("grep_find_templates_tests", [case_file_name[0]])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH"'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_exit_assert", [0])
    def test_grep_find_positive(self,grep_commands_tests,grep_options_tests,grep_find_templates_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests, grep_find_templates_tests)
        assert grep_command.get_exit_status() == valid_exit_assert

    @pytest.mark.parametrize("grep_find_templates_tests", [case_file_name[0]])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH123"'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_exit_assert", [256])
    def test_grep_find_negative(self,grep_commands_tests,grep_options_tests,grep_find_templates_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests,grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == valid_exit_assert


    @pytest.mark.parametrize("grep_find_templates_tests", [case_file_name[0],case_file_name[4]])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH"','"#"','.txt','"JOH*"','[aBbCcDd]'})
    @pytest.mark.parametrize("grep_parameters_tests", {'-H','-v','-i','-i -v','-A 4','-B 2','-C 2','-c','-n', '-E'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_exit_assert", [0])
    def test_grep_parameters_find_positive(self,grep_commands_tests,grep_parameters_tests,grep_options_tests,
                                           grep_find_templates_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == valid_exit_assert

    @pytest.mark.parametrize("grep_find_templates_tests", [case_file_name[0]])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH123"','"@"','".jgep"','"*all*"'})
    @pytest.mark.parametrize("grep_parameters_tests", {'-i','-n','-w'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_exit_assert", [256])
    def test_grep_parameters_find_negative(self,grep_commands_tests,grep_parameters_tests,grep_options_tests,
                                           grep_find_templates_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == valid_exit_assert

    @pytest.mark.parametrize("grep_find_templates_tests", [case_file_name[4],case_file_name[2]])
    @pytest.mark.parametrize("grep_options_tests", {'"JOSEPH'})
    @pytest.mark.parametrize("grep_parameters_tests", {'-c','-w'})
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_exit_assert", [512])
    def test_grep_parameters_file_not_found(self,grep_commands_tests,grep_parameters_tests,grep_options_tests,
                                            grep_find_templates_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests,grep_parameters_tests,grep_options_tests,grep_find_templates_tests)
        assert grep_command.get_exit_status() == valid_exit_assert

    @pytest.mark.parametrize("grep_commands_tests", ['/bin/grep', 'grep','egrep','fgrep'])
    @pytest.mark.parametrize("valid_exit_assert", [512])
    def test_grep_without_parameters(self,grep_commands_tests, valid_exit_assert):
        grep_command = GrepAppClass(grep_commands_tests)
        assert grep_command.get_exit_status() == valid_exit_assert
