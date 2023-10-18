class Case:
    def __init__(self, test_case_id: str, name: str, step_description: str, expected_result: str):
        """
        Default class for test_cases
        Parent class for ExtendedCase
            :param test_case_id: id test_case
            :param name: name test_case
            :param step_description: description test_case
            :param expected_result: ER test_case
        """
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}", end="")


class ExtendedCase(Case):
    def __init__(self, test_case_id: str, name: str, step_description: str, expected_result: str, precondition: str,
                 environment: str):
        super().__init__(test_case_id, name, step_description, expected_result)
        self.precondition = precondition
        self.environment = environment

    def print_test_case_info(self):
        super().print_test_case_info()
        print(f"\nПредусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")


case = ExtendedCase('1', 'Наличие кнопки Принять', '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ',
                    'Кнопка доступна', 'Открыть сервис', 'Яндекс Браузер')
case.print_test_case_info()
