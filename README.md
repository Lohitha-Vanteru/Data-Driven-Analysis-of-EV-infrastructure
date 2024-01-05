# Data-Driven-Analysis-of-EV-infrastructure
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/162ba741-f938-4f03-a47a-19daea44fb3f)


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
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/a3f34aaa-c301-4704-877b-abf50b9fd94c)

- **Web Development:**
  - Built on Flask Architecture for a user-friendly website.
  - HTML, CSS, and JavaScript for dynamic web pages.
  - AWS S3 for data storage and retrieval.

- **Database Management:**
  - AWS S3 for secure and scalable storage of relevant EV charging-related data and predictions.

- **Machine Learning Models:**
  - Leveraged tools such as Pandas, scikit-learn, TensorFlow, Prophet, and PuLP.
  - Collaborative platforms include Google Colab and Google Cloud.
  - 
## Demo

### Home Page:
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/234bd5a7-39f8-4882-a038-db6d24d812cf)


- Overview of project divisions and functionalities.

### Charging Census Page:

- Displays projected EV counts and required charging stations by county and zip code.
- Drill down to the count of each vehicle type and infrastructure locations.
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/622dee09-6bcd-4566-90ae-d3a39f1dceed)
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/524cfd43-2ace-44da-b0cd-eabf08c3165f)

### Charging Snapshot Page:

- Shows energy usage requirements for each city based on user input.
- Graphs displaying load profiles at each hour of the day.
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/98d478ae-c827-4c96-9af6-3700d32e4849)

### Charge Map Page:

- Displays existing and proposed charging stations based on zip code and vehicle type.
- Details about station names, addresses, connector types, and projected future requirements.
![image](https://github.com/Lohitha-Vanteru/Data-Driven-Analysis-of-EV-infrastructure/assets/113141006/44eba0b4-08b7-4190-a95d-4f4d48bb4c74)

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

## License

This project is licensed under the [MIT License](LICENSE).


