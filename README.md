# Streamlit_demo
A repo to explore the possibilities within Streamlit. Content will be used at the PyWeb conference on the 5th January.

To install Streamlit:
```
pip install streamlit
```

Validate the installation by running the Hello app:
```
streamlit hello
```

This project uses poetry to manage dependencies. To add new packages run `poetry add my_package`.

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
