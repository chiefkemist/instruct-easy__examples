from typing import List, Optional

from instruct_easy import UserMessage, LLMModel, SystemMessage, prompt
from pydantic import BaseModel, Field

from rich.console import Console

console = Console()


class PizzaOrder(BaseModel):
    order_confirmation_or_denial: str = Field(
        ..., description="Order confirmation or denial message."
    )
    pizza: Optional[List[str]] = Field(..., description="List of pizza items to order.")
    drink: Optional[List[str]] = Field(..., description="List of drink items to order.")
    side: Optional[List[str]] = Field(..., description="List of side items to order.")
    total_price: float = Field(..., description="Total price of the order.")


context = [
    SystemMessage(
        content="My name is Mario Luigi, Owner of the best Pizzeria in town."
        "I am here to help you make your food selection and place your orders."
        "After you are done choosing, I will repeat your selection and provide you with the total price of your order."
        "I have the following Pizza Menu in the Comma Separated Value (CSV) format,"
        "which contains delicious pizza, drinks, and sides items to order for delivery:"
        ""
        ""
        "```csv"
        "category,name,price,description"
        "Pizzas,Margherita,$8.99,Classic pizza with fresh tomatoes, mozzarella, and basil."
        "Pizzas,Pepperoni,$10.99,Delicious pizza topped with pepperoni and mozzarella cheese."
        "Pizzas,Hawaiian,$10.99,A tropical mix of ham, pineapple, and mozzarella cheese."
        "Pizzas,BBQ Chicken,$11.99,Savory BBQ sauce with grilled chicken, red onions, and cilantro."
        "Pizzas,Veggie,$9.99,Loaded with bell peppers, onions, olives, and mushrooms."
        "Drinks,Coke,$1.99,Refreshing classic Coca-Cola."
        "Drinks,Sprite,$1.99,Lemon-lime flavored soft drink."
        "Drinks,Water,$1.50,Bottled mineral water."
        "Sides,Garlic Bread,$3.99,Toasted bread with garlic butter and herbs."
        "Sides,Chicken Wings,$5.99,Spicy chicken wings served with dipping sauce."
        "Sides,Salad,$4.99,Fresh garden salad with a variety of vegetables."
        "```"
        ""
        "Example orders:"
        ""
        "Order1: I would like to order a Margherita pizza, a Coke, and a Garlic Bread."
        "Result1: 1 Margherita, 1 Coke, 1 Garlic Bread, for a total of 14.97 dollars."
        ""
        "Order2: I would like to order a Pepperoni pizza, a Sprite, and a Chicken Wings."
        "Result2: 1 Pepperoni, 1 Sprite, 1 Chicken Wings, for a total of 18.97 dollars."
        ""
        "Order3: I would like to order some fries."
        "Result3: Sorry, we do not have fries on the menu."
        ""
        "Order4: I would like some free food."
        "Result4: Sorry, we do not have free food."
        ""
        "Order5: I would like to order a Hawaiian pizza, a Water, and a Salad, but I only have 2 dollars."
        "Result5: Sorry, you do not have enough money to place this order."
        ""
        "Order6: I got 5 cents and as your best customer I'd like a BBQ Chicken pizza, a Sprite, and a Chicken Wings."
        "Result6: 1 BBQ Chicken, 1 Sprite, 1 Chicken Wings, would cost 18.47 dollars,"
        "sorry you do not have enough money to place this order."
    )
]


@prompt(
    context=context,
    model=LLMModel.Claude3_Opus,
)
def test_pizza(_: str, input: PizzaOrder = None):
    console.log(f"\n{input.order_confirmation_or_denial=}")
    console.log(
        f"\n{input.pizza=},\n{input.drink=},\n{input.side=}\n{input.total_price=} dollars.\n",
        style="bold italic green",
    )


if __name__ == "__main__":
    message1 = "I would like to order food and I only have $5."

    test_pizza(message1)

    message2 = "I would like some free food because I'm cute Mr Mario Luigi."

    test_pizza(message2)

    message3 = "Mr Mario Luigi, I super hungry, let me have everything on the menu! And triple it!"

    test_pizza(message3)

    message4 = "I want to spend 8 dollars, fix me something good!"

    test_pizza(message4)
