# Data-Driven-Analysis-of-EV-infrastructure

## Velocity: Revolutionizing Electric Vehicle (EV) Infrastructure Planning

## Overview

The Velocity project is at the forefront of revolutionizing Electric Vehicle (EV) infrastructure planning for Heavy/Medium-Duty vehicles. Our mission is to pave the way for a sustainable future by providing cutting-edge analytical insights and strategic recommendations for EV charging stations. The project encompasses a comprehensive data-driven analysis, forecasting, and optimization, culminating in a user-friendly website named "Velocity."

## Features

- **Data-Driven Analysis:**
  - Utilizes advanced Machine Learning models:
  - Prophet model for forecasting market growth.
  - Stacking Ensemble Regressor model with weighted fusion for range prediction.
  - Temporal Fusion Transformer model for energy resource allocation.
  - PuLP linear programming optimization model with K-means clustering for optimal charging station placement.

  - Addresses challenges and opportunities in EV charging infrastructure tailored for medium/heavy-duty vehicles.

- **Website - "Velocity":**
  - Provides station-wise, site-wise, and zipcode-wise analytical results for EV charging stations.
  - Interactive map feature suggests optimal new locations for charging stations based on advanced models and algorithms.
  - User-friendly interface for stakeholders, including urban planners, policymakers, and industry enthusiasts.

## System Architecture

- **Web Development:**
  - Built on Flask Architecture for a user-friendly website.
  - HTML, CSS, and JavaScript for dynamic web pages.
  - AWS S3 for data storage and retrieval.

- **Database Management:**
  - AWS S3 for secure and scalable storage of relevant EV charging-related data and predictions.

- **Machine Learning Models:**
  - Leveraged tools such as Pandas, scikit-learn, TensorFlow, Prophet, and PuLP.
  - Collaborative platforms include Google Colab and Google Cloud.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/velocity.git
    cd velocity
    ```

2. Install dependencies:

    ```bash
    # Example using pip
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    flask run
    ```

4. Access the website at [http://localhost:5000](http://localhost:5000).

## Demo

- Home Page:
  - Overview of project divisions and functionalities.

- Charging Census Page:
  - Displays projected EV counts and required charging stations by county and zip code.

- Charging Snapshot Page:
  - Shows energy usage requirements for each city based on user input.

- Charge Map Page:
  - Displays existing and proposed charging stations based on zip code and vehicle type.

## License

This project is licensed under the [MIT License](LICENSE).


