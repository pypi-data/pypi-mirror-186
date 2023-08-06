# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ds_boost']

package_data = \
{'': ['*']}

install_requires = \
['jupyter>=1.0.0,<2.0.0',
 'lightgbm>=3.3.4,<4.0.0',
 'matplotlib>=3.6.3,<4.0.0',
 'notebook>=6.5.2',
 'pandas>=1.5.0',
 'psutil>=5.9.4,<6.0.0',
 'py-cpuinfo>=9.0.0,<10.0.0',
 'pyarrow>=9.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'seaborn>=0.12.2,<0.13.0']

extras_require = \
{':python_version >= "3.10" and python_version < "3.11"': ['tensorflow>=2.11.0,<3.0.0']}

setup_kwargs = {
    'name': 'ds-boost',
    'version': '0.1.0',
    'description': 'Package for Practical & efficient Data Science in Python. Initially written for data-science-keras repo',
    'long_description': "# Data science projects with Keras (Poetry Version)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)<br>\n\nAuthor: [Angel Martinez-Tenor](https://profile.angelmtenor.com/)\n\nRepository: [Github link](https://github.com/angelmtenor/data-science-keras)\n\n\nThis repo contains a set of data science projects solved with artificial neural networks implemented in [Keras](https://github.com/keras-team/keras/). It is based on a set of use cases from [Udacity](https://www.udacity.com/), [Coursera](https://www.coursera.org/) & [Kaggle](https://www.kaggle.com/)\n\nThe repo also introduces a minimal package **ds_boost** initally implemented as a helper for this repo\n\n\n\n\nDisclaimer: This notebooks-based repo was developed in early 2018. Since July 2022, I'm updating it using the best practices I've learned implementing solutions in production environment my experience as a lead data scientist\n\n\nA **non-poetry version** of this repo is available in the branch `no-poetry`\n\n## Scenarios\n### Classification models\n\n- [Enron Scandal](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/enron_scandal.ipynb) Identifies Enron employees who may have committed fraud\n\n- [Property Maintenance Fines](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/property_maintenance_fines.ipynb) Predicts the probability of a set of blight tickets to be paid on time\n\n- [Sentiment IMDB](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/sentiment_IMDB.ipynb)  Predicts positive or negative sentiments from movie reviews (NLP)\n\n\n- [Spam detector](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/spam_detector.ipynb) Predicts the probability that a given email is a spam email (NLP)\n\n- [Student Admissions](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/student_admissions.ipynb)  Predicts student admissions to graduate school at UCLA\n\n- [Titanic](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/titanic.ipynb)  Predicts survival probabilities from the sinking of the RMS Titanic\n\n### Regression models\n\n- [Bike Rental](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/bike_rental.ipynb) Predicts daily bike rental ridership\n\n- [House Prices](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/house_prices.ipynb) Predicts house sales prices from Ames Housing database\n\n- [Simple tickets](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/simple_tickets.ipynb)  Predicts the number of tickets requested by different clients\n\n\n### Recurrent models\n\n- [Machine Translation](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/machine_translation.ipynb)  Translates sentences from English to French (NLP)\n\n- [Simple Stock Prediction](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/simple_stock_prediction.ipynb) Predicts Alphabet Inc. stock price\n\n- [Text generator](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/text_generator.ipynb) Creates an English language sequence generator (NLP)\n\n### Social network models\n\n- [Network](https://github.com/angelmtenor/data-science-keras/blob/master/notebooks/network.ipynb)  Predicts missing salaries and new email connections from a company's email network\n\n\n## Setup & Usage\n*Python 3.8+ required. Conda environment with Python 3.10 suggested*\n\n1. Clone the repository using `git`:\n\n    ```bash\n    git clone https://github.com/angelmtenor/data-science-keras.git\n    ```\n\n2. Enter to the root path of the repo and use or create a new conda environment for development:\n\n```bash\n$ conda create -n dev python=3.10 -y && conda activate dev\n```\n\n3. Install the minimal package developed as a helper for this repo:\n    ```bash\n    pip install dist/ds_boost-0.1.0-py3-none-any.whl\n    ```\n\n4. Open the desired project/s with [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html)\n    ```bash\n    cd data-science-keras\n    jupyter notebook\n    ```\n\n## Development Mode\nIn the root folder of the cloned repository, install all the required dev packages and the ds-boost mini package (**Make** required):\n```bash\nmake setup\n```\n\nTo install tensorflow with GPU support, follow the instructions of this guide: [Install TensorFlow GPU](https://www.tensorflow.org/install/pip#install_cuda_with_apt).\n\nQA (manual pre-commit):\n```bash\nmake qa\n```\n\n###  Development Tools Required:\n\n**A Container/Machine with Conda, Git and Poetry as closely as defined in `.devcontainer/Dockerfile`:**\n\n- This Dockerfile contains a non-root user so the same configuration can be applied to a WSL Ubuntu Machine and any Debian/Ubuntu CLoud Machine (Vertex AI workbench, Azure VM ...)\n- In case of having an Ubuntu/Debian machine with non-root user (e.g.: Ubuntu in WSL, Vertex AI VM ...), just install the tools from  *non-root user (no sudo)** section of `.devcontainer/Dockerfile`  (sudo apt-get install \\<software\\> may be required)\n- A pre-configured Cloud VM usually has Git and Conda pre-installed, those steps can be skipped\n- The development container defined in `.devcontainer/Dockerfile` can be directly used for a fast setup (Docker required).  With Visual Studio Code, just open the root folder of this repo, press `F1` and select the option **Dev Containers: Open Workspace in Container**. The container will open the same workspace after the Docker Image is built.\n\n\n## Contributing\n\nCheck out the contributing guidelines\n\n## License\n\n`ds_boost` was created by Angel Martinez-Tenor. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`ds_boost` was created from a Data Science Template developed by Angel Martinez-Tenor. The template was built upon `py-pkgs-cookiecutter` [template] (https://github.com/py-pkgs/py-pkgs-cookiecutter)\n",
    'author': 'Angel Martinez-Tenor',
    'author_email': 'angelmtenor@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
