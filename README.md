# PageObjectStepik

Убрала ссылки с промо, чтобы было проще проверять тест. не ожидая прогона по всем ссылкам.


base_page.py - здесь хранятся методы, которые применяются по всему проекту, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - здесь хранятся локаторы в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать.

main_page.py - здесь хранятся методы по конкретной странице, завернутые в класс этой страницы. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py.

test_main_page.py - здесь хранятся тест-кейсы, которые будуь запускаться с помощью pytest.
