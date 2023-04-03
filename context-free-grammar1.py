def is_valid_word(grammar, start_symbol, word):
    """
    Returns True if the given word is valid according to the given grammar and start symbol, False otherwise
    """
    def parse_nonterminal(nonterminal, index, visited):
        """
        Recursive function that parses the given nonterminal symbol starting at the given index in the word
        """
        if (nonterminal, index) in visited:
            # If we've already visited this nonterminal at this index, we can stop parsing to avoid infinite loops
            return False, index

        visited.add((nonterminal, index))

        if index == len(word):
            # If we've reached the end of the word, we can only match the empty string if the nonterminal can derive it
            return ("" in grammar[nonterminal]), index

        # Try each production for the nonterminal and see if any of them succeed
        for production in grammar[nonterminal]:
            # For each symbol in the production, try to parse it starting at the current index
            symbol_index = index
            for symbol in production:
                if symbol in grammar:
                    # If the symbol is a nonterminal, recursively parse it
                    symbol_parsed, symbol_index = parse_nonterminal(symbol, symbol_index, visited.copy())
                    if not symbol_parsed:
                        # If the symbol couldn't be parsed, move on to the next production
                        break
                else:
                    # If the symbol is a terminal, try to match it with the current character in the word
                    if symbol_index < len(word) and word[symbol_index] == symbol:
                        symbol_index += 1
                    else:
                        break
            else:
                # If we successfully parsed all symbols in the production, return True
                return True, symbol_index

        # If we've tried all productions and none of them succeeded, return False
        return False, index

    # Call the parsing function for the start symbol and check if it successfully parsed the whole word
    return parse_nonterminal(start_symbol, 0, set())[0]

# Example usage
grammar = {
    "S": [["A", "B"]],
    "A": [["a", "A", "A"], ["a", "A"], ["a"]],
    "B": [["b", "B"], ["b"]]
}

start_symbol = "S"

word = input("Enter a word: ")
if is_valid_word(grammar, start_symbol, word):
    print(f"{word} is a valid word according to the grammar.")
else:
    print(f"{word} is not a valid word according to the grammar.")
