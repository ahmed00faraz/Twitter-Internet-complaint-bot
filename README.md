# Internet Speed Twitter Bot

This Python bot automates the process of checking your internet speed using [SpeedTest](https://www.speedtest.net/) and tweets at your Internet Service Provider (ISP) if the speeds are below your promised plan.

## Features

- Automatically checks your internet speed.
- Tweets a complaint to your ISP if your download/upload speeds are lower than promised.
- Uses Selenium to interact with SpeedTest and Twitter.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium WebDriver](https://selenium.dev/) (for automating the browser)
- WebDriver for your browser:
  - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (for Chrome)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/internet-speed-twitter-bot.git
    cd internet-speed-twitter-bot
    ```

2. **Install dependencies:**

    ```bash
    pip install selenium
    ```

3. **Download WebDriver:**

   - Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your `PATH` or specify the path when initializing the WebDriver.

## Usage

1. **Update your credentials:**

    Open the script and update the following variables with your details:

    ```python
    TWITTER_EMAIL = "YOUREMAIL@gmail.com"
    TWITTER_PASSWORD = "PASSWORD"
    PROMISED_UP = 30  # Your promised upload speed
    PROMISED_DOWN = 30  # Your promised download speed
    ```

2. **Run the bot:**

    ```bash
    python internet_speed_twitter_bot.py
    ```

3. The bot will:

    - Visit [SpeedTest.net](https://www.speedtest.net/) to measure your internet speed.
    - If your upload or download speed is below the promised levels, it will automatically log in to Twitter and tweet a message to your ISP.

## Example Tweet

```
Hey Internet Provider, why is my Internet speed 15Mbps down / 5Mbps up when I pay for 30Mbps down / 30Mbps up?
```

## Contributing

Contributions are welcome! Feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License.

---

Now you can just copy and paste this into your `README.md` file!
