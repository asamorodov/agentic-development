# Chapter IV direct API example V7 report

## Change

The integrated Chapter IV file was edited in-place:

```text
work/theory-writing/chapters/IV_spdd_specification_lifecycle.md
```

The billing example was rewritten into a more direct technical formulation. The text now introduces the example as an API method instead of making the reader reconstruct the task from a loose description.

## Main edits

- The example now starts from a direct engineering formulation: the system has API method `POST /usage/quote`.
- The method's purpose, inputs, output, data sources and rules are named directly.
- The paragraph no longer asks the reader to infer the implementation scenario from the phrase "calculate model usage cost".
- `fallback-тариф` was replaced with `тариф по умолчанию`.
- The SPDD cycle paragraph now says more directly that `/spdd-reasons-canvas` turns the loose task into a specification of that API method.

## Rationale

Technical examples in the theory text should be as direct as possible. The reader should not have to reconstruct the task from scattered hints before understanding how the example moves through Canvas, generation, tests, review, `prompt-update` and `sync`.
