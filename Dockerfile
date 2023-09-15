FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Install Flask (the web framework) and gunicorn (a production-ready server)
RUN pip install Flask gunicorn

# Copy the Python script into the container
COPY app.py .

# Expose port 80 to allow external access
EXPOSE 80

# Command to run the HTTP server using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
