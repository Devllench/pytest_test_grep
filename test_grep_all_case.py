import pytest
from fixture.grep_app import GrepAppClass

# тесты grep
class TestAll:

    # тестирования всех параметров
    # тест считается пройденым если мы получаем ожидаемое количество символов
    # для проверки теста можно использовать встроенные утилиты linux
    # Пример: grep --v | wc -m минус 1 символ
    @pytest.mark.parametrize("grep_options_tests", ['--v', '--version'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [375])
    def test_test(self, grep_commands_tests, grep_options_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_options_tests", ['--v', '--version'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [375])
    def test_version(self, grep_commands_tests, grep_options_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_options_tests", ['--help'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [4736])
    def test_help(self, grep_commands_tests, grep_options_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"(aa|JON)"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-E','--extended-regexp', '-P','--perl-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [36])
    def test_pattern_syntax_extended_perl_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                              grep_find_templates_tests, valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-G', '--basic-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [181])
    def test_pattern_syntax_basic_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JOSEPH"'])
    @pytest.mark.parametrize("grep_parameters_tests",['-F', '--fixed-strings'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [6])
    def test_pattern_syntax_fixed_string(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", [''])
    @pytest.mark.parametrize("grep_parameters_tests", ['-e good', '--regexp=good'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [35])
    def test_matching_control_regexp(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                         grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['JONH*'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-i', '--ignore-case'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [33])
    def test_matching_control_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                      grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-i', '--ignore-case'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [21])
    def test_matching_control_ignore(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--no-ignore-case'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [2])
    def test_matching_control_no_ignore(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests,valid_len_assert):

        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-v','--invert-match'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [6543])
    def test_matching_control_invert(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"WILLIAM.txt"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-w','--word-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [11])
    def test_matching_control_word_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"CHARLES"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-x', '--line-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [7])
    def test_matching_control_line_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-y'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [21])
    def test_matching_control_y(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-c','--count'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [3])
    def test_output_control_count(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--color=always', '--colour=always'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [10343])
    def test_output_control_color(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-L', '--files-without-match'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [22])
    def test_output_control_no_match(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-L', '--files-without-match'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [22])
    def test_output_control_no_match(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-l', '--files-with-matches'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [20])
    def test_output_control_match(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-m 4', '--max-count=4'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [34])
    def test_output_control_m_count(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-o', '--only-matching'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [19])
    def test_output_control_only_count(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-q', '--quiet', '--silent'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [0])
    def test_output_control_quiet(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert


    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log_bad.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-s', '--no-messages'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [0])
    def test_output_control_no_mes(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-b', '--byte-offset'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [57])
    def test_prefix_control_byte(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-H', '--with-filename'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [138])
    def test_prefix_control_with_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-h', '--no-filename'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [132])
    def test_prefix_control_with_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"abs"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-h', '--no-filename'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [4])
    def test_prefix_control_no_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                      grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # проверить тест
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--label=grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [769])
    def test_prefix_control_label(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-n','--line-number'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [285])
    def test_prefix_control_l_num(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-T -H', '--initial-tab -H'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [797])
    def test_prefix_control_tab(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # проверить тест
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-u', '--unix-byte-offsets'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [181])
    def test_prefix_control_ux_byte(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"txt"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Z', '--null'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [64])
    def test_prefix_control_null(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-A 0',' --after-context=0'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [259])
    def test_line_control_after(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Ao 10 '])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [42])
    def test_line_control_after_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-B 4',' --before-context=4'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [969])
    def test_line_control_before(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Bo 10'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [42])
    def test_line_control_before_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-C 1','-1', '--context=1'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [624])
    def test_line_control_before(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Co 14'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [42])
    def test_line_control_before_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавить бинарный файл для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-a','--text'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [181])
    def test_fb_sel_text(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавить бинарный файл для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--binary-files=text'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [181])
    def test_fb_sel_sel_bin(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавить бинарный файл для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--binary-files=te'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [37])
    def test_fb_sel_bin_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавить устройство для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JONH*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-D read' ,'--devices=read'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [33])
    def test_fb_sel_devices(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                         grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JONH*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-d read', '--directories=read'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [33])
    def test_fb_sel_dir(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_*'])
    @pytest.mark.parametrize("grep_options_tests", ['"DANIEL"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--exclude=*log.txt'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [29])
    def test_fb_sel_exclude(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"DANIEL"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--exclude-dir=*'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [57])
    def test_fb_sel_exclude_dir(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                        grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"DANIA*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-I'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [85])
    def test_fb_sel_i(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"absf*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--include=*'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [27])
    def test_fb_sel_include(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                      grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"NATE*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-r', '--recursive'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [180])
    def test_fb_sel_recurs(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                      grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавить дерриктории
    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"NATET*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-R', '--dereference-recursive'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [0])
    def test_fb_sel_der_recurs(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                           grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавит бинарный файл
    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"NORBERT"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-U', '--binary'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [58])
    def test_other_options_bin(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                               grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

    # добавит бинарный файл
    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"HORM*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-z','--null-data'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    @pytest.mark.parametrize("valid_len_assert", [6748])
    def test_other_options_bin(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                               grep_find_templates_tests,valid_len_assert):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == valid_len_assert

