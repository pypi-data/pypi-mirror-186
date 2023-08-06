"""
This program implements TOPSIS, a multi-criteria decision analysis (MCDA) method, using command line arguments
as follows:
    python topsis.py <Input data file> <Weights> <Impacts> <Output data file>

Author: Amrita Bhatia
"""
import sys
import numpy as np
import pandas as pd


def get_normalised_matrix(df):
    """
    Normalises the features of the decision matrix.
    """
    denom = np.sqrt(np.sum(np.square(df), axis = 0))

    return np.divide(df, denom)


def get_weighted_matrix(df, w):
    """
    Multiplies features with their respective weights.
    """
    return np.multiply(df, w)


def get_score_and_rank(df, i):
    """
    Calculates TOPSIS score from positive and negative seperation measures.
    """
    positive_ideal = df.max()
    positive_ideal.iloc[np.where(i == '-')] = df.min().iloc[np.where(i == '-')]

    negative_ideal = df.min()
    negative_ideal.iloc[np.where(i == '-')] = df.max().iloc[np.where(i == '-')]

    # Seperation measures i.e. Euclidean distances from ideal values
    S_positive = np.sqrt(np.sum(np.square(df - positive_ideal), axis = 1))
    S_negative = np.sqrt(np.sum(np.square(df - negative_ideal), axis = 1))

    # TOPSIS score
    performance_score = S_negative/(S_negative + S_positive)
    ranks = performance_score.rank(ascending = False)

    return performance_score, ranks


def main():
    try:
        if len(sys.argv) != 5:
            raise(IndexError)

        df = pd.read_csv(sys.argv[1], index_col=0)
        w = sys.argv[2]
        i = sys.argv[3]
        output_path = sys.argv[4]

    except FileNotFoundError as e:
        raise SystemExit(e)

    except IndexError:
        raise SystemExit(f"Usage: topsis <input_file_name> <weights> <impacts> <output_file_name>")

    else:
        w = w.replace(" ", "").split(",")
        try:
            w = np.array(w, dtype = float)
        except Exception:
            raise SystemExit("Weights must be numeric and seperated by ','. For example, \"0.25,0.25,1,0.25\"")

        i = np.array(i.replace(" ", "").split(","))


    try:
        if ((i == '+')|(i == '-')).all() != True:
            raise Exception("Impacts must be either '+' or '-' and seperated by ','. For example, \"+,-,+,-\"")

        if len(df.columns) < 2:
            raise Exception("Input file must contain 3 or more columns")

        if (len(df.columns) != len(w)) or (len(w) != len(i)):
            raise Exception("Length of weights and impacts should be equal to number of features")
        
        # if (df.dtypes == 'object'):
        if df.applymap(np.isreal).all().all() != True:
            raise Exception("Columns (excluding first one) in input file must contain numeric values only")

    except Exception as e:
        raise SystemExit(e)


    normalised_df = get_normalised_matrix(df)
    weighted_n_df = get_weighted_matrix(normalised_df, w)

    df['TOPSIS Score'], df['Rank'] = get_score_and_rank(weighted_n_df, i)

    df.to_csv(output_path)

if __name__ == "__main__":
    main()