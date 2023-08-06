from __future__ import annotations
from datetime import date
import streamlit as st
from numpy.random import shuffle
from ..backend import Tree, Source, Card, display_card_content


def start_training(cards: list[Card], num_cards: int, order: str) -> None:
    if "training_in_progress" not in st.session_state:
        st.session_state.training_in_progress = True
    if "streak" not in st.session_state:
        st.session_state.streak = 0
    if order == "Random":
        shuffle(st.session_state.cards)
    st.session_state.cards = cards[:num_cards]
    if "progress" not in st.session_state:
        st.session_state.progress = 0


def quit_training() -> None:
    # update streak
    current_streak = st.session_state.db.metadata["stats"]["current_streak"]
    new_streak = max(current_streak, st.session_state.streak)
    st.session_state.db.metadata["stats"]["current_streak"] = new_streak
    st.session_state.db.metadata["stats"]["previous_streak"] = current_streak
    # reset streamlit state
    if "training_in_progress" in st.session_state:
        del st.session_state.training_in_progress
    if "training_finished" in st.session_state:
        del st.session_state.training_finished
    if "progress" in st.session_state:
        st.session_state.progress = 0
    if "streak" in st.session_state:
        st.session_state.streak = 0
    # update database stats
    for source in st.session_state.sources:
        st.session_state.db.save_source(source)


def request_answer() -> None:
    if "show_answer" not in st.session_state:
        st.session_state.show_answer = True


def next_card() -> None:
    # update stats for current card
    for result_idx in range(3):
        state_key = f"result_{result_idx}"
        if state_key in st.session_state and st.session_state[state_key]:
            break
    if result_idx == 2:
        st.session_state.streak += 1
    else:
        st.session_state.streak = 0
    current_card = st.session_state.cards[st.session_state.progress]
    if current_card.stats is None:
        current_card.stats = dict()
    today = date.today().isoformat()
    if today not in current_card.stats:
        current_card.stats[today] = list()
    current_card.stats[today].append(result_idx)
    # update training state
    st.session_state.progress += 1
    if "show_answer" in st.session_state:
        del st.session_state.show_answer
    if st.session_state.progress == len(st.session_state.cards):
        if "training_finished" not in st.session_state:
            st.session_state.training_finished = True


# _______________________________________________________________________________________________ #

def select_cards() -> None:
    if "cards" not in st.session_state:
        st.session_state.cards: list[Card] = list()
    if "sources" not in st.session_state:
        st.session_state.sources: list[Source] = list()
    titles = list(st.session_state.db.metadata["sources"].keys())
    st.subheader("Select sources")
    st.caption(
        "If the *tags* multiselect is not empty, the *references* multiselect will be ignored."
    )
    left, right = st.columns(2)
    are_tags_used = "cards_by_tags" in st.session_state and len(st.session_state.cards_by_tags) > 0
    with left:
        cards_by_references = st.multiselect("By references", titles, disabled=are_tags_used)
    with right:
        st.multiselect("By tags", ["tag1", "tag2"], key="cards_by_tags")  # cards_by_tags
        # TODO: implements cards by tags
    select_all = st.checkbox("Select all sources")
    if select_all:
        cards_by_references = titles
    if len(cards_by_references) == 0:
        return
    sources = [st.session_state.db.load_source(title) for title in cards_by_references]
    st.session_state.sources = sources
    with st.expander("Select subparts", expanded=True):
        st.caption("For now, Cards can only be filtered on one depth level.")
        delimiters = ["Part", "Section", "Subsection", "Subsubsection"]
        delimiter = st.selectbox("Delimiter", delimiters)
        selected_depth = delimiters.index(delimiter)
        st.write("___")
        for source in sources:
            st.write(f"##### {source.title}")
            subsources = list(filter(lambda x: x.depth == selected_depth, source.tree.nodes))
            subsources = [s.name for s in subsources]
            scope = st.multiselect("Cards scope", subsources)
            all_subsources = st.checkbox("Select all")
            if all_subsources:
                scope = subsources
            subtrees = list()
            for node_name in scope:
                for node in source.tree.nodes:
                    if node.name == node_name:
                        break
                subtree = Tree(node)
                subtrees.append(subtree)
            cards = list()
            for tree in subtrees:
                for node in tree.nodes:
                    cards.extend(node.cards)
            num_cards = len(cards)
            _, mid, _ = st.columns(3)
            with mid:
                st.write("Number of cards selected: ", len(cards))
                if len(cards) > 0:
                    slider_msg = "Number of cards to use for training"
                    num_cards = st.slider(slider_msg, 0, len(cards), value=len(cards))
    order = st.radio("Cards ordering", ["Follow source's structure", "Random"], horizontal=True)
    st.button(
        "Validate cards selection",
        on_click=start_training, args=(cards, num_cards, order), disabled=not num_cards
    )


def run_training() -> None:
    st.subheader("Flashcards training")
    if "training_finished" in st.session_state and st.session_state.training_finished:
        left, right = st.columns([4, 1], gap="large")
        with left:
            st.success("Training finished !")
        with right:
            st.button("Quit training", on_click=quit_training)
        return
    st.progress(st.session_state.progress / len(st.session_state.cards))
    card = st.session_state.cards[st.session_state.progress]
    with st.expander("Current Flash Card", expanded=True):
        left, right = st.columns([3, 1], gap="large")
        with left:
            st.write(f"##### {card.title}")
        # st.write("")
        _, mid, _ = st.columns(3, gap="large")
        with right:
            st.button("Show answer", on_click=request_answer)
        st.write("___")
        if "show_answer" in st.session_state and st.session_state.show_answer:
            display_card_content(card)
            st.write("___")
            msg, left, mid, right = st.columns([5, 3, 4, 3], gap="large")
            with msg:
                st.write("**Did i know it ?**")
            # _, left, mid, right, _ = st.columns([2, 1, 2, 1, 2])
            with left:
                st.button("Yes", key="result_2", on_click=next_card)
            with mid:
                st.button("Not so well", key="result_1", on_click=next_card)
            with right:
                st.button("No", key="result_0", on_click=next_card)


def cards_tab() -> None:
    st.header("Flash Cards")
    if not ("training_in_progress" in st.session_state and st.session_state.training_in_progress):
        select_cards()
    else:
        run_training()
