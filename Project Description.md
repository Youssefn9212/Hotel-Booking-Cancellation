# Hotel Booking Cancellation Prediction
---

### **Table of Contents**

1. [Introduction](#introduction)
2. [Project Contributors](#project-contributors)
3. [Project Phases](#project-phases)
   - [Phase 1: Problem Identification and Specification](#phase-1-problem-identification-and-specification)
   - [Phase 2: Data Preparation, Cleaning, and Feature Engineering](#phase-2-data-preparation-cleaning-and-feature-engineering)
   - [Phase 3: Experimental Analysis of the Machine Learning Models](#phase-3-experimental-analysis-of-the-machine-learning-models)
   - [Phase 4: Model Fine-Tuning and Utility Application](#phase-4-model-fine-tuning-and-utility-application)
   - [Phase 5: Model Deployment and Future Improvements](#phase-5-model-deployment-and-future-improvements)
4. [Conclusion](#conclusion)

---

### **Introduction**

In the dynamic landscape of the hospitality industry, the efficiency of managing hotel bookings plays a vital role in the achievement of success within an establishment or organization. The increasing frequency of online bookings and online platforms has become the most common form of hotel reservations. However, this rise in online activity comes with its own set of challenges, with cancellations being a primary threat to hotel owners. This project focuses on optimizing the process of hotel bookings and the prevention of cancellations using machine learning models. By leveraging predictive analytics, the project aims to provide valuable insights to hotel management and the hospitality industry as a whole, improving operational efficiency, resource allocation, and overall customer satisfaction. The project is divided into **five phases**, each addressing a key step in the project deployment. Below is a detailed description of each phase.

---

### Project Contributors
- **Youssef Nakhla**  
- **Karim AbouDaoud**

---

![Project Overview](https://github.com/user-attachments/assets/cdfc5805-635e-4ca1-852b-7a2cd0126207)

---

### Project Phases

---

#### **Phase 1: Problem Identification and Specification**

- **Objective:** Understand the challenges of hotel booking cancellations and prepare the necessary dataset for predictive modeling.

- **Key Tasks:**
  1. **Introduction to the Problem:**
     - Explored the impact of cancellations on hotel management, including revenue loss, resource misallocation, and customer satisfaction.
     - Highlighted the potential of machine learning to mitigate cancellations and optimize hotel booking systems.
  
  2. **Literature Review:**
     - Reviewed prior research on machine learning applications in the hospitality industry, including:
       - Logistic regression models for cancellation prediction.
       - The use of time-series analysis and machine learning to understand evolving cancellation trends.
       - Studies emphasizing the influence of price dynamics and guest demographics on cancellations.
  
  3. **Data Collection and Overview:**
     - Chose a detailed dataset containing 31 variables and 119,000 observations from [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand).
     - Variables include booking details (e.g., lead time, arrival date), guest demographics, and reservation statuses.
     - Justified the choice of the first dataset over a smaller alternative for deeper analysis and enhanced model accuracy.

- **Outcome:** A well-understood problem scope and a comprehensive dataset ready for analysis in subsequent project phases.

---


#### **Phase 2: Data Preparation, Cleaning, and Feature Engineering**

- **Objective:** Refine and enhance the dataset for optimal machine learning model performance.

- **Key Tasks:**
  1. **Handling Missing Values:**
     - Dropped observations with missing values in the `children` column.
     - Filled missing values in the `country` column with the mode ("Portugal").
     - Dropped features `agent` and `company` due to a high proportion of missing values.
  
  2. **Encoding Categorical Variables:**
     - One-hot encoded features like `hotel`, `meal`, `market segment`, and `distribution channel`.
     - Transformed `country` into two categories: `Portugal` and `International`.
     - Simplified `meal` by merging "Undefined" and "SC" categories.
  
  3. **Feature Engineering:**
     - Created a `kids` feature by combining `children` and `babies`.
     - Combined `stays in weekend nights` and `stays in week nights` into a single feature, `total_stays`.
     - Normalized `lead_time` and dropped the original column.
     - Combined `arrival year`, `month`, and `day` into a single `arrival_date` feature.
  
  4. **Outlier Treatment:**
     - Corrected the outlier in the `ADR` column by setting the value of 5400 to 540.

  5. **New Target Variable:**
     - Consolidated `reservation_status` categories. Combined "Canceled" and "No-show" into "0" (reservation not completed), and "Check-out" was encoded as "1" (reservation completed).

- **Outcome:** A clean dataset with 43 features and 118,983 observations, ready for training machine learning models.

---

#### **Phase 3: Experimental Analysis of the Machine Learning Models**

- **Objective:** Evaluate various machine learning models to predict hotel booking cancellations, identify the top-performing models, and determine the best model for deployment.

- **Key Tasks:**
  1. **Model Selection and Training:**
     - Addressed the binary classification nature of the problem and selected the following models:
       - Logistic Regression
       - K-Nearest Neighbors (KNN)
       - Naive Bayes
       - Artificial Neural Networks (ANN) with multiple activation functions
       - Decision Trees (ID3, CART)
       - Random Forest
     - Utilized the scikit-learn library for implementation.
     - Split the dataset into 80% training and 20% testing data.

  2. **Performance Metrics:**
     - Evaluated each model using accuracy, F1 score, precision, recall, True Negative Rate (TNR), and Area Under the Curve (AUC) metrics.
     - Conducted 5-fold cross-validation to ensure generalizability.

  3. **Results Summary:**
     - **Top 3 Performing Models:**
       - **Random Forest:**
         - Accuracy: 87.4%
         - F1 Score: 82.5%
         - Precision: 85%
         - Recall: 80%
       - **Artificial Neural Network (ReLU Activation):**
         - Accuracy: 85.7%
         - F1 Score: 79.7%
         - Precision: 84%
         - Recall: 76%
       - **K-Nearest Neighbors (k=11):**
         - Accuracy: 84.7%
         - F1 Score: 78%
         - Precision: 82%
         - Recall: 75%

     - Other models, such as Naive Bayes (58.7% accuracy) and Logistic Regression (79.9% accuracy), showed limited performance.

  4. **Model Insights and Observations:**
     - **Random Forest:** 
       - Demonstrated the best overall performance.
       - Highly accurate in capturing complex feature interactions.
       - Resilient to overfitting due to its ensemble learning approach.
       - Computationally intensive but suitable for the project’s goals.
     - **Artificial Neural Network (ReLU Activation):**
       - Achieved high accuracy and F1 score.
       - Requires significant computational resources and lacks interpretability.
     - **K-Nearest Neighbors:**
       - Simple and effective for small datasets.
       - Computational and memory constraints make it less suitable for larger datasets.

  5. **Final Model Selection:**
     - Selected **Random Forest** as the most suitable model due to its robustness, accuracy, and ability to handle complex data patterns effectively.

- **Outcome:** Identified Random Forest as the optimal model for predicting hotel booking cancellations, with plans to further refine and optimize it in subsequent phases.

---

#### **Phase 4: Model Fine-Tuning and Utility Application**

- **Objective:** Optimize the selected model, refine feature engineering, and deploy a user-friendly utility application for hotel booking cancellation prediction.

---

### **Model Fine-Tuning**

- **Initial Evaluation:**
  - Fine-tuned the **Random Forest** model by defining and optimizing hyperparameters, including:
    - Number of estimators
    - Maximum depth
    - Minimum samples split
    - Minimum samples leaf
    - Bootstrap
  - Conducted grid search for hyperparameter optimization but found limited improvements with additional ensemble techniques like bagging and boosting.

- **Feature Engineering Updates:**
  - Revisited the original dataset and applied new transformations:
    - `Country`: Encoded each country numerically into one column instead of one-hot encoding.
    - `Agent`: Filled missing values with `0` instead of dropping the feature.
    - `Lead Time`: Normalized using a logarithmic scale instead of MinMax scaling.
    - `Arrival Date`: Retained and encoded as numerical values instead of dropping.
    - `Babies` and `Children`: Kept as separate features instead of combining them into `kids`.
    - `Reservation Status Date`: Extracted month and year, then dropped the original column.
    - Outliers were retained and analyzed rather than dropped outright.

- **Model Evaluation:**
  - Achieved a significant improvement in model performance:
    - **Accuracy:** ~93%
    - **Entropy Loss:** 0.206
  - Split the dataset into training (80%) and testing (20%) data.
  - Further optimized the dataset split to 95% training and 5% testing, resulting in:
    - **Training Accuracy:** 99.7%
    - **Testing Accuracy:** 94%

---

### **Utility Application**

- **Objective:** Develop a web-based interface to make the machine learning model accessible to users.

- **Implementation:**
  - **Framework:** Used **Streamlit** to create the interface and backend logic.
  - **Features:**
    - Accepts datasets or single instances as input.
    - Preprocesses input data with categorical encoding and data validation.
    - Utilizes the trained Random Forest Classifier for prediction.
    - Displays processed input and model predictions to users.
  - **Deployment:**
    - Deployed the application on **Streamlit Cloud** for seamless user interaction via a web-based API.
    - Users can submit features and receive predictions without requiring the model locally.

---

### **Outcome**
- A highly accurate **Random Forest Classifier** tailored to the dataset.
- A scalable and user-friendly **utility application** for real-time hotel booking cancellation prediction.

---

#### **Phase 5: Model Deployment and Future Improvements**

- **Objective:** Deploy a user-friendly web application for predicting hotel booking cancellations and outline potential enhancements for future development.

---

### **Model Deployment**

- **Process:**
  - Saved the trained **Random Forest Classifier** model using the `pickle` library.
  - Enabled seamless loading of the model for inference in the web application.
  - Leveraged the model's knowledge from historical hotel booking data to predict cancellations for new instances.

---

### **User Interface Design**

- **Framework:**
  - Built a user-friendly interface using the **Streamlit** Python library.
  - Designed input fields for various hotel booking features, such as:
    - Lead time
    - Arrival date
    - Booking channel
    - Other relevant features

- **Preprocessing:**
  - Ensured consistency with the model by preprocessing user inputs, including:
    - Handling missing values.
    - Encoding categorical variables to match the trained model's requirements.

---

### **Making Predictions**

- **Process:**
  - Collected user inputs through the web interface.
  - Preprocessed the inputs and passed them to the trained model.
  - Generated predictions, including:
    - The likelihood of booking cancellation.
    - The associated probability.

---

### **Displaying Results**

- **Features:**
  - Displayed the predicted outcome and probability in a clear and intuitive format.
  - Provided insights into the model, including:
    - The type of model used.
    - Hyperparameters.
    - Performance metrics (e.g., accuracy, precision, recall).

---

### **Future Improvements**

- **Proposed Enhancements:**
  1. Transition the desktop application to a **cloud-based platform** for greater accessibility.
  2. Gather user feedback to improve the interface and usability.
  3. Continuously monitor the model's performance on real-world data to identify:
     - Potential biases.
     - Opportunities for refinement and re-training.

---

### **Outcome**
- Successfully deployed a **desktop-based application** for predicting hotel booking cancellations.
- Established a foundation for future development into a scalable, cloud-based solution.

---

### **Conclusion**

The Hotel Booking Cancellation Prediction project successfully demonstrates the integration of a complete machine learning pipeline, from data preparation and feature engineering to model training, fine-tuning, and deployment. Through extensive experimentation and analysis, the **Random Forest Classifier** was identified as the optimal model, achieving exceptional performance metrics with a testing accuracy of 94%. 

The development of a user-friendly utility application using **Streamlit** ensures accessibility, allowing users to easily interact with the predictive model and make informed decisions based on real-time predictions. This project underscores the value of machine learning in addressing complex challenges in the hospitality industry, such as optimizing resource allocation and improving revenue management.

While the deployed application meets its initial objectives, there are opportunities for enhancement. Transitioning to a cloud-based platform, gathering user feedback, and continuously monitoring the model's performance on real-world data will further improve its scalability, accuracy, and usability. These efforts will ensure that the system remains robust and adaptable to evolving user needs and industry dynamics.

The successful completion of this project establishes a solid foundation for predictive analytics in the hospitality sector, providing a framework for future innovations and applications in the domain.

---




