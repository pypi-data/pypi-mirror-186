import streamlit as st
from ..backend.card import CardTagException


def request_parsing() -> None:
    if "parsing_requested" not in st.session_state:
        st.session_state["parsing_requested"] = True


def request_adding() -> None:
    if "adding_requested" not in st.session_state:
        st.session_state["adding_requested"] = True


def request_source_removing(title: str) -> None:
    if "title_to_remove" not in st.session_state:
        st.session_state["title_to_remove"] = title


def request_tag_removing(tag: str) -> None:
    if "tag_to_remove" not in st.session_state:
        st.session_state["tag_to_remove"] = tag


def parse_if_requested() -> None:
    if "parsing_requested" not in st.session_state:
        return
    if "source" not in st.session_state and st.session_state.file is not None:
        try:
            st.session_state["source"] = st.session_state.db.make_source_from_file(
                st.session_state.file
            )
        except CardTagException as e:
            if "card_tag_exception" not in st.session_state:
                st.session_state.card_tag_exception = e
        del st.session_state.parsing_requested
    if "added" in st.session_state:
        del st.session_state.added


def add_if_requested() -> None:
    if "adding_requested" not in st.session_state:
        return
    st.session_state.db.add_source(st.session_state.source)
    del st.session_state.source
    del st.session_state.adding_requested
    if "added" not in st.session_state:
        st.session_state["added"] = True
    st.experimental_rerun()


def remove_title_if_requested() -> None:
    if "title_to_remove" not in st.session_state:
        return
    st.session_state.db.remove_source(st.session_state.title_to_remove)
    del st.session_state.title_to_remove
    del st.session_state.db
    if "added" in st.session_state:
        del st.session_state.added
    st.experimental_rerun()


def remove_tag_if_requested() -> None:
    if "tag_to_remove" not in st.session_state:
        return
    for metadata in st.session_state.db.metadata["sources"].values():
        if st.session_state.tag_to_remove in metadata["tags"]:
            metadata.pop(metadata.index(st.session_state.tag_to_remove))
    del st.session_state.tag_to_remove
    st.experimental_rerun()


def check_duplicates() -> bool:
    return "source" in st.session_state and st.session_state.db.source_exists(
        st.session_state.source
    )


def add_tag() -> None:
    if len(st.session_state.new_tag) > 0 and (
        st.session_state.new_tag not in st.session_state.new_tags
    ):
        st.session_state.new_tags.append(st.session_state.new_tag)


def display_if_parsed() -> None:
    if "source" not in st.session_state:
        return
    if "card_tag_exception" in st.session_state:
        st.error(f"""
            There was an error while parsing your .tex file's cards:
            {st.session_state.card_tag_exception}
        """)
    st.write("""
    **Bellow is the result of the .tex parsing.
    If it is correct, you can validate it to add the content to your sources database.**
    """)
    st.write("___")
    st.write(f"**Title**: {st.session_state.source.title}")
    with st.expander("Tree structure"):
        st.write(st.session_state.source.tree.structure)
    st.write("___")


def success_if_added() -> None:
    if "added" not in st.session_state:
        return
    st.success("Source added.")


# _______________________________________________________________________________________________ #

def current_sources() -> None:
    st.subheader("Current sources")
    with st.expander("Click to expand"):
        st.caption("Removed sources metadata are kept on disk and can be recover.")
        for title in st.session_state.db.metadata["sources"].keys():
            left, right = st.columns([5, 1])
            left.write(f"**{title}**")
            right.button(
                "Remove", on_click=request_source_removing, args=(title, ), key="remove_tag"
            )


def current_tags() -> None:
    tags = list()
    for metadata in st.session_state.db.metadata["sources"].values():
        tags.extend(metadata.get("tags", []))
    st.subheader("Current tags")
    with st.expander("Click to expand"):
        for tag in tags:
            left, right = st.columns([5, 1])
            left.write(f"**{tag}**")
            right.button("Remove", on_click=request_tag_removing, args=(tag, ))


def add_source_panel() -> None:
    st.write("___")
    st.subheader("Add source")
    st.file_uploader("Select .tex file", type="tex", key="file", on_change=request_parsing)


def add_tag_panel() -> None:
    if "source" not in st.session_state:
        return
    if "new_tags" not in st.session_state:
        st.session_state.new_tags = list()
    tags = list()
    for metadata in st.session_state.db.metadata["sources"].values():
        tags.extend(metadata.get("tags", []))
    tags.extend(st.session_state.new_tags)
    st.subheader("Add tags to your source")
    with st.expander("Add Tags"):
        st.write("Tags can be used to select flash cards for training or stats display.")
        st.multiselect("Existing tags", tags, default=st.session_state.new_tags)
        st.text_input("New tag", max_chars=50, on_change=add_tag, key="new_tag")
        st.caption("Press Enter to validate new tag")


def add_button() -> None:
    if "source" not in st.session_state:
        return
    button_str = "Add source"
    if check_duplicates():
        st.warning("""
            Duplicate source detected. The source you uploaded is already in the database.
            If you add it anyway, it will replace the existing one.
            Your current stats will be kept.
            This should be done mostly for updating a source.
        """)
        button_str = "Update source"
    st.button(button_str, on_click=request_adding)


def sources_tab():
    current_sources()
    current_tags()
    remove_title_if_requested()
    remove_tag_if_requested()
    add_source_panel()
    parse_if_requested()
    display_if_parsed()
    add_tag_panel()
    add_button()
    add_if_requested()
    success_if_added()
