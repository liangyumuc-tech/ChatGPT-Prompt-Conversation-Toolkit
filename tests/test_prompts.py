from chatgpt_toolkit.prompts import Prompt, PromptManager


def test_prompt_render():
    prompt = Prompt(
        name="translate",
        template="Translate this text into {language}: {text}",
        variables=["language", "text"],
    )

    result = prompt.render(
        language="German",
        text="Hello",
    )

    assert result == "Translate this text into German: Hello"


def test_prompt_manager_add_and_get():
    manager = PromptManager()

    prompt = Prompt(
        name="test",
        template="Hello {name}",
        variables=["name"],
    )

    manager.add(prompt)

    assert manager.get("test") is prompt


def test_prompt_manager_list():
    manager = PromptManager()

    manager.add(
        Prompt(
            name="z_prompt",
            template="Z",
        )
    )

    manager.add(
        Prompt(
            name="a_prompt",
            template="A",
        )
    )

    assert manager.list() == ["a_prompt", "z_prompt"]


def test_prompt_manager_render():
    manager = PromptManager()

    manager.add(
        Prompt(
            name="greeting",
            template="Hello {name}!",
            variables=["name"],
        )
    )

    result = manager.render(
        "greeting",
        name="Daniel",
    )

    assert result == "Hello Daniel!"


def test_missing_variable():
    prompt = Prompt(
        name="test",
        template="Hello {name}",
        variables=["name"],
    )

    try:
        prompt.render()
        assert False
    except ValueError as error:
        assert "name" in str(error)


def test_remove_prompt():
    manager = PromptManager()

    manager.add(
        Prompt(
            name="test",
            template="Test",
        )
    )

    manager.remove("test")

    assert manager.list() == []
