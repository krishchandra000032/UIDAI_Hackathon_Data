# UIDAI_Data_Hackathon2026
UIDAI Hackathon 2026: Aadhar Data Analytics & Forecasting Engine
📌 Project Overview
This repository hosts an end-to-end Data Intelligence Pipeline developed for the UIDAI Data Hackathon 2026. It is designed to ingest raw, noisy Aadhar administrative data (Enrolment, Biometric, and Demographic updates), sanitize it using fuzzy logic, and derive high-value actionable insights using Machine Learning.

The system addresses three critical challenges in large-scale government datasets:

Data Quality: Automated cleaning of inconsistent State/District names.

Fraud Detection: Unsupervised learning to flag anomalous volume spikes.

Resource Planning: AI-driven forecasting of future footfall for 2026.

🚀 Key Features
Self-Healing Data: Uses FuzzyWuzzy and Levenshtein distance to automatically merge variations like "West Bengal" and "west bengal" without manual dictionaries.

Unified Master Dataset: Merges disparate CSV sources (Biometric, Demographic, Enrolment) into a single analytical source of truth.

Anomaly Detection: Implements an Isolation Forest algorithm to detect statistical outliers (potential fraud or "ghost" centres) in the top 1% of transactions.

Predictive Modeling: Uses Gradient Boosting Regressors to forecast daily footfall for the next 365 days, accounting for seasonal and weekly cyclic patterns.
