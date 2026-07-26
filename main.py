import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Fake Social Media Account Detection",
    page_icon="🛡",
    layout="wide"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.title{
    text-align:center;
    color:#00E5FF;
    font-size:42px;
    font-weight:bold;
}

.sub{
    text-align:center;
    color:white;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="title">Fake Social Media Account Detection</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub">Random Forest Classifier</p>',
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

df = pd.read_csv("fake_social_media.csv")

# ---------------------------------------------------
# DATASET INFORMATION
# ---------------------------------------------------

st.header("Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.info(f"Rows : {df.shape[0]}")
    st.info(f"Columns : {df.shape[1]}")

with col2:
    st.info(f"Missing Values : {df.isnull().sum().sum()}")
    st.info(f"Duplicate Rows : {df.duplicated().sum()}")

# ---------------------------------------------------
# DATA PREPROCESSING
# ---------------------------------------------------

st.header("Data Preprocessing")

label_encoder = LabelEncoder()

df["platform"] = label_encoder.fit_transform(df["platform"])

st.success("Platform column encoded successfully.")

X = df.drop("is_fake", axis=1)

y = df["is_fake"]

# ---------------------------------------------------
# TRAIN TEST SPLIT
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

st.success("Train Test Split Completed")

st.write("Training Samples :", X_train.shape[0])
st.write("Testing Samples :", X_test.shape[0])

# ---------------------------------------------------
# RANDOM FOREST MODEL
# ---------------------------------------------------

st.header("Random Forest Model Training")

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

st.success("Model Trained Successfully")

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

# ---------------------------------------------------
# MODEL METRICS
# ---------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

auc = roc_auc_score(y_test, y_prob)

# ---------------------------------------------------
# DISPLAY METRICS
# ---------------------------------------------------

st.header("Model Performance")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Accuracy", f"{accuracy*100:.2f}%")

c2.metric("Precision", f"{precision*100:.2f}%")

c3.metric("Recall", f"{recall*100:.2f}%")

c4.metric("F1 Score", f"{f1*100:.2f}%")

c5.metric("AUC Score", f"{auc:.3f}")

# ---------------------------------------------------
# SAVE VARIABLES
# ---------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
}).sort_values(
    by="Importance",
    ascending=False
)

# ==========================================================
# PART 2
# VISUALIZATION
# ==========================================================

st.divider()

st.header("Model Verification")

# ---------------------------------------------------
# CONFUSION MATRIX
# ---------------------------------------------------
st.subheader("Confusion Matrix")

col1, col2, col3 = st.columns([2,3,2])

with col2:
    fig, ax = plt.subplots(figsize=(2.5,2))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        cbar=False,
        annot_kws={"size":7},
        xticklabels=["Real","Fake"],
        yticklabels=["Real","Fake"],
        ax=ax
    )

    ax.tick_params(labelsize=7)

    st.pyplot(fig, use_container_width=False)
# ---------------------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------------------

st.subheader("Feature Importance")

col1, col2, col3 = st.columns([1,4,1])

with col2:
    fig, ax = plt.subplots(figsize=(4,2.5))

    sns.barplot(
        data=feature_importance,
        x="Importance",
        y="Feature",
        palette="viridis",
        ax=ax
    )

    ax.tick_params(axis='x', labelsize=6)
    ax.tick_params(axis='y', labelsize=6)

    plt.tight_layout()

    st.pyplot(fig, use_container_width=False)
# ---------------------------------------------------
# PIE CHART
# ---------------------------------------------------
st.subheader("Fake vs Real Accounts")

count = df["is_fake"].value_counts()

col1, col2, col3 = st.columns([2,2,2])

with col2:
    fig, ax = plt.subplots(figsize=(2.5,2.5))

    ax.pie(
        count,
        labels=["Real","Fake"],
        autopct="%1.1f%%",
        textprops={"fontsize":6}
    )

    st.pyplot(fig, use_container_width=False)

# ==========================================================
# PREDICT NEW ACCOUNT
# ==========================================================

st.divider()

st.header("Predict New Social Media Account")

platform_name = st.selectbox(
    "Platform",
    label_encoder.classes_
)

platform = label_encoder.transform([platform_name])[0]

has_profile_pic = st.selectbox(
    "Has Profile Picture",
    [0,1]
)

bio_length = st.number_input(
    "Bio Length",
    value=100
)

username_randomness = st.slider(
    "Username Randomness",
    0.0,
    1.0,
    0.5
)

followers = st.number_input(
    "Followers",
    value=500
)

following = st.number_input(
    "Following",
    value=300
)

ratio = st.number_input(
    "Follower Following Ratio",
    value=1.5
)

account_age = st.number_input(
    "Account Age (Days)",
    value=365
)

posts = st.number_input(
    "Posts",
    value=100
)

posts_day = st.number_input(
    "Posts Per Day",
    value=1.2
)

caption_similarity = st.slider(
    "Caption Similarity",
    0.0,
    1.0,
    0.20
)

content_similarity = st.slider(
    "Content Similarity",
    0.0,
    1.0,
    0.30
)

follow_rate = st.slider(
    "Follow Unfollow Rate",
    0.0,
    10.0,
    2.0
)

spam_rate = st.slider(
    "Spam Comment Rate",
    0.0,
    1.0,
    0.10
)

generic_rate = st.slider(
    "Generic Comment Rate",
    0.0,
    1.0,
    0.10
)

links = st.selectbox(
    "Suspicious Links in Bio",
    [0,1]
)

verified = st.selectbox(
    "Verified",
    [0,1]
)

if st.button("Predict"):

    sample = pd.DataFrame([[
        platform,
        has_profile_pic,
        bio_length,
        username_randomness,
        followers,
        following,
        ratio,
        account_age,
        posts,
        posts_day,
        caption_similarity,
        content_similarity,
        follow_rate,
        spam_rate,
        generic_rate,
        links,
        verified
    ]], columns=X.columns)

    prediction = model.predict(sample)[0]

    probability = model.predict_proba(sample)

    confidence = np.max(probability) * 100

    st.divider()

    if prediction == 1:
        st.error("🚨 Fake Account Detected")
    else:
        st.success("✅ Genuine Account")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    prob_df = pd.DataFrame({
        "Class": ["Real", "Fake"],
        "Probability": [
            probability[0][0],
            probability[0][1]
        ]
    })

    fig, ax = plt.subplots(figsize=(5,4))

    sns.barplot(
        data=prob_df,
        x="Class",
        y="Probability",
        palette=["green","red"],
        ax=ax
    )

    ax.set_ylim(0,1)

    st.pyplot(fig)

st.divider()

st.success("🎉 Fake Social Media Account Detection System Completed Successfully")
