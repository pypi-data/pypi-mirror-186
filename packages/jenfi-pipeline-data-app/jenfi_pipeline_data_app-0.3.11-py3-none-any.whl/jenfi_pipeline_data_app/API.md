# Jenfi Data App API

## Primary Return Functions

| Return status      | Function Call                                | Example                                            |
| ------------------ | -------------------------------------------- | -------------------------------------------------- |
| success            | `Jenfi.write_result(result: dict)`           |                                                    |
| not_applicable     | `Jenfi.exit_not_applicable(message: ...)`    | notebook designed for SG, but running a VN company |
| insufficent_data   | `Jenfi.exit_insufficient_data(message: ...)` | notebook requires 6m of historical data            |
| no_result_returned |                                              | if none of the above was called                    |

## Return Payloads

```json
{
  "<result_key>": "<result_data>",
  "<result_key2>": ["<result_data2>"],
  ...
  "run_metadata": {
    "status": "<success|not_applicable|insufficent_data>",
    "message": "<custom-mesage-if-given>"
  }
}
```

## DB Query Caching

`db_query`, `query_one`, `query_all` all have caching.

Caching is a combination of `logical_step_name` + `state_machine_run_id` + `query_str`.

This allows caching across time (different `state_machine_run_id`s) and steps even if the `query_str` is the same.
