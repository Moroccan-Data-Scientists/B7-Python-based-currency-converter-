import streamlit as st

def main():
    st.title("About Us")

    # Custom CSS for styling
    st.markdown("""
    <style>
    .team-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        width: 150px;
        height: 180px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.01);
        transition: transform 0.3s ease;
    }
    .team-card:hover {
        transform: scale(1.05);
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.05);
    }
    .team-card img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        border: 1px solid gray;
        margin-bottom: 10px;
    }
    .team-card a {
        color: gray;
        text-decoration: none;
        font-weight: thin;
    }
    .team-card a:hover {
        color: #005f73;
    }
    .huggingface-banner {
        background-color: #0a9396;
        color: white;
        padding: 10px;
        margin-top: 30px;
        text-align: center;
        border-radius: 10px;
    }
    .huggingface-banner a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .huggingface-banner img {
        height: 30px;
        margin-right: 10px;
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Welcome to Currency Converter, Your Trusted Partner in Moroccan Currency Exchange!
    At Currency Converter, we specialize in providing fast, reliable, and accurate currency conversion services specifically tailored to the Moroccan Dirham (MAD). Our platform is designed to cater to both individuals and businesses seeking to navigate the complexities of currency exchange involving MAD.
    
    ## Team:
    """, unsafe_allow_html=True)

    ## Team members GitHub usernames
    team_members = [
        ("Karmouch Adnane", "blank-mind-op"),
        ("Wiame Jouihri", "wiamejh"),
        ("Torqui Redouane", "torqui1"),
        ("Amine Boumadian", "AmineBMD1"),
        ("Bassam Mejlaoui", "mejbass"),
        ("Amine ait yaaza", "dflhqiofioqzefpiozemj"),
        ("Kara Salah Eddine", "karaone1"),
        ("Maamri redouane", "Redouane77777"),
        ("HANANE EL HILALI", "hanane-el-hilali"),
    ]

    # Create columns for team members
    cols_per_row = 4
    for i in range(0, len(team_members), cols_per_row):
        cols = st.columns(cols_per_row, gap="large")
        for j in range(cols_per_row):
            if i + j < len(team_members):
                member, id = team_members[i + j]
                avatar_url = f"https://github.com/{id}.png"
                with cols[j]:
                    st.markdown(f"""
                        <div class='team-card'>
                            <a href='https://github.com/{id}' target='_blank'>
                                <img src='{avatar_url}'/><br>{member}
                            </a>
                        </div>
                    """, unsafe_allow_html=True)

    # Hugging Face banner
    st.markdown("""
    <div class='huggingface-banner'>
        <a href='https://huggingface.co/MoroccanDS' target='_blank'>
            <img src='https://huggingface.co/front/assets/huggingface_logo.svg' alt='Hugging Face logo' />
            Visit our MoroccanDS Hugging Face Account
        </a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
