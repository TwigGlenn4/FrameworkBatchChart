# 1.2.0

- Make script settings more descriptive
- Handle blank path in `OLD_DIRNAME`
- Change `DOWNLOAD_PATH` to `OVERRIDE_DOWNLOAD_PATH` and default to the directory containing script
- `clear_old_charts()` now only moves files that match `URL_LIST`
- Prepare for github upload

# 1.2.1

- Update installation instructions after testing a clean install on a virtual machine.

# 1.3.0

- Implement Python virtual environment to work on `externally-managed-environment`s such as the default Python shipping on Xubuntu 24.04.
- Implement `chromedriver-autoinstaller` from pip to better handle installing chromedriver. Xubuntu 24.04 now ships chromedriver only with the chromium snap, which was previously breaking things.
- Remove `CHROME_PATH` variable as I believe that is now handled by `chromedriver-autoinstaller`.