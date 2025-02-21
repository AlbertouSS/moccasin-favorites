from script.deploy import deploy_favorites
import pytest

@pytest.fixture
def favorites_contract():
    return deploy_favorites()

''' TEST WITHOUT FIXTURE'''
# def test_starting_values():
#     favorites_contract = deploy_favorites()
#     assert favorites_contract.retrieve() == 7
    
# def test_change_values():
#     # Arrange
#     favorites_contract = deploy_favorites()
#     # Act
#     favorites_contract.store(200)
#     # Assert
#     assert favorites_contract.retrieve() == 200    
    
# def test_add_people():
#     # Arrange
#     favorites_contract = deploy_favorites()
#     person = "Alice"
#     favorite_number = 100
#     # Act
#     favorites_contract.add_person(person, favorite_number)
#     # Assert
#     assert favorites_contract.list_of_people(0) == (favorite_number, person)

''' TEST WITH FIXTURE'''
def test_starting_values(favorites_contract):
    assert favorites_contract.retrieve() == 7
    
def test_change_values(favorites_contract):
    # Act
    favorites_contract.store(200)
    # Assert
    assert favorites_contract.retrieve() == 200
    
def test_add_people(favorites_contract):
    person = "Alice"
    favorite_number = 100
    # Act
    favorites_contract.add_person(person, favorite_number)
    # Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, person)