"""
Module for review penalizer processing logic

Review Penalizer:
Ratings are good because they give us an impression of how many people think a movie is good or bad.
However, it does matter how many people voted.
The aim is to penalize those movies where the number of ratings is low.

Find the movie with the maximum number of ratings (out of the TOP 20 only).
This is going to be the benchmark. Compare every movie’s number of ratings to this
and penalize each of them based on the following rule:
- Every 100k deviation from the maximum translates to a point deduction of 0.1.

For example:
-   suppose that the movie with the highest number of ratings has 2.456.123 ratings.
    This means that for a given movie with 1.258.369 ratings and an IMDB review score of 9.4,
    the amount of the deduction is 1.1 and therefore the adjusted rating is 8.3.

@TODO: [X] - fix the type hinting for the movies parameter
       [X] - fix the logic for the numbber of ratings lookup
       (currently we are getting the higher review instead of the higher number of ratings)
"""
from __future__ import annotations

from typing import Any


def penalize_reviews(movies: list[dict[str, Any]]) -> tuple[list[dict[str]], list[dict[str]]]:
    """
    penalize reviews form a list of movies

    Args:
        movies (list[dict[str, Any]]): list of movies.

    Returns:
        tuple[list[dict[str, Any]], list[dict[str, Any]]]: tuple of penalized reviews and
        non-penalized reviews.
    """
    # get max number of reviews
    max_reviews = max(movie['votes'] for movie in movies)
    # get penalized reviews
    penalized_reviews = []
    non_penalized_reviews = []
    for movie in movies:
        # get number of reviews
        review = movie['votes']
        # get penalized review
        to_review = movie.copy()
        if review < max_reviews:
            # get number of reviews difference
            reviews_difference = max_reviews - review
            # get the points deduction
            points_deduction = reviews_difference / 100000 * 0.1
            # get the penalized rating and round it to 1 decimals
            penalized_rating = round(movie['rating'] - points_deduction, 1)
            # update penalized review
            to_review['rating'] = penalized_rating
            to_review['penalized'] = True
            # append penalized review
            penalized_reviews.append(to_review)
        else:
            # append non-penalized review
            # TODO: mitigate the risk of having the same number of reviews for multiple movies?
            non_penalized_reviews.append(to_review)

    return penalized_reviews, non_penalized_reviews
