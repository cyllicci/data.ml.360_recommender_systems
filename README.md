# data.ml.360_recommender_systems
Repository for DATA.ML.360 Recommender Systems project work.

## Requirements
- Python 3.12.3
- Dependencies listed in requirements.txt

## Python environment setup

This project uses Python 3.12.3

### 1. Clone the repository

```bash
git clone https://github.com/cyllicci/data.ml.360_recommender_systems.git
cd data.ml.360_recommender_systems
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**MacOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Deactivate the environment

When finished, you can deactivate the virtual environment:

```bash
deactivate
```

## Dataset

This project uses the MovieLens 1M dataset provided by GroupLens.

### Download instructions

1. Download the MovieLens 1M dataset from:
   https://grouplens.org/datasets/movielens/1m/

2. Download the `ml-1m.zip` file.

3. Extract the ZIP file.

4. Place the extracted `ml-1m` folder inside the project's `data/` directory.

The expected directory structure is:

```text
data/
└── ml-1m/
    ├── ratings.dat
    ├── movies.dat
    ├── users.dat
    └── README
```

### Dataset files

- `ratings.dat`: User ratings and timestamps.
- `movies.dat`: Movie titles, release years and genres.
- `users.dat`: User demographic information.

### Usage terms

The dataset is provided by GroupLens. Users must follow the dataset's official usage terms.

## Running the project

After downloading the MovieLens 1M dataset and installing the dependencies, run the project with:

```bash
python run_all.py --data-dir ./data/ml-1m
```

The `--data-dir` argument specifies the location of the MovieLens 1M dataset.

The script will automatically:
1. Load the dataset.
2. Analyze the data.
3. Create the temporal train/validation/test split.
4. Train the recommendation models.
5. Evaluate the models.
6. Save results and figures.