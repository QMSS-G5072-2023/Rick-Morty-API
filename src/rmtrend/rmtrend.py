import praw

import requests

def fetch_character_info(character_name):
    """
    Fetch basic information for a character from the Rick & Morty API.

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

    Note:
    - Make sure to input the full name of the character, for example, "Rick Sanchez", instead of "Rick".

    """
    api_url = f"https://rickandmortyapi.com/api/character/?name={character_name}"
    response = requests.get(api_url)

    try:
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        data = response.json()
        if data['results']:
            character_data = data['results'][0]

            # Fetch episode count
            episode_count = len(character_data.get('episode', []))

            return {
                "Name": character_data['name'],
                "Status": character_data['status'],
                "Species": character_data['species'],
                "Gender": character_data['gender'],
                "Origin": character_data['origin']['name'] if 'origin' in character_data else None,
                "Episode Count": episode_count,
                "Image": character_data['image'],
                "URL": character_data['url']
            }
        else:
            print(f"Character '{character_name}' not found. Please input the full name of the character, for example, Rick Sanchez, instead of Rick.")
            return None

    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return None


def fetch_location_info(location_name):
    """
    Fetch basic information for a location from the Rick & Morty API.

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


    """
    api_url = f"https://rickandmortyapi.com/api/location/?name={location_name}"
    response = requests.get(api_url)

    try:
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        data = response.json()
        if data['results']:
            location_data = data['results'][0]

            # Fetch episode count
            residents_count = len(location_data.get('residents', []))

            return {
                "Name": location_data['name'],
                "Type": location_data['type'],
                "Dimension": location_data['dimension'],
                "Number of residents": residents_count,
                "URL": location_data['url']
            }
        else:
            print(f"Location '{location_name}' not found. Please input the full name of the character, for example, Citadel of Ricks.")
            return None

    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return None


def recent_reddit(keyword):
    """
    Searches Reddit posts in the rickandmorty subreddits for a given keyword and returns 
    information about the top 10 most recent posts.

    The function connects to the Reddit API using environment variables for 
    authentication. It then searches across all subreddits for the specified 
    keyword, filtering and returning details of the top 10 most recent posts 
    that include the keyword in their title.

    Parameters:
    keyword (str): The keyword to search for in post titles.

    Returns:
    list of dict: A list containing dictionaries for each of the top 10 posts. 
    Each dictionary contains the title, upvote count, and number of comments 
    of the post.

    Example:
    >>> recent_reddit('Rick')
    The most recent 10 posts in the Rick and Morty Subreddit with their titles containing Rick:
    [{'title': 'Why I love Rick as a Character', 'upvotes': 4, 'comments': 2},
    {'title': '"What if" series Rick and Morty', 'upvotes': 1, 'comments': 0},
     ...]
    """

    reddit = praw.Reddit(client_id='OUWF7u-Ge1u2hmfZF--ThQ',
                         client_secret='XSxLekiKv8jJu4tEpbFbUyyc-bwPuA',
                         user_agent='Rick&Morty_trend_AZLoF_v1.0',
                         username='AZ_LoF',
                         password='Just4QMSS')

    subreddit = reddit.subreddit('rickandmorty')
    count = 0
    posts_info = []

    for submission in subreddit.search(keyword, sort='new'):
        title = submission.title
        if keyword.lower() in title.lower():
            upvotes = submission.score
            num_comments = submission.num_comments
            posts_info.append({
                'title': title,
                'upvotes': upvotes,
                'comments': num_comments
            })

            count += 1
            if count >= 10:
                break
    print(f"The most recent 10 posts in the Rick and Morty Subreddit with their titles containing {keyword}:")
    return posts_info
