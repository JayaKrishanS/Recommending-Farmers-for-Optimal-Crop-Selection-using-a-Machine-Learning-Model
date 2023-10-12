import  pickle
import streamlit as st

model = pickle.load(open("Crop_recommendation_model.pkl","rb"))

tab1,tab2 = st.tabs(["About project", "Predict"])

with tab1:
    st.markdown("<h2> Recommending Farmers for Optimal Crop Selection using a Machine Learning Model</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: orange;'>Summary :</h5>", unsafe_allow_html=True)    
    st.markdown("* In this crop recommendation project, a dataset comprising 2200 records was sourced from Kaggle to guide optimal crop selection for farmers.")
    st.markdown("* The project starts with the loading of the dataset, followed by a exploratory data analysis (EDA) phase to gain insights into its structure and characteristics. Subsequently, feature engineering was undertaken to effectively separate the data into training and target components. This step aimed at preparing the dataset for the subsequent machine learning modeling phase.")
    st.markdown("* For the predictive modeling, three algorithms — Decision Tree, Random Forest, and Gradient Boosting—were employed. These machine learning models were strategically chosen to capturing diverse patterns within the agricultural dataset")
    st.markdown("* The Random Forest (RF) model emerged as the standout performer across all evaluation metrics. Its exceptional performance in terms of accuracy, precision, recall, and F1-score made it the natural choice for further application.")
    st.markdown("* Following the model evaluation, the decision was made to proceed with the Random Forest model for the development of a Streamlit application.")
    github_url_1 = "https://github.com/JayaKrishanS/Recommending-Farmers-for-Optimal-Crop-Selection-using-a-Machine-Learning-Model.git"
    st.markdown(f'<a href="{github_url_1}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)
    st.markdown("---")

with tab2:
    st.markdown("<h5 style='color: orange;'>Kindly enter the details for prediction</h5>", unsafe_allow_html=True)

    
    st.write(' ')

    N = st.number_input("Ratio of Nitrogen (N)", value = 104)
    P = st.number_input(" Ratio of Phosphorous (P)", value = 18)
    K = st.number_input(" Ratio of Potassium (K)", value = 30)
    temperature = st.number_input("Temperature", value = 23.603016)
    humidity = st.number_input("humidity", value = 60.396475)
    ph = st.number_input("ph", value = 6.779833)
    Rainfall = st.number_input("Rainfall", value = 140.937041)


    crop_predict = []
    if st.button('Predict'):
        crop_prediction = model.predict([[N, P, K, temperature, humidity, ph, Rainfall]])
        if (crop_prediction == 20):
            crop_predict = 'The suitable crop is Rice'
        if (crop_prediction == 11):
            crop_predict = 'The suitable crop is Maize'
        if (crop_prediction == 3):
            crop_predict = 'The suitable crop is chickpea'
        if (crop_prediction == 9):
            crop_predict = 'The suitable crop is kidneybeans'
        if (crop_prediction == 18):
            crop_predict = 'The suitable crop is pigeonpeas '
        if (crop_prediction == 13):
            crop_predict = 'The suitable crop is mothbeans'
        if (crop_prediction == 14):
            crop_predict = 'The suitable crop is mungbean'
        if (crop_prediction == 2):
            crop_predict = 'The suitable crop is blackgram'
        if (crop_prediction == 10):
            crop_predict = 'The suitable crop is lentil '
        if (crop_prediction == 19):
            crop_predict = 'The suitable crop is pomegranate'
        if (crop_prediction == 1):
            crop_predict = 'The suitable crop is banana'
        if (crop_prediction == 12):
            crop_predict = 'The suitable crop is mango'
        if (crop_prediction == 7):
            crop_predict = 'The suitable crop is grapes'
        if (crop_prediction == 21):
            crop_predict = 'The suitable crop is watermelon'
        if (crop_prediction == 15):
            crop_predict = 'The suitable crop is kidneybeans'
        if (crop_prediction == 0):
            crop_predict = 'The suitable crop is apple'
        if (crop_prediction == 16):
            crop_predict = 'The suitable crop is orange'
        if (crop_prediction == 17):
            crop_predict = 'The suitable crop is papaya'
        if (crop_prediction == 6):
            crop_predict = 'The suitable crop is cotton'
        if (crop_prediction == 8):
            crop_predict = 'The suitable crop is jute'
        if (crop_prediction == 4):
            crop_predict = 'The suitable crop is coconut'
        if (crop_prediction == 5):
            crop_predict = 'The suitable crop is coffee'
        
        st.success(crop_predict)
