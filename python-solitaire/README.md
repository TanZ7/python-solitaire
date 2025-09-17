# Python Terminal Solitaire

A classic Klondike Solitaire game playable entirely within your terminal. This project is built with Python and features a clean, color-coded text interface with card icons.

## Features

-   **Classic Klondike Rules:** Implements the standard rules of Klondike Solitaire.
-   **Text-Based Interface:** Clean and organized display using icons (♠♥♦♣) and colors for red/black suits.
-   **Complete Card Movement:**
    -   Move single cards (from Waste to Tableau/Foundation, Tableau to Foundation).
    -   Move stacks of cards between Tableau piles.
-   **Core Game Mechanics:**
    -   Draw from the Stock pile.
    -   Automatically flips face-down cards in the Tableau.
    -   Resets the Stock pile from the Waste pile when empty.
-   **Win Detection:** The game automatically detects when you have won and displays a victory message.

## Requirements

-   Python 3.x

## How to Run

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd python-solitaire
    ```

2.  **(Optional but Recommended) Create and activate a virtual environment:**
    -   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Run the game:**
    ```sh
    python -m src.main
    ```

## How to Play

The game is controlled by typing commands into the terminal.

### Pile Naming

-   **Tableau Piles:** `t1`, `t2`, `t3`, `t4`, `t5`, `t6`, `t7`
-   **Foundation Piles:** `f1`, `f2`, `f3`, `f4`
-   **Waste Pile:** `w` or `waste`

### Commands

-   **Draw a card:**
    ```
    d
    ```
-   **Move a single card:**
    -   Format: `move [from_pile] [to_pile]`
    -   Example: `move w t5` (Move from Waste to Tableau 5)
    -   Example: `move t1 f1` (Move from Tableau 1 to Foundation 1)

-   **Move a stack of cards:**
    -   Format: `move [from_pile] [num_cards] [to_pile]`
    -   Example: `move t2 3 t6` (Move 3 cards from Tableau 2 to Tableau 6)

-   **Quit the game:**
    ```
    q
    ```
