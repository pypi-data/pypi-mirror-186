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
 'pydantic>=1.10.4,<2.0.0',
 'pypandoc_binary>=1.10,<2.0',
 'requests>=2.28.2,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{':extra == "file"': ['marko>=1.2.2,<2.0.0']}

entry_points = \
{'console_scripts': ['leetscrape = leetscrape.scripts:leetscrape_question',
                     'leetupload_solution = '
                     'leetscrape.scripts:leetupload_solution']}

setup_kwargs = {
    'name': 'leetscrape',
    'version': '0.1.10',
    'description': 'Introducing LeetScrape - a powerful and efficient Python package designed to scrape problem statements and their topic and company tags, difficulty, test cases, hints, and code stubs from LeetCode.com. Easily download and save LeetCode problems to your local machine, making it convenient for offline practice and studying. It is perfect for anyone preparing for coding interviews. With the LeetScrape, you can boost your coding skills and improve your chances of landing your dream job.',
    'long_description': '# LeetScrape\n\n[![Python application](https://github.com/nikhil-ravi/LeetcodeScraper/actions/workflows/python-app.yml/badge.svg)](https://github.com/nikhil-ravi/LeetcodeScraper/actions/workflows/python-app.yml) [![deploy-docs](https://github.com/nikhil-ravi/LeetScrape/actions/workflows/deploy-docs.yml/badge.svg)](https://leetscrape.chowkabhara.com) [![PYPI](https://img.shields.io/pypi/v/leetscrape)](https://pypi.org/project/leetscrape/) [![codecov](https://codecov.io/gh/nikhil-ravi/LeetScrape/branch/main/graph/badge.svg?token=GWOVLPYSUA)](https://codecov.io/gh/nikhil-ravi/LeetScrape)\n\nIntroducing the LeetScrape - a powerful and efficient Python package designed to scrape problem statements and basic test cases from LeetCode.com. With this package, you can easily download and save LeetCode problems to your local machine, making it convenient for offline practice and studying. It is perfect for software engineers and students preparing for coding interviews. The package is lightweight, easy to use and can be integrated with other tools and IDEs. With the LeetScrape, you can boost your coding skills and improve your chances of landing your dream job.\n\nUse this package to get the list of Leetcode questions, their topic and company tags, difficulty, question body (including test cases, constraints, hints), and code stubs in any of the available programming languages.\n\nDetailed documentation available [here](https://leetscrape.chowkabhara.com/).\n\n## Installation\n\nStart by installing the package from pip or conda:\n```bash\npip install leetscrape\n# or using conda:\nconda install leetscrape\n# or using poetry:\npoetry add leetscrape\n```\n\n\n## Usage\n\n### Command Line\nRun the `leetscrape` command to get a code stub and a pytest test file for a given Leetcode question:\n```bash\n$ leetscrape --titleSlug two-sum --qid 1\n```\nAt least one of the two arguments is required.\n- `titleSlug` is the slug of the leetcode question that is in the url of the question, and\n- `qid` is the number associated with the question.\n\n### Other classes\n\nImport the relevant classes from the package:\n\n```python\nfrom leetscrape.GetQuestionsList import GetQuestionsList\nfrom leetscrape.GetQuestionInfo import GetQuestionInfo\nfrom leetscrape.utils import combine_list_and_info, get_all_questions_body\n```\n\n### Scrape the list of problems\nGet the list of questions, companies, topic tags, categories using the [`GetQuestionsList`](/GetQuestionsList/#getquestionslist) class:\n\n```python\nls = GetQuestionsList()\nls.scrape() # Scrape the list of questions\nls.to_csv(directory_path="../data/") # Save the scraped tables to a directory\n```\n\n### Get Question statement and other information\nQuery individual question\'s information such as the body, test cases, constraints, hints, code stubs, and company tags using the [`GetQuestionInfo`](/GetQuestionsList/#getquestionslist) class:\n\n```python\n# This table can be generated using the previous commnd\nquestions_info = pd.read_csv("../data/questions.csv")\n\n# Scrape question body\nquestions_body_list = get_all_questions_body(\n    questions_info["titleSlug"].tolist(),\n    questions_info["paidOnly"].tolist(),\n    save_to="../data/questionBody.pickle",\n)\n\n# Save to a pandas dataframe\nquestions_body = pd.DataFrame(\n    questions_body_list\n).drop(columns=["titleSlug"])\nquestions_body["QID"] = questions_body["QID"].astype(int)\n```\n\n> **Note**\n> The above code stub is time consuming (10+ minutes) since there are 2500+ questions.\n\nCreate a new dataframe with all the questions and their metadata and body information.\n\n```python\nquestions = combine_list_and_info(\n    info_df = questions_body, list_df=ls.questions, save_to="../data/all.json"\n)\n```\n\n### Upload scraped data to a Database\nCreate a PostgreSQL database using the [SQL](https://github.com/nikhil-ravi/LeetScrape/blob/dcabdd8bd11b03aac0b725c0adc4881b9be9a48f/example/sql/create.sql) dump and insert data using `sqlalchemy`.\n\n```python\nfrom sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker\n\nengine = create_engine("<database_connection_string>", echo=True)\nquestions.to_sql(con=engine, name="questions", if_exists="append", index=False)\n# Repeat the same for tables ls.topicTags, ls.categories,\n# ls.companies, # ls.questionTopics, and ls.questionCategory\n```\n\nUse the [`queried_questions_list`](https://github.com/nikhil-ravi/LeetScrape/blob/dcabdd8bd11b03aac0b725c0adc4881b9be9a48f/example/sql/create.sql#L228-L240) PostgreSQL function (defined in the SQL dump) to query for questions containy query terms:\n\n```sql\nselect * from queried_questions_list(\'<query term>\');\n```\n\nUse the [`all_questions_list`](https://github.com/nikhil-ravi/LeetScrape/blob/dcabdd8bd11b03aac0b725c0adc4881b9be9a48f/example/sql/create.sql#L243-L253) PostgreSQL function (defined in the SQL dump) to query for all the questions in the database:\n\n```sql\nselect * from all_questions_list();\n```\n\nUse the [`get_similar_questions`](https://github.com/nikhil-ravi/LeetScrape/blob/dcabdd8bd11b03aac0b725c0adc4881b9be9a48f/example/sql/create.sql#L255-L270) PostgreSQL function (defined in the SQL dump) to query for all questions similar to a given question:\n\n```sql\nselect * from get_similar_questions(<QuestionID>);\n```\n\n\n### Extract solutions from a `.py` file\n\nYou may want to extract solutions from a `.py` files to upload them to a database. You can do so using the [`ExtractSolutions`](/src/leetscrape/ExtractSolutions.py) class.\n```python\nfrom leetscrape.ExtractSolutions import extract\n# Returns a dict of the form {QuestionID: solutions}\nsolutions = extract(filename=<path_to_python_script>)\n```\n\nUse the [`upload_solutions`](/utils/#leetscrape.utils.upload_solutions) method to upload the extracted solution code stubs from your python script to the PosgreSQL database.\n\n```python\nfrom leetscrape.ExtractSolutions import upload_solutions\nupload_solutions(engine=<sqlalchemy_engine>, row_id = <row_id_in_table>, solutions: <solutions_dict>)\n```\n',
    'author': 'Nikhil Ravi',
    'author_email': 'nr337@cornell.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikhil-ravi/LeetScrape',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
