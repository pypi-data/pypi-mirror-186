from __future__ import annotations
import streamlit as st
import datetime
from ..backend import Source
from ..backend.stats import get_last_month_date, get_scores


def get_stats() -> tuple[tuple[float, float, int], tuple[int, int]]:
    today = datetime.date.today()
    last_month = get_last_month_date(today)
    scores = get_scores(st.session_state.stats, last_month)
    current_streak = st.session_state.db.metadata["stats"]["current_streak"]
    previous_streak = st.session_state.db.metadata["stats"]["previous_streak"]
    streaks = (previous_streak, current_streak)
    return scores, streaks


def select_cards() -> None:
    if "stat_sources" not in st.session_state:
        st.session_state.stat_sources: list[Source] = list()
    if "stats" not in st.session_state:
        st.session_state.stats = None
    titles = list(st.session_state.db.metadata["sources"].keys())
    st.caption(
        "If the *tags* multiselect is not empty, the *references* multiselect will be ignored."
    )
    left, right = st.columns(2)
    are_tags_used = (
        "stat_cards_by_tags" in st.session_state and len(st.session_state.stat_cards_by_tags) > 0
    )
    with left:
        cards_by_references = st.multiselect(
            "By references", titles, disabled=are_tags_used, key="stat_cards_by_references"
        )
    with right:
        st.multiselect("By tags", ["tag1", "tag2"], key="stat_cards_by_tags")  # cards_by_tags
        # TODO: implements cards by tags
    left, right = st.columns(2)
    select_all = left.checkbox("Select all sources", value=True)
    if select_all:
        cards_by_references = titles
    if len(cards_by_references) == 0:
        return
    sources = [st.session_state.db.load_source(title) for title in cards_by_references]
    stats = dict()
    num_cards = 0
    for source in sources:
        nodes = list(filter(lambda x: len(x.cards) > 0, source.tree.nodes))
        num_cards += len(nodes)
        stats[source.title] = {
            node.name: {card.title: card.stats for card in node.cards} for node in nodes
        }
    st.session_state.stat_sources = sources
    st.session_state.stats = stats
    with right:
        st.write("Number of cards selected: ", num_cards)
    st.write("___")


def display_stats() -> None:
    if st.session_state.stats is None:
        return
    scores, streaks = get_stats()
    previous_score, last_month_score, last_training = scores
    score_delta = last_month_score - previous_score
    previous_streak, current_streak = streaks
    streak_delta = current_streak - previous_streak
    st.write("### Last month")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average score", last_month_score, score_delta)
    col2.metric("Longest streak", current_streak, streak_delta)
    col3.metric("Training", last_training)


def stats_tab() -> None:
    st.header("Statistics")
    select_cards()
    display_stats()
