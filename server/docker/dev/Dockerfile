FROM python:3.7-alpine

# Copy over files
COPY . ./server
WORKDIR /server/app

# Install dependencies
RUN pip install -r requirements.txt

# Pull in config
ARG CONFIG_FILE="../config/config.localdev.yaml"
ENV CONFIG_FILE=${CONFIG_FILE}

CMD ["sh", "-c", "python3 ./steam_strand.py"]
# Run all unit tests with 'python3 -m unittest /app/steam_stand_tests
