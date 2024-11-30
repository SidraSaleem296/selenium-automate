# Install dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    curl \
    unzip \
    libx11-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libgbm-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb && \
    dpkg -i google-chrome.deb && \
    apt-get install -f && \
    rm google-chrome.deb

# Install ChromeDriver
RUN LATEST=$(curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin && \
    rm chromedriver_linux64.zip
