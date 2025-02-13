FROM python:3.10-slim

# Install gnupg and other necessary packages
RUN apt-get update && apt-get install -y gnupg2 wget curl unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome
#RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
#    apt-get update && \
#    apt-get install -y google-chrome-stable
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt --fix-broken install
RUN apt-get install google-chrome-stable -y


# Download and install ChromeDriver
#RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
#    #wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
#    wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/124.0.6367.60/chromedriver_linux64.zip && \
#    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
#    rm /tmp/chromedriver.zip

# Install Selenium
RUN pip install selenium webdriver_manager

# Install Selenium
RUN pip install selenium

# Copy your Python script into the container
COPY screenshot.py /app/screenshot.py

WORKDIR /app

# Run your script
CMD ["python3", "screenshot.py"]
