import wikipedia


def main():
    wiki_search_input = "Placeholder"
    while wiki_search_input != "":
        try:
            wiki_search_input = input("Enter page title or search phrase: ")
            if wiki_search_input != "":
                wiki_page = wikipedia.page(wiki_search_input)
                print("Title - {}\nSummary - {}\nUrl - {}".format(wiki_page.title, wikipedia.summary(wiki_search_input), wiki_page.url))
            else:
                pass
        except wikipedia.exceptions.DisambiguationError as e:
            print("Search was not specific enough. Consider searching for a result from the following options:\n", e.options)
    print("Thank you for your time.")


main()
