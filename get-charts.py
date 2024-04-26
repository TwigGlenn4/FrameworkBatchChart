#!/usr/bin/python3
# TwigGlenn4
# get-chart-pictures 1.2.0

# python built-in modules
import os
from time import sleep
from glob import glob
from json import dumps
from datetime import date
from pathlib import Path
# pip modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from wand.image import Image


### SETTINGS ###

# List of urls to vist, keys are the filename without extension
URL_LIST = {  "FW16BatchChart": "https://docs.google.com/spreadsheets/d/12nY1kIrX8Isnfkr5E2J14ZdPPNDHkAsUxieSKjGgeak/edit#gid=2043735750",
              "FW16BatchChartDelta": "https://docs.google.com/spreadsheets/d/12nY1kIrX8Isnfkr5E2J14ZdPPNDHkAsUxieSKjGgeak/edit#gid=1296480151",
              "FW16BatchChartFar": "https://docs.google.com/spreadsheets/d/12nY1kIrX8Isnfkr5E2J14ZdPPNDHkAsUxieSKjGgeak/edit#gid=1037368929"
}
# Uncomment below to use only 1 url for debugging.
# URL_LIST = {"FW16BatchChart": "https://docs.google.com/spreadsheets/d/12nY1kIrX8Isnfkr5E2J14ZdPPNDHkAsUxieSKjGgeak/edit#gid=2043735750"} #DEBUG

# Full path of the destination folder for saved images. Leave "" to save images to the folder containing this script.
OVERRIDE_DOWNLOAD_PATH = ""

# Subdirectory of destination folder to move old charts into. Will not move them is set to ""
OLD_DIRNAME = "old/"

# How long to sleep after doing something that takes time in selenium (loading a page, printing to PDF, etc), because selenium dosen't pause execution in time for me.
SELENIUM_SLEEP = 0.1 # I think 0.1 seconds is enough for Selenium to take over waiting until it's done.

# This is the default filename when printed to PDF.
DEFAULT_FILENAME = "Framework 16 Batch Chart - Google Sheets.pdf"

# Directory containing chrome's actual executable for usage by Selenium. Will open a new auto/testing instance, not your saved profile.
CHROME_PATH = "/opt/google/chrome/"

# Some URL to visit so that the automated browser dosen't linger in the Google Sheets anonymous viewers list.
FINAL_URL = "about://version"

### SETTINGS END ###



# default download_path to dir containing this script if not set
download_path = OVERRIDE_DOWNLOAD_PATH
if OVERRIDE_DOWNLOAD_PATH == "":
  download_path = str(Path(__file__).parent.resolve())+"/"
print("Saving files to " + download_path)



def print_chart(driver): # sends all keybinds to print a page from google sheets.
  actions = webdriver.ActionChains(driver)

  # Bring up Google Sheet's print dialog
  actions.key_down(Keys.CONTROL)
  actions.send_keys('p')
  actions.key_up(Keys.CONTROL)
  actions.perform()
  sleep(SELENIUM_SLEEP)

  # Select the 'Print' button
  actions.send_keys(Keys.TAB)
  actions.send_keys(Keys.ENTER)
  actions.perform()
  sleep(SELENIUM_SLEEP)

  # Print to PDF
  actions.send_keys(Keys.ENTER)
  actions.perform()
  sleep(SELENIUM_SLEEP)


def clear_old_charts(): # moves any charts in current dir to OLD_DIRNAME.
  if OLD_DIRNAME == "":
    return # don't try moving files to themselves, nothing will change anyway.
  
  # ensure OLD_DIRNAME exists in download_path
  if not os.path.exists(download_path+OLD_DIRNAME):
    os.makedirs(download_path+OLD_DIRNAME)

  count = 0
  for file in URL_LIST.keys():
    pdf_src = download_path+file+"_*.pdf"
    png_src = download_path+file+"_*.png"
    
    # using glob to match any file in the download path with the right name and a wildcard for the date.
    for filename in glob(pdf_src):
      dest = download_path+OLD_DIRNAME+filename.replace(download_path, "")
      os.rename(filename, dest)
      count += 1
    
    for filename in glob(png_src):
      dest = download_path+OLD_DIRNAME+filename.replace(download_path, "")
      os.rename(filename, dest)
      count += 1

  print(f"Moved {count} old charts")


def pdf_to_png( pdf_filename, png_filename ):
  with Image(filename=pdf_filename, resolution=144) as img:
    img.compression_quality = 100
    img.trim(reset_coords=True) # crops transparent border
    img.save(filename=png_filename)



# Selenium chrome settings
settings = {
  "recentDestinations": [{
    "id": "Save as PDF",
    "origin": "local",
    "account": "",
  }],
  "selectedDestinationId": "Save as PDF",
  "version": 2
}
prefs = {'printing.print_preview_sticky_settings.appState': dumps(settings),
         "savefile.default_directory": download_path}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument("--no-sandbox");
chrome_options.add_argument("--disable-dev-shm-usage");
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(options=chrome_options)



clear_old_charts()

date_string = date.today().strftime("%y-%m-%d")
print(date_string)
print()



# Download and convert each graph in URL_LIST
for graph, url in URL_LIST.items():
  print(f"Fetching {graph} from {url}")

  driver.get(url)
  sleep(SELENIUM_SLEEP)
  
  print_chart(driver)
  
  # rename default saved filename to new filename.
  filename = f"{graph}_{date_string}"
  filename_pdf = filename+".pdf"
  filename_png = filename+".png"

  try: # Try to rename the downloaded pdf to the proper name.
    os.rename(DEFAULT_FILENAME, filename_pdf) 

  except FileNotFoundError: # If the file does not exits, alert the user
    print(f"  ERROR: Could not save {filename_pdf}. Has the default downloaded filename changed from '{DEFAULT_FILENAME}'?")

  else: # If no exceptions, then convert from PDF to PNG.
    print(f"  {filename_pdf} saved...")
    # os.system("pdf-to-png "+filename_pdf)
    pdf_to_png(filename_pdf, filename_png)
    os.remove(filename_pdf)
    print(f"  {filename_png} converted...")


driver.get(FINAL_URL) # Prevents anonymous from lingering in google sheets
driver.quit()
