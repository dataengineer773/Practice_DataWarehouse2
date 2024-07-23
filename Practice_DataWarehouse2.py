# Create a check_for_nulls test on column billedamount in the table FactBilling :
test1={
    "testname":"Check for nulls",
    "test":check_for_nulls,
    "column": "billedamount",
    "table": "FactBilling"
}


# Create a check_for_duplicates test on column billid in the table FactBilling :
test2={
    "testname":"Check for duplicates",
    "test":check_for_duplicates,
    "column": "billid",
    "table": "FactBilling"
}


# Create a check_for_valid_values test on column quarter in the table DimMonth. The valid values are 1, 2, 3, 4 :
test3={
    "testname":"Check for valid values",
    "test":check_for_valid_values,
    "column": "quarter",
    "table": "DimMonth",
    "valid_values":{1,2,3,4}
}