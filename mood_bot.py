import streamlit as st
import random

def main():
    st.title("Mood Booster Bot")

    name = st.text_input("What is your name?")

    if name:
        mood = st.radio(
            f"Hello, {name}!, How are you today?",
            ("Fine", "Not fine"),
        ).lower()  # Convert to lowercase for consistency

        if mood == "fine":
            st.write(f"I am glad to hear that you're fine, enjoy the rest of your day.")
        elif mood == "not fine":
            st.write("I am sorry to hear that, is there anything I can do to help?")
            choice = st.radio(
                "Pick an option:",
                (
                    "Suggest a nice song for me to listen to",
                    "Recommend an encouraging bible verse",
                    "Re-affirm me",
                    "I just need some quiet time",
                ),
            )
            if st.button("Get Response"):
                if choice == "Suggest a nice song for me to listen to":
                    songs = [
                        "Walking on Sunshine by Katrina & The Waves",
                        "Happy by Pharrell Williams",
                        "Here Comes The Sun by The Beatles",
                        "Good Life by OneRepublic",
                        "Can't Stop the Feeling! by Justin Timberlake",
                        "Uptown Funk by Mark Ronson ft Bruno Mars",
                        "Stronger by Britney Spears",
                        "Golden by Harry Styles",
                    ]
                    suggestion = random.choice(songs)
                    st.write(f"How about listening to '{suggestion}'?")
                elif choice == "Recommend an encouraging bible verse":
                    verses = [
                        "Romans 8:38-39 (NIV)",
                        "Philippians 4:13 (NIV)",
                        "Psalm 23:4 (NIV)",
                        "Deuteronomy 31:6 (NIV)",
                        "Matthew 11:28 (NIV)",
                        "2 Corinthians 5:17 (NIV)",
                        "Joshua 1:9 (NIV)",
                        "Psalm 46:1 (NIV)",
                    ]
                    suggestion = random.choice(verses)
                    st.write(f"Here's an encouraging verse: {suggestion}")
                elif choice == "Re-affirm me":
                    quotes = [
                        "I am capable",
                        "I choose joy",
                        "I am worthy",
                        "I embrace growth",
                        "I am strong",
                        "I trust myself",
                        "I radiate positivity",
                        "I am enough",
                    ]
                    suggestion = random.choice(quotes)
                    st.write(f"Remember: {suggestion}")
                elif choice == "I just need some quiet time":
                    st.write(
                        "Some quiet time will do you some good, but remember I am always here if you need me."
                    )
                else:
                    st.write("Please select an option.")
        else:
            st.write("Have a nice day!")

if __name__ == "__main__":
    main()