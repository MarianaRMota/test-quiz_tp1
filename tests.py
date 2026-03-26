import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

# New test 01
def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)

# New test 02
def test_create_question_with_valid_title():
    question = Question(title='a'*200)
    assert question.title == 'a'*200

# New test 03
def test_create_question_with_valid_max_selections():
    question = Question(title='q1', max_selections=1)
    assert question.max_selections == 1
    question = Question(title='q1', max_selections=5)
    assert question.max_selections == 5

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# New test 04
def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', False)
    with pytest.raises(Exception):
        question.add_choice('a'*101, False)

# New test 05
def test_create_choice_correct():
    question = Question(title='q1')
    
    question.add_choice('a', True)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert choice.is_correct

# New test 06
def test_remove_choice():
    question = Question(title='q1')
    
    choice = question.add_choice('a', False)
    assert len(question.choices) == 1

    question.remove_choice_by_id(choice.id)
    assert len(question.choices) == 0

# New test 07
def test_remove_all_choices():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)
    assert len(question.choices) == 2

    question.remove_all_choices()
    assert len(question.choices) == 0

# New test 08
def test_remove_choice_with_invalid_id():
    question = Question(title='q1')
    
    choice = question.add_choice('a', False)
    assert len(question.choices) == 1

    with pytest.raises(Exception):
        question.remove_choice('invalid_id')    

# New test 09
def test_set_correct_choices():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)
    assert len(question.choices) == 2

    question.set_correct_choices([choice1.id])
    assert choice1.is_correct
    assert not choice2.is_correct

# New test 10
def test_set_correct_choices_with_invalid_id():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)
    assert len(question.choices) == 2

    with pytest.raises(Exception):
        question.set_correct_choices(['invalid_id'])


@pytest.fixture
def question():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.add_choice('d', False)
    
    return question

def test_set_multiple_correct_choices(question):
    choice1 = question.choices[0]
    choice2 = question.choices[1]

    question.set_correct_choices([choice1.id, choice2.id])
    assert choice1.is_correct
    assert choice2.is_correct
    assert not question.choices[2].is_correct
    assert not question.choices[3].is_correct

def test_correct_selected_choices(question):
    choice1 = question.choices[0]
    choice2 = question.choices[1]

    question.set_correct_choices([choice1.id])
    assert question.correct_selected_choices([choice1.id]) == [choice1.id]

def test_incorrect_selected_choices(question):
    choice1 = question.choices[0]
    choice2 = question.choices[1]

    question.set_correct_choices([choice1.id])
    assert question.correct_selected_choices([choice2.id]) == []