cards = []

# Now, you need to create all 52 cards
for rank in ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"):
    for suit in ("hearts", "diamonds", "club", "spade"):
        if suit in ("hearts, diamonds"):
            cards.append(
                (rank, suit, "red")
            )
        else:
            cards.append(
                (rank, suit, "black")
            )

        # print created card
        print(cards[-1])

print(f"There are a total of {len(cards)}")