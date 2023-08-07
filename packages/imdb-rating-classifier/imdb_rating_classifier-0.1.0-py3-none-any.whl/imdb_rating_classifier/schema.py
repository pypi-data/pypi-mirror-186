"""
Module for predefined table/JSON schemas

The intent of this module is to define the schema for the IMDB movie chart data.
@TODO: - Validate the schema using a dataclass?
"""
from __future__ import annotations

import typing as t
from dataclasses import dataclass

import pandas as pd


@dataclass
class MovieChart:
    """
    Movie chart data class

    Validate the schema using a dataclass?
    """

    rank: int
    title: str
    year: int
    rating: float
    votes: int
    url: str
    poster_url: str
    penalized: bool

    def __post_init__(self):
        """
        Post initialization
        """
        # validate that the rank is between 1 and 250
        if not 1 <= self.rank <= 250:
            raise ValueError(f'Invalid rank: {self.rank}')

        # validate that the year is between 1900 and 2023
        if not 1900 <= self.year <= 2023:
            raise ValueError(f'Invalid year: {self.year}')

        # validate that the rating is between 0.0 and 10.0
        if not 0.0 <= self.rating <= 10.0:
            raise ValueError(f'Invalid rating: {self.rating}')

        # validate that the votes is greater than 0
        if not self.votes > 0:
            raise ValueError(f'Invalid votes: {self.votes}')

        # validate that the penalized is a boolean
        if not isinstance(self.penalized, bool):
            raise ValueError(f'Invalid penalized: {self.penalized}')

    def __repr__(self) -> str:
        """
        Movie chart representation
        """
        return f'MovieChart({self.to_dict()})'

    def to_dict(self) -> dict[str, t.Any]:
        """
        Convert the MovieChart object to a dictionary

        Returns:
            dict: Movie chart data.
        """
        return {
            'rank': self.rank,
            'title': self.title,
            'year': self.year,
            'rating': self.rating,
            'votes': self.votes,
            'url': self.url,
            'poster_url': self.poster_url,
            'penalized': self.penalized,
        }


def validate(movies_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cast the Dataframe columns to the correct type.

    Args:
        movies_data (pd.DataFrame): Movie chart data.

    Returns:
        pd.DataFrame: Movie chart data.
    """
    # cast the year column to int
    movies_df['year'] = movies_df['year'].astype(int)

    # cast the rating column to float
    movies_df['rating'] = movies_df['rating'].astype(float)

    # cast the votes column to int
    movies_df['votes'] = movies_df['votes'].astype(int)

    # cast the rank column to int
    movies_df['rank'] = movies_df['rank'].astype(int)

    # cast the penalized column to bool
    movies_df['penalized'] = movies_df['penalized'].astype(bool)

    return movies_df
