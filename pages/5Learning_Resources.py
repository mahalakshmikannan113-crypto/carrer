import streamlit as st

st.title("📚 Learning Resources")

st.write("Choose a subject and learn step by step.")

subjects = {
    "☕ Java": [
        ("Topic 1: Java Basics",
         "Introduction to Java, variables, data types, and basic syntax."),
        ("Topic 2: Conditions & Loops",
         "Learn if-else, switch, for loop, while loop, and do-while loop."),
        ("Topic 3: Arrays & Strings",
         "Learn arrays, string operations, and common problems."),
        ("Topic 4: Methods",
         "Learn how to create and use methods in Java."),
        ("Topic 5: OOP",
         "Learn classes, objects, inheritance, polymorphism, and encapsulation.")
    ],

    "🐍 Python": [
        ("Topic 1: Python Basics",
         "Learn Python syntax, variables, data types, and basic input/output."),
        ("Topic 2: Conditions & Loops",
         "Learn if-else statements, for loops, and while loops."),
        ("Topic 3: Functions",
         "Learn how to create and use functions in Python."),
        ("Topic 4: Lists & Dictionaries",
         "Learn Python lists, tuples, sets, and dictionaries."),
        ("Topic 5: Modules",
         "Learn how to use modules and libraries in Python.")
    ],

    "💻 C Programming": [
        ("Topic 1: C Basics",
         "Learn C syntax, variables, data types, and basic input/output."),
        ("Topic 2: Conditions & Loops",
         "Learn if-else, switch, for, while, and do-while."),
        ("Topic 3: Arrays",
         "Learn one-dimensional and two-dimensional arrays."),
        ("Topic 4: Functions",
         "Learn how to create and call functions in C."),
        ("Topic 5: Pointers",
         "Learn the basic concept and use of pointers.")
    ],

    "🌐 HTML & CSS": [
        ("Topic 1: HTML Basics",
         "Learn HTML structure, tags, headings, paragraphs, and links."),
        ("Topic 2: Forms & Tables",
         "Learn how to create forms and tables using HTML."),
        ("Topic 3: CSS Basics",
         "Learn CSS selectors, properties, fonts, and backgrounds."),
        ("Topic 4: Layout",
         "Learn Flexbox, Grid, margins, padding, and positioning."),
        ("Topic 5: Responsive Design",
         "Learn how to make websites work on different screen sizes.")
    ],

    "🧱 OOP": [
        ("Topic 1: Classes & Objects",
         "Learn the basic concepts of classes and objects."),
        ("Topic 2: Constructors",
         "Learn how constructors are used to initialize objects."),
        ("Topic 3: Encapsulation",
         "Learn how to protect data using encapsulation."),
        ("Topic 4: Inheritance",
         "Learn how one class can inherit properties and methods from another."),
        ("Topic 5: Polymorphism",
         "Learn method overloading and method overriding.")
    ],

    "🗄️ SQL": [
        ("Topic 1: SQL Basics",
         "Learn databases, tables, rows, columns, and basic SQL."),
        ("Topic 2: SELECT & WHERE",
         "Learn how to retrieve and filter data."),
        ("Topic 3: INSERT, UPDATE & DELETE",
         "Learn how to add, modify, and remove database records."),
        ("Topic 4: JOIN",
         "Learn how to combine data from multiple tables."),
        ("Topic 5: GROUP BY",
         "Learn grouping, aggregate functions, and basic data analysis.")
    ],

    "🤖 Machine Learning": [
        ("Topic 1: Introduction to ML",
         "Learn what machine learning is and how it works."),
        ("Topic 2: Data Preparation",
         "Learn about datasets, cleaning, and preparing data."),
        ("Topic 3: Supervised Learning",
         "Learn classification and regression concepts."),
        ("Topic 4: Unsupervised Learning",
         "Learn clustering and pattern discovery."),
        ("Topic 5: ML Projects",
         "Learn how to build a simple machine learning project.")
    ]
}

subject = st.selectbox(
    "Choose a subject",
    list(subjects.keys())
)

topics = subjects[subject]

topic_key = f"topic_{subject}"

if topic_key not in st.session_state:
    st.session_state[topic_key] = 0

current = st.session_state[topic_key]

title, content = topics[current]

st.divider()

st.header(title)
st.write(content)

st.write(f"Topic {current + 1} of {len(topics)}")

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Previous"):
        if current > 0:
            st.session_state[topic_key] -= 1
            st.rerun()

with col2:
    if st.button("Next Topic ➡️"):
        if current < len(topics) - 1:
            st.session_state[topic_key] += 1
            st.rerun()

if current == len(topics) - 1:
    st.success("🎉 You completed this learning path!")