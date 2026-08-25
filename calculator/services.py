from decimal import Decimal


# FUNKCJA OGÓLNA - REKOMENDOWANA POWIERZCHNIA
def calculate_recommended_area(
    adults,
    children,
    pets,
    remote_work,
    hobby,
    bikes,
    storage_level,
):
    minimum_area = calculate_minimum_area(
        adults=adults,
        children=children,
        storage_level=storage_level,
    )

    living_dining_area = calculate_living_dining_area(
        adults=adults,
        children=children,
    )

    kitchen_area = calculate_kitchen_area(
        storage_level=storage_level,
    )

    bedroom_area = calculate_bedroom_area(
        adults=adults,
        children=children,
    )

    bathroom_area = calculate_bathroom_area()

    work_area = calculate_work_area(
        remote_work=remote_work,
    )

    hobby_area = calculate_hobby_area(
        hobby=hobby,
    )

    bikes_area = calculate_bikes_area(
        bikes=bikes,
    )

    pet_area = calculate_pet_area(
        pets=pets,
    )

    communication_area = calculate_communication_area(
        adults=adults,
        children=children,
    )

    calculated_area = (
        living_dining_area
        + kitchen_area
        + bedroom_area
        + bathroom_area
        + work_area
        + hobby_area
        + bikes_area
        + pet_area
        + communication_area
    )

    return max(
        minimum_area,
        calculated_area,
    )


# MINIMALNA POWIERZCHNIA FUNKCJONALNA
def calculate_minimum_area(
    adults,
    children,
    storage_level,
):
    living_dining_area = Decimal("18.00")
    kitchen_area = Decimal("5.50")

    bedroom_area = calculate_minimum_bedroom_area(
        adults=adults,
        children=children,
    )

    bathroom_area = Decimal("3.20")

    communication_area = calculate_communication_area(
        adults=adults,
        children=children,
    )

    storage_adjustment = calculate_storage_adjustment(
        storage_level=storage_level,
    )

    minimum_area = (
        living_dining_area
        + kitchen_area
        + bedroom_area
        + bathroom_area
        + communication_area
        + storage_adjustment
    )

    return minimum_area


# REKOMENDOWANA LICZBA POKOI
def calculate_recommended_rooms(
    adults,
    children,
    remote_work,
):
    rooms = 1  # salon

    if adults > 0:
        rooms += 1

    if adults > 2:
        additional_adults = adults - 2

        rooms += (
            additional_adults + 1
        ) // 2

    if children > 0:
        rooms += (
            children + 1
        ) // 2

    return rooms


# DODATKOWA REKOMENDACJA POKOJU
def calculate_extra_room_recommendation(
    remote_work,
    hobby,
):
    if remote_work and hobby:
        return "Gabinet / Pokój wielofunkcyjny"

    if remote_work:
        return "Wydzielone miejsce do pracy"

    if hobby:
        return "Wydzielona strefa hobby / sportu"

    return None


# SALON
def calculate_living_room_area(adults, children):
    total_people = adults + children

    seating_area = Decimal("6.00")
    coffee_table_area = Decimal("1.20")
    tv_area = Decimal("1.00")
    storage_area = Decimal("1.50")
    communication_area = Decimal("1.50")

    if total_people > 2:
        seating_area += (
            Decimal(total_people - 2)
            * Decimal("1.20")
        )

    area = (
        seating_area
        + coffee_table_area
        + tv_area
        + storage_area
        + communication_area
    )

    return area


# JADALNIA
def calculate_dining_area(adults, children):
    total_people = adults + children

    if total_people <= 2:
        return Decimal("3.00")

    elif total_people <= 4:
        return Decimal("4.00")

    elif total_people <= 6:
        return Decimal("5.50")

    else:
        return Decimal("7.00")


# SALON + JADALNIA
def calculate_living_dining_area(adults, children):
    living_room_area = calculate_living_room_area(
        adults=adults,
        children=children,
    )

    dining_area = calculate_dining_area(
        adults=adults,
        children=children,
    )

    calculated_area = (
        living_room_area
        + dining_area
    )

    minimum_area = Decimal("18.00")

    return max(
        minimum_area,
        calculated_area,
    )


# KUCHNIA
def calculate_kitchen_area(storage_level):
    storage_zone = Decimal("1.20")
    washing_zone = Decimal("1.00")
    preparation_zone = Decimal("1.50")
    cooking_zone = Decimal("1.00")
    communication_zone = Decimal("1.50")

    if storage_level == "medium":
        storage_zone += Decimal("0.80")

    elif storage_level == "large":
        storage_zone += Decimal("1.80")

    calculated_area = (
        storage_zone
        + washing_zone
        + preparation_zone
        + cooking_zone
        + communication_zone
    )

    minimum_area = Decimal("5.50")

    return max(
        minimum_area,
        calculated_area,
    )


# MINIMALNA POWIERZCHNIA SYPIALNI
def calculate_minimum_bedroom_area(adults, children):
    area = Decimal("0.00")

    if adults == 1:
        area += Decimal("8.00")

    elif adults >= 2:
        area += Decimal("13.00")

        if adults > 2:
            area += (
                Decimal(adults - 2)
                * Decimal("8.00")
            )

    if children > 0:
        area += (
            Decimal(children)
            * Decimal("8.00")
        )

    return area


# SYPIALNIA / SYPIALNIE
def calculate_bedroom_area(adults, children):
    calculated_area = Decimal("0.00")

    if adults == 1:
        bed_area = Decimal("2.00")
        wardrobe_area = Decimal("1.50")
        access_area = Decimal("2.00")
        communication_area = Decimal("1.00")

        calculated_area += (
            bed_area
            + wardrobe_area
            + access_area
            + communication_area
        )

    elif adults >= 2:
        bed_area = Decimal("3.00")
        wardrobe_area = Decimal("2.00")
        access_area = Decimal("3.00")
        communication_area = Decimal("1.50")

        calculated_area += (
            bed_area
            + wardrobe_area
            + access_area
            + communication_area
        )

    minimum_area = calculate_minimum_bedroom_area(
        adults=adults,
        children=children,
    )

    return max(
        minimum_area,
        calculated_area,
    )


# ŁAZIENKA / WC
def calculate_bathroom_area():
    toilet_zone = Decimal("0.80")
    sink_zone = Decimal("0.70")
    bathing_zone = Decimal("1.00")
    washing_machine_zone = Decimal("0.80")
    communication_zone = Decimal("1.00")

    calculated_area = (
        toilet_zone
        + sink_zone
        + bathing_zone
        + washing_machine_zone
        + communication_zone
    )

    minimum_area = Decimal("3.20")

    return max(
        minimum_area,
        calculated_area,
    )


# PRACA ZDALNA
def calculate_work_area(remote_work):
    if not remote_work:
        return Decimal("0.00")

    desk_area = Decimal("2.00")
    chair_area = Decimal("1.00")
    access_area = Decimal("1.00")

    return (
        desk_area
        + chair_area
        + access_area
    )


# KOREKTA PRZECHOWYWANIA
def calculate_storage_adjustment(storage_level):
    if storage_level == "small":
        return Decimal("-4.00")

    elif storage_level == "large":
        return Decimal("4.00")

    return Decimal("0.00")


# SPORT / HOBBY
def calculate_hobby_area(hobby):
    if not hobby:
        return Decimal("0.00")

    return Decimal("3.00")


# ROWERY
def calculate_bikes_area(bikes):
    if bikes == 0:
        return Decimal("0.00")

    return (
        Decimal(bikes)
        * Decimal("1.20")
    )


# ZWIERZĘTA
def calculate_pet_area(pets):
    if pets == 0:
        return Decimal("0.00")

    return (
        Decimal(pets)
        * Decimal("1.50")
    )


# OGÓLNA KOMUNIKACJA
def calculate_communication_area(adults, children):
    total_people = adults + children

    area = Decimal("1.50")

    if total_people > 2:
        area += (
            Decimal(total_people - 2)
            * Decimal("0.50")
        )

    return area


# PODZIAŁ POWIERZCHNI DLA UŻYTKOWNIKA
def calculate_area_breakdown(
    adults,
    children,
    pets,
    remote_work,
    hobby,
    bikes,
    storage_level,
):
    living_dining_area = calculate_living_dining_area(
        adults=adults,
        children=children,
    )

    kitchen_area = calculate_kitchen_area(
        storage_level=storage_level,
    )

    bedrooms_area = calculate_bedroom_area(
        adults=adults,
        children=children,
    )

    bathroom_area = calculate_bathroom_area()

    work_area = calculate_work_area(
        remote_work=remote_work,
    )

    hobby_area = calculate_hobby_area(
        hobby=hobby,
    )

    bikes_area = calculate_bikes_area(
        bikes=bikes,
    )

    pets_area = calculate_pet_area(
        pets=pets,
    )

    communication_area = calculate_communication_area(
        adults=adults,
        children=children,
    )

    storage_adjustment = calculate_storage_adjustment(
        storage_level=storage_level,
    )

    return {
        "living_dining": living_dining_area,
        "kitchen": kitchen_area,
        "bedrooms": bedrooms_area,
        "bathroom": bathroom_area,
        "work": work_area,
        "hobby": hobby_area,
        "bikes": bikes_area,
        "pets": pets_area,
        "communication": communication_area,
        "storage_adjustment": storage_adjustment,
    }