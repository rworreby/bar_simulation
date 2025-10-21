from bar_simulation.person import Person


def main():
    p1 = Person()
    print("Number of instances in Person:", Person.get_no_instances())
    p2 = Person()
    p3 = Person()
    print("Number of instances in Person:", Person.get_no_instances())
    del p3
    print("Number of instances in Person:", Person.get_no_instances())


if __name__ == "__main__":
    main()
