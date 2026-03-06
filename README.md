# 📁 Discount Calculator

A Python function that calculates the final price of an item after applying a percentage discount — with full input validation.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project was built to reinforce conditional statements and logical operators in Python. The function takes a price and a discount percentage, validates both inputs thoroughly, and returns the final price after the discount is applied. Edge cases like zero prices, full 100% discounts, and nonnumeric inputs are all handled.

## 🧠 What I Learned

- **`isinstance()` with multiple types** — Checking that inputs are either int or float by passing a tuple of types: `isinstance(price, (int, float))`
- **Chained `elif` conditions** — Structuring a validation chain so that each check only runs if the previous one passed, keeping the logic clean and readable
- **Logical operators** — Using `or` to catch both ends of an invalid range in a single condition: `discount < 0 or discount > 100`
- **Returning early with error messages** — Returning a descriptive string from each invalid branch rather than raising an exception, making the function easy to use and test
- **Floating point inputs** — Testing with values like `74.5` and `20.0` to confirm the function handles decimals correctly alongside whole numbers

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x   | Core Language |

## 💡 How It Works

`applyDiscount(price, discount)` validates both inputs then calculates:
```
discount_amount = price × (discount / 100)
final_price     = price - discount_amount
```

**Example Output:**
```
applyDiscount(100, 20)   → 80.0
applyDiscount(200, 50)   → 100.0
applyDiscount(50, 0)     → 50.0
applyDiscount(100, 100)  → 0.0
applyDiscount(74.5, 20.0) → 59.6
```

## 🚀 Future Improvements

- [ ] Add support for multiple discount tiers (e.g. loyalty discounts stacked on sale prices)
- [ ] Round the output to 2 decimal places to match real currency formatting
- [ ] Write unit tests with pytest to cover all valid and invalid input combinations
- [ ] Extend into a small shopping cart calculator that applies discounts across multiple items

## 📂 Project Structure

```
discount-calculator/
│
├── P2DiscountCalculator.py    # applyDiscount function and test calls
└── README.md
```

*Part of my Python learning journey 🐍 — practising conditional statements, logical operators, and input validation*
