from dotenv import load_dotenv
from os import getenv
import sys

load_dotenv()

misp_url=f"{getenv("MISP_URL")}"
misp_key=f"{getenv("MISP_AUTH_KEY")}"
misp_verifycert=getenv("MISP_VERIFYCERT") == '1'
if (misp_url != "" and misp_key != "" and misp_verifycert != ""):
    print(
f"""
Loaded `misp_url`, `misp_key`, and `misp_verifycert`:
    `misp_url`: {misp_url}
    `misp_key`: {misp_key}
    `misp_verifycert`: {misp_verifycert}
""")
else:
    print("Error loading environment variables `misp_url`, `misp_key` or `misp_verifycert`. Contact admin")
    sys.exit(-1)
