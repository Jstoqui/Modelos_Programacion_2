
data Suit = Club | Diamond | Heart | Spade deriving (Read, Show, Enum, Eq, Ord)
 
data CardValue = Two | Three | Four
     | Five | Six | Seven | Eight | Nine | Ten 
     | Jack | Queen | King | Ace
    deriving (Read,  Show, Enum, Eq, Ord)

data Card = Card {value :: CardValue, 
                    suit :: Suit}
    deriving (Read, Show, Eq)
    
type Deck = [Card]
 

 
deck::Deck
deck = [Card val su | val <- [Two .. Ace], su <- [Club .. Spade]]


