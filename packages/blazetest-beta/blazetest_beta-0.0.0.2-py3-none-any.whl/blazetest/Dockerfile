FROM public.ecr.aws/lambda/python:3.9 as stage

RUN yum install unzip -y -q && \
    yum clean all -y -q && \
    rm -rf /var/cache/yum

# Install latest Chromedriver
COPY .blazetest/scripts/install_chromedriver.sh /tmp/
RUN /usr/bin/bash /tmp/install_chromedriver.sh

FROM public.ecr.aws/lambda/python:3.9 as build

ENV PLAYWRIGHT_BROWSERS_PATH=/usr/bin/ \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /tmp/

# Install Chrome dependencies
RUN yum install atk cups-libs dbus gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel glib2 fontconfig unzip -y -q  && \
    yum update nss -y && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    mkdir -p /tmp/junitxml/ && \
    python3 -m pip install --upgrade pip -q && \
    python3 -m pip install -r /tmp/requirements.txt -q && \
    python3 -m pip install pytest-playwright -q && \
    python3 -m pip install boto3 -q && \
    python3 -m playwright install chromium

# Copy project files and tests
ADD . ${LAMBDA_TASK_ROOT}/
ADD .blazetest/tests_runner_handler ${LAMBDA_TASK_ROOT}/tests_runner_handler

# Copy venv, chromedriver and browsers
COPY --from=stage /usr/bin/chromedriver /usr/bin/chromedriver
RUN ln -s /usr/bin/chromium*/chrome-linux/chrome /usr/bin/google-chrome

ENV PATH="$PATH:/use/bin/google-chrome"

CMD ["tests_runner_handler.handler.run_tests"]