import webbrowser as wb
import time

URLS = (
    "https://gmail.com",
    "https://youtube.com",
    "https://linkedin.com",
    "https://github.com/palsudipta95"
)

wb.open_new(URLS[0])
time.sleep(2)

for url in URLS[1:]:
    wb.open_new_tab(url)
    time.sleep(0.5)