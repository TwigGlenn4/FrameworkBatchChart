# Framework Batch Chart Download Tool
A tool for automatically downloading charts from Google Sheets to .png images for my Framework 16 Batch Charts.


# How it works
1. Use Selenium to open the link to the chart on Google Sheets
2. Print to PDF using the custom print dialog
3. Convert the saved .pdf to a .png with ImageMagick
4. Repeat for each chart
5. Visit some URL so an anonymous user doesn't linger in the Google Sheets viewers list


# How can I use this tool?

### This tool is LINUX ONLY!
It has only been tested on Xubuntu 23.10, but should work on any modern Ubuntu derviative and maybe more.

I have no plans to port this to Windows, but if anyone can manage to make it work without breaking Ubuntu support I'd be happy to accept a pull request.

## Requirements
- Python 3
- Google Chrome
- ImageMagick - Image manipulation tool
- Wand - Connects Python to ImageMagick
- Selenium - Allows Python to control a dedicated Chrome instance.

## Installation
1. Install Google Chrome from the chrome website if you don't already use it.
2. Install ImageMagick with `sudo apt install imagemagick`
3. Install Wand and Selenium with `pip3 install selenium wand`
4. Download this repository, or just the `get-charts.py` script.

## Configure settings in `get-charts.py`
- Change `CHROME_PATH` if you want to try Chromium or another browser compatible with selenium's `webdriver.Chrome()`, but be warned that selenium does not handle snaps well.
- If you want to download a different set of charts, edit `URL_LIST` to your list, and `DEFAULT_FILENAME` should be updated to the default filename given by saving to PDF. This is usually the tab title.

## Run
Open a terminal in the directory containing the script and run `python3 get-charts.py`.


# Additional Files
I've also included copies of the latest (as of writing) raw text for my [Framework Forum updates](https://community.frame.work/t/framework-laptop-16-batch-shipment-chart/47120/143) and [Reddit summaries](https://www.reddit.com/r/framework/comments/1c93xvy/framework_16_batch_chart_weekly_summary_41424_to/).

- [Template_ForumUpdate.txt](Template_ForumUpdate.txt)
- [Template_RedditSummary.txt](Template_RedditSummary.txt)


# Changelog
[CHANGELOG.md](CHANGELOG.md)


# License
- This script is licensed with the MIT license, see [LICENSE.md](LICENSE.md) for details.
