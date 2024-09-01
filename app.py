import streamlit as st

st.markdown(
    """
    <style>


        /* Apply moving gradient to the entire background */
        html, body, [data-testid="stAppViewContainer"], .main {
            height: 100%;
            width: 100%;
            background: linear-gradient(45deg, #234275, #172E52, #1B214E, #191A25);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
        }

        @keyframes gradientBG {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        /* Ensure the app content is visible over the gradient background */
        .stApp {
            background: transparent;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        }

        /* General fade-in effect */
        .fade-in {
            opacity: 0;
            animation: fadeInAnimation ease 2s;
            animation-fill-mode: forwards;
        }

        @keyframes fadeInAnimation {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        /* Hero section styles */
        .hero-section {
            background-image: url("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjcwZWNkcW45NWtjcDllcmxqZms4N3ppbjEyYnFxMmszbnQ1cjFkbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NNVrFKZF3s61W/giphy.webp");
            background-size: cover;
            background-position: center;
            padding: 100px;
            color: white;
            text-align: center;
            border-radius: 10px;
        }

        .hero-title {
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .hero-subtitle {
            font-size: 1.5em;
            font-weight: italic;
        }

        /* Sidebar link hover effect */
        .sidebar-link {
            font-size: 18px;
            color: white;
            text-decoration: none;
            padding: 10px;
            display: block;
            transition: background-color 0.3s, color 0.3s;
            background: linear-gradient(45deg, #43608F, #294B77, #1B214E, #191A25);
            background-size: 400% 400%;
            animation: gradientBG 5s ease infinite;
            border-radius: 5px;
        }

        .sidebar-link:hover {
            color: #FFCA28;
            text-decoration: underline;
        }

        .contact-container {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
            text-align: center;
        }
        .contact-header {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 20px;
            color: #294B77;
        }
        .contact-info {
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        .contact-info a {
            color: #43608F;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        .contact-info a:hover {
            color: #FFCA28;
            text-decoration: underline;
        }
        .contact-icon {
            font-size: 1.5em;
            margin-right: 10px;
            color: #294B77;
        }

        .View-button {
            background-color: #294B77;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .View-button:hover {
            background-color: #234275;
            color: gold;
            text-decoration: none;
        }
    </style>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var fadeElements = document.querySelectorAll('.fade-in');
        var options = {
            threshold: 0.5
        };

        var observer = new IntersectionObserver(function(entries, observer) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-visible');
                } else {
                    entry.target.classList.remove('fade-in-visible');
                }
            });
        }, options);

        fadeElements.forEach(element => {
            observer.observe(element);
        });
    });
    </script>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div id="hero" class="hero-section fade-in">
        <div class="hero-title">Trisan Jae B. Españo</div>
        <div class="hero-subtitle">From Passion to Profession</div>
    </div>
    """, unsafe_allow_html=True
)

st.write('<div id="about" class="fade-in">', unsafe_allow_html=True)
st.write("# About Me")
st.write("""
Hello, I’m Trisan Jae B. Españo, and I’m currently pursuing a Bachelor of Science in Information Technology at CIT - University. 
         My aspiration is to become a skilled IT professional and make a meaningful contribution to the IT industry.
""")
st.write("## My Journey")
st.markdown("---")

st.write("""
**2000s**: Grew up in Inayawan, Cebu City, where I lived a simple life.

**2010s**: 
- **Elementary**: Attended CBD College.
- **Junior High School**: Continued my education at Divino Amore Academy, Talisay City.
- **Senior High School**: Graduated from Cebu Institute of Technology.

**2020s**: Currently enrolled in the Bachelor of Science in Information Technology program at CIT - University.
""")
st.write('</div>', unsafe_allow_html=True)

st.write('<div id="portfolio" class="fade-in">', unsafe_allow_html=True)
st.header("Portfolio")

st.subheader("Projects")
with st.expander("Prodigi"):
    st.write("**Developed using Django and SQLite | Deployed on PythonAnywhere**")
    st.write("""
    - Built a web application that allows users to create and manage daily tasks and personal diary entries.
        - Successfully deployed on PythonAnywhere, ensuring accessibility and reliability.
        - Implemented user authentication, task categorization, and diary features.
        - Integrated the LanguageTool API for grammar checking within the diary feature, improving user-generated content quality.
    """)

    code = '''def fetchTextSuggestions(text):
    fetch("https://api.languagetool.org/v2/check", {
        method: "POST",
        body: "text=" + encodeURIComponent(text) + "&language=en-US",
        headers: {"Content-Type": ""}     
    })'''
    st.code(code, language="python")

   
    st.markdown(
            """
            <style>
            .github-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #181818;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                cursor: pointer;
            }

             .github-button:hover {
                color: #D13839;
                background-color: #1F1F1F;
            }
            </style>
            
            <a href="https://github.com/Wrecage/Prodigi" target="_blank" class="github-button" style="text-decoration: none;">View on GitHub</a>
            """, 
            unsafe_allow_html=True
        )
    st.video("https://youtu.be/k55jYfu8d5o")






    

with st.expander("Reflect Daily"):
    st.write("**Developed using React and Java Spring Boot**")
    st.write("""
    - Created a responsive task management application focused on efficient task tracking and prioritization.
        - Integrated front-end React components with a robust Spring Boot back-end to manage tasks and deadlines.
        - Designed with a user-friendly interface to enhance productivity and user engagement.
        - Created API services from Spring Boot to manage tasks and deadlines.
        - Connected API services to React components using Axios.
        - Routed components in React using React Router.
    """)
    st.markdown(
            """
            <style>
            .github-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #181818;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                cursor: pointer;
            }

             .github-button:hover {
                color: #D13839;
                background-color: #1F1F1F;
            }
            </style>
            
            <a href="https://github.com/sc-tompar/ReflectDaily" target="_blank" class="github-button" style="text-decoration: none;">View on GitHub</a>
            """, 
            unsafe_allow_html=True
        )
    st.video("https://youtu.be/xAn8SmISvjg")


with st.expander("StoryCraft"):
    st.write("**Developed using Flask | Integrated Groq API (llama3-8b-8192) for Story Generation**")
    st.write("""
    - Developed an AI-driven web application that generates creative stories based on user input.
        - Utilized the llama3-8b-8192 model from Groq API for advanced story generation, providing users with a wide variety of narrative possibilities.
    """)


    code = '''import os

    from groq import Groq

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)'''
    st.code(code, language="python")



    st.markdown(
            """
            <style>
            .github-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #181818;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                cursor: pointer;
            }

             .github-button:hover {
                color: #D13839;
                background-color: #1F1F1F;
            }
            </style>
            
            <a href="https://github.com/Wrecage/StoryCraft" target="_blank" class="github-button" style="text-decoration: none;">View on GitHub</a>
            """, 
            unsafe_allow_html=True
        )
    st.video("https://youtu.be/z11iDqZyhgc")


with st.expander("Social Sphere"):
    st.write("**Developed using Django and PostgreSQL | Deployed on PythonAnywhere**")
    st.write("""
    - Designed a comprehensive social media management platform enabling users to schedule posts, and analyze engagement metrics.
        - Deployed on PythonAnywhere for online access and configured with a PostgreSQL database hosted on Railway for efficient data management and storage.
        - Successfully integrated Facebook Meta Developer APIs to automate posts directly from the website to a Facebook page, streamlining social media management for users.    
    """)

    st.markdown("### Facebook Graph API URLs Used")
    code = '''https://graph.facebook.com/v21.0/{}/photos
https://graph.facebook.com/v21.0/{}/insights
https://graph.facebook.com/v21.0/{}/posts
    '''
    st.code(code, language="python")

    st.markdown(
            """
            <style>
            .github-button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #181818;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                cursor: pointer;
            }

             .github-button:hover {
                color: #D13839;
                background-color: #1F1F1F;
            }
            </style>
            
            <a href="https://github.com/Wrecage/SocialSphere" target="_blank" class="github-button" style="text-decoration: none;">View on GitHub</a>
            """, 
            unsafe_allow_html=True
        )
    st.video("https://youtu.be/WI2VbaL3_dc")




    

st.markdown("---")
st.write('</div>', unsafe_allow_html=True)

st.write('<div id="skills" class="fade-in">', unsafe_allow_html=True)
st.header("Skills")

st.subheader("Technical Skills")
skill_proficiency = {
    "Python (Django)": 90,
    "Java": 80,
    "C":70,
    "C++":60,
    "React": 80,
    "Spring Boot": 75,
    "Flask": 70,
    "HTML/CSS/JavaScript": 90,
    "MySQL/PostgreSQL/SQLite": 70,
    "Cloud Platforms (PythonAnywhere, Railway)": 90,
    "API Integration": 80,
    "System Administration (Group Policies, Virtual Machines)": 65
}

for skill, proficiency in skill_proficiency.items():
    st.write(f"{skill}")
    st.progress(proficiency / 100)

st.subheader("Soft Skills")
soft_skills = [
    "Strong problem-solving abilities",
    "Effective communication",
    "Team collaboration",
    "Time management",
    "Adaptability to new technologies"
]

for skill in soft_skills:
    st.write(f"- {skill}")

st.write('</div>', unsafe_allow_html=True)

st.write('<div id="contact-me" class="fade-in">', unsafe_allow_html=True)
st.subheader("Contact Me")
st.markdown(
    """
    <div class="contact-info">
        <i class="contact-icon">📧</i><a href="mailto:baculivenje@gmail.com" style="text-decoration: none;">baculivenje@gmail.com</a>
    </div>
    """, unsafe_allow_html=True
)

# Display Phone Number
st.markdown(
    """
    <div class="contact-info">
        <i class="contact-icon">📞</i><a href="tel:+639155634149" style="text-decoration: none;">0915 563 4149</a>
    </div>
    """, unsafe_allow_html=True
)

resume_url = "https://drive.google.com/file/d/176J_aaAvYpuP4XIjZaruUHJszBrRy4-t/view?usp=sharing"
st.markdown(
    f"""
    <a href="{resume_url}" class="View-button" View="Espano_Resume.pdf">View My Resume</a>
    """,
    unsafe_allow_html=True
)


st.write('</div>', unsafe_allow_html=True)

st.sidebar.markdown('<a href="#hero" class="sidebar-link" style="text-decoration: none;">📙 Autobiography</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#portfolio" class="sidebar-link" style="text-decoration: none;">💼 Portfolio</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#skills" class="sidebar-link" style="text-decoration: none;">🔧 Skills</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#contact-me" class="sidebar-link" style="text-decoration: none;">📩 Contact Me</a>', unsafe_allow_html=True)