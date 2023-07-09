import streamlit as st
from src.data_management import load_transaction_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

def page_factors_of_fraud_body():
    st.header("Factors of Fraud")

    df = load_transaction_data()

    st.info(
        "The senior management team at Auckland Capital Bank (ACB) "
        "want to better undeststand the patterns from their transaction data "
        "in order to identify the most relevant variables correlated "
        "to a churned customer."
    )

    if st.checkbox("Inspect Transaction Data"):
        st.write(
            f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n\n"
            f"The first 10, used to give an indication of the format of the data, are below.")

        st.write(df.head(10))

    st.divider()

    st.subheader("Correlation Study")

    st.write(
        f"A correlation study was conducted using Jupyter notebooks to better understand how "
        f"the variables in the transaction data are correlated to Fraud levels. \n\n"
        f"The most correlated variables are: \n"
        f"* Ratio to Median Purchase Price\n"
        f"* Online Order\n"
        f"* Distance from Home\n"
        f'* Used Pin Number\n'
    )

    vars_to_study = ['ratio_to_median_purchase_price', 'online_order', 'distance_from_home','used_pin_number']
    df_eda = df.filter(vars_to_study + ['fraud'])
    df_eda['online_order'] = df_eda['online_order'].replace({1: 'Online', 0: 'Not Online'})
    df_eda['used_pin_number'] = df_eda['used_pin_number'].replace({1: 'Pin Used', 0: 'No Pin'})
    df_eda['fraud'] = df_eda['fraud'].replace({1.0: 'Fraud', 0: 'No Fraud'})

    if st.checkbox("View Fraud Levels per Variable"):
        churn_level_per_variable(df_eda)

    st.subheader("Conclusions")

    st.success(
        "1. Transactions occuring more than 60.27km from home are more likely "
        "to be fraudulent than transactions closer to home. (Hypothesis 1)\n"
        "   * Rather than a linear relationship, there appears to be a 'tipping "
        "point' at which point the transaction is more likely to be fraudulent.\n\n"
        "2. Transactions that occur online are more likely to be fraudulent than "
        "transactions made offline. (Hypothesis 2)\n\n"
        "Also and significantly:\n"
        "* Transactions that are more than 4.08x the median purchase price are "
        "more likely to be fraudulent than smaller transactions.\n"
        "  * Rather than a linear relationship, there appears to be a 'tipping "
        "point' at which point the transaction is more likely to be fraudulent."
    )


    st.divider()

    st.caption(
        "NOTE: The scenario presented is fictional and was undertaken for the developer's "
        "Data Analytics milestone project as part of Code Institute's Diploma in Full Stack Software "
        "Development."
    )

def plot_categorical(df, col, target_var):
    plt.figure(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks()
    plt.ylabel("Count")
    plt.xlabel(f"{col.replace('_',' ').title()}")
    plt.title(f"{col.replace('_',' ').title()}", fontsize=20, y=1.05)
    plt.legend(title="Fraud")
    plt.savefig(f"outputs/plots/{col}-against-fraud.png")
    st.image(f"outputs/plots/{col}-against-fraud.png")


def plot_numerical(df, col, target_var,xlim=None):
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.ylabel("Count")
    plt.xlabel(f"{col.replace('_',' ').title()}")
    plt.title(f"{col.replace('_',' ').title()}", fontsize=20, y=1.05)
    if xlim is not None:
        plt.xlim(xlim)  
    plt.savefig(f"outputs/plots/{col}-against-fraud.png")
    st.image(f"outputs/plots/{col}-against-fraud.png")


def churn_level_per_variable(df_eda):
    target_var = 'fraud'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            variable_percentile = df_eda[col].quantile(0.95)
            plot_numerical(df_eda, col, target_var, xlim=[0, variable_percentile])

