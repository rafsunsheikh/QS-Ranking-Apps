import streamlit as st
import pandas as pd

url  = "https://raw.githubusercontent.com/rafsunsheikh/qs_ranking/main/2024_QS_World_University_Rankings.csv"
df = pd.read_csv(url)

dataset = df[["Unnamed: 26", "Unnamed: 27"]]
dataset = dataset.dropna()
new_df = dataset.iloc[3:].copy()
new_df.reset_index(drop=True, inplace=True)
new_df = new_df.dropna()

new_df['Unnamed: 26'] = pd.to_numeric(new_df['Unnamed: 26'], errors='coerce', downcast='float') # Score
new_df['Unnamed: 27'] = pd.to_numeric(new_df['Unnamed: 27'], errors='coerce', downcast='float') # Rank
new_df = new_df.dropna()

X = new_df.drop("Unnamed: 27", axis = 1)
y = new_df["Unnamed: 27"]


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)




environmental_sustainability_score = 0
sustainable_institute_score = 0
sustainable_education_score = 0
sustainable_research_score = 0

social_impact_score = 0
equality_score = 0
knowledge_exchange_score = 0
educational_impact_score = 0
employability_and_oppurtunity_score = 0
quality_of_life_score = 0



# Set the page to wide mode to use the full width of the screen
st.set_page_config(layout="wide")


def sustainable_institute_section():
    global sustainable_institute_score
    # Create a two-column layout
    sustainable_institute_left_column, sustainable_institute_right_column = st.columns(2)

    # Employee Reputation

    st.divider()
    with sustainable_institute_left_column:

        st.subheader("Sustainable Institute")
        st.write("")
        st.subheader("Our university considers the following indicators")
        sustainable_institute_options =[
                "Our university holds membership in officially-recognised climate action or sustainability groups",
                "Our university has a publicly available sustainability strategy and energy emissions report",
                "Our university has student societies focused on environmental sustainability",
                "Our university has a published commitment to becoming NetZero"
                ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in sustainable_institute_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our university holds membership in officially-recognised climate action or sustainability groups" in option:
                    sustainable_institute_score += (100/4)
                elif "Our university has a publicly available sustainability strategy and energy emissions report" in option:
                    sustainable_institute_score += (100/4)
                elif "Our university has student societies focused on environmental sustainability" in option:
                    sustainable_institute_score += (100/4)
                elif "Our university has a published commitment to becoming NetZero" in option:
                    sustainable_institute_score += (100/4)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {sustainable_institute_score:.2f}")


    with sustainable_institute_right_column:
        st.write("Sustainable Institute")

        st.bar_chart({"a: yet to achieve": [100-sustainable_institute_score],
                        "b: score achieved": [sustainable_institute_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])




def sustainable_education_section():
    global sustainable_education_score
    # Create a two-column layout
    sustainable_education_left_column, sustainable_education_right_column = st.columns(2)

    # Employee Reputation

    st.divider()
    with sustainable_education_left_column:

        st.subheader("Sustainable Education")
        st.write("")
        st.subheader("Our university considers the following indicators")
        sustainable_education_options =[
                "Our alumni has great impacts and academic reputation within earth, marine and environmental sciences works",
                "Our university offers courses that embed climate science and/or sustainability within the curriculum",
                "Our university offers sustainability-focused courses in other degrees",
                "Our university has a research centre dedicated to environmental sustainability"
                ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in sustainable_education_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our alumni has great impacts and academic reputation within earth, marine and environmental sciences works" in option:
                    sustainable_education_score += (100/4)
                elif "Our university offers courses that embed climate science and/or sustainability within the curriculum" in option:
                    sustainable_education_score += (100/4)
                elif "Our university offers sustainability-focused courses in other degrees" in option:
                    sustainable_education_score += (100/4)
                elif "Our university has a research centre dedicated to environmental sustainability" in option:
                    sustainable_education_score += (100/4)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {sustainable_education_score:.2f}")

    with sustainable_education_right_column:
        st.write("Sustainable Education")

        st.bar_chart({"a: yet to achieve": [100-sustainable_education_score],
                        "b: score achieved": [sustainable_education_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])


def sustainable_research_section():
    global sustainable_research_score
    # Create a two-column layout
    sustainable_research_left_column, sustainable_research_right_column = st.columns(2)

    # Employee Reputation

    st.divider()
    with sustainable_research_left_column:

        st.subheader("Sustainable Research")
        st.write("")
        st.subheader("Our university considers the following indicators")
        sustainable_research_options =[
                "Our university conducts research activity around the United Nation’s Sustainable Development Goals",
                "Our government is funding research and development in this area",
                ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in sustainable_research_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our university conducts research activity around the United Nation’s Sustainable Development Goals" in option:
                    sustainable_research_score += (100/2)
                elif "Our government is funding research and development in this area" in option:
                    sustainable_research_score += (100/2)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {sustainable_research_score:.2f}")

    with sustainable_research_right_column:
        st.write("Sustainable Research")

        st.bar_chart({"a: yet to achieve": [100-sustainable_research_score],
                        "b: score achieved": [sustainable_research_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])


def equality_section():
    global equality_score
    # Create a two-column layout
    equality_left_column, equality_right_column = st.columns(2)


    st.divider()
    with equality_left_column:
        st.subheader("Equality")
        st.write("")
        st.subheader("Our university considers the following indicators")
        equality_options =[
                "public equality is available in our university",
                "Our university has a published diversity and inclusion policy",
                "disability support is available in our university",
        ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0

        female_student_percentage_score = st.slider("Select the percentage of female students at the university", 0.0, 100.0, 0.0)
        female_faculty_percentage_score = st.slider("Select the percentage of female faculty at the university", 0.0, 100.0, 0.0)

        # Female Student Percentage Calculate
        if 0.0 < female_student_percentage_score < 15.0:
            equality_score += ((100/5) * 0.2)
        elif 15.0 <= female_student_percentage_score < 25.0:
            equality_score += ((100/5) * 0.4)
        elif 25.0 <= female_student_percentage_score < 35.0:
            equality_score += ((100/5) * 0.6)
        elif 35.0 <= female_student_percentage_score < 45.0:
            equality_score += ((100/5) * 0.8)
        elif 45.0 <= female_student_percentage_score < 55.0:
            equality_score += ((100/5) * 1.0)
        elif 55.0 <= female_student_percentage_score < 65.0:
            equality_score += ((100/5) * 0.8)
        elif 65.0 <= female_student_percentage_score < 75.0:
            equality_score += ((100/5) * 0.6)
        elif 75.0 <= female_student_percentage_score < 85.0:
            equality_score += ((100/5) * 0.4)
        elif 85.0 <= female_student_percentage_score <= 100.0:
            equality_score += ((100/5) * 0.2)



        # Female Faculty Percentage Calculate
        if 0.0 < female_faculty_percentage_score < 15.0:
            equality_score += ((100/5) * 0.2)
        elif 15.0 <= female_faculty_percentage_score < 25.0:
            equality_score += ((100/5) * 0.4)
        elif 25.0 <= female_faculty_percentage_score < 35.0:
            equality_score += ((100/5) * 0.6)
        elif 35.0 <= female_faculty_percentage_score < 45.0:
            equality_score += ((100/5) * 0.8)
        elif 45.0 <= female_faculty_percentage_score < 55.0:
            equality_score += ((100/5) * 1.0)
        elif 55.0 <= female_faculty_percentage_score < 65.0:
            equality_score += ((100/5) * 0.8)
        elif 65.0 <= female_faculty_percentage_score < 75.0:
            equality_score += ((100/5) * 0.6)
        elif 75.0 <= female_faculty_percentage_score < 85.0:
            equality_score += ((100/5) * 0.4)
        elif 85.0 <= female_faculty_percentage_score <= 100.0:
            equality_score += ((100/5) * 0.2)


        selected_options_content = []
        for option in equality_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "public equality is available in our university" in option:
                    equality_score += (100/5)
                elif "Our university has a published diversity and inclusion policy" in option:
                    equality_score += (100/5)
                elif "disability support is available in our university" in option:
                    equality_score += (100/5)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {equality_score:.2f}")

    with equality_right_column:
        st.write("Equality")

        st.bar_chart({"a: yet to achieve": [100-equality_score],
                        "b: score achieved": [equality_score]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])



def knowledge_exchange_section():
    global knowledge_exchange_score
    # Create a two-column layout
    knowledge_exchange_left_column, knowledge_exchange_right_column = st.columns(2)

    # Knowledge Exchange

    st.divider()
    with knowledge_exchange_left_column:
        st.subheader("Knowledge Exchange")
        st.write("")
        st.subheader("Our university considers the following indicators")
        knowledge_exchange_options =[
                "Our university is committed to knowledge transfer in collaboration with less-economically-supported institutions",
                "Our university is inclinaed to partner with other institutions and organisations",
                ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in knowledge_exchange_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our university is committed to knowledge transfer in collaboration with less-economically-supported institutions" in option:
                    knowledge_exchange_score += (100/2)
                elif "Our university is inclinaed to partner with other institutions and organisations" in option:
                    knowledge_exchange_score += (100/2)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {knowledge_exchange_score:.2f}")

    with knowledge_exchange_right_column:
        st.write("Knowledge Exchange")

        st.bar_chart({"a: yet to achieve": [100-knowledge_exchange_score],
                        "b: score achieved": [knowledge_exchange_score]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])




def educational_impact_section():
    global educational_impact_score
    # Create a two-column layout
    educational_impact_left_column, educational_impact_right_column = st.columns(2)

    # Educational Impact

    st.divider()
    with educational_impact_left_column:
        st.subheader("Educational Impact")
        st.write("")
        st.subheader("Our university considers the following indicators")
        educational_impact_options =[
                "Our university conducts research into quality education",
                "Our alumni plays vital impact in the field of education",
                "Our university has good academic reputation in relevant social subjects",
                "Our students are free in pursuing their research without censorship",
                "Our academics are free in pursuing their research without censorship"
                ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in educational_impact_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our university conducts research into quality education" in option:
                    educational_impact_score += (100/5)
                elif "Our alumni plays vital impact in the field of education" in option:
                    educational_impact_score += (100/5)
                elif "Our university has good academic reputation in relevant social subjects" in option:
                    educational_impact_score += (100/5)
                elif "Our students are free in pursuing their research without censorship" in option:
                    educational_impact_score += (100/5)
                elif "Our academics are free in pursuing their research without censorship" in option:
                    educational_impact_score += (100/5)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {educational_impact_score:.2f}")

    with educational_impact_right_column:
        st.write("Educational Impact")

        st.bar_chart({"a: yet to achieve": [100-educational_impact_score],
                        "b: score achieved": [educational_impact_score]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])


def employability_and_oppurtunity_section():
    global employability_and_oppurtunity_score
    # Create a two-column layout
    employability_and_oppurtunity_left_column, employability_and_oppurtunity_right_column = st.columns(2)

    # Employability and Oppurtunity

    st.divider()
    with employability_and_oppurtunity_left_column:
        st.subheader("Employability and Oppurtunity")
        st.write("")
        st.subheader("Our university considers the following indicators")
        employability_and_oppurtunity_options =[
                "Research into work and economic growth are conducted in our university",
                "Research into peace, justice and strong institutions are conducted in our university",
        ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0

        unemployment_rate_score = st.slider("Select the unemployment rate of our students in the country", 0.0, 100.0, 0.0)
        # Unemployment Rate Calculate
        if unemployment_rate_score > 0.0:
            employability_and_oppurtunity_score += ((100/3) * (100-unemployment_rate_score)/100)
        selected_options_content = []
        for option in employability_and_oppurtunity_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Research into work and economic growth are conducted in our university" in option:
                    employability_and_oppurtunity_score += (100/3)
                elif "Research into peace, justice and strong institutions are conducted in our university" in option:
                    employability_and_oppurtunity_score += (100/3)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {employability_and_oppurtunity_score:.2f}")

    with employability_and_oppurtunity_right_column:
        st.write("Employability and Oppurtunity")

        st.bar_chart({"a: yet to achieve": [100-employability_and_oppurtunity_score],
                        "b: score achieved": [employability_and_oppurtunity_score]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])



def quality_of_life_section():
    global quality_of_life_score
    # Create a two-column layout
    quality_of_life_left_column, quality_of_life_right_column = st.columns(2)

    # Quality of Life

    st.divider()
    with quality_of_life_left_column:
        st.subheader("Quality of Life")
        st.write("")
        st.subheader("Our university considers the following indicators")
        quality_of_life_options =[
                "Our university is committed to promoting wellbeing both within and outside the campus.",
                "Our university has initiated a research activity aimed at studying the quality of life in the local community.",
                "There are a variety of health options on campus, including a fitness center, counseling services, and a health clinic, to support the well-being of our students and staff.",
                "The air quality in the region is good",
        ]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in quality_of_life_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our university is committed to promoting wellbeing both within and outside the campus." in option:
                    quality_of_life_score += (100/4)
                elif "Our university has initiated a research activity aimed at studying the quality of life in the local community." in option:
                    quality_of_life_score += (100/4)
                elif "There are a variety of health options on campus, including a fitness center, counseling services, and a health clinic, to support the well-being of our students and staff." in option:
                    quality_of_life_score += (100/4)
                elif "The air quality in the region is good" in option:
                    quality_of_life_score += (100/4)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {quality_of_life_score:.2f}")

    with quality_of_life_right_column:
        st.write("Quality of Life")

        st.bar_chart({"a: yet to achieve": [100-quality_of_life_score],
                        "b: score achieved": [quality_of_life_score]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])







def main():

    st.title("QS Sustainability Rankings")
    st.write("The new QS World University Rankings: Sustainability 2023 assess 700 universities around the world to determine their environmental and social impact.")
    st.write("Institutional impact is evaluated across eight categories (or indicators) to effectively capture university performance when it comes to making positive change for people and planet.")
    st.write("The rankings can provide a helpful starting point to understanding how environmentally and socially conscious a university is. ")
    st.write("Indicators are split into environmental sustainability measures – including sustainable institutions, sustainable education and sustainable research – and social impact measures – including equality, knowledge exchange, educational impact, employability and opportunities, and quality of life.")
    st.divider()
    left_column, middle_column, right_column = st.columns(3)

    with left_column:

        left_1, left_2 = st.columns(2)
        with left_1:
            score_placeholder = st.empty()
            st.write("(Higher is better)")
            overall_score_bar_chart_placeholder = st.empty()
        with left_2:
            ranking_placeholder = st.empty()
            st.write("(Lower is better)")
            overall_rank_bar_chart_placeholder = st.empty()


    with middle_column:
        middle_column_placeholder = st.empty()

    with right_column:
        right_1, right_2 = st.columns(2)
        # st.write("QS Sustainability Rankings")
        with right_1:
            st.subheader("Environmental Impact")
            overall_environmental_impact_bar_chart_placeholder = st.empty()
            # st.write("Environmental Impact")
        with right_2:
            st.subheader("Social Impact")
            overall_social_impact_bar_chart_placeholder = st.empty()
            # st.write("Social Impact")
        # bar_chart_placeholder = st.empty()

    # environmental_impact_left_column, environmental_impact_right_column = st.columns(2)

    # with environmental_impact_left_column:
    st.subheader("Environmental Impact")
    st.write("The environmental impact rankings reflect the outward impact a university is making when it comes to building a sustainable institution, engaging in relevant and impactful research and embedding sustainability in the curriculum.")

    # with environmental_impact_right_column:
    st.write("Environmental Impact")

    environmental_impact_bar_chart_placeholder = st.empty()


    sustainable_education_section()
    sustainable_institute_section()
    sustainable_research_section()



    # social_impact_left_column, social_impact_right_column = st.columns(2)

    # with social_impact_left_column:

    st.subheader("Social Impact")
    st.write("How seriously do institutions take their role in creating a more equal, fair and just world? As well as environmental impact, the QS Sustainability Rankings also considers university impact around today’s biggest social issues.")

    # with social_impact_right_column:
    st.write("Social Impact")

    social_impact_bar_chart_placeholder = st.empty()

    equality_section()
    knowledge_exchange_section()
    educational_impact_section()
    employability_and_oppurtunity_section()
    quality_of_life_section()

    environmental_sustainability_score = (sustainable_education_score * 0.33 + sustainable_institute_score * 0.33 + sustainable_research_score * 0.34)
    social_impact_score = (equality_score * 0.2 + knowledge_exchange_score * 0.2 + educational_impact_score * 0.2 + employability_and_oppurtunity_score * 0.2 + quality_of_life_score * 0.2)


    environmental_impact_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-sustainable_education_score, 100-sustainable_institute_score, 100-sustainable_research_score],
                        "b: score achieve": [sustainable_education_score, sustainable_institute_score, sustainable_research_score]}, height=500, color=["#48ffff", "#ff7648"], use_container_width=False, width=800)

    social_impact_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-equality_score, 100-knowledge_exchange_score, 100-educational_impact_score, 100-employability_and_oppurtunity_score, 100-quality_of_life_score],
                        "b: score achieve": [equality_score, knowledge_exchange_score, educational_impact_score, employability_and_oppurtunity_score, quality_of_life_score]}, height=500, color=["#abdd87", "#a075c0"], use_container_width=False, width=1000)


    overall_environmental_impact_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-environmental_sustainability_score],
                "b: score achieved": [environmental_sustainability_score]}, height=500, color=["#abdd87", "#a075c0"], use_container_width=False, width=250)
    overall_social_impact_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-social_impact_score],
                "b: score achieved": [social_impact_score]}, height=500, color=["#abdd87", "#a075c0"], use_container_width=False, width=250)

    final_score = (environmental_sustainability_score * ((3*100)/8)/100) + (social_impact_score * ((5*100)/8)/100)
    score_placeholder.subheader(f"QS Sustainability Rankings Score: {final_score:.2f}")
    overall_score_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-final_score],
                      "b: achieved": [final_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])


    pred = np.array([[final_score]])
    rank = random_forest_reg.predict(pred)

    ranking_placeholder.subheader(f"Sustainability Ranking Outcome is {int(rank)}")
    overall_rank_bar_chart_placeholder.bar_chart({"a: yet to achieve": [692 - int(rank)],
                      "b: achieved": [int(rank)]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])





if __name__ == "__main__":
    main()

