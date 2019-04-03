def can_two_movies_fill_flight(movies_durations, flight_duration):

    movie_pairs = set()
    for movie_duration in movies_durations:

        if movie_duration in movie_pairs:
            return True

        movie_pairs.add(flight_duration - movie_duration)

    return False
