#Классы для опередления параметров тестов
class GrepPar:

    @staticmethod
    def get_case_file_name(case_id):
        if case_id == 0:
            case_data = ['grep_unitest_log.txt',
                      'grep_unitest_log_2.txt',
                      'grep_unitest_log_bad.txt',
                      'grep_unitest_log*',
                      'grep_*',
                      'g*']

            return case_data

