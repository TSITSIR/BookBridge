# Setup
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Configurations
st.set_page_config(page_title="BookBridge",
                   page_icon="📚",
                   layout="wide",
                   menu_items={"About": "This quiz was made by a middle schooler to help you select some books you could have an interest in! Hope you found/can find something you would like!\nNote: If you wish to remove buttons in the upper-right to minimize distractions on the website, add /?mode=kid to the URL."} 
                   )

# Read query parameter 
params = st.query_params
mode = params.get("mode", ["adult"])[0]  # default to "adult"

# If not in adult mode, hide Streamlit UI elements
if mode != "adult":
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# Books dataframe
books = pd.DataFrame({
    "Title": [
      "Charlotte's Web - E.B. White",
      "Harry Potter (Series) - J.K. Rowling",
      "Matilda - Roald Dahl",
      "Chronicles of Narnia (Series) - C.S. Lewis",
      "Winnie-the-Pooh (Series) - A.A. Milne",
      "The Buddy Files (Series) - Dori Hillestad Butler",
      "The Wind in the Willows - Kenneth Grahame",
      "Percy Jackson & The Olympians (Series) - Rick Riordan",
      "Graphic Novels of Percy Jackson & The Olympians (Series) - Rick Riordan",
      "The Secret Garden - Frances Hodgson Burnett",
      "The Phantom Tollbooth - Norton Juster",
      "Anne of Green Gables (Series) - L.M. Montgomery",
      "Tom Sawyer and Huckleberry Finn (Series) - Mark Twain",
      "The Boxcar Children (Series) - Gertrude Chandler Warner",
      "A Wrinkle in Time - Madeleine L'Engle",
      "Where the Red Fern Grows - Wilson Rawls",
      "The Wonderful Wizard of Oz - L. Frank Baum",
      "Wonder - R.J. Palacio",
      "The One and Only Ivan - Katherine Applegate",
      "Big Nate (Series) - Lincoln Pierce",
      "Click (Series) - Kayla Miller",
      "I Survived (Series) - Lauren Tarshis",
      "I Survived, The Graphic Novels (Series) - Lauren Tarshis",
      "The Wild Robot (Series) - Peter Brown",
      "The Iron Giant: a Story in Five Nights - Ted Hudges",
      "Franny K. Stein: Mad Scientist (Series) - Jim Benton",
      "The Outsiders - S.E. Hinton",
      "The Boy in the Striped Pajamas - John Boyne",
      "Nim's Island - Wendy Orr",
      "The Magic Tree House (Series) - Mary Pope Osborne",
      "My Father's Dragon - Ruth Gannett",
      "Time Warp Trio (Series) - Jon Scieszka",
      "The Magic School Bus (Series) - Joanna Cole",
      "Jasmine Toguchi, Mochi Queen - Debbi Michiko Florence",
      "Desmond Cole Ghost Patrol (Series) - Andres Miedoso",
      "Zoey and Sassafras (Series) - Asia Citro",
      "The Hobbit - J.R.R. Tolkien",
      "The Hobbit, The Graphic Novel - Chuck Dixon",
      "The Lord of the Rings (Series) - J.R.R. Tolkien",
      "Tree of Dreams - Laura Resau",
      "Hatchet - Gary Paulsen",
      "The Mysterious Benedict Society - Trenton Lee Stewart",
      "Alice in Wonderland - Lewis Carroll",
      "Sherlock Holmes (Series) - Arthur Conan Doyle",
      "Number the Stars - Lois Lowry",
      "The Westing Game - Ellen Raskin",
      "The City of Ember - Jeanne DuPrau",
      "Nancy Drew Diaries (Series) - Carolyn Keene and Sara Paretsky",
      "Green Eggs and Ham - Dr. Seuss",
      "Dog Man (Series) - Dav Pilkey",
      "The Watsons Go to Birmingham - 1963 - Christopher Paul Curtis",
      "National Geographic Kids (Series) - National Geographic Society",
      "The Giving Tree - Shel Silverstein",
      "Abe Lincoln: The Boy who Loved Books - Kay Winters",
      "Hidden Figures (Series) - Margot Lee Shetterly",
      "The Crossover - Kwame Alexander",
      "The Crossover (Graphic Novel) - Kwame Alexander",
      "The Breadwinner (Series) - Deborah Ellis",
      "Maus - Art Spiegelman",
      "New Kid - Jerry Craft",
      "The Kite Runner - Khaled Hosseini",
      "I am Malala - Malala Yousafzai",
      "The Fault in Our Stars - John Green",
      "Children of Blood and Bone - Tomi Adeyemi",
      "The Storm Runner - Jennifer Cervantes",
      "Amina's Voice - Hena Khan",
      "The Giver Quartet (Series) - Lois Lowry",
      "The Hunger Games (Series) - Suzanne Collins",
      "Brown Girl Dreaming - Jacqueline Woodson",
      "A Monster Calls - Patrick Ness",
      "If You Give a Mouse a Cookie - Laura Joffe Numeroff",
      "The Rainbow Fish - Marcus Pfister",
      "Ada Twist, Scientist - Andrea Beaty",
      "The Food Group (Series) - Jory John",
      "The Hate U Give (Series) - Angie Thomas",
      "Like Water for Chocolate - Laura Esquivel",
      "Frog and Toad (Series) - Arnold Lobel",
      "Clifford, the Big Red Dog - Norman Bridwell",
      "Biscuit - Alyssa Satin Capucilli",
      "The Night Gardener - Terry and Eric Fan",
      "Goodnight Moon - Margaret Wise Brown",
      "The Miraculous Journey of Edward Tulane - Kate DiCamillo",
      "The Peculiar Pig - Joy Steuerwald",
      "One Hundred Years of Solitude - Gabriel Garcia Marquez",
      "Dream Count - Chimamanda Ngozi Adichie",
      "The Lines we Cross - Randa Abdel-Fattah",
      "The Family Book - Todd Parr",
      "Tristan Strong (Series) - Mbalia Kwame",
      "Tristan Strong, the Graphic Novels (Series) - Robert Venditti",
      "One of Us is Lying (Series) - Karen McManus",
      "Animal Farm - George Orwell",
      "Lumberjanes (Series) - Noelle Stevenson, Grace Ellis, and Shannon Watters",
      "Aristotle and Dante Discover the Secrets of the Universe - Benjamin Alire Saenz",
      "The Cousins - Karen McManus",
      "The Honest Truth - Dan Gemeinhart",
      "The Girl who Thought in Pictures - Julia Finley Mosca",
      "Ender's Game - Orson Scott Card",
      "Strange the Dreamer - Laini Taylor",
      "The Secret of the Old Clock (Series) - Carolyn Keene",
      "Out of My Mind (Series) - Sharon M. Draper",
      "Ghost - Jason Reynolds",
      "Little Shaq - Shaquille O'Neal",
      "Jake Maddox Sports (Series) - Jake Maddox",
      "Power Forward  - Hena Khan",
      "Golden Arm - Carl Deuker"
        ],
    "Drive": [2, 4, 6, 7, 2, 4, 3, 6, 6, 5,
              8, 6, 5, 5, 8, 5, 7, 9, 8, 10,
              6, 2, 2, 4, 7, 5, 7, 5, 4, 1,
              2, 3, 4, 8, 2, 4, 3, 3, 4, 6,
              4, 6, 4, 3, 2, 6, 4, 3, 5, 2,
              7, 1, 6, 9, 9, 7, 6, 4, 7, 5,
              9, 7, 4, 8, 6, 9, 3, 8, 2, 6,
              3, 2, 2, 5, 4, 8, 8, 5, 3, 4,
              7, 5, 8, 5, 6, 3, 2, 6, 6, 3,
              4, 3, 7, 9, 4, 8, 3, 5, 3, 3,
              8, 6, 5, 3, 2],
    "Pace": [5, 7, 6, 7, 3, 9, 10, 8, 8, 2,
             6, 3, 7, 3, 8, 5, 7, 4, 6, 10,
             7, 8, 8, 4, 5, 8, 5, 6, 6, 10,
             7, 8, 5, 7, 9, 8, 1, 5, 2, 3,
             6, 5, 8, 5, 6, 5, 7, 8, 10, 9,
             6, 3, 5, 4, 5, 6, 6, 7, 8, 7,
             7, 3, 4, 6, 5, 4, 6, 7, 4, 7,
             9, 6, 8, 7, 5, 6, 9, 9, 3, 5,
             8, 6, 8, 3, 5, 4, 9, 8, 9, 6,
             7, 9, 6, 7, 6, 10, 7, 8, 7, 6,
             7, 9, 8, 6, 5],
    "Tone": [4, 5, 6, 3, 10, 5, 6, 5, 5, 4,
             5, 7, 5, 6, 5, 6, 5, 7, 3, 7,
             5, 2, 2, 5, 6, 7, 3, 1, 8, 9,
             8, 8, 7, 8, 5, 7, 5, 5, 4, 8,
             3, 4, 5, 5, 2, 6, 5, 7, 9, 5,
             3, 2, 8, 8, 6, 4, 4, 2, 1, 6,
             3, 2, 2, 3, 6, 4, 2, 3, 3, 1,
             9, 7, 10, 8, 4, 3, 9, 10, 9, 8,
             10, 3, 6, 3, 2, 2, 6, 4, 5, 2,
             2, 8, 5, 6, 3, 9, 3, 4, 7, 5,
             6, 10, 9, 6, 6],
    "Pictures": [7, 1, 6, 2, 9, 6, 6, 2, 10, 4,
                 7, 6, 2, 7, 7, 2, 3, 8, 9, 10,
                 10, 2, 10, 9, 6, 8, 4, 1, 8, 10,
                 5, 8, 9, 6, 8, 9, 6, 10, 7, 9,
                 1, 4, 4, 6, 1, 2, 8, 4, 10, 10,
                 2, 9, 7, 7, 8, 1, 9, 3, 9, 10,
                 6, 8, 1, 2, 4, 7, 2, 2, 8, 9,
                 10, 10, 10, 9, 7, 2, 10, 8, 9, 10,
                 6, 8, 5, 2, 1, 10, 10, 1, 10, 1,
                 1, 10, 2, 1, 1, 10, 7, 3, 3, 1,
                 3, 8, 6, 1, 2],
    "Setting": [3, 9, 5, 10, 5, 4, 5, 9, 9, 5,
                8, 6, 7, 4, 10, 5, 10, 1, 7, 1,
                1, 2, 2, 4, 8, 3, 2, 1, 4, 9,
                6, 9, 5, 2, 6, 7, 10, 10, 10, 8,
                1, 2, 9, 2, 1, 4, 6, 3, 7, 7,
                1, 1, 6, 2, 1, 1, 1, 1, 3, 2,
                3, 1, 1, 9, 10, 1, 7, 4, 1, 9,
                6, 7, 2, 4, 2, 5, 6, 7, 3, 5,
                2, 3, 4, 5, 6, 2, 1, 10, 10, 1,
                6, 4, 2, 1, 2, 2, 8, 9, 2, 1,
                2, 2, 1, 2, 1],
    "Reading level": [75, 87, 75, 94, 47, 60,
                      90, 83, 83, 90, 90, 94,
                      110, 60, 98, 89, 80, 83,
                      80, 60, 62, 70, 70, 82,
                      85, 46, 110, 94, 80, 50,
                      78, 72, 60, 70, 69, 62,
                      95, 90, 110, 107, 98, 97,
                      88, 109, 100, 99, 99, 83,
                      34, 46, 98, 70, 38, 60,
                      90, 100, 90, 100, 108, 85,
                      120, 107, 108, 112, 94, 83,
                      100, 108, 82, 103, 33, 30,
                      40, 70, 120, 130, 47, 26,
                      30, 63, 38, 88, 70, 129,
                      109, 110, 40, 98, 95, 100,
                      119, 83, 109, 109, 94, 60,
                      109, 128, 70, 97, 109, 40,
                      60, 68, 110
    ],
    "Genre": [
         "Animal Fiction", "Fantasy", "Magical Realism", "Fantasy", "Animal Fiction",
         "Mystery", "Animal Fiction", "Fantasy", "Fantasy", "Realistic Fiction",
         "Fantasy", "Historical Fiction", "Adventure", "Mystery", "Science Fiction",
         "Realistic Fiction", "Fantasy", "Realistic Fiction", "Animal Fiction", "Realistic Fiction",
         "Realistic Fiction", "Historical Fiction", "Historical Fiction", "Science Fiction",  "Science Fiction",
         "Science Fiction", "Realistic Fiction", "Historical Fiction", "Adventure", "Adventure",
         "Adventure", "Adventure", "Non-Fiction", "Realistic Fiction", "Mystery",
         "Adventure", "Fantasy", "Fantasy", "Fantasy", "Adventure",
         "Adventure", "Science Fiction", "Fantasy", "Mystery", "Historical Fiction",
         "Mystery", "Science Fiction", "Mystery", "Fantasy", "Adventure",
         "Historical Fiction", "Non-Fiction", "Fable", "Non-Fiction", "Non-Fiction",
         "Sport-Realistic Fiction", "Sport-Realistic Fiction", "Historical Fiction", "Historical Fiction", "Realistic Fiction",
         "Historical Fiction", "Non-Fiction", "Realistic Fiction", "Fantasy", "Fantasy",
         "Realistic Fiction", "Science Fiction", "Adventure", "Non-Fiction", "Fantasy",
         "Animal Fiction", "Animal Fiction", "Science Fiction", "Fiction", "Realistic Fiction",
         "Magical Realism", "Animal Fiction", "Animal Fiction", "Animal Fiction", "Magical Realism",
         "N/A", "Fantasy", "Animal Fiction", "Magical Realism", "Fiction",
         "Realistic Fiction", "Realistic Fiction", "Adventure", "Fantasy", "Mystery",
         "Animal Fiction", "Adventure", "Realistic Fiction", "Mystery", "Adventure",
         "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Realistic Fiction",
         "Sport-Realistic Fiction", "Sport", "Sport", "Sport", "Sport-Realistic Fiction"
    ]
})

# Update genre entries for books that clearly span more than one genre
books.loc[books["Title"].str.contains("Harry Potter", case=False), "Genre"] = "Fantasy-Magical Realism"
books.loc[books["Title"].str.contains("Percy Jackson", case=False), "Genre"] = "Fantasy-Adventure"
books.loc[books["Title"] == "A Wrinkle in Time - Madeleine L'Engle", "Genre"] = "Science Fiction-Fantasy"
books.loc[books["Title"].str.contains("I Survived", case=False), "Genre"] = "Historical Fiction-Adventure"
books.loc[books["Title"] == "The Hobbit - J.R.R. Tolkien", "Genre"] = "Fantasy-Adventure"
books.loc[books["Title"] == "The Hobbit, The Graphic Novel - Chuck Dixon", "Genre"] = "Fantasy-Adventure"
books.loc[books["Title"] == "The Lord of the Rings (Series) - J.R.R. Tolkien", "Genre"] = "Fantasy-Adventure"
books.loc[books["Title"] == "The Magic Tree House (Series) - Mary Pope Osborne", "Genre"] = "Adventure-Fantasy"
books.loc[books["Title"] == "Time Warp Trio (Series) - Jon Scieszka", "Genre"] = "Adventure-Science Fiction"
books.loc[books["Title"] == "The Magic School Bus (Series) - Joanna Cole", "Genre"] = "Science Fiction-Non-Fiction"
books.loc[books["Title"] == "A Monster Calls - Patrick Ness", "Genre"] = "Magical Realism-Fantasy"
books.loc[books["Title"] == "Children of Blood and Bone - Tomi Adeyemi", "Genre"] = "Fantasy-Adventure"
books.loc[books["Title"] == "Tree of Dreams - Laura Resau", "Genre"] = "Fantasy-Magical Realism"
books.loc[books["Title"] == "The Wild Robot (Series) - Peter Brown", "Genre"] = "Science Fiction-Animal Fiction"
books.loc[books["Title"] == "Wonder - R.J. Palacio", "Genre"] = "Realistic Fiction-Historical Fiction"
books.loc[books["Title"] == "The One and Only Ivan - Katherine Applegate", "Genre"] = "Animal Fiction-Realistic Fiction"
books.loc[books["Title"] == "The Secret Garden - Frances Hodgson Burnett", "Genre"] = "Magical Realism-Realistic Fiction"
books.loc[books["Title"] == "Anne of Green Gables (Series) - L.M. Montgomery", "Genre"] = "Historical Fiction-Realistic Fiction"
books.loc[books["Title"] == "National Geographic Kids (Series) - National Geographic Society", "Genre"] = "Non-Fiction-Science"

# UI Start
st.title("BookBridge Recommendation Quiz")

# Grade assigning by numeric value
grade_mapping_lexile = {
    "1st Grade": 32, 
    "2nd Grade": 45,
    "3rd Grade": 55,
    "4th Grade": 68,
    "5th Grade": 83,
    "6th Grade": 95,
    "7th Grade": 102,
    "8th Grade": 115
}
                     
reading_level = st.radio("What is your reading level?", list(grade_mapping_lexile.keys()),
                         help=("This program was designed for 1st to 8th graders; if your reading level falls outside of this range, you may have to rely on another resource to find a book you may love."))
reading_level_numeric = grade_mapping_lexile[reading_level]

# Define the range of acceptable reading levels (within a set amount, weighted towards challenging kids)
min_level = reading_level_numeric - 8
max_level = reading_level_numeric + 15

# Filter books to only include those within the range of acceptable reading levels
filtered_books = books[(books['Reading level'] >= min_level) & (books['Reading level'] <= max_level)].copy()

# Expand hyphenated genres into sets
filtered_books["Genre List"] = filtered_books["Genre"].apply(lambda g: g.split("-"))

# Create binary encoding for genres
mlb = MultiLabelBinarizer()
genre_encoded = mlb.fit_transform(filtered_books["Genre List"])
genre_columns = [f"Genre: {g}" for g in mlb.classes_]

# Create a DataFrame with the one-hot encoded genres
genre_df = pd.DataFrame(genre_encoded, columns=genre_columns, index=filtered_books.index)

# Merge into filtered_books
filtered_books = pd.concat([filtered_books, genre_df], axis=1)

genre_df_normalized = genre_df.div(genre_df.sum(axis=1), axis=0)

# Slider explanation functions
def get_drive_explanation(value):
    if value <= 2:
        return "I really like books that focus much more on all the events that are happening."
    elif value <= 4:
        return "I like books that mostly prioritize the narrative outside of characters."
    elif value <= 6:
        return "I like books that show both how the characters are inside, and what they do in the events of the books themselves."
    elif value <= 8:
        return "I like books that show a lot of character changes and inner lives."
    else:
        return "I love books that are all about telling me the characters' thoughts and feelings."

    
def get_pace_explanation(value):
    if value <= 2:
        return "I enjoy books that are slow-paced and give me time to think."
    elif value <= 4:
        return "I'm a fan of books that are quite slow, with some time to think, but not overly slow."
    elif value <= 6:
        return "I like books with a moderate pace, not too fast nor too slow."
    elif value <= 8:
        return "I like books that are fast-paced and keep me engaged."
    else:
        return "I love fast-paced books that keep me on the edge of my seat."

    
def get_tone_explanation(value):
    if value <= 2:
        return "I prefer books with a very serious and dramatic tone."
    elif value <= 4:
        return "I enjoy books with a mostly serious tone but with some light moments."
    elif value <= 6:
        return "I like books that are balanced in tone—serious and light-hearted."
    elif value <= 8:
        return "I enjoy books that are light and fun with some serious undertones."
    else:
        return "I love books that are funny, upbeat, and light in tone."

    
def get_pictures_explanation(value):
    if value <= 2:
        return "I like books with very few or no pictures. I don't really need them."
    elif value <= 4:
        return "I enjoy books with some pictures, but not too many."
    elif value <= 6:
        return "I like a balance of pictures and text in my books."
    elif value <= 8:
        return "I enjoy books with more pictures than text."
    else:
        return "I love books with lots of pictures and visual storytelling."

    
def get_setting_explanation(value):
    if value <= 2:
        return "I prefer books set in realistic, grounded environments."
    elif value <= 4:
        return "I like books that take place in semi-realistic worlds with a little fantasy."
    elif value <= 6:
        return "I like stories where the real world blends with a hint of fantasy."
    elif value <= 8:
        return "I prefer books that take me to otherworldly or distant settings."
    else:
        return "I love books set in completely imaginative or fantastical worlds."

# Slider Questions
drive = st.slider("Do you like stories that are more focused on the plot/storyline, or on the characters in the book themselves?", 1, 10, 1, 1,
                  help="1: Books are plot-driven, meaning that the main emphasis (focus) is on the storyline and not so much the characters. 10: Books are character-driven, shaped by the people in it and how they grow or show their emotions in the book.")
st.caption(get_drive_explanation(drive))

st.text("")

pace = st.slider("Do you prefer books that move quickly or slowly?", 1, 10, 1, 1,
                 help="1: Books move slower in the storyline. 10: Books move quicker in the storyline.")
st.caption(get_pace_explanation(pace))

st.text("")

tone = st.slider("Do you like books with a serious or light tone?", 1, 10, 1, 1,
                 help="1: Books have more serious tone. 10: Books are lighter or funnier.")
st.caption(get_tone_explanation(tone))

st.text("")

pictures = st.slider("Do you prefer books with more pictures or more text?", 1, 10, 1, 1,
                     help="1: Books have few, if any pictures, and much more text. 10: Books have plenty of pictures and visuals.")
st.caption(get_pictures_explanation(pictures))

st.text("")

setting = st.slider("Do you enjoy books set in realistic or magical settings?", 1, 10, 1, 1,
                    help="1:Books are in a realistic world. 10: Books are full of magic or fantasy, and are imaginative.")
st.caption(get_setting_explanation(setting))

# Optional Genre Question
genre_options = ["No preference", "Sport", "Fantasy", "Animal Fiction", "Mystery", "Adventure", "Science Fiction", "Historical Fiction", "Realistic Fiction", "Non-Fiction"]
selected_genre = st.selectbox("Select a genre you're most interested in:", genre_options,
                              help="Please note that your genre preference will not change your entire set of recommendations, only influence it. Non-Fiction includess memoirs and biographies, as well as standard fact-based books.")

if not filtered_books.empty:
    # User preferences vector (Drive, Pace, Tone, Pictures, Setting)
    user_preferences = np.array([[drive, pace, tone, pictures, setting]])
    user_preferences = np.tile(user_preferences, (len(filtered_books), 1))

    book_vectors = filtered_books[["Drive", "Pace", "Tone", "Pictures", "Setting"]].values

    # Feature weights: Drive, Pace, Tone, Pictures, Setting
    weights = np.array([1.0, 0.9, 1.0, 0.8, 0.7])  # Slightly softer weights

    # Compute squared differences and apply weights
    differences = (user_preferences - book_vectors) ** 2
    weighted_differences = differences * weights

    # Calculate base Euclidean distance
    base_distance = np.sqrt(np.sum(weighted_differences, axis=1))

    # ----------- Genre Similarity Adjustment -----------
    genre_penalty = np.zeros(len(filtered_books))

    if selected_genre.lower() != "no preference":
        selected_genre_lower = selected_genre.lower()

        for i, genre in enumerate(filtered_books["Genre"]):
            book_genres = [g.strip().lower() for g in genre.split("-")]
            if selected_genre_lower not in book_genres:
                match_score = sum(1 for g in book_genres if g == selected_genre_lower)
                penalty_factor = 1 - (match_score / len(book_genres))
                genre_penalty[i] = penalty_factor * 3  # Softer max genre penalty

    # Total distance includes genre penalty
    total_distance = base_distance + genre_penalty

    # ----------- Adjusted Normalization for Forgiveness -----------
    max_attr_diff = 15  # Assume broader range of possible differences
    max_attr_distance = np.sqrt(np.sum(weights * (max_attr_diff ** 2)))
    max_total_distance = max_attr_distance + 3  # Include max genre penalty

    # Convert to similarity percentage (more generous range)
    similarity_percentage = (1 - (total_distance / max_total_distance)) * 100
    similarity_percentage = np.clip(similarity_percentage, 0, 100)

    # Assign and sort
    filtered_books.loc[:, "Similarity"] = similarity_percentage
    top_books = filtered_books.sort_values("Similarity", ascending=False).head(5)

# Filter by Genre if selected
if selected_genre != "No preference":
    genre_filtered_books = filtered_books[filtered_books["Genre"] == selected_genre]
else:
    genre_filtered_books = filtered_books

# Add FontAwesome CDN to the app
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

                
# Defining function to categorize books based on data
def categorize_feature(value, feature_type):
    """
    Categorizes each feature value (e.g., Drive, Pace, Tone, etc.) into a human-readable string 
    based on its range: 1-2, 3-4, 5-6.
    """
    if feature_type == "Drive":
        if value <= 2:
            return "Very plot-driven"
        elif value <= 4:
            return "Mainly plot-driven"
        elif value <= 6:
            return "Balanced between plot and character-Driven"
        elif value <= 8:
            return "Mainly character-driven"
        else:
            return "Very character-driven"
        
    elif feature_type == "Pace":
        if value <= 2:
            return "Very slow-paced"
        elif value <= 4:
            return "Slow-paced"
        elif value <= 6:
            return "Medium-paced"
        elif value <= 8:
            return "Fast-paced"
        else:
            return "Very fast-paced"
    
    elif feature_type == "Tone":
        if value <= 2:
            return "Very solemn"
        elif value <= 4:
            return "Slightly serious or dark"
        elif value <= 6:
            return "Bittersweet/Balanced"
        elif value <= 8:
            return "Light-hearted"
        else:
            return "Very Cheerful"
    
    elif feature_type == "Pictures":
        if value <= 2:
            return "No or very few pictures"
        elif value <= 4:
            return "Few pictures"
        elif value <= 6:
            return "Some pictures"
        elif value <= 8:
            return "Many pictures"
        else:
            return "Tons of pictures"
    
    elif feature_type == "Setting":
        if value <= 2:
            return "Fully realistic"
        elif value <= 4:
            return "Mostly realistic"
        elif value <= 6:
            return "Blend of reality and fantasy"
        elif value <= 8:
            return "Quite fantastical"
        else:
            return "Very fantastical"
    else:
        return ""  # Default return for unknown feature types


# Recommendation display, with all books, book info, and bar graph.

if st.button("Get Recommendations", key="recommendations_button"): # Recommendation button
    with st.spinner("Recommendations loading..."):  # Show the spinner within the container
      
        top_books = filtered_books.nlargest(5, "Similarity") # For closest 5 books, by similarity

        if filtered_books.empty:
            st.warning("No books available in your reading range. If possible, try altering your preferences.")
        else:
            st.success("Complete!") # Success message

        # Books Displayed with Expander for Info
        for _, row in top_books.iterrows():
            # Get the categorized features for each book
            drive_category = categorize_feature(row["Drive"], "Drive")
            pace_category = categorize_feature(row["Pace"], "Pace")
            tone_category = categorize_feature(row["Tone"], "Tone")
            pictures_category = categorize_feature(row["Pictures"], "Pictures")
            setting_category = categorize_feature(row["Setting"], "Setting")

            # Display book title and create an expander for detailed information
            with st.expander(f"**{row['Title']}**", expanded=False):
                st.write(f"**Drive**: {drive_category}")
                st.write(f"**Pace**: {pace_category}")
                st.write(f"**Tone**: {tone_category}")
                st.write(f"**Pictures**: {pictures_category}")
                st.write(f"**Setting**: {setting_category}")

        # Add the short title to the DataFrame
        top_books.loc[:, "Short Title"] = top_books["Title"].apply(lambda x: textwrap.shorten(x, width=30, placeholder="..."))

        # Normalize similarity scores to a range between 0 and 1 for colormap
        norm = plt.Normalize(0, 100)

        # Define the colormap from red (low) to green (high)
        cmap = plt.cm.RdYlGn

        # Create the colors based on the similarity scores
        colors = [cmap(norm(val)) for val in top_books["Similarity"]]

        # Plot the similarity scores as a bar chart
        st.subheader("Your Matches")

        plt.figure(figsize=(10, 4))
        plt.bar(top_books["Short Title"], top_books["Similarity"], color=colors, width=0.5)

        # Customize the plot
        
        plt.ylabel("How Similar your Matches are (%)")
        plt.ylim(0, 100)  # Ensure the y-axis is from 0% to 100%

        # Set the y-ticks at increments of 10
        plt.yticks(range(0, 101, 10))
        
        # Rotate the X-axis labels      
        plt.xticks(rotation=72, ha='right', fontsize=12)

        # Display the plot
        st.pyplot(plt)
