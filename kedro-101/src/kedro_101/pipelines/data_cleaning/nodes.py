"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 0.19.13
"""

import pandas as pd

def data_cleaning(input_df: pd.DataFrame) -> pd.DataFrame:
    # Extract deck
    input_df['Deck'] = input_df['Cabin'].apply(lambda x: x.split("/")[0] if not pd.isna(x) else None)

    # Extract side
    input_df['Side'] = input_df['Cabin'].apply(lambda x: x.split("/")[-1] if not pd.isna(x) else None)

    # Fill na median for 'Age' column
    median_age = input_df['Age'].median()
    input_df['Age'].fillna(median_age, inplace=True)

    # Fill na mode for 'HomePlanet' and 'Destination' columns
    mode_home_planet = input_df['HomePlanet'].mode()[0]
    input_df['HomePlanet'].fillna(mode_home_planet, inplace=True)

    mode_destination = input_df['Destination'].mode()[0]
    input_df['Destination'].fillna(mode_destination, inplace=True)

    mode_deck = input_df['Deck'].mode()[0]
    input_df['Deck'].fillna(mode_destination, inplace=True)

    mode_side = input_df['Side'].mode()[0]
    input_df['Side'].fillna(mode_destination, inplace=True)

    # Fill na constant values for the remaining columns we are going to use
    input_df['VIP'].fillna(False, inplace=True)
    input_df['CryoSleep'].fillna(False, inplace=True)
    input_df['VRDeck'].fillna(0, inplace=True)
    input_df['RoomService'].fillna(0, inplace=True)
    input_df['FoodCourt'].fillna(0, inplace=True)
    input_df['ShoppingMall'].fillna(0, inplace=True)
    input_df['Spa'].fillna(0, inplace=True)
    input_df['VRDeck'].fillna(0, inplace=True)

    input_df.drop(["PassengerId", "Cabin", "Name"], axis=1, inplace=True)

    return input_df