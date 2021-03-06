from selenium.webdriver.common.by import By

class BasePageLocators():
    DASHBOARD_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scrolsl-trigger'][@href='/slate_portal']")
    CLUSTERS_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/clusters']")
    APPS_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/applications']")
    SECRETS_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/secrets']")
    INSTANCES_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/instances']")
    MY_GROUPS_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/groups']")
    ALL_GROUPS_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/public-groups']")
    CLI_ACCESS_SIDE_BTN = (By.XPATH, "//a[@class='nav-link js-scroll-trigger'][@href='/cli']")


class DashboardPageLocators():
    APPS_LINK = (By.LINK_TEXT, 'Apps')
    VIEW_ALL_APPS_BTN = (By.LINK_TEXT, 'View all apps')


class AppsPageLocators():
    STABLE_APPS_TAB = (By.LINK_TEXT, 'Stable Applications')
    INCUBATOR_APPS_TAB = (By.LINK_TEXT, 'Incubator Applications')


class AppsDetailPageLocators():
    INSTALL_APP_BTN = (By.XPATH, "//div[@class='install-app']")
    ADD_NEW_SECRET_BTN = (By.XPATH, "//div[@style='padding-left: 10px;']")

class AppCreatePageLocators():
    NEXT_BTN = (By.XPATH, "//button[@type='submit']")

class AppCreateFinalPageLocators():
    INSTALL_BTN = (By.XPATH, "//button[@type='submit']")

class SearchResultsPageLocators():
    pass