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
    def test_version(self, grep_commands_tests, grep_options_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests)
        assert grep_command.get_len_exit_data() == 375

    @pytest.mark.parametrize("grep_options_tests", ['--help'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_help(self, grep_commands_tests, grep_options_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_options_tests)
        assert grep_command.get_len_exit_data() == 4736

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"(aa|JON)"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-E','--extended-regexp', '-P','--perl-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_pattern_syntax_extended_perl_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 36

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-G', '--basic-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_pattern_syntax_basic_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 181

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JOSEPH"'])
    @pytest.mark.parametrize("grep_parameters_tests",['-F', '--fixed-strings'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_pattern_syntax_fixed_string(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 6

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", [''])
    @pytest.mark.parametrize("grep_parameters_tests", ['-e good', '--regexp=good'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_regexp(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                         grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 35

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['JONH*'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-i', '--ignore-case'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                      grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 33

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-i', '--ignore-case'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_ignore(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 21

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--no-ignore-case'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_no_ignore(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 2

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-v','--invert-match'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_invert(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 6543

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"WILLIAM.txt"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-w','--word-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_word_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                           grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 11

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"CHARLES"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-x', '--line-regexp'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_line_reg(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 7

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-y'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_matching_control_y(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 21

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-c','--count'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_count(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 3

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--color=always', '--colour=always'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_color(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 10343

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-L', '--files-without-match'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_no_match(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 22

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-L', '--files-without-match'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_no_match(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 22

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-l', '--files-with-matches'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_match(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 20

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"ON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-m 4', '--max-count=4'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_m_count(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 34

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-o', '--only-matching'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_only_count(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 19

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-q', '--quiet', '--silent'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_quiet(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                       grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 0

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-q', '--quiet', '--silent'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_quiet(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 0

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log_bad.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-s', '--no-messages'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_output_control_quiet(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 0

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-b', '--byte-offset'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_byte(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 57

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-H', '--with-filename'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_with_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 138

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"aa"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-h', '--no-filename'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_with_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 132

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt grep_unitest_log_2.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"abs"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-h', '--no-filename'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_no_file(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                      grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 4

    # проверить тест
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--label=grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_label(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 769

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-n','--line-number'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_l_num(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 285

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-T -H', '--initial-tab -H'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_tab(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                  grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 797

    # проверить тест
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-u', '--unix-byte-offsets'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_ux_byte(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 181

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"txt"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Z', '--null'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_prefix_control_null(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 64

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-A 0',' --after-context=0'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_line_control_after(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 259

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Ao 10 '])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_line_control_after_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 42

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-B 4',' --before-context=4'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_line_control_before(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 969

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Bo 10'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_line_control_before_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 42

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-C 1','-1', '--context=1'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_line_control_before(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                 grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 624

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log*'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-Co 14'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_line_control_before_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 42

    # добавить бинарный файл для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-a','--text'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_text(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 181

    # добавить бинарный файл для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--binary-files=text'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_sel_bin(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 181

    # добавить бинарный файл для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JON*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--binary-files=te'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_bin_err(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                     grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 37

    # добавить устройство для проверки
    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JONH*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-D read' ,'--devices=read'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_devices(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                         grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 33

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_unitest_log.txt'])
    @pytest.mark.parametrize("grep_options_tests", ['"JONH*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-d read', '--directories=read'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_dir(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 33

    @pytest.mark.parametrize("grep_find_templates_tests", ['grep_*'])
    @pytest.mark.parametrize("grep_options_tests", ['"DANIEL"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--exclude=*log.txt'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_exclude(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                            grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 29

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"DANIEL"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--exclude-dir=*'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_exclude_dir(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                        grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 57

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"DANIA*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-I'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_i(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 85

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"absf*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['--include=*'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_include(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                      grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 27

    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"NATE*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-r', '--recursive'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_recurs(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                      grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 180

    # добавить дерриктории
    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"NATET*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-R', '--dereference-recursive'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_fb_sel_der_recurs(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                           grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 0

    # добавит бинарный файл
    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"NORBERT"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-U', '--binary'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_other_options_bin(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                               grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 58

    # добавит бинарный файл
    @pytest.mark.parametrize("grep_find_templates_tests", ['g*'])
    @pytest.mark.parametrize("grep_options_tests", ['"HORM*"'])
    @pytest.mark.parametrize("grep_parameters_tests", ['-z','--null-data'])
    @pytest.mark.parametrize("grep_commands_tests", ['grep'])
    def test_other_options_bin(self, grep_commands_tests, grep_parameters_tests, grep_options_tests,
                               grep_find_templates_tests):
        grep_command = GrepAppClass(grep_commands_tests, grep_parameters_tests, grep_options_tests,
                                    grep_find_templates_tests)
        assert grep_command.get_len_exit_data() == 6748

