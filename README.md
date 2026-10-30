<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <h1 align="center">QS Ranking Apps</h1>
  <p align="center">
    Three interactive Streamlit apps that let a university try out "what if" scores against the QS ranking methods and see a predicted rank.
    <br /><br />
    <a href="#getting-started"><strong>Get started »</strong></a>
    <br /><br />
    <a href="#usage">Usage</a>
    &middot;
    <a href="https://github.com/rafsunsheikh/QS-Ranking-Apps/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/rafsunsheikh/QS-Ranking-Apps/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#the-three-apps">The Three Apps</a></li>
        <li><a href="#how-the-prediction-works">How The Prediction Works</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

University planning teams often ask a simple question: "If we improve this indicator, how much would our QS ranking move?" This repository answers that question with three small web apps. You enter or adjust indicator scores, each app combines them with the QS weights into an overall score, and a machine learning model turns that score into an estimated rank.

For example, in the Ranking Dashboard you can drag the Academic Reputation slider up from 36 to 60 and watch the overall score and the predicted rank update straight away.

### The Three Apps

| App | Folder | What you do in it |
|-----|--------|-------------------|
| **QS Ranking Predictive Dashboard** | `QS_Ranking_Dashboard/` | Move sliders for the nine QS World University Rankings indicators (Academic Reputation 30%, Citations per Faculty 20%, Employer Reputation 15%, Faculty Student Ratio 10%, and 5% each for International Faculty Ratio, International Student Ratio, International Research Network, Employment Outcomes and Sustainability). For some indicators the app also shows the staff or student ratio needed to reach that score, plus a short "How to Achieve?" checklist. |
| **QS Employability Rankings** | `QS_Employability_Ranking/` | Tick statements that describe your institution under five indicators: Employer Reputation (30%), Alumni Outcomes (25%), Partnerships with Employers per Faculty (25%), Employer/Student Connections (10%) and Graduate Employment Rate (10%). Each indicator gets a score out of 100 and a bar chart. |
| **QS Sustainability Rankings** | `QS_Sustainability_Ranking/` | Tick indicators across eight categories. Three (Sustainable Institutions, Sustainable Education, Sustainable Research) form the Environmental Impact score and five (Equality, Knowledge Exchange, Educational Impact, Employability and Opportunities, Quality of Life) form the Social Impact score. They are combined in a 3 to 5 ratio. |

### How The Prediction Works

Each app downloads a QS World University Rankings CSV file at start up from the public [rafsunsheikh/qs_ranking][data-repo] repository (the 2026 file for the dashboard, the 2024 file for the other two). It then trains a scikit-learn `RandomForestRegressor` that learns the link between a published overall score and the published rank. Your simulated score is fed into this model to get the estimated rank. Treat the result as a rough guide, not an official QS figure.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][python-shield]][python-url]
* [![Streamlit][streamlit-shield]][streamlit-url]
* [![pandas][pandas-shield]][pandas-url]
* [![NumPy][numpy-shield]][numpy-url]
* [![scikit-learn][sklearn-shield]][sklearn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

* Python 3 with `pip`
* An internet connection, because each app downloads its ranking data from GitHub when it starts

### Installation

1. Clone the repository.
   ```sh
   git clone https://github.com/rafsunsheikh/QS-Ranking-Apps.git
   cd QS-Ranking-Apps
   ```
2. Create and activate a virtual environment (optional, but recommended).
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies. Streamlit is not listed in `requirements.txt`, so install it as well.
   ```sh
   pip install -r requirements.txt streamlit
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Run any of the three apps with Streamlit. Each one opens in your browser.

```sh
# Overall QS World University Rankings predictor
streamlit run QS_Ranking_Dashboard/app.py

# QS Employability Rankings simulator
streamlit run QS_Employability_Ranking/app.py

# QS Sustainability Rankings simulator
streamlit run QS_Sustainability_Ranking/app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

```
QS-Ranking-Apps/
├── QS_Ranking_Dashboard/app.py        # slider dashboard for the overall ranking
├── QS_Employability_Ranking/app.py    # checklist simulator for employability
├── QS_Sustainability_Ranking/app.py   # checklist simulator for sustainability
├── requirements.txt
└── LICENSE
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are welcome. Fork the repo, create a feature branch (`git checkout -b feature/my-change`), commit your changes, push the branch, and open a Pull Request. You can also open an issue to report a bug or suggest an idea.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See [`LICENSE`][license-url] for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

MD Rafsun Sheikh, [@rafsunsheikh][profile-url] on GitHub

Project link: [https://github.com/rafsunsheikh/QS-Ranking-Apps][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/rafsunsheikh/QS-Ranking-Apps.svg?style=for-the-badge
[contributors-url]: https://github.com/rafsunsheikh/QS-Ranking-Apps/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/rafsunsheikh/QS-Ranking-Apps.svg?style=for-the-badge
[stars-url]: https://github.com/rafsunsheikh/QS-Ranking-Apps/stargazers
[issues-shield]: https://img.shields.io/github/issues/rafsunsheikh/QS-Ranking-Apps.svg?style=for-the-badge
[issues-url]: https://github.com/rafsunsheikh/QS-Ranking-Apps/issues
[license-shield]: https://img.shields.io/github/license/rafsunsheikh/QS-Ranking-Apps.svg?style=for-the-badge
[license-url]: https://github.com/rafsunsheikh/QS-Ranking-Apps/blob/master/LICENSE
[repo-url]: https://github.com/rafsunsheikh/QS-Ranking-Apps
[profile-url]: https://github.com/rafsunsheikh
[data-repo]: https://github.com/rafsunsheikh/qs_ranking
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[streamlit-shield]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-url]: https://streamlit.io/
[pandas-shield]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[pandas-url]: https://pandas.pydata.org/
[numpy-shield]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[numpy-url]: https://numpy.org/
[sklearn-shield]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white
[sklearn-url]: https://scikit-learn.org/
