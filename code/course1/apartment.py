from typing import List, Optional, Dict, Any, Tuple


class Apartment:
    def update_apartment_name(
        building: List[List[int]], floor: int, unit: int, name: str
    ) -> str:
        building[floor][unit] = name
        return building

    def find_unoccupied_apartment(building: List[List[int]]) -> Tuple[int, int]:
        empty_units = []
        for floor_index, floor in enumerate(building):
            for unit_index, name in enumerate(floor):
                if name == "":
                    return (floor_index, unit_index)
        return (-1, -1)

    def expand_building(building: List[List[int]]) -> List[List[int]]:
        if not building or not building[-1]:
            raise ValueError("Invalid building structure")

        top_floor_units = building[-1]
        top_floor_number = top_floor_units[0] // 100
        unit_count = len(top_floor_units)

        new_floor_number = top_floor_number + 1
        new_units = [new_floor_number * 100 + i for i in range(1, unit_count + 1)]

        building.append(new_units)
        return building

    def add_tenant(building: List[List[int]], new_tenant: str) -> List[List[int]]:
        first_empty_unit = None
        for floor_index, floor in enumerate(building):
            for unit_index, current_tenant in enumerate(floor):
                if current_tenant == "":
                    first_empty_unit = (floor_index, unit_index)
                    building[floor_index][unit_index] = new_tenant
                    return building

        if not first_empty_unit:
            building.append([new_tenant])

        return building
