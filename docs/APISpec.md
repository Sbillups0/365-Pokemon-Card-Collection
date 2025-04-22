API Specification
1. Get Pack Catalog
   - Returns a catalog list of currently offered packs. Includes information related to quantity, name, and cost.
   - i.e. Get Pack Catalog ---> Grass_Pack (5): 20 Coins, Water_Pack (5): 20 Coins
2. Get Collection(user_id, Type: Optional addition, if not included, will return entire collection)
   - Returns a list of the user's card collection based on their provided user_id. (Along with associated information, like total cost)
   - If extra information is included in the proper structure, it returns a subset of the user's collection. (Type: Water Pokemon)
   - i.e. Get Collection(bob, Grass) ---> [Venusaur, Celibee, Rowlett]
3. Get Card(card_name)
   - Returns information related to the card_name passed into the endpoint. (Type, Cost, Pack)
   - i.e. Get Card(Charizard) ---> Charizard (50): Fire, Fire_Pack
4. Display/Put Card(user_id, card_name)
   - Adds a card to the user's display if they have space and have it in their collection.
5. Sell All Cards(user_id, Price: Optional addition, if not included, will sell all cards)
   - Sells entire collection, adding coins to the user's inventory
   - Additional information passed can be used to sell below a certain price threshold. (Sell_All_Cards(100) -> Sell all cards less than 100 coins)
6. Sell Card(user_id, card_name)
   - Sells an individual card based on the provided card_name, adding coins to the user's inventory. (As long as the user has one in their collection)
7. Create/Put Deck(user_id, card_name[5])
   - Creates a deck based on the provided list of card_names, adding it to user's deck collection. (Must include at 5 cards in a deck)
8. View/Get Decks(user_id)
   - Returns a list of the user's current decks. (Users may have no more than 3 decks total)
9. Buy Pack(user_id, pack_name)
   - Adds pack to user_id's inventory, subtracting the corresponding coin cost.
10. Open Card Pack(user_id, pack_name)
   - Returns a list of 5 cards, adding them to the user's collection and subtracting the pack's coin cost. The cards are pulled randomly based on the provided pack_name.
   - i.e. Get Card Pack(bob, Grass) ---> [Oddish, Rowlett, Shaymin, Snivy, Leafeon EX]
11. Battle(user_id, deck_name)
   - As long as the user provides a valid deck_name, a text message describing the battle is returned. The user may gain gold based on the results of the battle. (Higher deck value = Better odds)
   - i.e. Battle(Bob, Grass) ---> "you got demolished, sucks to suck. No gold gained"
   - i.e. Battle(Bob, Pay2Win) ---> "Lightwork, gained 50 gold"
12. Get Inventory(user_id)
   - Returns list of packs in the user's inventory, along with their quantities.
   - i.e. Get Inventory(bob) ---> [Grass(5), Water(2), Fire(7)] 


