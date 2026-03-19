# ⏱️ Simple Timer (Tkinter)

## Description

This is a graphical countdown timer built using Python and Tkinter. It allows users to enter a time in **MM:SS format**, start the countdown, pause/unpause it, and restart when needed.

## Features

* Input time in **MM:SS format**
* Start countdown timer
* Pause and resume the timer
* Restart the timer anytime
* Displays alert when time is up
* Input validation for correct format
* Clean and simple user interface

## How It Works

* User enters time (e.g., `05:30`)
* Click **Start** to begin countdown
* Use **Pause/Unpause** to control the timer
* Click **Restart** to reset the timer
* A popup message appears when the timer reaches `00:00`

## Requirements

* Python 3.x
* Tkinter (comes pre-installed with most Python versions)

## How to Run

1. Save the script as `timer.py`
2. Run the file:

   ```bash
   python timer.py
   ```

## Notes

* Time must be entered in **MM:SS format**
* Invalid input will trigger an error message
* The timer cannot start with `00:00`

## Author

Created as a simple GUI project using Tkinter.
