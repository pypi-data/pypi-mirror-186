import logging
from gramadan import features
from .features import Form, FormSg, FormPlGen

logging.warning(
    "You are using the v2 package within GramadánPy. "
    "It has not been fully tested, and is not comparable "
    "to the real Gramadán functionality... you have been warned!\n"
    "To address perceived minor issues, this actually changes some of the "
    "regex matching in Opers.Slenderize - marked with a v2 flag."
)

features.Form = Form
features.FormSg = FormSg
features.FormPlGen = FormPlGen
