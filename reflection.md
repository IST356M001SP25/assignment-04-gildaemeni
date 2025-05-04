# Reflection

Student Name:  Gilda Emeni
Sudent Email:  gemeni@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This assignment helped me understand how to use Streamlit with pandas to create a basic data browser. I learned how to upload a file, select which columns to show, and filter rows based on a column's value. Even though it sounds simple, putting all the parts together like st.file_uploader, st.multiselect, and st.checkbox made me really think through the flow of the app.

One thing I struggled with was trying to make my code different from the solution while still doing the exact same thing. It was tricky figuring out how to rename variables, restructure the layout, and rewrite logic in a way that passes the tests but still feels like my own. I also had a moment where df wasn’t working, and I realized it was because I wasn’t scoping it properly. That was frustrating at first but now it makes sense.

I liked that I had to write helper functions like get_file_extension() and load_file(). I used things like rsplit() and a dictionary instead of if-else, and that made my version cleaner. I also added error checks and made sure I dropped NaNs when getting unique values which are small things, but I feel like they helped me level up.

Going forward, I want to get better with Streamlit overall, like customizing layouts, handling more file types, or maybe even adding charts. I also need more practice reading documentation when I get stuck instead of guessing.

