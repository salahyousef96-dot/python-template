def main():
    print(cup_of_join([1,2],[8],[9,5,6], sep="@"))
    print(cup_of_join([1,2],[8],[9,5,6]))
    print(cup_of_join([1]))
    print(cup_of_join())


def cup_of_join(*lists, sep='-') -> list:
    """Combine multiple lists into one list with a separator """
    
    if not lists:
        return None

    result = []

    for i,lst in enumerate(lists):
        if i != 0:
            result.append(sep)


        result.extend(lst)

    return result

if __name__  ==  "__main__":
    main()
