import pytest
import allure


# 3. 通过 allure.severity按重要性级别来标记，有5种级别：

#       - Blocker级别：阻塞

#       - Critical级别：严重

#       - Normal级别：正常

#       - Minor级别：不太重要

#       - Trivial级别：不重要
def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestclassWithNormalSeverity(object):
    def test_inside_teh_normalserverity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass
