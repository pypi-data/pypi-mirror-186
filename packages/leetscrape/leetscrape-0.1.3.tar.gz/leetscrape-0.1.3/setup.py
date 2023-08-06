# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['leetscrape']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.46,<2.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'psycopg2>=2.9.5,<3.0.0',
 'requests>=2.28.2,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'leetscrape',
    'version': '0.1.3',
    'description': 'Introducing LeetScrape - a powerful and efficient Python package designed to scrape problem statements and their topic and company tags, difficulty, test cases, hints, and code stubs from LeetCode.com. Easily download and save LeetCode problems to your local machine, making it convenient for offline practice and studying. It is perfect for anyone preparing for coding interviews. With the LeetScrape, you can boost your coding skills and improve your chances of landing your dream job.',
    'long_description': '# Leetcode Questions Scraper\n\n[![Python application](https://github.com/nikhil-ravi/LeetcodeScraper/actions/workflows/python-app.yml/badge.svg)](https://github.com/nikhil-ravi/LeetcodeScraper/actions/workflows/python-app.yml) [![deploy-docs](https://github.com/nikhil-ravi/LeetScrape/actions/workflows/deploy-docs.yml/badge.svg)](https://leetscrape.chowkabhara.com) [![PYPI](https://img.shields.io/pypi/v/leetscrape)](https://pypi.org/project/leetscrape/)\n\nIntroducing the LeetScrape - a powerful and efficient Python package designed to scrape problem statements and basic test cases from LeetCode.com. With this package, you can easily download and save LeetCode problems to your local machine, making it convenient for offline practice and studying. It is perfect for software engineers and students preparing for coding interviews. The package is lightweight, easy to use and can be integrated with other tools and IDEs. With the LeetScrape, you can boost your coding skills and improve your chances of landing your dream job.\n\nUse this package to get the list of Leetcode questions, their topic and company tags, difficulty, question body (including test cases, constraints, hints), and code stubs in any of the available programming languages.\n\n## Usage\n\nImport the relevant classes from the [`leetcode`](/src/leetcode/) package:\n\n```python\nfrom leetscrape.GetQuestionsList import GetQuestionsList\nfrom leetscrape.GetQuestionInfo import GetQuestionInfo\nfrom leetscrape.utils import combine_list_and_info, get_all_questions_body\n```\n\nGet the list of questions, companies, topic tags, categories using the [`GetQuestionsList`](/src/leetcode/GetQuestionsList.py) class:\n\n```python\nls = GetQuestionsList()\nls.scrape() # Scrape the list of questions\nls.to_csv(directory_path="../data/") # Save the scraped tables to a directory\n```\n\n> **Warning**\n> The default ALL_JSON_URL in the [`GetQuestionsList`](/src/leetcode/GetQuestionsList.py) class might be out-of-date. Please update it by going to https://leetcode.com/problemset/all/ and exploring the Networks tab for a query returning all.json.\n\nQuery individual question\'s information such as the body, test cases, constraints, hints, code stubs, and company tags using the [`GetQuestionInfo`](/src/leetcode/GetQuestionInfo.py) class:\n\n```python\n# This table can be generated using the previous commnd\nquestions_info = pd.read_csv("../data/questions.csv")\n\n# Scrape question body\nquestions_body_list = get_all_questions_body(\n    questions_info["titleSlug"].tolist(),\n    questions_info["paidOnly"].tolist(),\n    save_to="../data/questionBody.pickle",\n)\n\n# Save to a pandas dataframe\nquestions_body = pd.DataFrame(\n    questions_body_list\n).drop(columns=["titleSlug"])\nquestions_body["QID"] = questions_body["QID"].astype(int)\n```\n\n> **Note**\n> The above code stub is time consuming (10+ minutes) since there are 2500+ questions.\n\nCreate a new dataframe with all the questions and their metadata and body information.\n\n```python\nquestions = combine_list_and_info(\n    info_df = questions_body, list_df=ls.questions, save_to="../data/all.json"\n)\n```\n\nCreate a PostgreSQL database using the [SQL](/example/sql/create.sql) dump and insert data using `sqlalchemy`.\n\n```python\nfrom sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker\n\nengine = create_engine("<database_connection_string>", echo=True)\nquestions.to_sql(con=engine, name="questions", if_exists="append", index=False)\n# Repeat the same for tables ls.topicTags, ls.categories,\n# ls.companies, # ls.questionTopics, and ls.questionCategory\n```\n\nUse the `queried_questions_list` PostgreSQL function (defined in the SQL dump) to query for questions containy query terms:\n\n```sql\nselect * from queried_questions_list(\'<query term>\');\n```\n\nUse the `all_questions_list` PostgreSQL function (defined in the SQL dump) to query for all the questions in the database:\n\n```sql\nselect * from all_questions_list();\n```\n\nUse the `get_similar_questions` PostgreSQL function (defined in the SQL dump) to query for all questions similar to a given question:\n\n```sql\nselect * from get_similar_questions(<QuestionID>);\n```\n\nUse the [`extract_solutions`](/src/leetcode/utils.py:) method to extract solution code stubs from your python script. Note that the solution method should be a part of a class named `Solution` (see [here](/example/solutions/q_0001_TwoSum.py) for an example):\n\n```python\n# Returns a dict of the form {QuestionID: solutions}\nsolutions = extract_solutions(filename=<path_to_python_script>)\n```\n\nUse the [`upload_solutions`](/src/leetcode/utils.py:) method to upload the extracted solution code stubs from your python script to the PosgreSQL database.\n\n```python\nupload_solutions(engine=<sqlalchemy_engine>, row_id = <row_id_in_table>, solutions: <solutions_dict>)\n```\n',
    'author': 'Nikhil Ravi',
    'author_email': 'nr337@cornell.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikhil-ravi/LeetScrape',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
