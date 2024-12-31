# Hotel Booking Cancellation Prediction

This project aims to build a complete machine learning pipeline to forecast the probability of a potential customer canceling their hotel booking. Predictions are based on reservation criteria, including variables like arrival date, number of guests, deposit type, and more. The project is divided into **five phases**, each addressing a key step in the project deployment. Below is a detailed description of each phase.

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

---

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

