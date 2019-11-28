def to_camel_case(text):
    st = text.replace('_', '-').split('-')
    res = "".join([line.capitalize() for line in st[1:]])
    return "{}{}".format(st[0], res)


to_camel_case("the-stealth-warrior")
to_camel_case("The-Stealth-Warrior")

assert to_camel_case('') == '', "An empty string was provided but not returned"
assert to_camel_case("the_stealth-warrior") == "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value"
assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value"
assert to_camel_case("A-B-C") == "ABC", "to_camel_case('A-B-C') did not return correct value"