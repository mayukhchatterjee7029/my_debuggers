def nan_detector(df) -> None:
    """
    Detects the number of missing values in the dataset.
    """

    import pandas as pd ## importing pandas library

    na_col_count = 0
    na_col_index = []

    if not isinstance(df, pd.DataFrame):
        print("Please pass a pandas DataFrame")
        return
    
    for index, col in enumerate(df.isna().sum()):
        if col > 0:
            na_col_count += 1
            na_col_index.append([df.columns[index], f"Index = {index}"])

    print(f"Count of columns having NaN values = {na_col_count}")
    print(f"Null values containing Columns = {na_col_index}")

