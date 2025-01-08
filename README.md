# Social Media Performance Analysis

This project is a submission for the **Level Supermind Hackathon**, where we developed a basic analytics module to analyze engagement data from mock social media accounts using **Langflow** and **DataStax Astra DB**.

---

## 📋 Overview

The objective of this project is to create an analytics module that:
1. Fetches and stores social media engagement data.
2. Analyzes post performance based on engagement metrics.
3. Provides insights using GPT integration in Langflow.

---

## 🔧 Tools & Technologies

- **Langflow**: For workflow creation and GPT integration.
- **DataStax Astra DB**: For database operations and storing mock engagement data.
- **Python**: For additional scripting and data handling.
- **GitHub**: Repository for code and documentation.

---

## 🗂️ Project Structure

```
├── datasets/
│   ├── mock_engagement_data.json   # Simulated dataset
├── langflow_workflow/
│   ├── workflow.json               # Langflow workflow file
├── scripts/
│   ├── data_insertion.py           # Script to populate Astra DB
│   ├── query_analysis.py           # Script for querying Astra DB
├── insights/
│   ├── generated_insights.txt      # GPT-generated insights
├── README.md                       # Project documentation
├── LICENSE                         # License details
└── requirements.txt                # Dependencies
```

---

## 🚀 Features

### 1. **Fetch Engagement Data**
- Simulated a small dataset of social media engagement, including:
  - Post types: Carousel, Reels, Static Images.
  - Metrics: Likes, Shares, Comments.
- Stored this dataset in **DataStax Astra DB** for database operations.

### 2. **Analyze Post Performance**
- Built a workflow in **Langflow** to:
  - Accept post types (e.g., Carousel, Reels, Static Images) as input.
  - Query the dataset in Astra DB to calculate average engagement metrics for each post type.

### 3. **Provide Insights**
- Utilized GPT integration in Langflow to generate simple insights, such as:
  - Carousel posts have 20% higher engagement than static posts.
  - Reels drive 2x more comments compared to other formats.

---

## 🖥️ Demo Video

Watch the complete walkthrough of the project: [YouTube Video Link](#)

---

## 📊 How It Works

### **Step 1: Data Generation and Storage**
1. Created a simulated dataset representing mock social media engagement.
2. Used `data_insertion.py` to populate the Astra DB database with the dataset.

### **Step 2: Workflow Creation**
1. Designed a **Langflow workflow**:
   - Input: Post types (Carousel, Reels, Static Images).
   - Output: Average engagement metrics from Astra DB.

### **Step 3: Insights Generation**
1. Integrated GPT in Langflow to analyze the engagement metrics.
2. Generated actionable insights based on the analyzed data.

---

## 🤝 Submission Details

- **Hackathon Name**: [SuperMind Hackathon](https://www.findcoder.io/hackathons/SuperMind-Hackathon/67668c927a79c23209528177)
- **GitHub Repository**: [GitHub Repository Link](#)
- **Demo Video**: [YouTube Video Link](#)
- **Description**: [FindCoder Project Link](#)

---
