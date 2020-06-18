# about

This project explores simple Python + Selenium tests with pytest.

## run 

In project root folder, run:

### all tests

`pytest .`

### selected test

`pytest tests/test_home_page.py::TestHomePage::test_initial_message_visibility_default`

or

`pytest -k 'test_initial_message_visibility_default'`

## sample console output

```log
 pytest -k 'test_initial_message_visibility_default'
========================================================================== test session starts ===========================================================================
platform linux -- Python 3.6.10, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /home/user/projects/github_open/python-selenium
plugins: pytest_check-0.3.8
collected 3 items / 2 deselected / 1 selected                                                                                                                            

tests/test_home_page.py .                                                                                                                                          [100%]

==================================================================== 1 passed, 2 deselected in 2.58s =====================================================================
````
