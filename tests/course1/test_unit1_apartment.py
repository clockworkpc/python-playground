import pytest
from code.course1.apartment import Apartment


# Update Apartment Name in Building Directory
def test_update_apartment_name():
    building = [["Alice", "Bob"], ["Carol", "Dave"]]
    updated = Apartment.update_apartment_name(building, 0, 1, "Ben")
    assert updated[0][1] == "Ben"


# Unoccupied Apartment Identifier
def test_unoccupied_apartment_identifier():
    building = [["Alice", ""], ["", "Dave"]]
    assert Apartment.find_unoccupied_apartment(building) == (0, 1)


# Expand the Digital Apartment Building
def test_expand_apartment_building():
    building = [[101, 102], [201, 202]]
    expanded = Apartment.expand_building(building)
    assert expanded[-1] == [301, 302]


# Apartment Building Management in Python
def test_apartment_management():
    building = [["Alice", ""]]
    updated = Apartment.add_tenant(building, "Bob")
    assert updated[0][1] == "Bob"


def test_manage_building_no_vacancy_add_floor():
    building = [["Anna", "Ben"], ["Cara", "Dan"]]
    updated = Apartment.add_tenant(building, "Eli")
    assert len(updated) == 3
    assert updated[2][0] == "Eli"
    assert all(cell == "" for cell in updated[2][1:])


def test_manage_building_fill_first_vacancy_only():
    building = [["", "Bob"], ["", ""]]
    updated = Apartment.add_tenant(building, "Alice")
    assert updated[0][0] == "Alice"
    assert updated[1][0] == ""
    assert updated[1][1] == ""


def test_manage_building_empty_building_initializes():
    building = []
    updated = Apartment.add_tenant(building, "Zara")
    assert len(updated) == 1
    assert updated[0][0] == "Zara"
    if len(updated[0]) > 1:
        assert all(cell == "" for cell in updated[0][1:])


def test_manage_building_fill_later_floor():
    building = [["John", "Doe"], ["", ""]]
    updated = Apartment.add_tenant(building, "Sara")
    assert updated[1][0] == "Sara"


def test_manage_building_single_full_floor_expands():
    building = [["Tom", "Jerry"]]
    updated = Apartment.add_tenant(building, "Spike")
    assert len(updated) == 2
    assert updated[1][0] == "Spike"
