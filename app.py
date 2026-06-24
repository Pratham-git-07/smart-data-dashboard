import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# TITLE
st.title("Smart Data Dashboard")

st.divider()

# FILE UPLOAD

uploaded_file = st.file_uploader(label="Upload you file: ", type="csv")

st.divider()

# PREVIEWING THE FILE
def show_preview(df):
    st.header("Dataset Preview")
    st.write(df.head(5))
    st.divider()

def show_overview(df):
    st.subheader("Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
    with col4:
        st.metric("Duplicate Values", df.duplicated().sum())
    st.divider()

# SHOWING FULL DATA
def show_full_data(df):
    st.subheader("See whole Data")
    if st.button("Show whole Data"):
        st.write(df)
    st.divider()


# SHOWING DTYPES
def show_dtypes(df):
    st.subheader("Dataset value types")
    if st.button("Show Data Types"):
        st.write(df.dtypes)
    st.divider()

# REMOVING DUPLICATES
def remove_duplicates(df):
    st.subheader("Remove_duplicates")
    if st.button("Remove Duplicates"):
        df.drop_duplicates(inplace=True)
        st.write(f'Duplicates dropped successfully')
        st.write(f'The remaining (Rows, Columns) are: {df.shape}')
    st.divider()

# SHOWING STATISTICS
def show_statistics(df):
    st.subheader("Statistics")
    selected_column = st.selectbox("Select a column:",["Select a column:"] + list(df.select_dtypes(include="number").columns))
    if selected_column != "Select a column:":
        st.write(df[selected_column].describe())
    st.divider()


# CHART REPRESENTATION
def visualization(df):
    st.subheader("Visualization")
    select_column = st.selectbox("Select a column: ", df.columns)

    # HISTOGRAM

    if select_column in ["Age", "Salary", "Performance_Score", "Experience_Years"]:
        if st.button("Generate Histogram"):
            fig, ax = plt.subplots()
            ax.hist(df[select_column], bins=10, color="Green", edgecolor="black")
            ax.set_title(f'{select_column} Distribution')
            ax.set_xlabel(select_column)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

    # BAR CHART
    elif select_column in ["City", "Department"]:
        if st.button("Generate Bar Chart"):
            st.bar_chart(df[select_column].value_counts())

    # LINE CHART
    elif select_column in "Joining_Year":
        if st.button("Generate Line Chart"):
            st.line_chart(df.groupby("Joining_Year").size().sort_index())
    st.divider()

# SCATTER PLOTS
def scatter_plots(df):
        st.subheader("Scatter Plots")
        scatter_plot_options = st.selectbox("Select Scatter Plot", ["Select Scatter Plot", "Age vs Salary","Experience_Years vs Salary", "Experience_Years vs Performance_Score"])
        if scatter_plot_options != "Select Scatter Plot":
            if scatter_plot_options == "Age vs Salary":
                st.scatter_chart(data=df, x='Age', y="Salary")
            elif scatter_plot_options == "Experience_Years vs Salary":
                st.scatter_chart(df, x="Experience_Years", y="Salary")
            elif scatter_plot_options == "Experience_Years vs Performance_Score":
                st.scatter_chart(df, x='Experience_Years', y="Performance_Score")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    show_preview(df)
    show_overview(df)
    show_full_data(df)
    show_dtypes(df)
    remove_duplicates(df)
    show_statistics(df)
    visualization(df)
    scatter_plots(df)









    
    

