I. Подготовка:

1. Установить IDE (например Pycharm)
2. Установить python 3.10 и добавить его в path (потребуется перезагрузка)
3. Установить git
4. Для запуска аллюра скачать и установить jdk https://jdk.java.net/18/
установить аллюр через scoop (windows) - https://github.com/allure-framework/allure2
добавить в переменные среды JAVA_HOME со ссылкой на установленный дистрибутив 
5. Клонировать репозиторий (проект)
6. В настройках указать интерпретатор в IDE (например python 3.10)
7. Установить необходимые пакеты из requirements.txt при помощи IDE или python -m pip install -r requirements. txt


II. Настройка конфигурации [testit](https://testit.software/blog/post/kak-nastroit-peredachu-rezultatov-avtotestov-iz-allure-report-v-sistemu-test-it
):

1) Развернуть на рабочий стенд Test IT (url должен быть без “/“ в конце; аккуратнее с http/https)
$ testit --url http://testit.smeta.ru
2) Установить действующий api secret key из профиля пользователя:
$ testit --privatetoken {youretoken}
3) Установить импорт в необходимый проект:
$ testit --projectid {id}
4) Установить конфигурацию импорта:
$ testit --configurationid {id}
5) Вывод конфигурационного файла на экран:
$ testit -sh

III. Запуск тестов
1) Тестирование можно запустить из командной строки интерпретатора Python, используя команду:
$ python -m pytest
Ключ -m маркированных тестов:
$ pytest -m test
Ключ –v запуск тестов с подробным отчетом о ходе его прохождени:
$ pytest –v testing/
Запуск всех UI тестов с указанием пути отчета:
$ pytest -v .\estimate_tests\ui --alluredir=./allure-results
2) Формирование отчета в allure (не обязательный):
$ allure serve ./allure-results
3) Перенос отчета из allure в testit:
$ testit --resultsdir .allure-results
4) Результаты test-run можно посмотреть в [testit](http://testit.smeta.ru/projects/1/autotests/test-runs?periodInDays=1)
