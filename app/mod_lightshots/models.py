from ghost import Ghost
import urllib
import time
import re

class Screenshot:
  def __init__(self, url):
    self.url = url
  
  def capture(self):
    filename = "shots/" + self.generate_filename(self.url)
    self.save_screenshot(self.url, filename)
    return filename

  def generate_filename(self, url):
    stripped_url = re.sub(r'\W+', '', url)
    timestamp = int(time.time())

    return str(timestamp) + "_" + stripped_url + ".jpg"

  def save_screenshot(self, url, path):
    ghost = Ghost(wait_timeout=120)
    page, extra = ghost.open(url)
    ghost.capture_to(path)
