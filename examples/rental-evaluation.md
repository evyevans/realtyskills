# Example: checking rental cash flow

**Skill:** [Rental Property Evaluation](../skills/deals-and-investment-analysis/rental-property-underwriting-model/SKILL.md)

All figures are fictional USD scenarios for a US property. This is arithmetic practice, not an investment recommendation or a market benchmark.

## Input

| Item | Assumption |
|---|---:|
| Purchase price | USD 300,000 |
| Monthly rent | USD 2,500 |
| Vacancy and credit loss | 5% of scheduled rent |
| Annual property taxes | USD 3,600 |
| Annual insurance | USD 1,200 |
| Annual maintenance expense | USD 1,500 |
| Management fee | 8% of collected rent |
| Owner-paid utilities and HOA | USD 0 |
| Annual capital reserve, outside NOI | USD 1,500 |
| Loan principal | USD 225,000 |
| Loan rate and amortization | 6% nominal annual rate; 30 years; monthly payments |
| Initial cash invested | USD 75,000 down payment + USD 6,000 closing costs |

## Illustrative output

| Calculation | Result |
|---|---:|
| Scheduled annual rent: 2,500 × 12 | USD 30,000 |
| Vacancy loss: 30,000 × 5% | USD 1,500 |
| Effective gross income | USD 28,500 |
| Management: 28,500 × 8% | USD 2,280 |
| Operating expenses: 3,600 + 1,200 + 1,500 + 2,280 | USD 8,580 |
| Net operating income (NOI): 28,500 − 8,580 | USD 19,920 |
| Cap rate: NOI / purchase price | 6.64% |
| Monthly principal and interest | USD 1,348.99 |
| Annual debt service, using unrounded monthly payment | USD 16,187.86 |
| Debt service coverage ratio (DSCR): NOI / debt service | 1.23 |
| Annual cash flow after debt and capital reserve | USD 2,232.14 |
| Cash-on-cash return: cash flow / 81,000 | 2.76% |

The payment uses `principal × monthly_rate / (1 − (1 + monthly_rate)^−360)`. This US loan convention is not a universal mortgage calculation convention. Taxes, financing, maintenance, rent, and vacancy must be checked for the actual property.

## Downside scenario

At 10% vacancy, effective income becomes USD 27,000, management USD 2,160, and NOI USD 18,540. Annual cash flow after debt and the same reserve falls to USD 852.14. This demonstrates sensitivity to one assumption, not the full investment risk.

## Review

Keep NOI, financing costs, and capital reserves distinct. Use full precision for calculations and round displayed results. Verify lender underwriting definitions, financing terms, local taxes, all operating costs, and capital needs before relying on a model. No appreciation or tax benefit is assumed here.
