print("QUESTION NO 1: regex patterns")
import pandas as pd
import re
pattern = r"^\d{2}/\d{2}/\d{4}$"
text = "26/06/2025"
if re.match(pattern, text):
    print("Valid Date")
else:
    print("Invalid Date")
