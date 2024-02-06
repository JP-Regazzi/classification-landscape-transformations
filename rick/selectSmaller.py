import geopandas as gpd
import random
import os

# General
BASE_PATH = os.getcwd()

NEW_FILE_NAME = "data/10samples.geojson"

N_SAMPLES = 10

## Read data
train_df = gpd.read_file(f'{BASE_PATH}/data/train.geojson', index_col=0)

## Sorting
train_df_aleatorio = train_df.sample(N_SAMPLES, random_state=1)  # Você pode ajustar random_state para obter resultados reproduzíveis

## Exporting
train_df_aleatorio.to_file(NEW_FILE_NAME, driver='GeoJSON')