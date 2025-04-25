![streamlit_logo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png)

# Streamlit demo

A repo to explore the possibilities within Streamlit. Consists of different streamlit applications to showcase the possibilities of Streamlit.

To install Streamlit:
```
pip install streamlit
```

Validate the installation by running the Hello app:
```
streamlit hello
```

This project uses poetry to manage dependencies. To add new packages run `poetry add my_package`. To update packages run `poetry update`.

To activate the virtual environment run:

```
poetry shell
```

To deactivate the environment run `exit`

To install the pre-commit hooks run:
```
pre-commit install
```

To run the visualisations do:

```
streamlit run app/english_culture.py
```
and a new window will appear in your browser with the app.

To run unit tests with pytest:
```
pytest
```
This project uses GitHub actions to automatically run linting checks and unit tests before branches are committed to the main branch
