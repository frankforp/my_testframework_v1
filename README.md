# my_testframework_v1
#requirements
python 3.x
selenium2
pytest
pytest-html

#usage
1. In top-level dir, type pytest:
>pytest
2. If you want to generate a html report
>pytest --html=report.html

#options
#--settings, choose from (config.settings_stage or config.settings_prod), using config.settings_stage by default.
>pytest --settings=config.settings_prod
#--browser, choose from (chrome,ie,firefox), using chrome by default
--browser=chrome

#name convension
The test script should be test_*.py
The test class in test script should be start with Test
The test method or function should start with test_

#steps for adding a test case
1. Add a testcase in TestCase.xlsx under AutoCase folder
2. Create a corresponding page module under Pages folder, including element finding and manipulate
Note that the new page class inherit from BasePage
3. Create a test script under corresponding folder under Modules
