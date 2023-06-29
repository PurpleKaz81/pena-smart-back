from utilities import qualifiers

def calculate_qualifier_years_total(qualifiers):
    sorted_qualifiers = sorted(qualifiers, key=lambda x: x['id'])

    additional_years = (len(sorted_qualifiers) - 1) * 1.5 if len(sorted_qualifiers) > 1 else 0
    for index, qualifier in enumerate(sorted_qualifiers):
        qualifier['years'] = 0 if index == 0 else 1.5

    total_years = additional_years

    base_sentence = 6
    if len(sorted_qualifiers) == 1:
        base_sentence = 12
    elif len(sorted_qualifiers) > 1:
        base_sentence = 12 + additional_years

    return {
        'checkedQualifiers': sorted_qualifiers,
        'totalYears': total_years,
        'baseSentence': base_sentence
    }
