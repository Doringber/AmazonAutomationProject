
from selenium.webdriver.common.by import By

class Locators():
    # --- Home Page Locators ---
    SEARCH_TEXTBOX=(By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON=(By.XPATH,"//div[contains(@class,'nav-search-submit')]/input")
    TODAY_DEALS = (By.LINK_TEXT,"Today's Deals")

    # --- Search Results Page Locators ---
    SEARCH_RESULT_LINK=(By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]")
    ITEMS_SEARCH_RESULT=(By.CLASS_NAME, 'a-size-base-plus a-color-base a-text-normal')

    # --- Product Details Page Locators ---
    ADD_TO_CART_BUTTON=(By.ID, "add-to-cart-button")
    VIEW_DEAL_BUTTON=(By.XPATH,"//div[@id='102_dealView_0']//a[@class='a-button-text a-text-center'][contains(text(),'View Deal')]")
    LIST_ITEMS=(By.CLASS_NAME,"s-result-list s-search-results sg-row")

    # --- Sub Cart Page Locators ---
    SUB_CART_DIV=(By.ID,"hlb-subcart")
    PROCEED_TO_BUY_BUTTON=(By.ID,"hlb-ptc-btn-native")
    CART_COUNT=(By.ID,"nav-cart-count")
    CART_LINK=(By.ID,"nav-cart")

    # --- Cart Page Locators ---
    DELETE_ITEM_LINK=(By.XPATH,"//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]")
    CART_COUNT=(By.ID,'nav-cart-count')
    PROCEED_TO_CHECKOUT_BUTTON=(By.NAME,"proceedToCheckout")

    # --- Signin Page Locators ---
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX=(By.ID,"ap_email")
    SIGN_IN_HOME_SCREEN_BUTTON = (By.ID,"nav-link-accountList")
    SIGN_IN_INNER_BUTTON = (By.XPATH,"//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][contains(text(),'Sign in')]")
    CONTINUE_BUTTON = (By.ID,"continue")
    SIGN_IN_LOCATOR_ALERT = (By.CLASS_NAME,"a-alert-heading")
    EMPTY_CART_SCREEN_LOCATOR = (By.CLASS_NAME,"sc-empty-cart-header")

    # --- Signin Page Locators ---
    IMDB_SEARCH = (By.ID,'self_implemented_search')
    IMDB_SEARCH_FILED = (By.ID,'search_query')
    IMDB_RESULT_SUGGSTION = (By.XPATH,"//*[@text='Star Wars: The Rise of Skywalker']")
    IMDB_MOVIE_PAGE_ID = (By.ID,"com.imdb.mobile:id/title")

    # --- sql test --- #
    RESULT_SCREEN_SQL = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    # --- hover --- #
    HOVER_TO = (By.ID, "nav-your-amazon")
    ORDERS = (By.XPATH,"//span[@class='nav-line-2'][contains(text(),'')]")
    SELECT = (By.XPATH, "//select[@id='searchDropdownBox']")

    # ---Kan --- #
    SEARCH_BUTTON = (By.XPATH, "//img[@class='image-2']")
    KAN_SEARCH_TEXT_BOX = (By.ID, "gsc-i-id1")
    KAN_TEXT_RESULT = (By.ID,'resInfo-0')














