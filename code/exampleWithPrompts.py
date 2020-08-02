from downloader import Downloader

cookie = """
ADD YOUR COOKIE HERE
"""

cookiePrompt = input("Do you want to input a new cookie?: ")
if cookiePrompt == ('y' or 'Y'): cookie = input("new cookie: ")

dl = Downloader(cookie=cookie)

dlPrompt = input("What is the URL for your lesson?: ")

# download by class URL:
dl.download_course_by_url(dlPrompt)
