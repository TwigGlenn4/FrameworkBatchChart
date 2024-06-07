# Framework Batch Chart Download Tool
A tool for automatically downloading charts from Google Sheets to .png images for my Framework 16 Batch Charts.


# How it works
1. Use Selenium to open the link to the chart on Google Sheets
2. Print to PDF with Sheets' print dialog
3. Convert the saved .pdf to a .png with ImageMagick
4. Repeat for each chart
5. Visit some URL(Default: `about://version`) so an anonymous user doesn't linger in the Google Sheets viewers list


# How can I use this tool?

### This tool is LINUX ONLY!
The current version has been tested on Xubuntu 24.04 on Python 3.12.3, but should work on any modern Ubuntu derviative and maybe more.

I have no plans to port this to Windows, but feel free to fork if you want to give it a shot. It has not been tested on WSL.

## Requirements
- Python 3
- Google Chrome
- ImageMagick - Image manipulation tool
- Wand - Connects Python to ImageMagick
- Selenium - Allows Python to control a web browser.
- Chromedriver-Autoinstaller - Allows Selenium to properly interface with chrome.

## Installation
1. Download this repository, or just the `get-charts.py` script.
2. Install Google Chrome from the chrome website if you don't already use it.
3. Install ImageMagick, pip, and python's virtual environment manager with `sudo apt install imagemagick python3-pip python3-venv`
4. Setup a Python virtual environment by running `python3 -m venv batchchart_venv` in the folder containing `get-charts.py`
5. Activate the Python virtual environment with `source batchchart_venv/bin/activate`
6. Install Wand, Selenium, and Chromedriver-Autoinstaller with `pip3 install wand selenium chromedriver-autoinstaller`
7. Allow ImageMagick to work with PDF files by removing `<policy domain="coder" rights="none" pattern="PDF" />` from the file `/etc/ImageMagick-6/policy.xml`.

## Configure settings in `get-charts.py`
- Most of the variables are self explaning, and I have comments in the script to describe how they work too.
- If you want to download a different set of charts, edit `URL_LIST` to your list, and `DEFAULT_FILENAME` should be updated to the default filename given by saving to PDF. This is usually the tab title.

## Run
1. Open a terminal in the directory containing the script and virtual environment
1. Activate the virtual environment if not already active. `source batchchart_venv/bin/activate`. The venv is active when you see `(batchchart_venv)` before your command prompt.
2. Run `python3 get-charts.py`. The first run may take extra time while the testing browser loads.


# Additional Files
I've also included copies of the raw text for previous [Framework Forum updates](https://community.frame.work/t/framework-laptop-16-batch-shipment-chart/47120/143) and [Reddit summaries](https://www.reddit.com/r/framework/comments/1c93xvy/framework_16_batch_chart_weekly_summary_41424_to/).

- [Template_ForumUpdate.txt](Template_ForumUpdate.txt)
- [Template_RedditSummary.txt](Template_RedditSummary.txt)


# Changelog
[CHANGELOG.md](CHANGELOG.md)


# License
- This script is licensed with the MIT license, see [LICENSE.md](LICENSE.md) for details.
