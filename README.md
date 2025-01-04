## Project 1: 200 Countries, 200 Years, 4 Minutes

## Introduction

This project, "200 Countries, 200 Years, 4 Minutes," recreates the renowned Hans Rosling's data visualization. We built the database using pandas and sqlite3, performed proof-of-concept validation with matplotlib, and finalized the product using plotly.express.  

## How to Reproduce

- Install [Miniconda](https://docs.anaconda.com/miniconda)
- Build up environment according to `environment.yml` 

```shell
`conda env create -f environment.yml`
```
- Place the four CSV files from the `data/` folder into a `data/` directory in the working directory.
- Activate the environment and run `python create_gapminder_db.py`. This will create `gapminder.db` in the `data/` folder.
- Activate the environment and run `python plot_with_px.py`. This will create `gapminder_clone.html`.