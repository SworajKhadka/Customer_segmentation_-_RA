# Customer Segmentation & Churn Prediction in Retail

Understanding customer behavior is central to retention strategy in e-commerce and retail.  
This project develops an end-to-end customer analytics framework that segments customers based on purchase behavior and predicts churn risk using transactional retail data.

The analysis combines classical RFM methodology with behavioral features and machine learning to uncover actionable retention insights and segment-level risk patterns.

---

## Project Objective

The goal of this project is to:

- Identify meaningful customer segments based on purchasing behavior  
- Quantify churn risk across segments  
- Discover behavioral drivers of retention  
- Provide data-driven retention strategies  

---

## Analytical Approach

Customer behavior was modeled using two complementary feature groups:

**RFM Features**
- Recency — time since last purchase  
- Frequency — number of purchases  
- Monetary — total spend  

**Behavioral (RSS) Features**
- Average Order Value  
- Purchase Span (customer lifetime)  
- Purchase Interval (repeat cadence)  
- Repeat Purchase Ratio  

These features capture both value and engagement dynamics across customers.

---

## Segmentation & Churn Modeling

Customers were segmented using behavioral clustering and labeled into four interpretable groups:

- VIP Loyal  
- Regular  
- Occasional  
- Churned  

Churn probability was then modeled using logistic regression on RFM and behavioral features, achieving strong discrimination between retained and at-risk customers.

---

## Key Insights

The analysis reveals a clear behavioral gradient of retention:

- VIP customers exhibit extremely low churn (~4%)  
- Regular customers show moderate stability (~28% churn)  
- Occasional buyers display elevated churn (~46%)  
- Disengaged customers exceed 70% churn  

Purchase frequency and repeat interval emerge as the strongest drivers of retention, indicating that loyalty is primarily formed through consistent engagement over time rather than spend alone.

---

## Customer Segment Distribution

<img width="1294" height="650" alt="image" src="https://github.com/user-attachments/assets/4cca5148-9dfd-4fc2-8842-4c08a9c544a2" />


---

## Revenue Contribution by Segment

<img width="1294" height="650" alt="image" src="https://github.com/user-attachments/assets/b9f0321c-cbd5-4829-9a8a-5d46e435fb91" />


VIP customers contribute a disproportionately large share of revenue despite being fewer in number, highlighting their strategic importance.

---

## Churn Risk by Segment

<img width="1294" height="650" alt="image" src="https://github.com/user-attachments/assets/bbcd4c1a-bb38-4860-b8d4-87d638a9f468" />


Churn risk increases sharply as engagement weakens, validating the segmentation hierarchy.

---

## Customer Behavior Map (RFM Space)

<img width="1294" height="650" alt="image" src="https://github.com/user-attachments/assets/2c328ba5-cbc4-4cdc-adf1-162049860f2c" />


The behavioral map illustrates how loyal customers cluster around high frequency and low recency, while churned customers occupy the low-frequency, high-recency region.

---

## Purchase Interval Patterns

<img width="1294" height="650" alt="image" src="https://github.com/user-attachments/assets/4027ec5e-dea5-4846-acfe-ea802d939ff1" />


Shorter and more consistent purchase intervals are strongly associated with retention, reinforcing cadence as a key loyalty signal.

---

## Business Implications

The segmentation enables targeted retention strategy:

- **Churned** → win-back campaigns and reactivation offers  
- **Occasional** → habit-forming incentives and reminders  
- **Regular** → loyalty programs and tier progression  
- **VIP** → exclusive perks and priority experience  

This framework supports precision retention rather than uniform marketing.

---

## Tech Stack

Python  
Pandas  
Scikit-learn  
Plotly  
Jupyter Notebook  

##Author

Sworaj Khadka
Data Science


