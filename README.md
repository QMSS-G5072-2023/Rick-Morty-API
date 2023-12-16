# rmtrend

The package is designed as an API client for users to interact with the Rick & Morty API and to retrieve data from the rickandmorty subreddit with the Reddit API.

## Installation

```bash
$ pip install rmtrend
```

## Usage

The package offers 3 major functions for users to interact with Rick & Morty API and to retrieve data from rickandmorty subreddit.

### Function 1
### fetch_character_info
The function fetches basic information for a user designated character from the Rick & Morty API.

Parameters:
- character_name (str): The full name of the character.

Returns:
- dict: A dictionary containing character information, including status, species, gender, origin name, episode count, URL, and image.
Returns None if the character is not found.

Example:
    >>> fetch_character_info("Rick Sanchez")
    {
        'Name': 'Rick Sanchez',
        'Status': 'Alive',
        'Species': 'Human',
        'Gender': 'Male',
        'Origin': 'Earth (C-137)',
        'Episode Count': 31,
        'Image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg',
        'URL': 'https://rickandmortyapi.com/api/character/1'
    }

### Function 2
### fetch_location_info
The function fetches basic information for a user designated location from the Rick & Morty API.

Parameters:
- location_name (str): The name of the location.

Returns:
- dict: A dictionary containing location information, including name, type, dimension, number of residents, and url.
Returns None if the location is not found.

Example:
    >>> fetch_location_info("Citadel of Ricks")
    {
    'Name': 'Citadel of Ricks',
    'Type': 'Space station',
    'Dimension': 'unknown',
    'Number of residents': 101,
    'URL': 'https://rickandmortyapi.com/api/location/3'
    }

### Function 3
### recent_reddit
The function searches Reddit posts in the rickandmorty subreddits for a given keyword and returns information about the top 10 most recent posts.

Parameters:
keyword (str): The keyword to search for in post titles.

Returns:
list of dict: A list containing dictionaries for each of the top 10 posts. 
Each dictionary contains the title, upvote count, and number of comments of the post.

Example:
    >>> recent_reddit('Rick')
    The most recent 10 posts in the Rick and Morty Subreddit with their titles containing Rick:
    [{'title': 'Why I love Rick as a Character', 'upvotes': 4, 'comments': 2},
    {'title': '"What if" series Rick and Morty', 'upvotes': 1, 'comments': 0},
     ...]
    """

## Dependencies

The package requires the following dependencies:
python = "^3.9"
praw = "^7.0"
requests = "^2.31.0"
pytest = "^7.4.3"
requests-mock = "^1.11.0"

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`rmtrend` was created by Yuyang Zhang. It is licensed under the terms of the MIT license.

## Contact
Email: audreyz0712@gmail.com

## Credits

`rmtrend` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
