import sys
from var_print import varp

from SeleniumChrome import *

driver = SeleniumChrome(keep_alive=True)
driver.get("https://www.google.com")
