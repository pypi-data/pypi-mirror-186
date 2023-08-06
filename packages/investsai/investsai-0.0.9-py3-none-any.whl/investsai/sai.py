"""Summary
"""
import pandas as pd
import numpy as np
from typing import Union, List, Set, Tuple, Callable

from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

from pandarallel import pandarallel
import psutil
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class SAI(object):

    """This class applies SAI algorithm to stock selection; therefore, invest-SAI. It allows users to train SAI rules that
    runs to generate interpretable rule that generates well into identifying peforming securities in the future

    Attributes:
        nb_workers (int): The number of cpu available for parallelization
        parallel (bool): run the module in parallel
        params (dict): all the parameters required to instantiate the object
        q (int): quantile for discretization
        rules (pd.DataFrame): output rules and the correspoinding metrics
        te_ary (object): object that holds the tranformation to fpgrowth input data format
        verbose (boolean): flag to suppress progress bar and messages

    """

    def __init__(self, params: dict) -> None:
        """Object class to train SAI model to predict the top performing securities

        Args:
            params (dict): q: quantile for discretizing
                            parallel: parallelization
                            )

        Raises:
            ValueError: Description
        """
        self.params = params
        self.q = params.get('q', 2)
        self.verbose = params.get('verbose', True)
        progress_bar = True if self.verbose else False
        if self.q < 2:
            raise ValueError(
                "require to discretize input variables into at least 2 categories; variables that are not discretized into more than one category do not offer additional information")
        self.parallel = params.get('parallel', True)
        if self.parallel:
            nb_workers = params.get(
                'nb_workers', None)
            self.nb_workers = nb_workers if nb_workers else psutil.cpu_count(
                logical=False)
            pandarallel.initialize(
                progress_bar=progress_bar, nb_workers=self.nb_workers, verbose=0)

    def __discretize(self, df: Union[pd.Series, pd.DataFrame], q: int = 3) -> Tuple[pd.DataFrame, dict]:
        """Descretize numeric columns of dataframe into quantile buckets {Name}_1 - {Name}_q;
        N/A belongs to {Name}_0

        Args:
            df (Union[pd.Series, pd.DataFrame]): input pandas dataframe or series with only numeric cols
            q (int, optional): quantile for discretization

        Returns:
            Tuple[pd.DataFrame, dict]: return pandas dataframe with discretized categories and dictionary
            of dicretization cutpoints for all columns.

        Raises:
            TypeError: when input datafram in not a pandas dataframe or series
        """
        if not(isinstance(df, pd.DataFrame) | isinstance(df, pd.Series)):
            raise TypeError(
                "Function can only discretize pandas DataFrame or Series")
        df_new = df.copy() if isinstance(df, pd.DataFrame) else pd.DataFrame(
            data=df.copy(), columns=[df.name])

        def d(x: pd.Series, q: int) -> Tuple[pd.Series, np.array]:
            """sub method for lambda function to discretize a pandas series

            Args:
                x (pd.Series): input pandas series
                q (int): quantiles for discretization

            Returns:
                Tuple[pd.Series, np.array]: return series after discretization and discretization cutpoints
            """
            x_new, bins = pd.qcut(
                x, q, labels=[f'{x.name}_{str(i)}' for i in range(1, q + 1)], duplicates='drop', retbins=True)
            x_new = x_new.cat.add_categories(f'{x.name}_0')
            x_new[x_new.isna()] = f'{x.name}_0'
            return x_new, bins

        cutpoints = {}
        # df_new = df_new.copy()
        for column in df_new:
            df_new.loc[:, column], cutpoints[column] = d(
                df_new.loc[:, column], q)
        return df_new, cutpoints

    def __apply_discretize(self, df: Union[pd.Series, pd.DataFrame], cutpoints: dict) -> Tuple[pd.DataFrame, dict]:
        """This method discretes data by providing specific cutpoints

        Args:
            df (Union[pd.Series, pd.DataFrame]): Input dataframe/Series for discretization
            cutpoints (dict): cutoints provided for discretization

        Returns:
            Tuple[pd.DataFrame, dict]: discretized dataset and cutpoints used to discretize

        Raises:
            TypeError: raise error if the input df is not pandas dataframe or series
        """
        if not(isinstance(df, pd.DataFrame) | isinstance(df, pd.Series)):
            raise TypeError(
                "Function can only discretize pandas DataFrame or Series")
        df_new = df.copy() if isinstance(df, pd.DataFrame) else pd.DataFrame(
            data=df.copy(), columns=[df.name])

        for column in df_new:
            df_new.loc[df_new[column] <= cutpoints[column]
                       [0], column] = cutpoints[column][0] + cutpoints[column][0] * 0.0001
            df_new.loc[df_new[column] >= cutpoints[column]
                       [-1], column] = cutpoints[column][-1] - cutpoints[column][-1] * 0.0001
            df_new[column] = pd.cut(df_new.loc[:, column], cutpoints[column], labels=[
                f'{column}_{str(i)}' for i in range(1, self.q + 1)])
            df_new[column] = df_new.loc[:,
                                        column].cat.add_categories(f'{column}_0')
            df_new[column].loc[df_new[column].isna()] = f'{column}_0'
        return df_new, cutpoints

    def __discretize_mixed_type(self, df: pd.DataFrame, disc_func: Callable, **kwargs) -> Tuple[pd.DataFrame, dict]:
        """method to hand case when data has a mix of numeric and non-numeric columns (i.e. sector)

        Args:
            df (pd.DataFrame): Input pandas dataframe, it can contain pure numeric or mix of numeric/non-numeric
            disc_func (Callable): the descretization method used,
            **kwargs: arguments provided for the disc_func
            __discretize <- use quantile, __apply_discretize <- provide cutpoints

        Returns:
            Tuple[pd.DataFrame, dict]: pandas dataframe with discretized columns and discretization cutpoints

        Deleted Parameters:
            q (int): qunatile for discretization
        """
        # non_numeric_cols = [
        #     col for col in df.columns if not np.issubdtype(df[col].dtype, np.number)]

        if not(isinstance(df, pd.DataFrame)):
            raise TypeError(
                "Function can only input pandas DataFrame df")

        non_numeric_cols = df.select_dtypes(
            exclude=np.number).columns.tolist()

        if not non_numeric_cols:
            return disc_func(df=df, **kwargs)
        else:
            dff = df.loc[:, ~df.columns.isin(non_numeric_cols)]
            numerics_discretized, cutpoints = disc_func(df=dff, **kwargs)
            return pd.concat([numerics_discretized, df.loc[:, non_numeric_cols]], axis=1), cutpoints

    def __preprocess(self, X: pd.DataFrame, y: pd.DataFrame, q: int) -> List[List[str]]:
        """process input data dict and append discretized monthly pandas dataframe for training SAI

        Args:
            X (pd.DataFrame): Input data
            y (pd.DataFrame): response data, label {0,1} whether the security is successul (1)
            q (int): quantile for discretization

        Returns:
            List[List[str]]: list containts list of dicretized field representing a security
        """
        if not(isinstance(X, pd.DataFrame) & isinstance(y, pd.DataFrame)):
            raise TypeError(
                "Both X and y must be pandas DataFrame")

        if not isinstance(q, int):
            raise TypeError(
                "q for discretization must be integer")

        x_discretized, self.cutpoints = self.__discretize_mixed_type(
            df=X, q=q, disc_func=self.__discretize)
        y_cat = pd.DataFrame(y.iloc[:, 0].map(
            {1: 'success', 0: 'fail'}), columns=['y']).set_index(x_discretized.index)
        Xy = pd.concat(
            [x_discretized, y_cat], axis=1)
        return Xy.values.tolist()

    def fit(self, X: pd.DataFrame, y: pd.DataFrame, yreal: pd.DataFrame) -> None:
        """Train SAI with input data. Build Rules and assign probabilites to each rule

        Args:
            X (pd.DataFrame): Input data with variable/factor items (column) for all securities (row)
            y (pd.DataFrame): response variable suggest the security is considered successful (1)

        Deleted Parameters:
            metric (str, optional): metric used to sort output rules i.e. support, confidence, lift, leverage, conviction

        Raises:
            ValueError: Description
        """
        if not isinstance(X, pd.DataFrame):
            raise ValueError(
                "X must be a pandas DataFrame with dimension n x m (i.e. n is number of securities and m is the number of variables")
        if not isinstance(y, pd.DataFrame):
            raise ValueError(
                "y must be a pandas DataFrame with values as labels {0,1} indentifying whether the security at column n is considered as successful (1)")
        if X.shape[0] != y.shape[0]:
            raise ValueError(
                "The row dimension for both X and y must be the same")

        TrainData = self.__preprocess(X, y, q=self.q)
        te = TransactionEncoder()
        self.te_ary = te.fit(TrainData)
        dataset = pd.DataFrame(
            self.te_ary.transform(TrainData), columns=te.columns_)

        if self.verbose:
            print('\n...................................')
            print('   training Invest-SAI algorithm   ')
            print('...................................\n')

        freqitemset = fpgrowth(
            dataset, min_support=0.05, use_colnames=True)

        self.rules = association_rules(
            freqitemset, metric="confidence", min_threshold=0)

        def relevant_stocks(rule):
            """sub method for lambda function to calculate an equal-weighted average of the
                returns of all the relevant stocks that are passed by a rule
            Args:
                rule (TYPE): rule that represent equity charateristics

            Returns:
                TYPE: average returns from all the relevant stocks
            """
            relevant = []
            for s in TrainData:
                rel = set(rule).issubset(s)
                relevant.append(rel)
            return yreal.loc[relevant].mean()

        if self.parallel:
            self.rules = self.rules.loc[self.rules['consequents'].parallel_apply(
                lambda x: x.issubset(['success']) or x.issubset(['fail']))]
            self.rules['exp_returns'] = self.rules['antecedents'].parallel_apply(
                relevant_stocks)
        else:
            self.rules = self.rules.loc[self.rules['consequents'].apply(
                lambda x: x.issubset(['success']) or x.issubset(['fail']))]
            self.rules['exp_returns'] = self.rules['antecedents'].apply(
                relevant_stocks)

        numerator = self.rules['support'] * (1 - self.rules['antecedent support'] -
                                             self.rules['consequent support'] + self.rules['support'])
        denominator = (self.rules['consequent support'] - self.rules['support']) * (
            self.rules['antecedent support'] - self.rules['support'])
        mask = denominator != 0

        self.rules.loc[mask, 'odd_ratio'] = numerator.loc[mask] / \
            denominator.loc[mask]
        self.rules.dropna(inplace=True)
        self.rules = self.rules[['antecedents', 'consequents',
                                 'confidence', 'odd_ratio', 'lift', 'exp_returns']].sort_values('exp_returns', ascending=False)
        self.rules.rename(columns={'antecedents': 'rules',
                                   'confidence': 'cond_success_prob',
                                   'lift': 'causal_lift',
                                   'exp_returns': 'returns'}, inplace=True)

    def predict(self, X: pd.DataFrame, metric: str = 'returns', eval_metric: str = 'causal_lift', eval_val: float = 0) -> pd.DataFrame:
        """Assign to probabilties to a new set of securities using the learned rules
        equal-weighted the success probabilities of the rules that represent the security

        Args:
            X (pd.DataFrame): Input pandas dataframe with each row represent a security
            metric (str, optional): The metric used to rank securities, i.e. support, confidence, lift, leverage, conviction
            eval_metric (str, optional): provide a evaluation metric to further assess the rule (i.e. how many of the averaged rules
            are above a causal lift of 1, or how many of the averaged rules with returns > 0)
            eval_val (float, optional): set the threshold for evaluation (i.e. 0 with causal lift will count all averaged rules because
            causal lift is always > 0)

        Returns:
            pd.DataFrame: a pandas dataframe with the right-most column to rank securities

        Raises:
            ValueError: Description

        """
        if not isinstance(X, pd.DataFrame):
            raise ValueError(
                "X must be a pd.DataFrame containing the securities that users want to rank and the corresopnding variables")

        XTest, _ = self.__discretize_mixed_type(
            df=X, cutpoints=self.cutpoints, disc_func=self.__apply_discretize)

        rules_filtered = self.rules[self.rules[eval_metric] >= eval_val]

        if self.verbose:
            print('\n....................................')
            print('            predicting             ')
            print('...................................\n')

        if self.parallel:
            def avg_val(s: pd.Series, r: pd.DataFrame) -> float:
                """sub method for lambda function to calculate an equal-weighted average of the
                success probabilities of all the rules that represent a security

                Args:
                    s (pd.Series): a series of discreteize category to represent a security
                    r (pd.DataFrame): a pandas dataframe contains all rules and corresponding probabilites

                Returns:
                    float: expected sucess probability of the security
                """
                cnt = 0
                val = 0
                cnt_eval = 0
                for row in r.itertuples():
                    if getattr(row, 'rules').issubset(s):
                        val += getattr(row, metric)
                        cnt += 1
                        if getattr(row, eval_metric) >= eval_val:
                            cnt_eval += 1
                if cnt > 0:
                    return (val / cnt, cnt_eval)
                else:
                    return (np.nan, cnt_eval)

            probs = XTest.parallel_apply(
                lambda x: avg_val(x, rules_filtered), axis=1).tolist()

        else:
            XTest = XTest.values.tolist()
            probs = []

            def get_val(s: List, r: pd.Series) -> Tuple[bool, int]:
                """sub method for lambda function to evaluate whether a stock passed a rule, and if so, whether
                the rule is greater than the evaluation threshold (i.e. causal lift > 1)

                Args:
                    s (pd.Series): a series of discreteize category to represent a security
                    r (pd.DataFrame): a pandas series contains a rule and corresponding probabilites

                Returns:
                    tuple: boolean whether a stock passed a rule, 1 if the passed rule is greater than evaluation
                    threshold
                """
                if getattr(r, 'rules').issubset(s):
                    rule = True
                    cnt_eval = 1 if getattr(r, eval_metric) >= eval_val else 0
                else:
                    rule, cnt_eval = False, 0
                return rule, cnt_eval

            for s in XTest:
                rules = [list(z) for z in zip(
                    *rules_filtered.apply(lambda r: get_val(s, r), axis=1))]
                probs.append(
                    (rules_filtered.loc[rules[0], metric].mean(), sum(rules[1])))
        return pd.DataFrame(probs, columns=['exp_' + metric, 'cnt_eval'], index=X.index).sort_values('exp_' + metric, ascending=False)
