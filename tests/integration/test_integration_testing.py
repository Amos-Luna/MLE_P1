import pytest
from processing import (remove_links,
                        remove_hastags,
                        remove_numbers,
                        remove_users,
                        process_lemmatization,
                        process_stemming
                    )

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("cats and dogs are playing in the garden", "cat and dog are play in the garden"),
    ("the weather is getting colder", "the weather is get colder"),
    ("running shoes are important for runners", "run shoe are import for runner"),
])
def test_process_stemming_and_lemmatization(input_text, expected_output):
    processed_text = process_stemming(process_lemmatization(input_text))
    assert processed_text == expected_output