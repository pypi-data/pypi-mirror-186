import streamlit as st
from texflash.backend import Database
from texflash.frontend import sources_tab, cards_tab, stats_tab


def main() -> None:
    if "db" not in st.session_state:
        st.session_state.db = Database()
    st.set_page_config(page_title="TexToFlashcard", layout="centered")
    st.title("Tex to FlashCard")
    left, mid, right = st.tabs(["Sources", "Cards", "Stats"])
    with left:
        sources_tab()
    with mid:
        cards_tab()
    with right:
        stats_tab()


if __name__ == "__main__":
    main()
