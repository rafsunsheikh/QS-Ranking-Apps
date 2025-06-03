import streamlit as st
import pandas as pd


url  = "https://raw.githubusercontent.com/rafsunsheikh/qs_ranking/main/2024_QS_World_University_Rankings.csv"
df = pd.read_csv(url)

dataset = df[["Unnamed: 12", "Unnamed: 13"]]
dataset = dataset.dropna()
new_df = dataset.iloc[3:].copy()
new_df.reset_index(drop=True, inplace=True)
new_df = new_df.dropna()

new_df['Unnamed: 12'] = pd.to_numeric(new_df['Unnamed: 12'], errors='coerce', downcast='float')
new_df['Unnamed: 13'] = pd.to_numeric(new_df['Unnamed: 13'], errors='coerce', downcast='float')
new_df = new_df.dropna()

X = new_df.drop("Unnamed: 13", axis = 1)
y = new_df["Unnamed: 13"]


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)




employee_reputation_score = 0
alumni_outcomes_score = 0
partnership_employers_faculty_score = 0
employer_student_connection_score = 0
graduate_employment_rate_score = 0


# Set the page to wide mode to use the full width of the screen
st.set_page_config(layout="wide")


def employee_reputation_section():
    global employee_reputation_score
    # Create a two-column layout
    employee_reputation_left_column, employee_reputation_right_column = st.columns(2)

    # Employee Reputation

    st.divider()
    with employee_reputation_left_column:

        st.subheader("Employer Reputation")
        st.write("The Employer Reputation indicator is based on the insights of over 44,000 employers drawn from the QS Global Employer Survey, the largest of its kind in the world. The survey asks employers to identify those institutions from which they source the most competent, innovative, effective graduates, and which institutions they consider best at equipping students with relevant skills.")
        st.write("The indicator is worth 30% of the overall ranking score.")

        st.subheader("Our Graduates are having which quality discipline spefic knowledges?")
        employee_reputation_options =[
                "Our Graduate has innovative and creative skills in specific area, based on the course material",
                "Our Graduate has effective skills which fulfills the global skill demand",
                "Our graduates emphasize the importance of a strong reputation, as it is capable of enhancing their career prospects significantly.",
                "Our Graduate has relevant skills"]
        # Create multiple-choice tickboxes in the main content area
        # employee_reputation_score = 0
        selected_options_content = []
        for option in employee_reputation_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our Graduate has innovative and creative skills in specific area, based on the course material" in option:
                    employee_reputation_score += (100/4)
                elif "Our Graduate has effective skills which fulfills the global skill demand" in option:
                    employee_reputation_score += (100/4)
                elif "Our graduates emphasize the importance of a strong reputation, as it is capable of enhancing their career prospects significantly." in option:
                    employee_reputation_score += (100/4)
                elif "Our Graduate has relevant skills" in option:
                    employee_reputation_score += (100/4)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {employee_reputation_score:.2f}")


    with employee_reputation_right_column:
        st.write("Employer Reputation")

        st.bar_chart({"a: yet to achieve": [100-employee_reputation_score],
                        "b: score achieved": [employee_reputation_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])




def alumni_outcomes_section():
    global alumni_outcomes_score
        # Create a two-column layout
    alumni_outcome_left_column, alumni_outcome_right_column = st.columns(2)

    st.divider()
    with alumni_outcome_left_column:
        # Alumni Outcomes
        st.subheader("Alumni Outcomes")
        st.write("The Alumni Outcomes indicator is based on the insights of over 29,000 individuals who have graduated from these institutions. The survey asks alumni to identify the extent to which their institution prepared them for their current job, and to what extent they believe their university’s brand is respected by employers.")
        st.write("The indicator is worth 25% of the overall ranking score.")

        st.subheader("Our Graduates are maintained through Alumni management system")
        alumni_outcomes_options =[
                "We found that our graduates consistently ensure a high level of knowledge and education, setting a standard of excellence for future students.",
                "We believe that the degree program at our university is highly employability-oriented, preparing students with the skills and knowledge needed for success in the job market.",
                "We believe that our alumni credit their degree with fostering creative and innovative thinking-oriented skills that have been instrumental in their career success.",
                "We believe that our alumni are equipped with the skills to adjust to the ever-changing dynamics of the world, making them catalysts for world-changing initiatives.",
                "We believe that our alumni exemplify how ethics,organisation and individual values can be integral to leadership, as they consistently show these qualities in their professional endeavors.",
                "We believe that our alumni are highly sought after by employers, as they are known to be highly competent and effective in their respective fields.",
                "We found that our alumni network includes a dynamic group of young leaders, all high-achieving individuals who have excelled in various fields, with an age range spanning from 20 to 30 years old."
                ]
        # Create multiple-choice tickboxes in the main content area
        # alumni_outcomes_score = 0
        selected_options_content = []
        for option in alumni_outcomes_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "We found that our graduates consistently ensure a high level of knowledge and education, setting a standard of excellence for future students." in option:
                    alumni_outcomes_score += (100/7)
                elif "We believe that the degree program at our university is highly employability-oriented, preparing students with the skills and knowledge needed for success in the job market." in option:
                    alumni_outcomes_score += (100/7)
                elif "We believe that our alumni credit their degree with fostering creative and innovative thinking-oriented skills that have been instrumental in their career success." in option:
                    alumni_outcomes_score += (100/7)
                elif "We believe that our alumni are equipped with the skills to adjust to the ever-changing dynamics of the world, making them catalysts for world-changing initiatives." in option:
                    alumni_outcomes_score += (100/7)
                elif "We believe that our alumni exemplify how ethics,organisation and individual values can be integral to leadership, as they consistently show these qualities in their professional endeavors." in option:
                    alumni_outcomes_score += (100/7)
                elif "We believe that our alumni are highly sought after by employers, as they are known to be highly competent and effective in their respective fields." in option:
                    alumni_outcomes_score += (100/7)
                elif "We found that our alumni network includes a dynamic group of young leaders, all high-achieving individuals who have excelled in various fields, with an age range spanning from 20 to 30 years old." in option:
                    alumni_outcomes_score += (100/7)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score:{alumni_outcomes_score:.2f}")

    with alumni_outcome_right_column:
        st.write("Alumni Outcomes")

        st.bar_chart({"a: yet to achieve": [100-alumni_outcomes_score],
                        "b: score achieved": [alumni_outcomes_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])

def partnership_employers_faculty_section():
    global partnership_employers_faculty_score
        # Create a two-column layout
    partnerships_employers_faculty_left_column, partnerships_employers_faculty_right_column = st.columns(2)

    st.divider()
    with partnerships_employers_faculty_left_column:
        st.subheader("Partnerships with Employers per Faculty")
        st.write("The Partnerships with Employers per Faculty indicator is based on the insights of over 44,000 employers drawn from the QS Global Employer Survey, the largest of its kind in the world. The survey asks employers to identify those institutions from which they source the most competent, innovative, effective graduates, and which institutions they consider best at equipping students with relevant skills.")
        st.write("The indicator is worth 25% of the overall ranking score.")
        st.subheader("Our Graduates/academics are with industry partnerships programs")
        partnership_employers_faculty_options =[
                "We believe that our academics consistently publish their research in Scopus-indexed journals, often collaborating closely with industry partners.",
                "We believe that the impact of our research is exceptionally high, contributing to advancements in various fields and improving the lives of many.",
                "We believe that university has robust work indicators and strong learning partnerships with various industries.",
                "We believe that our university produces employable high quality graduates for globally known organisation.",
                ]
        # Create multiple-choice tickboxes in the main content area
        # partnership_employers_faculty_score = 0

        selected_options_content = []
        for option in partnership_employers_faculty_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "We believe that our academics consistently publish their research in Scopus-indexed journals, often collaborating closely with industry partners." in option:
                    partnership_employers_faculty_score += (100/4)
                elif "We believe that the impact of our research is exceptionally high, contributing to advancements in various fields and improving the lives of many." in option:
                    partnership_employers_faculty_score += (100/4)
                elif "We believe that university has robust work indicators and strong learning partnerships with various industries." in option:
                    partnership_employers_faculty_score += (100/4)
                elif "We believe that our university produces employable high quality graduates for globally known organisation." in option:
                    partnership_employers_faculty_score += (100/4)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {partnership_employers_faculty_score:.2f}")

    with partnerships_employers_faculty_right_column:
        st.write("Partnerships with Employers per Faculty")

        st.bar_chart({"a: yet to achieve": [100-partnership_employers_faculty_score],
                        "b: score achieved": [partnership_employers_faculty_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])


def employer_student_connection_section():
    global employer_student_connection_score
        # Create a two-column layout
    employer_student_connections_left_column, employer_student_connections_right_column = st.columns(2)

    st.divider()
    with employer_student_connections_left_column:
        st.subheader("Employer/Student Connections")
        st.write("The Employer/Student Connections indicator is based on the insights of over 44,000 employers drawn from the QS Global Employer Survey, the largest of its kind in the world. The survey asks employers to identify those institutions from which they source the most competent, innovative, effective graduates, and which institutions they consider best at equipping students with relevant skills.")
        st.write("The indicator is worth 10% of the overall ranking score.")
        st.subheader("Industry-student engagement in teaching & learning in different disciplines.")
        employer_student_connection_options =[
                "We have facilitated options so that employers have maintained an active presence on the university's campus throughout the past twelve months.",
                "We found that employers are offering motivated students the chance to network and gain valuable insights.",
                "We have options that employers provide students with opportunities to engage in career-launching internships and research experiences.",
                "The university collaborates with employers to organize career fairs, creating opportunities for students to access both internships and career prospects.",
                "At the university campus, employers collaborate with the institution to organize company presentations and self promoting activities."
                ]
        # Create multiple-choice tickboxes in the main content area
        # employer_student_connection_score = 0

        selected_options_content = []
        for option in employer_student_connection_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "We have facilitated options so that employers have maintained an active presence on the university's campus throughout the past twelve months." in option:
                    employer_student_connection_score += (100/5)
                elif "We found that employers are offering motivated students the chance to network and gain valuable insights." in option:
                    employer_student_connection_score += (100/5)
                elif "We have options that employers provide students with opportunities to engage in career-launching internships and research experiences." in option:
                    employer_student_connection_score += (100/5)
                elif "The university collaborates with employers to organize career fairs, creating opportunities for students to access both internships and career prospects." in option:
                    employer_student_connection_score += (100/5)
                elif "At the university campus, employers collaborate with the institution to organize company presentations and self promoting activities." in option:
                    employer_student_connection_score += (100/5)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {employer_student_connection_score:.2f}")

    with employer_student_connections_right_column:
        st.write("Employer/Student Connections")

        st.bar_chart({"a: yet to achieve": [100-employer_student_connection_score],
                        "b: score achieved": [employer_student_connection_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])


def graduate_employment_rate_section():
    global graduate_employment_rate_score
    # Create a two-column layout
    graduate_employment_rate_left_column, graduate_employment_rate_right_column = st.columns(2)

    st.divider()
    with graduate_employment_rate_left_column:
        st.subheader("Graduate Employment Rate")
        st.write("The Graduate Employment Rate indicator is based on the insights of over 29,000 individuals who have graduated from these institutions. The survey asks alumni to identify the extent to which their institution prepared them for their current job, and to what extent they believe their university’s brand is respected by employers.")
        st.write("The indicator is worth 10% of the overall ranking score.")
        st.subheader("High Quality discipline specific knowledge")
        graduate_employment_rate_options =[
                    "Our sound initiative to make our graduates to be highly conpetent and effective in their respective fields.",
                    "We give the skills to adjust to the ever-changing dynamics of the world, making them catalysts for world-changing initiatives.",
                    "We presume that our graduates are playing important roles in the economic development of the country. (We do believe)",
                    "We presume that our graduates are supposed to having a high level of knowledge and we provide a great education environment, setting for a standard of excellence for future students.",
                    "We believe that our graduates are getting Full time job within 12 months of graduation.",
                    "We believe that our graduates are getting Part time job within 06 months of graduation (If they wish to be accepting an offer).",
                    "We beleive that our graduates are getting Internship within 06 months of graduation (chances are likely to be high).",
                    "We believe that our graduates are getting Apprenticeship within 06 months of graduation (If they wish to be).",
                    "We believe that our graduates are getting Self-employed within 12 months of graduation (If they wish to be).",
        ]

        # Create multiple-choice tickboxes in the main content area
        # graduate_employment_rate_score = 0

        selected_options_content = []
        for option in graduate_employment_rate_options:
            selected = st.checkbox(f"{option}")
            if selected:
                if "Our sound initiative to make our graduates to be highly conpetent and effective in their respective fields." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We give the skills to adjust to the ever-changing dynamics of the world, making them catalysts for world-changing initiatives." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We presume that our graduates are playing important roles in the economic development of the country. (We do believe)" in option:
                    graduate_employment_rate_score += (100/9)
                elif "We presume that our graduates are supposed to having a high level of knowledge and we provide a great education environment, setting for a standard of excellence for future students." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We believe that our graduates are getting Full time job within 12 months of graduation." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We believe that our graduates are getting Part time job within 06 months of graduation (If they wish to be accepting an offer)." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We beleive that our graduates are getting Internship within 06 months of graduation (chances are likely to be high)." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We believe that our graduates are getting Apprenticeship within 06 months of graduation (If they wish to be)." in option:
                    graduate_employment_rate_score += (100/9)
                elif "We believe that our graduates are getting Self-employed within 12 months of graduation (If they wish to be)." in option:
                    graduate_employment_rate_score += (100/9)

                selected_options_content.append(option)
        # st.write("You selected:", ", ".join(selected_options_content))
        st.write(f"Your Score: {graduate_employment_rate_score:.2f}")

    with graduate_employment_rate_right_column:
        st.write("Graduate Employment Rate")

        st.bar_chart({"a: yet to achieve": [100-graduate_employment_rate_score],
                    "b: score achieved": [graduate_employment_rate_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])




def main():
    st.title("QS Employability Rankings")
    st.divider( )

    left_col, right_col = st.columns(2)
    with left_col:
        ranking_placeholder = st.empty()
        score_placeholder = st.empty()


    with right_col:
        right_1, right_2 = st.columns(2)
        with right_1:
            st.write("(Lower is better)")
            overall_rank_bar_chart_placeholder = st.empty()
            st.write("QS Employability Ranking")

        with right_2:
            st.write("(Higher is better)")
            overall_score_bar_chart_placeholder = st.empty()
            st.write("QS Employability Score")
    st.divider()

    st.subheader("QS Employability Rankings Factors")
    col_1, col_2, col_3, col_4, col_5, = st.columns(5)
    with col_1:

        right_1_bar_chart_placeholder = st.empty()
        st.write("Employer Reputation (30%)")
    with col_2:

        right_2_bar_chart_placeholder = st.empty()
        st.write("Alumni Outcomes (25%)")
    with col_3:

        right_3_bar_chart_placeholder = st.empty()
        st.write("Partnerships with Employers per Faculty (25%)")
    with col_4:

        right_4_bar_chart_placeholder = st.empty()
        st.write("Employer-Student Connections (10%)")
    with col_5:

        right_5_bar_chart_placeholder = st.empty()
        st.write("Graduate Employment Rate (10%)")

    st.divider()


    # col_1, col_2, middle_col, col_3, col_4, col_5, col_6, col_7 = st.columns(8)

    # with col_1:
    #     score_placeholder = st.empty()
    #     st.write("(Higher is better)")
    #     overall_score_bar_chart_placeholder = st.empty()


    # with col_2:
    #     ranking_placeholder = st.empty()
    #     st.write("(Lower is better)")
    #     overall_rank_bar_chart_placeholder = st.empty()

    # with middle_col:
    #     bar_chart_placeholder = st.empty()


    # with col_3:

    #     right_1_bar_chart_placeholder = st.empty()
    #     st.write("Employer Reputation (30%)")
    # with col_4:

    #     right_2_bar_chart_placeholder = st.empty()
    #     st.write("Alumni Outcomes (25%)")
    # with col_5:

    #     right_3_bar_chart_placeholder = st.empty()
    #     st.write("Partnerships with Employers per Faculty (25%)")
    # with col_6:

    #     right_4_bar_chart_placeholder = st.empty()
    #     st.write("Employer-Student Connections (10%)")
    # with col_7:

    #     right_5_bar_chart_placeholder = st.empty()
    #     st.write("Graduate Employment Rate (10%)")



    employee_reputation_section()
    alumni_outcomes_section()
    partnership_employers_faculty_section()
    employer_student_connection_section()
    graduate_employment_rate_section()


    right_1_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-employee_reputation_score],
                        "b: score achieved": [employee_reputation_score]}, use_container_width=True, height=500, color=["#a7d967", "#9967d9"])
    right_2_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-alumni_outcomes_score],
                        "b: score achieved": [alumni_outcomes_score]}, use_container_width=True, height=500, color=["#a7d967", "#9967d9"])
    right_3_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-partnership_employers_faculty_score],
                        "b: score achieved": [partnership_employers_faculty_score]}, use_container_width=True, height=500, color=["#a7d967", "#9967d9"])
    right_4_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-employer_student_connection_score],
                        "b: score achieved": [employer_student_connection_score]}, use_container_width=True, height=500, color=["#a7d967", "#9967d9"])
    right_5_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-graduate_employment_rate_score],
                        "b: score achieved": [graduate_employment_rate_score]}, use_container_width=True, height=500, color=["#a7d967", "#9967d9"])

    final_score = employee_reputation_score*0.30 + alumni_outcomes_score*0.25 + partnership_employers_faculty_score*0.25 + employer_student_connection_score*0.10 + graduate_employment_rate_score*0.10
    # score_placeholder.subheader(f"QS Employability Rankings Score: {final_score:.2f}")
    score_placeholder.markdown(f"<h3 style='text-align: center;'>QS Employability Rankings Score: {final_score:.2f}</h1>", unsafe_allow_html=True)

    overall_score_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-final_score],
                      "b: achieved": [final_score]}, use_container_width=False, width=350, height=450, color=["#48ffff", "#ff7648"])


    pred = np.array([[final_score]])
    rank = random_forest_reg.predict(pred)

    ranking_placeholder.markdown(f"<h3 style='text-align: center;'>Employability Ranking Outcome: {int(rank)}</h1>", unsafe_allow_html=True)
    overall_rank_bar_chart_placeholder.bar_chart({"a: yet to achieve": [597 - int(rank)],
                      "b: achieved": [int(rank)]}, use_container_width=False, width=350, height=450, color=["#abdd87", "#a075c0"])



if __name__ == "__main__":
    main()

